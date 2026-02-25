"""Generated response models for slug: autostrategy."""

from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, ValidationError, Field, RootModel

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class BudgetMaximalModel1(_BaseModel):
    bonus: int | None = None
    calls_from: int | None = Field(default=None, alias='callsFrom')
    calls_to: int | None = Field(default=None, alias='callsTo')
    real: int | None = None
    total: int = None
    views_from: int | None = Field(default=None, alias='viewsFrom')
    views_to: int | None = Field(default=None, alias='viewsTo')

class BudgetMinimalModel2(_BaseModel):
    bonus: int | None = None
    calls_from: int | None = Field(default=None, alias='callsFrom')
    calls_to: int | None = Field(default=None, alias='callsTo')
    real: int | None = None
    total: int = None
    views_from: int | None = Field(default=None, alias='viewsFrom')
    views_to: int | None = Field(default=None, alias='viewsTo')

class BudgetPriceRangesItemModel3(_BaseModel):
    calls_from: int = Field(alias='callsFrom')
    calls_to: int = Field(alias='callsTo')
    percent: int = None
    price_from: int = Field(alias='priceFrom')
    price_to: int = Field(alias='priceTo')
    views_from: int = Field(alias='viewsFrom')
    views_to: int = Field(alias='viewsTo')

class BudgetRecommendedModel4(_BaseModel):
    bonus: int | None = None
    calls_from: int | None = Field(default=None, alias='callsFrom')
    calls_to: int | None = Field(default=None, alias='callsTo')
    real: int | None = None
    total: int = None
    views_from: int | None = Field(default=None, alias='viewsFrom')
    views_to: int | None = Field(default=None, alias='viewsTo')

class Budget(_BaseModel):
    maximal: BudgetMaximalModel1 | None = None
    minimal: BudgetMinimalModel2 = None
    price_ranges: list[BudgetPriceRangesItemModel3] = Field(default=None, alias='priceRanges')
    recommended: BudgetRecommendedModel4 = None

class AutostrategyApiGetAutostrategyBudgetResponse(_BaseModel):
    budget: Budget = None
    calc_id: int | None = Field(default=None, alias='calcId')

class Campaign(_BaseModel):
    balance: int = None
    budget: int = None
    campaign_id: int = Field(default=None, alias='campaignId')
    campaign_type: str = Field(default=None, alias='campaignType')
    create_time: str = Field(default=None, alias='createTime')
    description: str = None
    finish_time: str = Field(default=None, alias='finishTime')
    items_count: int = Field(default=None, alias='itemsCount')
    start_time: str = Field(default=None, alias='startTime')
    status_id: int = Field(default=None, alias='statusId')
    title: str = None
    update_time: str = Field(default=None, alias='updateTime')
    user_id: int = Field(default=None, alias='userId')
    version: int = None

class AutostrategyApiCreateAutostrategyCampaignResponse(_BaseModel):
    campaign: Campaign = None

class AutostrategyApiEditAutostrategyCampaignResponse(_BaseModel):
    campaign: Campaign = None

class GetCampaignInfoForecastResultCallsModel5(_BaseModel):
    from_: int = Field(alias='from')
    lack_reason: Literal['not_enough_data', 'no_calltracking'] | None = Field(default=None, alias='lackReason')
    to: int

class GetCampaignInfoForecastResultViewsModel6(_BaseModel):
    from_: int = Field(alias='from')
    lack_reason: Literal['not_enough_data'] | None = Field(default=None, alias='lackReason')
    to: int

class GetCampaignInfoForecastResult(_BaseModel):
    calls: GetCampaignInfoForecastResultCallsModel5 = None
    views: GetCampaignInfoForecastResultViewsModel6 = None

class AutostrategyApiGetAutostrategyCampaignInfoResponseItemsItemModel7(_BaseModel):
    is_active: bool = Field(default=None, alias='isActive')
    item_id: int = Field(default=None, alias='itemId')

class AutostrategyApiGetAutostrategyCampaignInfoResponse(_BaseModel):
    campaign: Campaign = None
    forecast: GetCampaignInfoForecastResult = None
    items: list[AutostrategyApiGetAutostrategyCampaignInfoResponseItemsItemModel7] = None

class AutostrategyApiStopAutostrategyCampaignResponse(_BaseModel):
    campaign: Campaign = None

class AutostrategyApiGetAutostrategyCampaignsResponse(_BaseModel):
    campaigns: list[Campaign] = None
    total_count: int = Field(default=None, alias='totalCount')

class StatItemModel8CallsForecastModel9(_BaseModel):
    from_: int = Field(alias='from')
    to: int

class StatItemModel8ViewsForecastModel10(_BaseModel):
    from_: int = Field(alias='from')
    to: int

class StatItemModel8(_BaseModel):
    calls: int
    calls_forecast: StatItemModel8CallsForecastModel9 | None = Field(default=None, alias='callsForecast')
    date: str
    views: int
    views_forecast: StatItemModel8ViewsForecastModel10 | None = Field(default=None, alias='viewsForecast')

class Stat(RootModel[list[StatItemModel8]]):
    pass

class AutostrategyApiGetAutostrategyStatResponseTotalsModel11(_BaseModel):
    calls: int
    views: int

class AutostrategyApiGetAutostrategyStatResponse(_BaseModel):
    stat: Stat = None
    totals: AutostrategyApiGetAutostrategyStatResponseTotalsModel11 = None

__all__ = ['BudgetMaximalModel1', 'BudgetMinimalModel2', 'BudgetPriceRangesItemModel3', 'BudgetRecommendedModel4', 'Budget', 'AutostrategyApiGetAutostrategyBudgetResponse', 'Campaign', 'AutostrategyApiCreateAutostrategyCampaignResponse', 'AutostrategyApiEditAutostrategyCampaignResponse', 'GetCampaignInfoForecastResultCallsModel5', 'GetCampaignInfoForecastResultViewsModel6', 'GetCampaignInfoForecastResult', 'AutostrategyApiGetAutostrategyCampaignInfoResponseItemsItemModel7', 'AutostrategyApiGetAutostrategyCampaignInfoResponse', 'AutostrategyApiStopAutostrategyCampaignResponse', 'AutostrategyApiGetAutostrategyCampaignsResponse', 'StatItemModel8CallsForecastModel9', 'StatItemModel8ViewsForecastModel10', 'StatItemModel8', 'Stat', 'AutostrategyApiGetAutostrategyStatResponseTotalsModel11', 'AutostrategyApiGetAutostrategyStatResponse']
