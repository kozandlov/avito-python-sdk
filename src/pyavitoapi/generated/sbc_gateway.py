"""Generated API module for slug: sbc-gateway."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.sbc_gateway import SbcGatewayApiOpenApiAvailableResponse, SbcGatewayApiOpenApiMultiConfirmResponse, SbcGatewayApiOpenApiMultiCreateResponse, SbcGatewayApiOpenApiStatsResponse, SbcGatewayApiOpenApiTariffInfoResponse


class SbcGatewayApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def open_api_available(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> SbcGatewayApiOpenApiAvailableResponse:
        """Получение информации об объявлениях"""
        payload = await self._transport.request(
            method="POST",
            path_template="/special-offers/v1/available",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return SbcGatewayApiOpenApiAvailableResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for sbc-gateway.open_api_available (POST /special-offers/v1/available)",
                payload=payload,
                details={
                    "slug": "sbc-gateway",
                    "operation_id": "openApiAvailable",
                    "python_method": "open_api_available",
                    "http_method": "POST",
                    "path": "/special-offers/v1/available",
                    "errors": exc.errors(),
                },
            ) from exc

    async def open_api_multi_confirm(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> SbcGatewayApiOpenApiMultiConfirmResponse:
        """Отправка и оплата рассылки"""
        payload = await self._transport.request(
            method="POST",
            path_template="/special-offers/v1/multiConfirm",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return SbcGatewayApiOpenApiMultiConfirmResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for sbc-gateway.open_api_multi_confirm (POST /special-offers/v1/multiConfirm)",
                payload=payload,
                details={
                    "slug": "sbc-gateway",
                    "operation_id": "openApiMultiConfirm",
                    "python_method": "open_api_multi_confirm",
                    "http_method": "POST",
                    "path": "/special-offers/v1/multiConfirm",
                    "errors": exc.errors(),
                },
            ) from exc

    async def open_api_multi_create(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> SbcGatewayApiOpenApiMultiCreateResponse:
        """Создание рассылки"""
        payload = await self._transport.request(
            method="POST",
            path_template="/special-offers/v1/multiCreate",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return SbcGatewayApiOpenApiMultiCreateResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for sbc-gateway.open_api_multi_create (POST /special-offers/v1/multiCreate)",
                payload=payload,
                details={
                    "slug": "sbc-gateway",
                    "operation_id": "openApiMultiCreate",
                    "python_method": "open_api_multi_create",
                    "http_method": "POST",
                    "path": "/special-offers/v1/multiCreate",
                    "errors": exc.errors(),
                },
            ) from exc

    async def open_api_stats(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> SbcGatewayApiOpenApiStatsResponse:
        """Получение статистики"""
        payload = await self._transport.request(
            method="POST",
            path_template="/special-offers/v1/stats",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return SbcGatewayApiOpenApiStatsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for sbc-gateway.open_api_stats (POST /special-offers/v1/stats)",
                payload=payload,
                details={
                    "slug": "sbc-gateway",
                    "operation_id": "openApiStats",
                    "python_method": "open_api_stats",
                    "http_method": "POST",
                    "path": "/special-offers/v1/stats",
                    "errors": exc.errors(),
                },
            ) from exc

    async def open_api_tariff_info(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> SbcGatewayApiOpenApiTariffInfoResponse:
        """Получение информации о тарифе"""
        payload = await self._transport.request(
            method="POST",
            path_template="/special-offers/v1/tariffInfo",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return SbcGatewayApiOpenApiTariffInfoResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for sbc-gateway.open_api_tariff_info (POST /special-offers/v1/tariffInfo)",
                payload=payload,
                details={
                    "slug": "sbc-gateway",
                    "operation_id": "openApiTariffInfo",
                    "python_method": "open_api_tariff_info",
                    "http_method": "POST",
                    "path": "/special-offers/v1/tariffInfo",
                    "errors": exc.errors(),
                },
            ) from exc

__all__ = ["SbcGatewayApi"]
