"""Generated response models for slug: ads."""

from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, ValidationError, Field, RootModel

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class AccountContactModel1(_BaseModel):
    name: str
    phone: str

class AccountManagerModel2(_BaseModel):
    email: str
    name: str

class Account(_BaseModel):
    actual_address: str = Field(alias='actualAddress')
    contact: AccountContactModel1
    inn: str
    kpp: str
    legal_address: str = Field(alias='legalAddress')
    long_name: str = Field(alias='longName')
    manager: AccountManagerModel2 | None = None
    ogrn: str
    short_name: str = Field(alias='shortName')

class AdsApiV1GetAccountByIdResponse(_BaseModel):
    account: Account = None

class AdsApiV1CreateAccountResponse(_BaseModel):
    account_id: int = Field(alias='accountID')

class AdsApiV1AddUserResponse(_BaseModel):
    pass

class LegalRole(RootModel[Literal['rd', 'ra', 'rr']]):
    pass

class LegalType(RootModel[Literal['ul', 'ip']]):
    pass

class Advertiser(_BaseModel):
    account_id: int = Field(alias='accountId')
    actual_address: str = Field(alias='actualAddress')
    id: int
    inn: str
    kpp: str = None
    legal_address: str = Field(alias='legalAddress')
    legal_role: LegalRole = Field(alias='legalRole')
    legal_type: LegalType = Field(alias='legalType')
    long_name: str = Field(alias='longName')
    ogrn: str
    short_name: str = Field(alias='shortName')

class AdsApiV1GetAdvertisersListResponse(_BaseModel):
    advertisers: list[Advertiser]
    total: int

class AdsApiV1GetAccountBalanceByIdResponse(_BaseModel):
    balance: int
    bonus_balance: int = Field(alias='bonusBalance')

class AdsApiV1TransferBonusResponse(_BaseModel):
    pass

class CampaignType(RootModel[Literal['textImage', 'HTML', 'video']]):
    pass

class CampaignPaymentModel(RootModel[Literal['CPM', 'CPC']]):
    pass

class CampaignStatus(RootModel[Literal['draft', 'in_moderation', 'moderation_failed', 'partial_moderation', 'active', 'paused', 'stopped', 'finished', 'archived']]):
    pass

class Campaign(_BaseModel):
    account_id: int = Field(default=None, alias='accountId')
    additional_agreement_id: int | None = Field(default=None, alias='additionalAgreementID')
    advertiser_id: int = Field(default=None, alias='advertiserId')
    budget: int = None
    campaign_type: CampaignType = Field(default=None, alias='campaignType')
    contract_id: int = Field(default=None, alias='contractId')
    created_at: str = Field(default=None, alias='createdAt')
    end_date: str | None = Field(default=None, alias='endDate')
    id: int = None
    manager_id: int = Field(default=None, alias='managerID')
    name: str = None
    payment_model: CampaignPaymentModel = Field(default=None, alias='paymentModel')
    performance_additional_agreement_id: int | None = Field(default=None, alias='performanceAdditionalAgreementID')
    start_date: str | None = Field(default=None, alias='startDate')
    status: CampaignStatus = None
    updated_at: str | None = Field(default=None, alias='updatedAt')
    user_id: int = Field(default=None, alias='userId')

class AdsApiV1GetCampaignsListResponse(_BaseModel):
    campaigns: list[Campaign]
    total: int

class StatsData(_BaseModel):
    clicks: int
    cpc: float
    cpm: float
    ctr: float
    q25: float | None = None
    q50: float | None = None
    q75: float | None = None
    spend: int
    spend_bonus: int = Field(alias='spendBonus')
    timestamp: str | None = None
    video_views100: int | None = Field(default=None, alias='videoViews100')
    video_views25: int | None = Field(default=None, alias='videoViews25')
    video_views50: int | None = Field(default=None, alias='videoViews50')
    video_views75: int | None = Field(default=None, alias='videoViews75')
    views: int
    vtr: float | None = None

