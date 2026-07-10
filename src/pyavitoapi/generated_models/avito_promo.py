"""Generated response models for slug: avito-promo."""

from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, ValidationError, Field, RootModel

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class TransactionId(RootModel[str]):
    pass

class AvitoPromoApiAgencyBalanceResponseResultModel1(_BaseModel):
    reason: str
    status: Literal['processing', 'error']
    transaction_id: TransactionId = Field(alias='transactionId')

class AvitoPromoApiAgencyBalanceResponse(_BaseModel):
    result: AvitoPromoApiAgencyBalanceResponseResultModel1

class TransactionStatus(RootModel[Literal['processing', 'success', 'error']]):
    pass

class AvitoPromoApiAgencyTransactionsResponseResultItemModel2(_BaseModel):
    status: TransactionStatus
    transaction_id: TransactionId = Field(alias='transactionId')

class AvitoPromoApiAgencyTransactionsResponse(_BaseModel):
    result: list[AvitoPromoApiAgencyTransactionsResponseResultItemModel2]

class ErrorMessage(RootModel[str]):
    pass

class AvitoPromoApiAgencyTransactionResponseResultModel3(_BaseModel):
    message: ErrorMessage = None
    status: TransactionStatus
    transaction_id: TransactionId = Field(alias='transactionId')

class AvitoPromoApiAgencyTransactionResponse(_BaseModel):
    result: AvitoPromoApiAgencyTransactionResponseResultModel3

class AmountKopecks(RootModel[int]):
    pass

class AvitoPromoApiAgencyClientsResponseResultModel4ClientsItemModel5AdvanceModel6(_BaseModel):
    amount: AmountKopecks

class AvitoPromoApiAgencyClientsResponseResultModel4ClientsItemModel5BalanceModel7(_BaseModel):
    amount: AmountKopecks

class Id(RootModel[int]):
    pass

class DateTime(RootModel[str]):
    pass

class LinkType(RootModel[Literal['adv', 'trx']]):
    pass

class Counter(RootModel[int]):
    pass

class AvitoPromoApiAgencyClientsResponseResultModel4ClientsItemModel5StatisticsModel8(_BaseModel):
    active_items: Counter = Field(alias='activeItems')
    clicks: Counter
    spendings: AmountKopecks
    views: Counter

class Toggle(RootModel[bool]):
    pass

class AvitoPromoApiAgencyClientsResponseResultModel4ClientsItemModel5SubscriptionModel9(_BaseModel):
    category: Literal['auto', 'realty', 'services', 'job', 'goods']
    expired_to: DateTime = Field(default=None, alias='expiredTo')
    is_active: Toggle = Field(alias='isActive')
    level: Literal['basic', 'extended', 'maximal', 'ultra']

class AvitoPromoApiAgencyClientsResponseResultModel4ClientsItemModel5(_BaseModel):
    advance: AvitoPromoApiAgencyClientsResponseResultModel4ClientsItemModel5AdvanceModel6 = None
    balance: AvitoPromoApiAgencyClientsResponseResultModel4ClientsItemModel5BalanceModel7 = None
    client_id: Id = Field(alias='clientId')
    link_time: DateTime = Field(alias='linkTime')
    link_type: LinkType = Field(alias='linkType')
    main_user_id: Id = Field(default=None, alias='mainUserId')
    name: str
    statistics: AvitoPromoApiAgencyClientsResponseResultModel4ClientsItemModel5StatisticsModel8 = None
    status: Literal['new', 'active']
    subscription: AvitoPromoApiAgencyClientsResponseResultModel4ClientsItemModel5SubscriptionModel9 = None

class AvitoPromoApiAgencyClientsResponseResultModel4(_BaseModel):
    clients: list[AvitoPromoApiAgencyClientsResponseResultModel4ClientsItemModel5]
    total: Counter

class OkResponseStatus(RootModel[Literal['ok']]):
    pass

class AvitoPromoApiAgencyClientsResponse(_BaseModel):
    result: AvitoPromoApiAgencyClientsResponseResultModel4
    status: OkResponseStatus

class TargetTaskId(_BaseModel):
    task_id: Id = Field(alias='taskId')

class AvitoPromoApiAgencyClientsTargetCreateResponse(_BaseModel):
    result: TargetTaskId
    status: OkResponseStatus

class Inn(RootModel[str]):
    pass

class AvitoPromoApiAgencyClientsTargetResultResponseResultModel10ItemsItemModel11ResultsItemModel12(_BaseModel):
    category: Literal['goods', 'services', 'machinery', 'jobs']
    status: Literal['new', 'uplift', 'unavailable']

class AvitoPromoApiAgencyClientsTargetResultResponseResultModel10ItemsItemModel11(_BaseModel):
    inn: Inn
    is_error: bool = Field(alias='isError')
    results: list[AvitoPromoApiAgencyClientsTargetResultResponseResultModel10ItemsItemModel11ResultsItemModel12]

