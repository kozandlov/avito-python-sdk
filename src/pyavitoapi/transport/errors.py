"""Typed exceptions for pyAvitoApi transport and API calls."""

from __future__ import annotations

from typing import Any, Optional


class AvitoApiError(Exception):
    """Base API error."""

    def __init__(
        self,
        message: str,
        *,
        status_code: Optional[int] = None,
        payload: Optional[Any] = None,
        details: Optional[dict[str, Any]] = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.payload = payload
        self.details = details


class AvitoAuthError(AvitoApiError):
    """Auth/token-related error."""


class AvitoRateLimitError(AvitoApiError):
    """Rate-limit error with optional retry-after."""

    def __init__(self, message: str, *, retry_after: Optional[int] = None, payload: Optional[Any] = None) -> None:
        super().__init__(message, status_code=429, payload=payload)
        self.retry_after = retry_after


class AvitoTransportError(AvitoApiError):
    """Network/transport error."""


class AvitoValidationError(AvitoApiError):
    """Validation/schema error."""
