"""Generated API module for slug: item."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.item import ItemApiApplyVasResponse, ItemApiGetItemInfoResponse, ItemApiGetItemsInfoResponse, ItemApiItemAnalyticsResponse, ItemApiItemStatsShallowResponse, ItemApiPostCallsStatsResponse, ItemApiPutItemVasPackageV2Response, ItemApiPutItemVasResponse, ItemApiUpdatePriceResponse, ItemApiVasPricesResponse


class ItemApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def vas_prices(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> ItemApiVasPricesResponse:
        """Получение информации о стоимости услуг продвижения и доступных значках"""
        payload = await self._transport.request(
            method="POST",
            path_template="/core/v1/accounts/{userId}/vas/prices",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return ItemApiVasPricesResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for item.vas_prices (POST /core/v1/accounts/{userId}/vas/prices)",
                payload=payload,
                details={
                    "slug": "item",
                    "operation_id": "vasPrices",
                    "python_method": "vas_prices",
                    "http_method": "POST",
                    "path": "/core/v1/accounts/{userId}/vas/prices",
                    "errors": exc.errors(),
                },
            ) from exc

    async def post_calls_stats(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> ItemApiPostCallsStatsResponse:
        """Получение статистики по звонкам"""
        payload = await self._transport.request(
            method="POST",
            path_template="/core/v1/accounts/{user_id}/calls/stats/",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return ItemApiPostCallsStatsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for item.post_calls_stats (POST /core/v1/accounts/{user_id}/calls/stats/)",
                payload=payload,
                details={
                    "slug": "item",
                    "operation_id": "postCallsStats",
                    "python_method": "post_calls_stats",
                    "http_method": "POST",
                    "path": "/core/v1/accounts/{user_id}/calls/stats/",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_item_info(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> ItemApiGetItemInfoResponse:
        """Получение информации по объявлению"""
        payload = await self._transport.request(
            method="GET",
            path_template="/core/v1/accounts/{user_id}/items/{item_id}/",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return ItemApiGetItemInfoResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for item.get_item_info (GET /core/v1/accounts/{user_id}/items/{item_id}/)",
                payload=payload,
                details={
                    "slug": "item",
                    "operation_id": "getItemInfo",
                    "python_method": "get_item_info",
                    "http_method": "GET",
                    "path": "/core/v1/accounts/{user_id}/items/{item_id}/",
                    "errors": exc.errors(),
                },
            ) from exc

    async def put_item_vas(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> ItemApiPutItemVasResponse:
        """Применение дополнительных услуг"""
        payload = await self._transport.request(
            method="PUT",
            path_template="/core/v1/accounts/{user_id}/items/{item_id}/vas",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return ItemApiPutItemVasResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for item.put_item_vas (PUT /core/v1/accounts/{user_id}/items/{item_id}/vas)",
                payload=payload,
                details={
                    "slug": "item",
                    "operation_id": "putItemVas",
                    "python_method": "put_item_vas",
                    "http_method": "PUT",
                    "path": "/core/v1/accounts/{user_id}/items/{item_id}/vas",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_items_info(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> ItemApiGetItemsInfoResponse:
        """Получение информации по объявлениям"""
        payload = await self._transport.request(
            method="GET",
            path_template="/core/v1/items",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return ItemApiGetItemsInfoResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for item.get_items_info (GET /core/v1/items)",
                payload=payload,
                details={
                    "slug": "item",
                    "operation_id": "getItemsInfo",
                    "python_method": "get_items_info",
                    "http_method": "GET",
                    "path": "/core/v1/items",
                    "errors": exc.errors(),
                },
            ) from exc

    async def update_price(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> ItemApiUpdatePriceResponse:
        """Обновление цены объявления
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/core/v1/items/{item_id}/update_price",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return ItemApiUpdatePriceResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for item.update_price (POST /core/v1/items/{item_id}/update_price)",
                payload=payload,
                details={
                    "slug": "item",
                    "operation_id": "updatePrice",
                    "python_method": "update_price",
                    "http_method": "POST",
                    "path": "/core/v1/items/{item_id}/update_price",
                    "errors": exc.errors(),
                },
            ) from exc

    async def put_item_vas_package_v2(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> ItemApiPutItemVasPackageV2Response:
        """Применение пакета дополнительных услуг"""
        payload = await self._transport.request(
            method="PUT",
            path_template="/core/v2/accounts/{user_id}/items/{item_id}/vas_packages",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return ItemApiPutItemVasPackageV2Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for item.put_item_vas_package_v2 (PUT /core/v2/accounts/{user_id}/items/{item_id}/vas_packages)",
                payload=payload,
                details={
                    "slug": "item",
                    "operation_id": "putItemVasPackageV2",
                    "python_method": "put_item_vas_package_v2",
                    "http_method": "PUT",
                    "path": "/core/v2/accounts/{user_id}/items/{item_id}/vas_packages",
                    "errors": exc.errors(),
                },
            ) from exc

    async def apply_vas(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> ItemApiApplyVasResponse:
        """Применение услуг продвижения"""
        payload = await self._transport.request(
            method="PUT",
            path_template="/core/v2/items/{itemId}/vas/",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return ItemApiApplyVasResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for item.apply_vas (PUT /core/v2/items/{itemId}/vas/)",
                payload=payload,
                details={
                    "slug": "item",
                    "operation_id": "applyVas",
                    "python_method": "apply_vas",
                    "http_method": "PUT",
                    "path": "/core/v2/items/{itemId}/vas/",
                    "errors": exc.errors(),
                },
            ) from exc

    async def item_stats_shallow(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> ItemApiItemStatsShallowResponse:
        """Получение статистики по списку объявлений"""
        payload = await self._transport.request(
            method="POST",
            path_template="/stats/v1/accounts/{user_id}/items",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return ItemApiItemStatsShallowResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for item.item_stats_shallow (POST /stats/v1/accounts/{user_id}/items)",
                payload=payload,
                details={
                    "slug": "item",
                    "operation_id": "itemStatsShallow",
                    "python_method": "item_stats_shallow",
                    "http_method": "POST",
                    "path": "/stats/v1/accounts/{user_id}/items",
                    "errors": exc.errors(),
                },
            ) from exc

    async def item_analytics(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> ItemApiItemAnalyticsResponse:
        """Получение статистических показателей по профилю"""
        payload = await self._transport.request(
            method="POST",
            path_template="/stats/v2/accounts/{user_id}/items",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return ItemApiItemAnalyticsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for item.item_analytics (POST /stats/v2/accounts/{user_id}/items)",
                payload=payload,
                details={
                    "slug": "item",
                    "operation_id": "itemAnalytics",
                    "python_method": "item_analytics",
                    "http_method": "POST",
                    "path": "/stats/v2/accounts/{user_id}/items",
                    "errors": exc.errors(),
                },
            ) from exc

__all__ = ["ItemApi"]