class AvitoPromoApiAgencyClientsTargetResultResponseResultModel10(_BaseModel):
    items: list[AvitoPromoApiAgencyClientsTargetResultResponseResultModel10ItemsItemModel11]
    status: Literal['pending', 'success']

class AvitoPromoApiAgencyClientsTargetResultResponse(_BaseModel):
    result: AvitoPromoApiAgencyClientsTargetResultResponseResultModel10
    status: OkResponseStatus

class AvitoPromoApiAgencyFinancesBalanceResponse(_BaseModel):
    full: AmountKopecks
    pending: AmountKopecks

class AvitoPromoApiAgencyFinancesTransactionsHistoryResponseItemsItemModel13(_BaseModel):
    amount: AmountKopecks
    client_id: Id = Field(default=None, alias='clientId')
    operation_date_time: DateTime = Field(alias='operationDateTime')
    status: Literal['pending', 'success', 'blocked', 'failed']
    transaction_id: TransactionId = Field(alias='transactionId')

class AvitoPromoApiAgencyFinancesTransactionsHistoryResponse(_BaseModel):
    items: list[AvitoPromoApiAgencyFinancesTransactionsHistoryResponseItemsItemModel13]

class InviteId(_BaseModel):
    invite_id: Id = Field(alias='inviteId')

class AvitoPromoApiAgencyUsersInviteSendResponse(_BaseModel):
    result: InviteId
    status: OkResponseStatus

class AvitoPromoApiAgencyUsersInviteStatusResponseResultModel14(_BaseModel):
    status: Literal['pending', 'success', 'decline']

class AvitoPromoApiAgencyUsersInviteStatusResponse(_BaseModel):
    result: AvitoPromoApiAgencyUsersInviteStatusResponseResultModel14
    status: OkResponseStatus

class AvitoPromoApiAgencyUsersVerificationStatusResponseResultModel15(_BaseModel):
    agency_client_user_id: Id = Field(default=None, alias='agencyClientUserId')
    status: Literal['verified', 'not-verified']
    user_id: Id = Field(alias='userId')

class AvitoPromoApiAgencyUsersVerificationStatusResponse(_BaseModel):
    result: AvitoPromoApiAgencyUsersVerificationStatusResponseResultModel15
    status: OkResponseStatus

class StatsMetric(RootModel[Literal['views', 'contacts', 'contactsShowPhone', 'contactsMessenger', 'contactsShowPhoneAndMessenger', 'contactsSbcDiscount', 'viewsToContactsConversion', 'favorites', 'averageViewCost', 'averageContactCost', 'impressions', 'impressionsToViewsConversion', 'clickPackages', 'jobContacts', 'viewsToOrderedItemsConversion', 'orderedItems', 'orderedItemsPrice', 'deliveredItems', 'deliveredItemsPrice', 'bookingPlacedCount', 'bookingPlacedPrice', 'bookingApprovedCount', 'bookingApprovedPrice', 'bookingAcceptedCount', 'bookingAcceptedPrice', 'allSpending', 'spending', 'presenceSpending', 'promoSpending', 'restSpending', 'commission', 'spendingBonus', 'activeItems', 'newActiveItems', 'oldActiveItems']]):
    pass

class AvitoPromoApiStatsAccountsItemsResponseResultModel16GroupingsItemModel17MetricsItemModel18(_BaseModel):
    slug: StatsMetric
    value: Counter

class StatsMetricsGrouping(RootModel[Literal['day', 'week', 'month', 'totals']]):
    pass

class AvitoPromoApiStatsAccountsItemsResponseResultModel16GroupingsItemModel17(_BaseModel):
    id: Id
    metrics: list[AvitoPromoApiStatsAccountsItemsResponseResultModel16GroupingsItemModel17MetricsItemModel18]
    type: StatsMetricsGrouping

class AvitoPromoApiStatsAccountsItemsResponseResultModel16(_BaseModel):
    data_total_count: Counter = Field(alias='dataTotalCount')
    groupings: list[AvitoPromoApiStatsAccountsItemsResponseResultModel16GroupingsItemModel17]

class AvitoPromoApiStatsAccountsItemsResponse(_BaseModel):
    result: AvitoPromoApiStatsAccountsItemsResponseResultModel16

class Date(RootModel[str]):
    pass

class AmountDouble(RootModel[float]):
    pass

class AvitoPromoApiStatsAccountsSpendingsResponseResultModel19GroupingsItemModel20SpendingsItemModel21ServicesItemModel22(_BaseModel):
    slug: Literal['bbip', 'perf_vas', 'vas_xl', 'vas_highlight', 'sbc_discount', 'vas_sticker', 'vas_package', 'orders_commission', 'bookings_commission', 'delivery_subsidy', 'fbs_commission', 'tariff_listing', 'lf', 'tariff_remainder', 'cpa_click_package', 'cpa_target_call', 'cpa_target_chat', 'cpa_job_contact', 'service_fee', 'cpa_rfp_contact', 'cpa_transfer_select', 'profile_promo', 'profile_promo_v2', 'tariff_ext', 'chat_bot', 'cv', 'other']
    value: AmountDouble

