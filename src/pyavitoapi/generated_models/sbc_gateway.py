"""Generated response models for slug: sbc-gateway."""

from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, ValidationError, Field

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class SbcGatewayApiOpenApiAvailableResponseItemsItemModel1(_BaseModel):
    is_available: bool = Field(alias='isAvailable')
    item_id: int = Field(alias='itemId')
    reason: str | None = None

class SbcGatewayApiOpenApiAvailableResponse(_BaseModel):
    items: list[SbcGatewayApiOpenApiAvailableResponseItemsItemModel1] = None

class SbcGatewayApiOpenApiMultiConfirmResponse(_BaseModel):
    ok: bool = None

class SbcGatewayApiOpenApiMultiCreateResponseCommonModel2OffersItemModel3ExpiresAtModel4(_BaseModel):
    max: int
    min: int

class SbcGatewayApiOpenApiMultiCreateResponseCommonModel2OffersItemModel3(_BaseModel):
    expires_at: SbcGatewayApiOpenApiMultiCreateResponseCommonModel2OffersItemModel3ExpiresAtModel4 = Field(alias='expiresAt')
    message_price: int | None = Field(default=None, alias='messagePrice')
    offer_text: str = Field(default=None, alias='offerText')
    slug: str
    type: Literal['discount', 'text']

class SbcGatewayApiOpenApiMultiCreateResponseCommonModel2TariffModel5(_BaseModel):
    due_date: str = Field(alias='dueDate')
    sends_left: int = Field(alias='sendsLeft')
    total_sends: int = Field(alias='totalSends')

class SbcGatewayApiOpenApiMultiCreateResponseCommonModel2(_BaseModel):
    offers: list[SbcGatewayApiOpenApiMultiCreateResponseCommonModel2OffersItemModel3]
    tariff: SbcGatewayApiOpenApiMultiCreateResponseCommonModel2TariffModel5 | None = None

class SbcGatewayApiOpenApiMultiCreateResponseDispatchesItemModel6DiscountModel7(_BaseModel):
    max_discount: int = Field(default=None, alias='maxDiscount')
    min_discount: int = Field(default=None, alias='minDiscount')

class SbcGatewayApiOpenApiMultiCreateResponseDispatchesItemModel6ErrorModel8(_BaseModel):
    message: str = None

class SbcGatewayApiOpenApiMultiCreateResponseDispatchesItemModel6ItemModel9(_BaseModel):
    id: int

class SbcGatewayApiOpenApiMultiCreateResponseDispatchesItemModel6(_BaseModel):
    available_audience_count: int = Field(alias='availableAudienceCount')
    discount: SbcGatewayApiOpenApiMultiCreateResponseDispatchesItemModel6DiscountModel7 = None
    error: SbcGatewayApiOpenApiMultiCreateResponseDispatchesItemModel6ErrorModel8 = None
    id: int
    item: SbcGatewayApiOpenApiMultiCreateResponseDispatchesItemModel6ItemModel9
    message_price: int | None = Field(alias='messagePrice')
    offers: list[str]
    status: Literal['notCreated', 'created']

class SbcGatewayApiOpenApiMultiCreateResponse(_BaseModel):
    common: SbcGatewayApiOpenApiMultiCreateResponseCommonModel2
    dispatches: list[SbcGatewayApiOpenApiMultiCreateResponseDispatchesItemModel6]

class SbcGatewayApiOpenApiStatsResponseStatsItemModel10(_BaseModel):
    accepted: int
    count: int
    discount: int = None
    expires_at: str = Field(alias='expiresAt')
    item_id: int = Field(alias='itemId')
    offer_slug: str = Field(alias='offerSlug')
    price: int
    sent_at: str = Field(alias='sentAt')

class SbcGatewayApiOpenApiStatsResponse(_BaseModel):
    stats: list[SbcGatewayApiOpenApiStatsResponseStatsItemModel10 | None] = None

class SbcGatewayApiOpenApiTariffInfoResponseTariffInfoModel11(_BaseModel):
    sends_left: int = Field(alias='sendsLeft')
    total_sends: int = Field(alias='totalSends')

class SbcGatewayApiOpenApiTariffInfoResponse(_BaseModel):
    tariff_info: SbcGatewayApiOpenApiTariffInfoResponseTariffInfoModel11 | None = Field(default=None, alias='tariffInfo')

__all__ = ['SbcGatewayApiOpenApiAvailableResponseItemsItemModel1', 'SbcGatewayApiOpenApiAvailableResponse', 'SbcGatewayApiOpenApiMultiConfirmResponse', 'SbcGatewayApiOpenApiMultiCreateResponseCommonModel2OffersItemModel3ExpiresAtModel4', 'SbcGatewayApiOpenApiMultiCreateResponseCommonModel2OffersItemModel3', 'SbcGatewayApiOpenApiMultiCreateResponseCommonModel2TariffModel5', 'SbcGatewayApiOpenApiMultiCreateResponseCommonModel2', 'SbcGatewayApiOpenApiMultiCreateResponseDispatchesItemModel6DiscountModel7', 'SbcGatewayApiOpenApiMultiCreateResponseDispatchesItemModel6ErrorModel8', 'SbcGatewayApiOpenApiMultiCreateResponseDispatchesItemModel6ItemModel9', 'SbcGatewayApiOpenApiMultiCreateResponseDispatchesItemModel6', 'SbcGatewayApiOpenApiMultiCreateResponse', 'SbcGatewayApiOpenApiStatsResponseStatsItemModel10', 'SbcGatewayApiOpenApiStatsResponse', 'SbcGatewayApiOpenApiTariffInfoResponseTariffInfoModel11', 'SbcGatewayApiOpenApiTariffInfoResponse']