class CreativeStatistic(_BaseModel):
    data: list[StatsData]
    group_id: int = Field(alias='groupId')
    id: int
    name: str
    total_data: StatsData = Field(alias='totalData')

class AdsApiV1GetCreativesStatisticResponse(_BaseModel):
    creatives: list[CreativeStatistic]

class GroupStatistic(_BaseModel):
    data: list[StatsData]
    id: int
    name: str
    total_data: StatsData = Field(alias='totalData')

class AdsApiV1GetGroupsStatisticResponse(_BaseModel):
    groups: list[GroupStatistic]

class CampaignStatistic(_BaseModel):
    campaign_type: CampaignType = Field(alias='campaignType')
    data: list[StatsData]
    id: int
    name: str
    payment_model: CampaignPaymentModel = Field(alias='paymentModel')
    total_data: StatsData = Field(alias='totalData')

class AdsApiV1GetCampaignStatisticResponse(_BaseModel):
    campaign: CampaignStatistic
    creatives: list[CreativeStatistic]
    groups: list[GroupStatistic]

class ShortAccount(_BaseModel):
    id: int
    short_name: str = Field(alias='shortName')

class ContractType(RootModel[Literal['service', 'intermediary', 'external']]):
    pass

class ContractForChildAccount(_BaseModel):
    account_id: int = Field(default=None, alias='accountID')
    cid: str | None = None
    client: Advertiser = None
    contractor: Advertiser = None
    date: str | None = None
    description: str | None = None
    id: int = None
    is_agent_acting_for_publisher: bool | None = Field(default=None, alias='isAgentActingForPublisher')
    is_creative_reporter: bool | None = Field(default=None, alias='isCreativeReporter')
    number: str | None = None
    object: str | None = None
    parent_id: int | None = Field(default=None, alias='parentId')
    subject: str | None = None
    type: ContractType = None

class ShortAccountWithContract(_BaseModel):
    account: ShortAccount
    contract: ContractForChildAccount = None

class AdsApiV1GetChildAccountsListResponse(_BaseModel):
    children: list[ShortAccountWithContract]

class V1GetAccountBalanceByIdOut(_BaseModel):
    balance: int
    bonus_balance: int = Field(alias='bonusBalance')

class ShortAccountWithBalance(_BaseModel):
    account: ShortAccount
    balance: V1GetAccountBalanceByIdOut

class AdsApiV1GetChildAccountsWithBalancesListResponse(_BaseModel):
    children: list[ShortAccountWithBalance]

class Contract(_BaseModel):
    account_id: int = Field(alias='accountID')
    cid: str | None = None
    client: Advertiser
    contractor: Advertiser
    date: str | None = None
    description: str | None = None
    id: int
    is_agent_acting_for_publisher: bool | None = Field(default=None, alias='isAgentActingForPublisher')
    is_creative_reporter: bool | None = Field(default=None, alias='isCreativeReporter')
    number: str | None = None
    object: str | None = None
    parent_id: int | None = Field(default=None, alias='parentId')
    subject: str | None = None
    type: ContractType

class AdsApiV1GetContractsListResponse(_BaseModel):
    contracts: list[Contract]
    total: int

class AdsApiV1CreateAdvertiserResponse(_BaseModel):
    id: int

class AdsApiV1CreateContractResponse(_BaseModel):
    id: int

class AdsApiV1CreateNonPayerAccountResponse(_BaseModel):
    account_id: int = Field(alias='accountID')
    client_key: str = Field(alias='clientKey')
    client_secret: str = Field(alias='clientSecret')

class LegalInfo(_BaseModel):
    age_restriction: int | None = Field(default=None, alias='ageRestriction')
    description: str | None = None
    kktu: str = None
    notes: str | None = None

class CreativesStatus(RootModel[Literal['draft', 'ready_for_moderation', 'in_moderation', 'moderation_failed', 'erir_registration', 'active', 'paused', 'stopped', 'finished', 'archived']]):
    pass

