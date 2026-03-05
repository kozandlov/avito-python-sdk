"""Generated response models for slug: item."""

from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, ValidationError, Field, RootModel

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class ItemApiVasPricesResponse(RootModel[dict[str, Any]]):
    pass

class CallsStatsDay(_BaseModel):
    answered: int = None
    calls: int = None
    date: str = None
    new: int = None
    new_answered: int = Field(default=None, alias='newAnswered')

class CallsStatsItem(_BaseModel):
    days: list[CallsStatsDay] = None
    employee_id: int = Field(alias='employeeId')
    item_id: int = Field(alias='itemId')

class ItemApiPostCallsStatsResponseResultModel1(_BaseModel):
    items: list[CallsStatsItem]

class ItemApiPostCallsStatsResponse(_BaseModel):
    result: ItemApiPostCallsStatsResponseResultModel1 = None

class InfoVas(_BaseModel):
    finish_time: str | None = None
    schedule: list[str] | None = None
    vas_id: Literal['vip', 'highlight', 'pushup', 'premium', 'xl'] = None

class ItemApiGetItemInfoResponse(_BaseModel):
    autoload_item_id: str | None = None
    finish_time: str | None = None
    start_time: str | None = None
    status: Literal['active', 'removed', 'old', 'blocked', 'rejected', 'not_found', 'another_user'] = None
    url: str | None = None
    vas: list[InfoVas] | None = None

class ItemApiPutItemVasResponse(_BaseModel):
    amount: float = None
    vas: InfoVas = None

class ItemApiGetItemsInfoResponseMetaModel2(_BaseModel):
    page: int = None
    per_page: int = None

class ItemApiGetItemsInfoResponseResourcesItemModel3CategoryModel4(_BaseModel):
    id: int = None
    name: str = None

class ItemApiGetItemsInfoResponseResourcesItemModel3(_BaseModel):
    address: str = None
    category: ItemApiGetItemsInfoResponseResourcesItemModel3CategoryModel4 = None
    id: int = None
    price: int | None = None
    status: Literal['active', 'removed', 'old', 'blocked', 'rejected'] = None
    title: str = None
    url: str | None = None

class ItemApiGetItemsInfoResponse(_BaseModel):
    meta: ItemApiGetItemsInfoResponseMetaModel2 = None
    resources: list[ItemApiGetItemsInfoResponseResourcesItemModel3] = None

class ItemApiUpdatePriceResponseResultModel5(_BaseModel):
    success: bool = None

class ItemApiUpdatePriceResponse(_BaseModel):
    result: ItemApiUpdatePriceResponseResultModel5

class ItemApiPutItemVasPackageV2Response(_BaseModel):
    amount: float = None

class ApplyVasResp(_BaseModel):
    operation_id: int = Field(alias='operationId')

class ItemApiApplyVasResponse(RootModel[dict[str, ApplyVasResp]]):
    pass

class StatisticsCountersItemModel7StatsItemModel8(_BaseModel):
    contacts: int = None
    date: str
    favorites: int = None
    uniq_contacts: int = Field(default=None, alias='uniqContacts')
    uniq_favorites: int = Field(default=None, alias='uniqFavorites')
    uniq_views: int = Field(default=None, alias='uniqViews')
    views: int = None

class StatisticsCountersItemModel7(_BaseModel):
    item_id: int = Field(default=None, alias='itemId')
    stats: list[StatisticsCountersItemModel7StatsItemModel8] = None

class StatisticsCounters(RootModel[list[StatisticsCountersItemModel7]]):
    pass

class ItemApiItemStatsShallowResponseResultModel6(_BaseModel):
    items: StatisticsCounters = None

class ItemApiItemStatsShallowResponse(_BaseModel):
    errors: dict[str, Any] = None
    result: ItemApiItemStatsShallowResponseResultModel6 = None

class ItemApiItemAnalyticsResponseResultModel9GroupingsItemModel10MetricsItemModel11(_BaseModel):
    slug: str
    value: float

class Groupings(RootModel[Literal['day', 'week', 'month', 'item', 'totals']]):
    pass

class ItemApiItemAnalyticsResponseResultModel9GroupingsItemModel10(_BaseModel):
    id: int = None
    metrics: list[ItemApiItemAnalyticsResponseResultModel9GroupingsItemModel10MetricsItemModel11] = None
    type: Groupings = None

class ItemApiItemAnalyticsResponseResultModel9(_BaseModel):
    data_total_count: int = Field(default=None, alias='dataTotalCount')
    groupings: list[ItemApiItemAnalyticsResponseResultModel9GroupingsItemModel10] = None
    timestamp: str = None

class ItemApiItemAnalyticsResponse(_BaseModel):
    result: ItemApiItemAnalyticsResponseResultModel9 = None

class ItemApiAccountSpendingsResponseResultModel12GroupingsItemModel13SpendingsItemModel14(_BaseModel):
    slug: str
    value: float

class SpendingsGroupings(RootModel[Literal['day', 'week', 'month']]):
    pass

class ItemApiAccountSpendingsResponseResultModel12GroupingsItemModel13(_BaseModel):
    date: str
    spendings: list[ItemApiAccountSpendingsResponseResultModel12GroupingsItemModel13SpendingsItemModel14]
    type: SpendingsGroupings

class ItemApiAccountSpendingsResponseResultModel12(_BaseModel):
    groupings: list[ItemApiAccountSpendingsResponseResultModel12GroupingsItemModel13]
    timestamp: int

class ItemApiAccountSpendingsResponse(_BaseModel):
    result: ItemApiAccountSpendingsResponseResultModel12

__all__ = ['ItemApiVasPricesResponse', 'CallsStatsDay', 'CallsStatsItem', 'ItemApiPostCallsStatsResponseResultModel1', 'ItemApiPostCallsStatsResponse', 'InfoVas', 'ItemApiGetItemInfoResponse', 'ItemApiPutItemVasResponse', 'ItemApiGetItemsInfoResponseMetaModel2', 'ItemApiGetItemsInfoResponseResourcesItemModel3CategoryModel4', 'ItemApiGetItemsInfoResponseResourcesItemModel3', 'ItemApiGetItemsInfoResponse', 'ItemApiUpdatePriceResponseResultModel5', 'ItemApiUpdatePriceResponse', 'ItemApiPutItemVasPackageV2Response', 'ApplyVasResp', 'ItemApiApplyVasResponse', 'StatisticsCountersItemModel7StatsItemModel8', 'StatisticsCountersItemModel7', 'StatisticsCounters', 'ItemApiItemStatsShallowResponseResultModel6', 'ItemApiItemStatsShallowResponse', 'ItemApiItemAnalyticsResponseResultModel9GroupingsItemModel10MetricsItemModel11', 'Groupings', 'ItemApiItemAnalyticsResponseResultModel9GroupingsItemModel10', 'ItemApiItemAnalyticsResponseResultModel9', 'ItemApiItemAnalyticsResponse', 'ItemApiAccountSpendingsResponseResultModel12GroupingsItemModel13SpendingsItemModel14', 'SpendingsGroupings', 'ItemApiAccountSpendingsResponseResultModel12GroupingsItemModel13', 'ItemApiAccountSpendingsResponseResultModel12', 'ItemApiAccountSpendingsResponse']