class AvitoPromoApiStatsAccountsSpendingsResponseResultModel19GroupingsItemModel20SpendingsItemModel21(_BaseModel):
    services: list[AvitoPromoApiStatsAccountsSpendingsResponseResultModel19GroupingsItemModel20SpendingsItemModel21ServicesItemModel22]
    slug: Literal['promotion', 'presence', 'commission', 'rest']
    value: AmountDouble

class StatsSpendingsGrouping(RootModel[Literal['day', 'week', 'month']]):
    pass

class AvitoPromoApiStatsAccountsSpendingsResponseResultModel19GroupingsItemModel20(_BaseModel):
    date: Date
    spendings: list[AvitoPromoApiStatsAccountsSpendingsResponseResultModel19GroupingsItemModel20SpendingsItemModel21]
    type: StatsSpendingsGrouping

class Timestamp(RootModel[int]):
    pass

class AvitoPromoApiStatsAccountsSpendingsResponseResultModel19(_BaseModel):
    groupings: list[AvitoPromoApiStatsAccountsSpendingsResponseResultModel19GroupingsItemModel20]
    timestamp: Timestamp

class AvitoPromoApiStatsAccountsSpendingsResponse(_BaseModel):
    result: AvitoPromoApiStatsAccountsSpendingsResponseResultModel19

__all__ = ['TransactionId', 'AvitoPromoApiAgencyBalanceResponseResultModel1', 'AvitoPromoApiAgencyBalanceResponse', 'TransactionStatus', 'AvitoPromoApiAgencyTransactionsResponseResultItemModel2', 'AvitoPromoApiAgencyTransactionsResponse', 'ErrorMessage', 'AvitoPromoApiAgencyTransactionResponseResultModel3', 'AvitoPromoApiAgencyTransactionResponse', 'AmountKopecks', 'AvitoPromoApiAgencyClientsResponseResultModel4ClientsItemModel5AdvanceModel6', 'AvitoPromoApiAgencyClientsResponseResultModel4ClientsItemModel5BalanceModel7', 'Id', 'DateTime', 'LinkType', 'Counter', 'AvitoPromoApiAgencyClientsResponseResultModel4ClientsItemModel5StatisticsModel8', 'Toggle', 'AvitoPromoApiAgencyClientsResponseResultModel4ClientsItemModel5SubscriptionModel9', 'AvitoPromoApiAgencyClientsResponseResultModel4ClientsItemModel5', 'AvitoPromoApiAgencyClientsResponseResultModel4', 'OkResponseStatus', 'AvitoPromoApiAgencyClientsResponse', 'TargetTaskId', 'AvitoPromoApiAgencyClientsTargetCreateResponse', 'Inn', 'AvitoPromoApiAgencyClientsTargetResultResponseResultModel10ItemsItemModel11ResultsItemModel12', 'AvitoPromoApiAgencyClientsTargetResultResponseResultModel10ItemsItemModel11', 'AvitoPromoApiAgencyClientsTargetResultResponseResultModel10', 'AvitoPromoApiAgencyClientsTargetResultResponse', 'AvitoPromoApiAgencyFinancesBalanceResponse', 'AvitoPromoApiAgencyFinancesTransactionsHistoryResponseItemsItemModel13', 'AvitoPromoApiAgencyFinancesTransactionsHistoryResponse', 'InviteId', 'AvitoPromoApiAgencyUsersInviteSendResponse', 'AvitoPromoApiAgencyUsersInviteStatusResponseResultModel14', 'AvitoPromoApiAgencyUsersInviteStatusResponse', 'AvitoPromoApiAgencyUsersVerificationStatusResponseResultModel15', 'AvitoPromoApiAgencyUsersVerificationStatusResponse', 'StatsMetric', 'AvitoPromoApiStatsAccountsItemsResponseResultModel16GroupingsItemModel17MetricsItemModel18', 'StatsMetricsGrouping', 'AvitoPromoApiStatsAccountsItemsResponseResultModel16GroupingsItemModel17', 'AvitoPromoApiStatsAccountsItemsResponseResultModel16', 'AvitoPromoApiStatsAccountsItemsResponse', 'Date', 'AmountDouble', 'AvitoPromoApiStatsAccountsSpendingsResponseResultModel19GroupingsItemModel20SpendingsItemModel21ServicesItemModel22', 'AvitoPromoApiStatsAccountsSpendingsResponseResultModel19GroupingsItemModel20SpendingsItemModel21', 'StatsSpendingsGrouping', 'AvitoPromoApiStatsAccountsSpendingsResponseResultModel19GroupingsItemModel20', 'Timestamp', 'AvitoPromoApiStatsAccountsSpendingsResponseResultModel19', 'AvitoPromoApiStatsAccountsSpendingsResponse']