class Creative(_BaseModel):
    account_id: int = Field(default=None, alias='accountID')
    advertiser_id: int = Field(default=None, alias='advertiserID')
    button_text: str | None = Field(default=None, alias='buttonText')
    campaign_id: int = Field(default=None, alias='campaignID')
    campaign_type: CampaignType = Field(default=None, alias='campaignType')
    description: str | None = None
    group_id: int = Field(default=None, alias='groupID')
    id: int = None
    legal_info: LegalInfo = Field(default=None, alias='legalInfo')
    link: str = None
    manager_id: int = Field(default=None, alias='managerID')
    name: str = None
    payment_model: CampaignPaymentModel = Field(default=None, alias='paymentModel')
    status: CreativesStatus = None
    title: str | None = None
    user_id: int = Field(default=None, alias='userID')

class AdsApiV1GetCreativesListResponse(_BaseModel):
    creatives: list[Creative]
    total: int

class AdsApiV1DeleteUserResponse(_BaseModel):
    pass

class AdsApiV1TransferFundsResponse(_BaseModel):
    pass

class AdsApiV1ChangeBudgetResponse(_BaseModel):
    pass

class AdsApiV1ChangePriceResponse(_BaseModel):
    pass

class ActivityScheduleHours(RootModel[list[int]]):
    pass

class GroupActivityScheduleModel3(_BaseModel):
    friday: ActivityScheduleHours = None
    monday: ActivityScheduleHours = None
    saturday: ActivityScheduleHours = None
    sunday: ActivityScheduleHours = None
    thursday: ActivityScheduleHours = None
    tuesday: ActivityScheduleHours = None
    wednesday: ActivityScheduleHours = None

class AudienceType(RootModel[Literal['basic', 'ready', 'autotargeting']]):
    pass

class BudgetFrequency(RootModel[Literal['weekly', 'entirePeriod']]):
    pass

class GroupFormat(RootModel[Literal['mediaRoot', 'mediaSellerProfile', 'mediaPremium', 'media', 'native', 'htmlPremium', 'html', 'video']]):
    pass

class FrequencyPeriod(RootModel[Literal['no_limit', 'day', 'week', 'month']]):
    pass

class Paces(RootModel[Literal['asap', 'even']]):
    pass

class GroupPriceControl(RootModel[Literal['manual', 'auto']]):
    pass

class ScheduleType(RootModel[Literal['always', 'weekdays9To20', 'custom']]):
    pass

class GroupsStatus(RootModel[Literal['draft', 'in_moderation', 'moderation_failed', 'will_launch_soon', 'active', 'will_stop_soon', 'pausing', 'paused', 'unpausing', 'stopped', 'finished', 'archived']]):
    pass

