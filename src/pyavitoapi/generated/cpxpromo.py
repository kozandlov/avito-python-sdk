"""Generated API module for slug: cpxpromo."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.cpxpromo import CpxpromoApiGetBidsResponse, CpxpromoApiGetPromotionsByItemIdsResponse, CpxpromoApiRemovePromotionResponse


class CpxpromoApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def get_bids(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> CpxpromoApiGetBidsResponse:
        """Получение детализированной информации о действующих и доступных ценах за целевые действия и бюджетах"""
        payload = await self._transport.request(
            method="GET",
            path_template="/cpxpromo/1/getBids/{itemId}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return CpxpromoApiGetBidsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for cpxpromo.get_bids (GET /cpxpromo/1/getBids/{itemId})",
                payload=payload,
                details={
                    "slug": "cpxpromo",
                    "operation_id": "getBids",
                    "python_method": "get_bids",
                    "http_method": "GET",
                    "path": "/cpxpromo/1/getBids/{itemId}",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_promotions_by_item_ids(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> CpxpromoApiGetPromotionsByItemIdsResponse:
        """Получение текущих цен за целевое действие и бюджетов по нескольким объявлениям"""
        payload = await self._transport.request(
            method="POST",
            path_template="/cpxpromo/1/getPromotionsByItemIds",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return CpxpromoApiGetPromotionsByItemIdsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for cpxpromo.get_promotions_by_item_ids (POST /cpxpromo/1/getPromotionsByItemIds)",
                payload=payload,
                details={
                    "slug": "cpxpromo",
                    "operation_id": "getPromotionsByItemIds",
                    "python_method": "get_promotions_by_item_ids",
                    "http_method": "POST",
                    "path": "/cpxpromo/1/getPromotionsByItemIds",
                    "errors": exc.errors(),
                },
            ) from exc

    async def remove_promotion(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> CpxpromoApiRemovePromotionResponse:
        """Остановка продвижения"""
        payload = await self._transport.request(
            method="POST",
            path_template="/cpxpromo/1/remove",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return CpxpromoApiRemovePromotionResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for cpxpromo.remove_promotion (POST /cpxpromo/1/remove)",
                payload=payload,
                details={
                    "slug": "cpxpromo",
                    "operation_id": "removePromotion",
                    "python_method": "remove_promotion",
                    "http_method": "POST",
                    "path": "/cpxpromo/1/remove",
                    "errors": exc.errors(),
                },
            ) from exc

    async def save_auto_bid(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:
        """Применение автоматической настройки"""
        payload = await self._transport.request(
            method="POST",
            path_template="/cpxpromo/1/setAuto",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        return None

    async def save_manual_bid(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:
        """Применение ручной настройки"""
        payload = await self._transport.request(
            method="POST",
            path_template="/cpxpromo/1/setManual",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        return None

__all__ = ["CpxpromoApi"]
