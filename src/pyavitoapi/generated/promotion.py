"""Generated API module for slug: promotion."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.promotion import PromotionApiCreateBbipOrderForItemsV1Response, PromotionApiGetBbipForecastsByItemsV1Response, PromotionApiGetBbipSuggestsByItemsV1Response, PromotionApiGetDictOfServicesV1Response, PromotionApiGetOrderStatusV1Response, PromotionApiGetServicesByItemsV1Response, PromotionApiListOrdersByUserV1Response


class PromotionApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def get_bbip_forecasts_by_items_v1(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> PromotionApiGetBbipForecastsByItemsV1Response:
        """BBIP. Прогноз продвижения"""
        payload = await self._transport.request(
            method="POST",
            path_template="/promotion/v1/items/services/bbip/forecasts/get",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return PromotionApiGetBbipForecastsByItemsV1Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for promotion.get_bbip_forecasts_by_items_v1 (POST /promotion/v1/items/services/bbip/forecasts/get)",
                payload=payload,
                details={
                    "slug": "promotion",
                    "operation_id": "get_bbip_forecasts_by_items_v1",
                    "python_method": "get_bbip_forecasts_by_items_v1",
                    "http_method": "POST",
                    "path": "/promotion/v1/items/services/bbip/forecasts/get",
                    "errors": exc.errors(),
                },
            ) from exc

    async def create_bbip_order_for_items_v1(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> PromotionApiCreateBbipOrderForItemsV1Response:
        """BBIP. Подключение услуги продвижения"""
        payload = await self._transport.request(
            method="PUT",
            path_template="/promotion/v1/items/services/bbip/orders/create",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return PromotionApiCreateBbipOrderForItemsV1Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for promotion.create_bbip_order_for_items_v1 (PUT /promotion/v1/items/services/bbip/orders/create)",
                payload=payload,
                details={
                    "slug": "promotion",
                    "operation_id": "create_bbip_order_for_items_v1",
                    "python_method": "create_bbip_order_for_items_v1",
                    "http_method": "PUT",
                    "path": "/promotion/v1/items/services/bbip/orders/create",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_bbip_suggests_by_items_v1(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> PromotionApiGetBbipSuggestsByItemsV1Response:
        """BBIP. Варианты бюджета продвижения"""
        payload = await self._transport.request(
            method="POST",
            path_template="/promotion/v1/items/services/bbip/suggests/get",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return PromotionApiGetBbipSuggestsByItemsV1Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for promotion.get_bbip_suggests_by_items_v1 (POST /promotion/v1/items/services/bbip/suggests/get)",
                payload=payload,
                details={
                    "slug": "promotion",
                    "operation_id": "get_bbip_suggests_by_items_v1",
                    "python_method": "get_bbip_suggests_by_items_v1",
                    "http_method": "POST",
                    "path": "/promotion/v1/items/services/bbip/suggests/get",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_dict_of_services_v1(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> PromotionApiGetDictOfServicesV1Response:
        """Словарь типов услуг продвижения"""
        payload = await self._transport.request(
            method="POST",
            path_template="/promotion/v1/items/services/dict",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return PromotionApiGetDictOfServicesV1Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for promotion.get_dict_of_services_v1 (POST /promotion/v1/items/services/dict)",
                payload=payload,
                details={
                    "slug": "promotion",
                    "operation_id": "get_dict_of_services_v1",
                    "python_method": "get_dict_of_services_v1",
                    "http_method": "POST",
                    "path": "/promotion/v1/items/services/dict",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_services_by_items_v1(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> PromotionApiGetServicesByItemsV1Response:
        """Список услуг продвижения"""
        payload = await self._transport.request(
            method="POST",
            path_template="/promotion/v1/items/services/get",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return PromotionApiGetServicesByItemsV1Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for promotion.get_services_by_items_v1 (POST /promotion/v1/items/services/get)",
                payload=payload,
                details={
                    "slug": "promotion",
                    "operation_id": "get_services_by_items_v1",
                    "python_method": "get_services_by_items_v1",
                    "http_method": "POST",
                    "path": "/promotion/v1/items/services/get",
                    "errors": exc.errors(),
                },
            ) from exc

    async def list_orders_by_user_v1(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> PromotionApiListOrdersByUserV1Response:
        """Список заявок"""
        payload = await self._transport.request(
            method="POST",
            path_template="/promotion/v1/items/services/orders/get",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return PromotionApiListOrdersByUserV1Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for promotion.list_orders_by_user_v1 (POST /promotion/v1/items/services/orders/get)",
                payload=payload,
                details={
                    "slug": "promotion",
                    "operation_id": "list_orders_by_user_v1",
                    "python_method": "list_orders_by_user_v1",
                    "http_method": "POST",
                    "path": "/promotion/v1/items/services/orders/get",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_order_status_v1(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> PromotionApiGetOrderStatusV1Response:
        """Статус заявки"""
        payload = await self._transport.request(
            method="POST",
            path_template="/promotion/v1/items/services/orders/status",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return PromotionApiGetOrderStatusV1Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for promotion.get_order_status_v1 (POST /promotion/v1/items/services/orders/status)",
                payload=payload,
                details={
                    "slug": "promotion",
                    "operation_id": "get_order_status_v1",
                    "python_method": "get_order_status_v1",
                    "http_method": "POST",
                    "path": "/promotion/v1/items/services/orders/status",
                    "errors": exc.errors(),
                },
            ) from exc

__all__ = ["PromotionApi"]
