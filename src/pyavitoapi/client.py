"""High-level async Avito SDK facade."""

from __future__ import annotations

from typing import Any

from pyavitoapi.auth import AvitoTokenManager, OAuthCredentials
from pyavitoapi.transport.http import AvitoHttpTransport

try:
    from pyavitoapi.generated_registry import REGISTRY
except Exception:  # pragma: no cover
    REGISTRY: dict[str, type[Any]] = {}


class AvitoAsyncClient:
    """Async facade that exposes all generated slug APIs as lazy properties."""

    def __init__(
        self,
        *,
        client_id: str,
        client_secret: str,
        base_url: str = "https://api.avito.ru",
        timeout: float = 30.0,
    ) -> None:
        self._transport = AvitoHttpTransport(base_url=base_url, timeout=timeout)
        self._token_manager = AvitoTokenManager(
            self._transport,
            OAuthCredentials(client_id=client_id, client_secret=client_secret),
        )
        self._apis: dict[str, Any] = {}

    async def __aenter__(self) -> "AvitoAsyncClient":
        await self._transport.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self._transport.__aexit__(exc_type, exc, tb)

    @property
    def auth(self) -> AvitoTokenManager:
        return self._token_manager

    def __getattr__(self, name: str) -> Any:
        slug = name.replace("_", "-")
        cls = REGISTRY.get(slug)
        if cls is None:
            raise AttributeError(f"Unknown API group: {name}")
        if slug not in self._apis:
            self._apis[slug] = cls(self._transport)
        return self._apis[slug]

    @property
    def available_apis(self) -> list[str]:
        return sorted(REGISTRY.keys())
