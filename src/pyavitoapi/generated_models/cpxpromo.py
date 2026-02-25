"""Generated response models for slug: cpxpromo."""

from __future__ import annotations

from typing import Any
from pydantic import BaseModel, ConfigDict, ValidationError, Field

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class BudgetValue(_BaseModel):
    compare: int
    max_forecast: int = Field(alias='maxForecast')
    min_forecast: int = Field(alias='minForecast')
    value_penny: int = Field(alias='valuePenny')

class Budget(_BaseModel):
    budgets: list[BudgetValue]
    max_limit_penny: int = Field(alias='maxLimitPenny')
    min_limit_penny: int = Field(alias='minLimitPenny')
    rec_budget_penny: int = Field(alias='recBudgetPenny')

class Auto(_BaseModel):
    budget_penny: int | None = Field(default=None, alias='budgetPenny')
    budget_type: str | None = Field(default=None, alias='budgetType')
    daily_budget: Budget = Field(alias='dailyBudget')
    max_budget_penny: int = Field(alias='maxBudgetPenny')
    min_budget_penny: int = Field(alias='minBudgetPenny')
    monthly_budget: Budget = Field(alias='monthlyBudget')
    weekly_budget: Budget = Field(alias='weeklyBudget')

class Bid(_BaseModel):
    compare: int
    max_forecast: int = Field(alias='maxForecast')
    min_forecast: int = Field(alias='minForecast')
    value_penny: int = Field(alias='valuePenny')

class Manual(_BaseModel):
    bid_penny: int | None = Field(default=None, alias='bidPenny')
    bids: list[Bid]
    limit_penny: int | None = Field(default=None, alias='limitPenny')
    max_bid_penny: int = Field(alias='maxBidPenny')
    max_limit_penny: int = Field(alias='maxLimitPenny')
    min_bid_penny: int = Field(alias='minBidPenny')
    min_limit_penny: int = Field(alias='minLimitPenny')
    rec_bid_penny: int = Field(alias='recBidPenny')

class CpxpromoApiGetBidsResponse(_BaseModel):
    action_type_id: int = Field(alias='actionTypeID')
    auto: Auto = None
    manual: Manual = None
    selected_type: str = Field(alias='selectedType')

class AutoPromotion(_BaseModel):
    budget_penny: int = Field(alias='budgetPenny')
    budget_type: str = Field(alias='budgetType')

class ManualPromotion(_BaseModel):
    bid_penny: int = Field(alias='bidPenny')
    limit_penny: int | None = Field(default=None, alias='limitPenny')

class CpxpromoApiGetPromotionsByItemIdsResponseItemsItemModel1(_BaseModel):
    action_type_id: int = Field(alias='actionTypeID')
    auto_promotion: AutoPromotion = Field(default=None, alias='autoPromotion')
    item_id: int = Field(alias='itemID')
    manual_promotion: ManualPromotion = Field(default=None, alias='manualPromotion')

class CpxpromoApiGetPromotionsByItemIdsResponse(_BaseModel):
    items: list[CpxpromoApiGetPromotionsByItemIdsResponseItemsItemModel1]

class CpxpromoApiRemovePromotionResponse(_BaseModel):
    message: str

__all__ = ['BudgetValue', 'Budget', 'Auto', 'Bid', 'Manual', 'CpxpromoApiGetBidsResponse', 'AutoPromotion', 'ManualPromotion', 'CpxpromoApiGetPromotionsByItemIdsResponseItemsItemModel1', 'CpxpromoApiGetPromotionsByItemIdsResponse', 'CpxpromoApiRemovePromotionResponse']
