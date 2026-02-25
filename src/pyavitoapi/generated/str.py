"""Generated API module for slug: str."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.str import StrApiGetRealtyBookingsResponse, StrApiPostRealtyPricesResponse, StrApiPutBookingsInfoResponse, StrApiPutIntervalsResponse


class StrApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def put_bookings_info(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> StrApiPutBookingsInfoResponse:
        """Заполнение календаря занятости объекта недвижимости"""
        payload = await self._transport.request(
            method="POST",
            path_template="/core/v1/accounts/{user_id}/items/{item_id}/bookings",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return StrApiPutBookingsInfoResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for str.put_bookings_info (POST /core/v1/accounts/{user_id}/items/{item_id}/bookings)",
                payload=payload,
                details={
                    "slug": "str",
                    "operation_id": "putBookingsInfo",
                    "python_method": "put_bookings_info",
                    "http_method": "POST",
                    "path": "/core/v1/accounts/{user_id}/items/{item_id}/bookings",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_realty_bookings(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> StrApiGetRealtyBookingsResponse:
        """Получение списка броней по объявлению
"""
        payload = await self._transport.request(
            method="GET",
            path_template="/realty/v1/accounts/{user_id}/items/{item_id}/bookings",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return StrApiGetRealtyBookingsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for str.get_realty_bookings (GET /realty/v1/accounts/{user_id}/items/{item_id}/bookings)",
                payload=payload,
                details={
                    "slug": "str",
                    "operation_id": "getRealtyBookings",
                    "python_method": "get_realty_bookings",
                    "http_method": "GET",
                    "path": "/realty/v1/accounts/{user_id}/items/{item_id}/bookings",
                    "errors": exc.errors(),
                },
            ) from exc

    async def post_realty_prices(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> StrApiPostRealtyPricesResponse:
        """Актуализация параметров для выбранных периодов
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/realty/v1/accounts/{user_id}/items/{item_id}/prices",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return StrApiPostRealtyPricesResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for str.post_realty_prices (POST /realty/v1/accounts/{user_id}/items/{item_id}/prices)",
                payload=payload,
                details={
                    "slug": "str",
                    "operation_id": "postRealtyPrices",
                    "python_method": "post_realty_prices",
                    "http_method": "POST",
                    "path": "/realty/v1/accounts/{user_id}/items/{item_id}/prices",
                    "errors": exc.errors(),
                },
            ) from exc

    async def put_intervals(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> StrApiPutIntervalsResponse:
        """Заполнение доступности объекта недвижимости с квотами и без"""
        payload = await self._transport.request(
            method="POST",
            path_template="/realty/v1/items/intervals",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return StrApiPutIntervalsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for str.put_intervals (POST /realty/v1/items/intervals)",
                payload=payload,
                details={
                    "slug": "str",
                    "operation_id": "putIntervals",
                    "python_method": "put_intervals",
                    "http_method": "POST",
                    "path": "/realty/v1/items/intervals",
                    "errors": exc.errors(),
                },
            ) from exc

    async def post_base_params(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:
        """Установка базовых параметров
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/realty/v1/items/{item_id}/base",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        return None

__all__ = ["StrApi"]
