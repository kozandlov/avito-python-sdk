"""Async HTTP transport for Avito API."""

from __future__ import annotations

import asyncio
from collections import deque
from datetime import datetime, timezone
from typing import Any, Optional

import httpx

from pyavitoapi.transport.errors import AvitoApiError, AvitoRateLimitError, AvitoTransportError


class AvitoHttpTransport:
    """Low-level async transport with retries and simple rate limiting."""

    def __init__(
        self,
        *,
        base_url: str = "https://api.avito.ru",
        timeout: float = 30.0,
        max_retries: int = 3,
        requests_per_second: int = 5,
        requests_per_minute: int = 100,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.requests_per_second = requests_per_second
        self.requests_per_minute = requests_per_minute
        self._client: Optional[httpx.AsyncClient] = None
        self._lock = asyncio.Lock()
        self._request_times = deque()

    async def __aenter__(self) -> "AvitoHttpTransport":
        self._client = httpx.AsyncClient(timeout=self.timeout, follow_redirects=True)
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        if self._client is not None:
            await self._client.aclose()
            self._client = None

    async def _throttle(self) -> None:
        async with self._lock:
            now = datetime.now(timezone.utc)

            while self._request_times and (now - self._request_times[0]).total_seconds() >= 60:
                self._request_times.popleft()

            if len(self._request_times) >= self.requests_per_minute:
                oldest = self._request_times[0]
                wait_seconds = max(0.0, 60.0 - (now - oldest).total_seconds())
                if wait_seconds > 0:
                    await asyncio.sleep(wait_seconds)

            second_count = sum(1 for t in self._request_times if (now - t).total_seconds() < 1)
            if second_count >= self.requests_per_second:
                await asyncio.sleep(0.2)

            self._request_times.append(datetime.now(timezone.utc))

    def _build_url(self, path_template: str, path_params: Optional[dict[str, Any]]) -> str:
        path = path_template
        if path_params:
            for key, value in path_params.items():
                path = path.replace("{" + key + "}", str(value))
        if not path.startswith("/"):
            path = "/" + path
        return self.base_url + path

    async def request(
        self,
        *,
        method: str,
        path_template: str,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        form_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> Any:
        if self._client is None:
            raise AvitoTransportError("Transport is not initialized; use async context manager")

        url = self._build_url(path_template, path_params)
        last_error: Optional[Exception] = None

        for attempt in range(1, self.max_retries + 1):
            await self._throttle()
            try:
                response = await self._client.request(
                    method=method,
                    url=url,
                    params=query,
                    json=json_body,
                    data=form_body,
                    headers=headers,
                )

                if response.status_code == 429:
                    retry_after_raw = response.headers.get("Retry-After")
                    retry_after = int(retry_after_raw) if retry_after_raw and retry_after_raw.isdigit() else None
                    raise AvitoRateLimitError(
                        "Rate limit exceeded",
                        retry_after=retry_after,
                        payload=_safe_json(response),
                    )

                if response.status_code >= 400:
                    raise AvitoApiError(
                        f"HTTP {response.status_code}",
                        status_code=response.status_code,
                        payload=_safe_json(response),
                    )

                if not response.content:
                    return {}
                return _safe_json(response)

            except AvitoRateLimitError as exc:
                last_error = exc
                if attempt == self.max_retries:
                    raise
                await asyncio.sleep(exc.retry_after or 1)
            except httpx.RequestError as exc:
                last_error = exc
                if attempt == self.max_retries:
                    raise AvitoTransportError(f"Network error: {exc}") from exc
                await asyncio.sleep(min(2 ** attempt, 5))
            except AvitoApiError as exc:
                if exc.status_code is not None and 500 <= exc.status_code < 600 and attempt < self.max_retries:
                    last_error = exc
                    await asyncio.sleep(min(2 ** attempt, 5))
                    continue
                raise

        raise AvitoTransportError(f"Request failed: {last_error}")


def _safe_json(response: httpx.Response) -> Any:
    try:
        return response.json()
    except Exception:
        return {"raw": response.text}