class Group(_BaseModel):
    account_id: int = Field(default=None, alias='accountID')
    actions: list[str] = None
    activity_schedule: GroupActivityScheduleModel3 = Field(default=None, alias='activitySchedule')
    advertiser_id: int = Field(default=None, alias='advertiserID')
    audience_type: AudienceType = Field(default=None, alias='audienceType')
    budget: int = None
    budget_frequency: BudgetFrequency = Field(default=None, alias='budgetFrequency')
    campaign_id: int = Field(default=None, alias='campaignID')
    campaign_type: CampaignType = Field(default=None, alias='campaignType')
    created_at: str = Field(default=None, alias='createdAt')
    format: GroupFormat = None
    frequency_count: int = Field(alias='frequencyCount')
    frequency_period: FrequencyPeriod = Field(default=None, alias='frequencyPeriod')
    have_creative: bool | None = Field(default=None, alias='haveCreative')
    id: int = None
    manager_id: int = Field(default=None, alias='managerID')
    name: str = None
    pace: Paces = None
    payment_model: CampaignPaymentModel = Field(default=None, alias='paymentModel')
    period_end_at: str | None = Field(default=None, alias='periodEndAt')
    period_start_at: str | None = Field(default=None, alias='periodStartAt')
    period_timezone: str = Field(default=None, alias='periodTimezone')
    price: int = None
    price_control: GroupPriceControl = Field(default=None, alias='priceControl')
    schedule_type: ScheduleType = Field(default=None, alias='scheduleType')
    start_asap: bool = Field(alias='startASAP')
    status: GroupsStatus = None
    targeting_age_ids: list[int] = Field(default=None, alias='targetingAgeIDs')
    targeting_audience_ids: list[str] = Field(default=None, alias='targetingAudienceIDs')
    targeting_family_status_ids: list[int] = Field(default=None, alias='targetingFamilyStatusIDs')
    targeting_gender_ids: list[int] = Field(default=None, alias='targetingGenderIDs')
    targeting_income_ids: list[int] = Field(default=None, alias='targetingIncomeIDs')
    targeting_interest_ids: list[str] = Field(default=None, alias='targetingInterestIDs')
    targeting_location_ids: list[int] = Field(default=None, alias='targetingLocationIDs')
    targeting_parent_status_ids: list[int] = Field(default=None, alias='targetingParentStatusIDs')
    updated_at: str = Field(default=None, alias='updatedAt')
    user_id: int = Field(default=None, alias='userID')

class AdsApiV1GetGroupsListResponse(_BaseModel):
    groups: list[Group]
    total: int

class AdsApiV1SetUserRoleResponse(_BaseModel):
    pass

class UserRole(RootModel[Literal['admin', 'viewer']]):
    pass

class User(_BaseModel):
    has_logged_in: bool = Field(alias='hasLoggedIn')
    id: int
    role: UserRole

class AdsApiV1GetUsersListByAccountResponse(_BaseModel):
    total: int
    users: list[User]

__all__ = ['AccountContactModel1', 'AccountManagerModel2', 'Account', 'AdsApiV1GetAccountByIdResponse', 'AdsApiV1CreateAccountResponse', 'AdsApiV1AddUserResponse', 'LegalRole', 'LegalType', 'Advertiser', 'AdsApiV1GetAdvertisersListResponse', 'AdsApiV1GetAccountBalanceByIdResponse', 'AdsApiV1TransferBonusResponse', 'CampaignType', 'CampaignPaymentModel', 'CampaignStatus', 'Campaign', 'AdsApiV1GetCampaignsListResponse', 'StatsData', 'CreativeStatistic', 'AdsApiV1GetCreativesStatisticResponse', 'GroupStatistic', 'AdsApiV1GetGroupsStatisticResponse', 'CampaignStatistic', 'AdsApiV1GetCampaignStatisticResponse', 'ShortAccount', 'ContractType', 'ContractForChildAccount', 'ShortAccountWithContract', 'AdsApiV1GetChildAccountsListResponse', 'V1GetAccountBalanceByIdOut', 'ShortAccountWithBalance', 'AdsApiV1GetChildAccountsWithBalancesListResponse', 'Contract', 'AdsApiV1GetContractsListResponse', 'AdsApiV1CreateAdvertiserResponse', 'AdsApiV1CreateContractResponse', 'AdsApiV1CreateNonPayerAccountResponse', 'LegalInfo', 'CreativesStatus', 'Creative', 'AdsApiV1GetCreativesListResponse', 'AdsApiV1DeleteUserResponse', 'AdsApiV1TransferFundsResponse', 'AdsApiV1ChangeBudgetResponse', 'AdsApiV1ChangePriceResponse', 'ActivityScheduleHours', 'GroupActivityScheduleModel3', 'AudienceType', 'BudgetFrequency', 'GroupFormat', 'FrequencyPeriod', 'Paces', 'GroupPriceControl', 'ScheduleType', 'GroupsStatus', 'Group', 'AdsApiV1GetGroupsListResponse', 'AdsApiV1SetUserRoleResponse', 'UserRole', 'User', 'AdsApiV1GetUsersListByAccountResponse']
