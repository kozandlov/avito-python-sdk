"""Generated response models for slug: stock-management."""

from __future__ import annotations

from typing import Any
from pydantic import BaseModel, ConfigDict, ValidationError

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class StockManagementApiPostStockManagement1InfoResponseStocksItemModel1(_BaseModel):
    is_multiple: bool
    is_out_of_stock: bool
    is_unlimited: bool
    item_id: int
    quantity: int

class StockManagementApiPostStockManagement1InfoResponse(_BaseModel):
    stocks: list[StockManagementApiPostStockManagement1InfoResponseStocksItemModel1] = None

class StockManagementApiPutStockManagement1StocksResponseStocksItemModel2(_BaseModel):
    errors: list[str] = None
    external_id: str | None = None
    item_id: int
    success: bool

class StockManagementApiPutStockManagement1StocksResponse(_BaseModel):
    stocks: list[StockManagementApiPutStockManagement1StocksResponseStocksItemModel2] = None

__all__ = ['StockManagementApiPostStockManagement1InfoResponseStocksItemModel1', 'StockManagementApiPostStockManagement1InfoResponse', 'StockManagementApiPutStockManagement1StocksResponseStocksItemModel2', 'StockManagementApiPutStockManagement1StocksResponse']
