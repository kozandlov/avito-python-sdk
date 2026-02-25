"""Generated response models for slug: trxpromo."""

from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, ValidationError, Field

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class TrxpromoApiApiTrxPromoOpenApiApplyResponseSuccessModel1ResultItemModel2ErrorModel3(_BaseModel):
    code: Literal[1001, 1002]
    message: str

class TrxpromoApiApiTrxPromoOpenApiApplyResponseSuccessModel1ResultItemModel2ValidCommissionRangeModel4(_BaseModel):
    step: int
    value_max: int = Field(alias='valueMax')
    value_min: int = Field(alias='valueMin')

class TrxpromoApiApiTrxPromoOpenApiApplyResponseSuccessModel1ResultItemModel2(_BaseModel):
    error: TrxpromoApiApiTrxPromoOpenApiApplyResponseSuccessModel1ResultItemModel2ErrorModel3 = None
    item_id: int = Field(alias='itemID')
    success: bool
    valid_commission_range: TrxpromoApiApiTrxPromoOpenApiApplyResponseSuccessModel1ResultItemModel2ValidCommissionRangeModel4 = Field(default=None, alias='validCommissionRange')

class TrxpromoApiApiTrxPromoOpenApiApplyResponseSuccessModel1(_BaseModel):
    result: list[TrxpromoApiApiTrxPromoOpenApiApplyResponseSuccessModel1ResultItemModel2]

class TrxpromoApiApiTrxPromoOpenApiApplyResponse(_BaseModel):
    success: TrxpromoApiApiTrxPromoOpenApiApplyResponseSuccessModel1

class TrxpromoApiApiTrxPromoOpenApiCancelResponseSuccessModel5ResultItemModel6ErrorModel7(_BaseModel):
    code: Literal[1001, 1002]
    message: str

class TrxpromoApiApiTrxPromoOpenApiCancelResponseSuccessModel5ResultItemModel6(_BaseModel):
    error: TrxpromoApiApiTrxPromoOpenApiCancelResponseSuccessModel5ResultItemModel6ErrorModel7 = None
    item_id: int = Field(alias='itemID')
    success: bool

class TrxpromoApiApiTrxPromoOpenApiCancelResponseSuccessModel5(_BaseModel):
    result: list[TrxpromoApiApiTrxPromoOpenApiCancelResponseSuccessModel5ResultItemModel6]

class TrxpromoApiApiTrxPromoOpenApiCancelResponse(_BaseModel):
    success: TrxpromoApiApiTrxPromoOpenApiCancelResponseSuccessModel5

class TrxpromoApiApiTrxPromoOpenApiCommissionsResponseSuccessModel8ResultItemModel9ErrorModel10(_BaseModel):
    code: Literal[1001]
    message: str

class TrxpromoApiApiTrxPromoOpenApiCommissionsResponseSuccessModel8ResultItemModel9SettingsModel11(_BaseModel):
    step: int
    value_max: int = Field(alias='valueMax')
    value_min: int = Field(alias='valueMin')

class TrxpromoApiApiTrxPromoOpenApiCommissionsResponseSuccessModel8ResultItemModel9(_BaseModel):
    error: TrxpromoApiApiTrxPromoOpenApiCommissionsResponseSuccessModel8ResultItemModel9ErrorModel10 = None
    item_id: int = Field(alias='itemID')
    promo_available: bool = Field(alias='promoAvailable')
    settings: TrxpromoApiApiTrxPromoOpenApiCommissionsResponseSuccessModel8ResultItemModel9SettingsModel11

class TrxpromoApiApiTrxPromoOpenApiCommissionsResponseSuccessModel8(_BaseModel):
    result: list[TrxpromoApiApiTrxPromoOpenApiCommissionsResponseSuccessModel8ResultItemModel9]

class TrxpromoApiApiTrxPromoOpenApiCommissionsResponse(_BaseModel):
    success: TrxpromoApiApiTrxPromoOpenApiCommissionsResponseSuccessModel8

__all__ = ['TrxpromoApiApiTrxPromoOpenApiApplyResponseSuccessModel1ResultItemModel2ErrorModel3', 'TrxpromoApiApiTrxPromoOpenApiApplyResponseSuccessModel1ResultItemModel2ValidCommissionRangeModel4', 'TrxpromoApiApiTrxPromoOpenApiApplyResponseSuccessModel1ResultItemModel2', 'TrxpromoApiApiTrxPromoOpenApiApplyResponseSuccessModel1', 'TrxpromoApiApiTrxPromoOpenApiApplyResponse', 'TrxpromoApiApiTrxPromoOpenApiCancelResponseSuccessModel5ResultItemModel6ErrorModel7', 'TrxpromoApiApiTrxPromoOpenApiCancelResponseSuccessModel5ResultItemModel6', 'TrxpromoApiApiTrxPromoOpenApiCancelResponseSuccessModel5', 'TrxpromoApiApiTrxPromoOpenApiCancelResponse', 'TrxpromoApiApiTrxPromoOpenApiCommissionsResponseSuccessModel8ResultItemModel9ErrorModel10', 'TrxpromoApiApiTrxPromoOpenApiCommissionsResponseSuccessModel8ResultItemModel9SettingsModel11', 'TrxpromoApiApiTrxPromoOpenApiCommissionsResponseSuccessModel8ResultItemModel9', 'TrxpromoApiApiTrxPromoOpenApiCommissionsResponseSuccessModel8', 'TrxpromoApiApiTrxPromoOpenApiCommissionsResponse']
