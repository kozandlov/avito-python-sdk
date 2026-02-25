"""Generated API module for slug: tariff."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.tariff import TariffApiGetTariffInfoResponse


class TariffApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def get_tariff_info(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> TariffApiGetTariffInfoResponse:
        """Информация по тарифу"""
        payload = await self._transport.request(
            method="GET",
            path_template="/tariff/info/1",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return TariffApiGetTariffInfoResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for tariff.get_tariff_info (GET /tariff/info/1)",
                payload=payload,
                details={
                    "slug": "tariff",
                    "operation_id": "getTariffInfo",
                    "python_method": "get_tariff_info",
                    "http_method": "GET",
                    "path": "/tariff/info/1",
                    "errors": exc.errors(),
                },
            ) from exc

__all__ = ["TariffApi"]
