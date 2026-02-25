"""Generated response models for slug: promotion."""

from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, ValidationError, Field, RootModel

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class ErrorByItemV1(_BaseModel):
    error_code: int = Field(alias='errorCode')
    error_text: str = Field(alias='errorText')
    item_id: int = Field(alias='itemId')

class BbipForecastByItemV1(_BaseModel):
    item_id: int = Field(alias='itemId')
    max: int
    min: int
    total_old_price: int = Field(alias='totalOldPrice')
    total_price: int = Field(alias='totalPrice')

class PromotionApiGetBbipForecastsByItemsV1Response(_BaseModel):
    errors: list[ErrorByItemV1]
    items: list[BbipForecastByItemV1]
    total_price: int = Field(default=None, alias='totalPrice')

class PromotionApiCreateBbipOrderForItemsV1Response(_BaseModel):
    errors: list[ErrorByItemV1]
    order_id: str | None = Field(default=None, alias='orderId')

class BbipSuggestBudgetV1(_BaseModel):
    is_recommended: bool = Field(default=None, alias='isRecommended')
    old_price: int = Field(alias='oldPrice')
    price: int

class BbipSuggestDurationRangeV1(_BaseModel):
    from_: int = Field(alias='from')
    recommended: int = None
    to: int

class BbipSuggestByItemV1(_BaseModel):
    budgets: list[BbipSuggestBudgetV1]
    duration: BbipSuggestDurationRangeV1
    item_id: int = Field(alias='itemId')

class PromotionApiGetBbipSuggestsByItemsV1Response(_BaseModel):
    errors: list[ErrorByItemV1]
    items: list[BbipSuggestByItemV1]

class ServiceInfoV1(_BaseModel):
    is_deprecated: bool = Field(default=None, alias='isDeprecated')
    name: str
    slug: str

class PromotionApiGetDictOfServicesV1Response(RootModel[list[ServiceInfoV1]]):
    pass

class ServiceV1(_BaseModel):
    end_date: str = Field(default=None, alias='endDate')
    name: str = None
    slug: str = None
    start_date: str = Field(default=None, alias='startDate')

class ServicesByItemV1(_BaseModel):
    item_id: int = Field(default=None, alias='itemId')
    services: list[ServiceV1] = None

class PromotionApiGetServicesByItemsV1Response(_BaseModel):
    errors: list[ErrorByItemV1] = None
    items: list[ServicesByItemV1] = None

class OrderStatus(RootModel[Literal['unknown', 'initialized', 'waiting', 'in_process', 'processed']]):
    pass

class OrderBrief(_BaseModel):
    created_at: str = Field(default=None, alias='createdAt')
    id: str = None
    status: OrderStatus = None

class PromotionApiListOrdersByUserV1ResponsePaginationModel1(_BaseModel):
    has_next_page: bool = Field(alias='hasNextPage')

class PromotionApiListOrdersByUserV1Response(_BaseModel):
    orders: list[OrderBrief]
    pagination: PromotionApiListOrdersByUserV1ResponsePaginationModel1

class OrderStatusByItemV1(_BaseModel):
    error_reason: str | None = Field(default=None, alias='errorReason')
    item_id: int = Field(default=None, alias='itemId')
    price: int = None
    slug: str = None
    status: OrderStatus = None

class PromotionApiGetOrderStatusV1Response(_BaseModel):
    errors: list[ErrorByItemV1] = None
    items: list[OrderStatusByItemV1] = None
    order_id: str = Field(default=None, alias='orderId')
    status: OrderStatus = None
    total_price: int = Field(default=None, alias='totalPrice')

__all__ = ['ErrorByItemV1', 'BbipForecastByItemV1', 'PromotionApiGetBbipForecastsByItemsV1Response', 'PromotionApiCreateBbipOrderForItemsV1Response', 'BbipSuggestBudgetV1', 'BbipSuggestDurationRangeV1', 'BbipSuggestByItemV1', 'PromotionApiGetBbipSuggestsByItemsV1Response', 'ServiceInfoV1', 'PromotionApiGetDictOfServicesV1Response', 'ServiceV1', 'ServicesByItemV1', 'PromotionApiGetServicesByItemsV1Response', 'OrderStatus', 'OrderBrief', 'PromotionApiListOrdersByUserV1ResponsePaginationModel1', 'PromotionApiListOrdersByUserV1Response', 'OrderStatusByItemV1', 'PromotionApiGetOrderStatusV1Response']
