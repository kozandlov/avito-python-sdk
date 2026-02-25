"""Generated API module for slug: auth."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.auth import AuthApiGetAccessTokenResponse


class AuthApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def get_access_token(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AuthApiGetAccessTokenResponse:
        """Получение access token"""
        payload = await self._transport.request(
            method="POST",
            path_template="/token",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AuthApiGetAccessTokenResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for auth.get_access_token (POST /token)",
                payload=payload,
                details={
                    "slug": "auth",
                    "operation_id": "getAccessToken",
                    "python_method": "get_access_token",
                    "http_method": "POST",
                    "path": "/token",
                    "errors": exc.errors(),
                },
            ) from exc

__all__ = ["AuthApi"]
