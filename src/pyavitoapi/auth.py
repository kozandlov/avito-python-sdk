"""OAuth token manager for Avito API."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Optional

from pydantic import BaseModel

from pyavitoapi.transport.errors import AvitoAuthError
from pyavitoapi.transport.http import AvitoHttpTransport


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "Bearer"
    expires_in: int
    refresh_token: Optional[str] = None
    scope: Optional[str] = None


@dataclass
class OAuthCredentials:
    client_id: str
    client_secret: str


class AvitoTokenManager:
    """Manages access token retrieval and refresh with a safety buffer."""

    def __init__(self, transport: AvitoHttpTransport, credentials: OAuthCredentials) -> None:
        self._transport = transport
        self._credentials = credentials
        self._token: Optional[TokenResponse] = None
        self._expires_at: Optional[datetime] = None
        self._lock = asyncio.Lock()

    async def get_client_credentials_token(self) -> TokenResponse:
        async with self._lock:
            if self._token and self._expires_at and self._expires_at > datetime.now(timezone.utc) + timedelta(minutes=5):
                return self._token

            payload = await self._transport.request(
                method="POST",
                path_template="/token",
                query=None,
                form_body={
                    "grant_type": "client_credentials",
                    "client_id": self._credentials.client_id,
                    "client_secret": self._credentials.client_secret,
                },
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )

            try:
                token = TokenResponse(**payload)
            except Exception as exc:
                raise AvitoAuthError(f"Invalid token response: {exc}") from exc

            self._token = token
            self._expires_at = datetime.now(timezone.utc) + timedelta(seconds=token.expires_in)
            return token

    async def auth_header(self) -> dict[str, str]:
        token = await self.get_client_credentials_token()
        return {"Authorization": f"Bearer {token.access_token}"}
