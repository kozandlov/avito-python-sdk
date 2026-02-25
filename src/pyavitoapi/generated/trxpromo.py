"""Generated API module for slug: trxpromo."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.trxpromo import TrxpromoApiApiTrxPromoOpenApiApplyResponse, TrxpromoApiApiTrxPromoOpenApiCancelResponse, TrxpromoApiApiTrxPromoOpenApiCommissionsResponse


class TrxpromoApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def api_trx_promo_open_api_apply(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> TrxpromoApiApiTrxPromoOpenApiApplyResponse:
        """Запуск продвижения"""
        payload = await self._transport.request(
            method="POST",
            path_template="/trx-promo/1/apply",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return TrxpromoApiApiTrxPromoOpenApiApplyResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for trxpromo.api_trx_promo_open_api_apply (POST /trx-promo/1/apply)",
                payload=payload,
                details={
                    "slug": "trxpromo",
                    "operation_id": "api_trx_promo_open_api_apply",
                    "python_method": "api_trx_promo_open_api_apply",
                    "http_method": "POST",
                    "path": "/trx-promo/1/apply",
                    "errors": exc.errors(),
                },
            ) from exc

    async def api_trx_promo_open_api_cancel(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> TrxpromoApiApiTrxPromoOpenApiCancelResponse:
        """Остановка продвижения"""
        payload = await self._transport.request(
            method="POST",
            path_template="/trx-promo/1/cancel",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return TrxpromoApiApiTrxPromoOpenApiCancelResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for trxpromo.api_trx_promo_open_api_cancel (POST /trx-promo/1/cancel)",
                payload=payload,
                details={
                    "slug": "trxpromo",
                    "operation_id": "api_trx_promo_open_api_cancel",
                    "python_method": "api_trx_promo_open_api_cancel",
                    "http_method": "POST",
                    "path": "/trx-promo/1/cancel",
                    "errors": exc.errors(),
                },
            ) from exc

    async def api_trx_promo_open_api_commissions(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> TrxpromoApiApiTrxPromoOpenApiCommissionsResponse:
        """Проверка доступности продвижения и размера комиссий"""
        payload = await self._transport.request(
            method="GET",
            path_template="/trx-promo/1/commissions",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return TrxpromoApiApiTrxPromoOpenApiCommissionsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for trxpromo.api_trx_promo_open_api_commissions (GET /trx-promo/1/commissions)",
                payload=payload,
                details={
                    "slug": "trxpromo",
                    "operation_id": "api_trx_promo_open_api_commissions",
                    "python_method": "api_trx_promo_open_api_commissions",
                    "http_method": "GET",
                    "path": "/trx-promo/1/commissions",
                    "errors": exc.errors(),
                },
            ) from exc

__all__ = ["TrxpromoApi"]
