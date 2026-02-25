"""Generated API module for slug: stock-management."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.stock_management import StockManagementApiPostStockManagement1InfoResponse, StockManagementApiPutStockManagement1StocksResponse


class StockManagementApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def post_stock_management_1_info(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> StockManagementApiPostStockManagement1InfoResponse:
        """Получение остатков"""
        payload = await self._transport.request(
            method="POST",
            path_template="/stock-management/1/info",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return StockManagementApiPostStockManagement1InfoResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for stock-management.post_stock_management_1_info (POST /stock-management/1/info)",
                payload=payload,
                details={
                    "slug": "stock-management",
                    "operation_id": "post_stock_management_1_info",
                    "python_method": "post_stock_management_1_info",
                    "http_method": "POST",
                    "path": "/stock-management/1/info",
                    "errors": exc.errors(),
                },
            ) from exc

    async def put_stock_management_1_stocks(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> StockManagementApiPutStockManagement1StocksResponse:
        """Редактирование остатков"""
        payload = await self._transport.request(
            method="PUT",
            path_template="/stock-management/1/stocks",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return StockManagementApiPutStockManagement1StocksResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for stock-management.put_stock_management_1_stocks (PUT /stock-management/1/stocks)",
                payload=payload,
                details={
                    "slug": "stock-management",
                    "operation_id": "put_stock_management_1_stocks",
                    "python_method": "put_stock_management_1_stocks",
                    "http_method": "PUT",
                    "path": "/stock-management/1/stocks",
                    "errors": exc.errors(),
                },
            ) from exc

__all__ = ["StockManagementApi"]
