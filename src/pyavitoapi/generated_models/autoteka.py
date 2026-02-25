"""Generated response models for slug: autoteka."""

from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, ValidationError, Field, RootModel

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class CatalogsFieldAutotekaValuesItemModel1(_BaseModel):
    label: str
    value_id: int = Field(alias='valueId')

class CatalogsFieldAutoteka(_BaseModel):
    data_type: str = Field(alias='dataType')
    id: int
    label: str
    values: list[CatalogsFieldAutotekaValuesItemModel1]

class CatalogsResolveResponseDataAutoteka(_BaseModel):
    fields: list[CatalogsFieldAutoteka]

class AutotekaApiCatalogsResolveResponse(_BaseModel):
    result: CatalogsResolveResponseDataAutoteka = None

class AutotekaApiGetLeadsResponsePaginationModel2(_BaseModel):
    last_id: int | None = Field(default=None, alias='lastId')

class AutotekaApiGetLeadsResponseResultItemModel3PayloadModel4ExtraPayloadModel5PriceAnalyticsModel6(_BaseModel):
    average_days_in_sale: int | None = Field(default=None, alias='averageDaysInSale')
    estimate_sell_price: int = Field(default=None, alias='estimateSellPrice')
    liquidity_rating: str = Field(default=None, alias='liquidityRating')
    seller_price_diff: int | None = Field(default=None, alias='sellerPriceDiff')

class AutotekaApiGetLeadsResponseResultItemModel3PayloadModel4ExtraPayloadModel5TeaserModel7(_BaseModel):
    crashes_badge: bool = Field(alias='crashesBadge')
    real_mileage_badge: bool = Field(alias='realMileageBadge')

class AutotekaApiGetLeadsResponseResultItemModel3PayloadModel4ExtraPayloadModel5(_BaseModel):
    city_name: str | None = Field(default=None, alias='cityName')
    has_pledge: bool | None = Field(default=None, alias='hasPledge')
    is_pro_seller: bool | None = Field(default=None, alias='isProSeller')
    phone_number: str | None = Field(default=None, alias='phoneNumber')
    pledge: str | None = None
    price_analytics: AutotekaApiGetLeadsResponseResultItemModel3PayloadModel4ExtraPayloadModel5PriceAnalyticsModel6 | None = Field(default=None, alias='priceAnalytics')
    region_name: str | None = Field(default=None, alias='regionName')
    seller: str | None = None
    teaser: AutotekaApiGetLeadsResponseResultItemModel3PayloadModel4ExtraPayloadModel5TeaserModel7 | None = None

class AutotekaApiGetLeadsResponseResultItemModel3PayloadModel4TriggerPayloadModel8LastEventsItemModel9(_BaseModel):
    event_date: str = Field(default=None, alias='eventDate')
    event_title: str = Field(default=None, alias='eventTitle')

class AutotekaApiGetLeadsResponseResultItemModel3PayloadModel4TriggerPayloadModel8(_BaseModel):
    last_events: list[AutotekaApiGetLeadsResponseResultItemModel3PayloadModel4TriggerPayloadModel8LastEventsItemModel9] = Field(default=None, alias='lastEvents')

class AutotekaApiGetLeadsResponseResultItemModel3PayloadModel4(_BaseModel):
    brand: str
    condition: str
    control_code: str = Field(alias='controlCode')
    description: str
    extra_payload: AutotekaApiGetLeadsResponseResultItemModel3PayloadModel4ExtraPayloadModel5 = Field(alias='extraPayload')
    item_created_at: str = Field(alias='itemCreatedAt')
    item_id: int = Field(alias='itemId')
    item_updated_at: str = Field(alias='itemUpdatedAt')
    mileage: int
    model: str
    owners: str | None
    price: int
    region_id: int = Field(alias='regionId')
    trigger_payload: AutotekaApiGetLeadsResponseResultItemModel3PayloadModel4TriggerPayloadModel8 = Field(alias='triggerPayload')
    url: str
    vin: str
    year: int

class AutotekaApiGetLeadsResponseResultItemModel3(_BaseModel):
    id: int
    payload: AutotekaApiGetLeadsResponseResultItemModel3PayloadModel4
    subscription_id: int = Field(alias='subscriptionId')

class AutotekaApiGetLeadsResponse(_BaseModel):
    pagination: AutotekaApiGetLeadsResponsePaginationModel2 = None
    result: list[AutotekaApiGetLeadsResponseResultItemModel3] = None

class AutotekaApiMonitoringBucketAddResponseResultModel10InvalidVehiclesItemModel11(_BaseModel):
    description: str = None
    vehicle_id: str = Field(default=None, alias='vehicleID')

class AutotekaApiMonitoringBucketAddResponseResultModel10(_BaseModel):
    invalid_vehicles: list[AutotekaApiMonitoringBucketAddResponseResultModel10InvalidVehiclesItemModel11] = Field(default=None, alias='invalidVehicles')
    is_ok: bool = Field(alias='isOk')

class AutotekaApiMonitoringBucketAddResponse(_BaseModel):
    result: AutotekaApiMonitoringBucketAddResponseResultModel10 = None

class AutotekaApiMonitoringBucketDeleteResponseResultModel12(_BaseModel):
    is_ok: bool = Field(alias='isOk')

class AutotekaApiMonitoringBucketDeleteResponse(_BaseModel):
    result: AutotekaApiMonitoringBucketDeleteResponseResultModel12 = None

class AutotekaApiMonitoringBucketRemoveResponseResultModel13InvalidVehiclesItemModel14(_BaseModel):
    description: str = None
    vehicle_id: str = Field(default=None, alias='vehicleID')

class AutotekaApiMonitoringBucketRemoveResponseResultModel13(_BaseModel):
    invalid_vehicles: list[AutotekaApiMonitoringBucketRemoveResponseResultModel13InvalidVehiclesItemModel14] = Field(default=None, alias='invalidVehicles')
    is_ok: bool = Field(alias='isOk')

class AutotekaApiMonitoringBucketRemoveResponse(_BaseModel):
    result: AutotekaApiMonitoringBucketRemoveResponseResultModel13 = None

class ResponseMonitoringGetRegAction(_BaseModel):
    actual_at: int | None = Field(default=None, alias='actualAt')
    brand: str = None
    model: str = None
    operation_code: int = Field(alias='operationCode')
    operation_date: str = Field(default=None, alias='operationDate')
    operation_date_from: str = Field(default=None, alias='operationDateFrom')
    operation_date_to: str | None = Field(default=None, alias='operationDateTo')
    owner_code: Literal[1, 2, 3, 4] | None = Field(default=None, alias='ownerCode')
    vin: str
    year: int = None

class AutotekaApiMonitoringGetRegActionsResponsePaginationModel15(_BaseModel):
    has_next: bool = Field(default=None, alias='hasNext')
    next_cursor: str = Field(default=None, alias='nextCursor')
    next_link: str = Field(default=None, alias='nextLink')

class AutotekaApiMonitoringGetRegActionsResponse(_BaseModel):
    data: list[ResponseMonitoringGetRegAction]
    pagination: AutotekaApiMonitoringGetRegActionsResponsePaginationModel15

class PackageAutoteka(_BaseModel):
    created_time: str = Field(alias='createdTime')
    expire_time: str = Field(alias='expireTime')
    reports_cnt: int = Field(alias='reportsCnt')
    reports_cnt_remain: int = Field(alias='reportsCntRemain')

class GetActivePackageResponseDataAutoteka(_BaseModel):
    package: PackageAutoteka = None

class AutotekaApiGetActivePackageResponse(_BaseModel):
    result: GetActivePackageResponseDataAutoteka = None

class PreviewIdOnlyAutoteka(_BaseModel):
    preview_id: int = Field(alias='previewId')

class RequestPreviewResponseDataAutoteka(_BaseModel):
    preview: PreviewIdOnlyAutoteka = None

class AutotekaApiPostPreviewByVinResponse(_BaseModel):
    result: RequestPreviewResponseDataAutoteka = None

class PreviewDataAutoteka(_BaseModel):
    brand: str = None
    model: str = None
    sell_by_pro_seller: bool = Field(default=None, alias='sellByProSeller')
    year: int = None

class PreviewAutoteka(_BaseModel):
    data: PreviewDataAutoteka = None
    preview_id: int = Field(alias='previewId')
    reg_number: str = Field(default=None, alias='regNumber')
    status: Literal['success', 'processing', 'notFound'] = None
    vin: str = None

class GetPreviewResponseDataAutoteka(_BaseModel):
    preview: PreviewAutoteka = None

class AutotekaApiGetPreviewResponse(_BaseModel):
    result: GetPreviewResponseDataAutoteka = None

class ReportWithoutDataAutoteka(_BaseModel):
    report_id: int = Field(alias='reportId')
    status: Literal['success', 'processing']

class CreateReportResponseDataAutoteka(_BaseModel):
    report: ReportWithoutDataAutoteka = None

class AutotekaApiPostReportResponse(_BaseModel):
    result: CreateReportResponseDataAutoteka = None

class AutotekaApiPostReportByVehicleIdResponse(_BaseModel):
    result: CreateReportResponseDataAutoteka = None

class ReportItemAutoteka(_BaseModel):
    created_at: str = Field(alias='createdAt')
    report_id: int = Field(alias='reportId')
    vin: str

class AutotekaApiGetReportListResponse(_BaseModel):
    result: list[ReportItemAutoteka]

class CrashesHistoryAutotekaDamageTypesItemModel17(_BaseModel):
    description: str = None
    slug: Literal['front-right', 'right-front-door', 'front-right-side', 'left-front', 'left-front-door', 'left-front-side', 'right-rear', 'right-rear-door', 'right-rear-side', 'left-rear', 'left-rear-door', 'left-rear-side', 'roof', 'bottom', 'front-hood', 'rear-hood'] = None
    type: Literal['yellow', 'red', 'other'] = None

class CrashesHistoryAutoteka(_BaseModel):
    additional: list[str]
    clearance_type: str | None = Field(default=None, alias='clearanceType')
    damage_map: list[str] = Field(alias='damageMap')
    damage_types: list[CrashesHistoryAutotekaDamageTypesItemModel17] = Field(alias='damageTypes')
    date: int
    region: str
    type: str

class ReportDataAutotekaAccidentsModel16(_BaseModel):
    crashes_history: list[CrashesHistoryAutoteka] = Field(alias='crashesHistory')
    request_time: int | None = Field(alias='requestTime')

class ArbitrationCasesCasesItemModel18(_BaseModel):
    case_id: str = Field(alias='caseId')
    case_number: str = Field(alias='caseNumber')
    case_url: str = Field(alias='caseUrl')
    content_types: list[str] = Field(alias='contentTypes')
    court: str
    file_name: str = Field(alias='fileName')
    file_url: str = Field(alias='fileUrl')
    instance_level: int = Field(alias='instanceLevel')
    instance_number: str = Field(alias='instanceNumber')
    registration_date: int = Field(alias='registrationDate')
    type: str

class ArbitrationCases(_BaseModel):
    cases: list[ArbitrationCasesCasesItemModel18] = None

class AvitoAuctionsAuctionsItemModel19(_BaseModel):
    date: str = None
    deal: bool = None
    images: list[str] = None
    mileage: int = None
    region: str = None

class AvitoAuctions(_BaseModel):
    auctions: list[AvitoAuctionsAuctionsItemModel19] = None

class AvitoItemAutotekaImagesItemModel20(_BaseModel):
    original_url: str = Field(alias='originalUrl')
    preview_url: str = Field(alias='previewUrl')
    thumbnail_url: str = Field(alias='thumbnailUrl')

class AvitoItemAutoteka(_BaseModel):
    date: str
    description: str
    images: list[AvitoItemAutotekaImagesItemModel20]
    is_crashed: bool = Field(alias='isCrashed')
    mileage: int
    price: int
    title: str

class AvitoPriceValuationMarketNormalPriceRangeModel21(_BaseModel):
    max: int
    min: int

class AvitoPriceValuation(_BaseModel):
    avg_market_price: int | None = Field(default=None, alias='avgMarketPrice')
    avg_mileage: int | None = Field(default=None, alias='avgMileage')
    avg_price_with_condition: int = Field(alias='avgPriceWithCondition')
    avg_year: float | None = Field(default=None, alias='avgYear')
    imv_url: str | None = Field(default=None, alias='imvUrl')
    items_count: int | None = Field(default=None, alias='itemsCount')
    market_normal_price_range: AvitoPriceValuationMarketNormalPriceRangeModel21 | None = Field(default=None, alias='marketNormalPriceRange')
    max_price: int | None = Field(default=None, alias='maxPrice')
    min_price: int | None = Field(default=None, alias='minPrice')

class CarImageAutoteka(_BaseModel):
    original_url: str = Field(alias='originalUrl')
    preview_url: str = Field(alias='previewUrl')

class CarsharingDataEventAutoteka(_BaseModel):
    company: str
    inaccurate_data: bool = Field(alias='inaccurateData')

class RecapAutoteka(_BaseModel):
    description: str | None
    label: str
    status: str
    type: str

class CarsharingDataAutoteka(_BaseModel):
    events: list[CarsharingDataEventAutoteka]
    recaps: list[RecapAutoteka]

class Customs(_BaseModel):
    color: str | None
    company: str | None = None
    created_at: int | None = Field(alias='createdAt')
    ecology: str | None
    from_country: str | None = Field(alias='fromCountry')
    mileage: int | None
    owner: str | None
    specification: str | None
    stat_price: float | None = Field(alias='statPrice')
    to_country: str | None = Field(alias='toCountry')

class DiagnosticsEventConditionModel22(_BaseModel):
    issues: list[str]

class DiagnosticsEventDamage(_BaseModel):
    degree: str | None
    part: str
    photo_url: str | None = Field(alias='photoUrl')
    type: str

class DiagnosticsEventPhoto(_BaseModel):
    name: str
    url: str

class DiagnosticsEvent(_BaseModel):
    city: str
    condition: DiagnosticsEventConditionModel22
    created_at: int = Field(alias='createdAt')
    damages: list[DiagnosticsEventDamage]
    dealer_name: str = Field(alias='dealerName')
    mileage: int
    photos: list[DiagnosticsEventPhoto]
    region: str

class Diagnostics(_BaseModel):
    events: list[DiagnosticsEvent]
    request_time: int = Field(alias='requestTime')

class Epts(_BaseModel):
    customs_clearance: str = Field(alias='customsClearance')
    customs_restrictions: str = Field(alias='customsRestrictions')
    last_action: str = Field(alias='lastAction')
    other_restrictions: str = Field(alias='otherRestrictions')
    recycling_fee: str = Field(alias='recyclingFee')
    status: str
    type: str

class EquipmentAutotekaBodyModel23(_BaseModel):
    description: Literal['Микроавтобус', 'Кабриолет', 'Купе', 'Кроссовер', 'Универсал', 'Минивэн', 'Хэтчбек', 'Внедорожник', 'Пикап', 'Седан', 'Фургон', 'Лимузин']
    title: str
    value: int

class EquipmentAutotekaBodyNumberModel24(_BaseModel):
    title: str
    value: str

class EquipmentAutotekaBrandModel25(_BaseModel):
    title: str
    value: Literal['AUDI', 'BENTLEY', 'BMW', 'CADILLAC', 'CHERY', 'CHEVROLET', 'CHRYSLER', 'CITROEN', 'DACIA', 'DAEWOO', 'DAF', 'DATSUN', 'DODGE', 'FIAT', 'FORD', 'FREIGHTLINER', 'GAZ', 'GEELY', 'GENESIS', 'GREAT WALL', 'HONDA', 'HYUNDAI', 'Honda', 'INFINITI', 'ISUZU', 'IVECO', 'JEEP', 'Jaguar', 'KAMAZ', 'KIA', 'LADA', 'LEXUS', 'LIFAN', 'Land Rover', 'MAN', 'MAZ', 'MAZDA', 'MERCEDES', 'MERCEDES-BENZ', 'MINI', 'MITSUBISHI', 'NISSAN', 'OPEL', 'PEUGEOT', 'PORSCHE', 'RENAULT', 'ROVER', 'SEAZ', 'SKODA', 'SMART', 'SSANGYONG', 'SUBARU', 'Suzuki', 'TAGAZ', 'TOYOTA', 'UAZ', 'VAZ', 'VOLKSWAGEN', 'VOLVO', 'YAMAHA', 'ZAZ']

class EquipmentAutotekaChasisNumberModel26(_BaseModel):
    title: str
    value: str

class EquipmentAutotekaColorModel27(_BaseModel):
    description: str
    title: str
    value: Literal['Бежево-Серый', 'Бежевый', 'Белый', 'Белый Металлик', 'Белый Перламутр', 'Белый Черный', 'Белый-Желтый-Серый', 'Белый/Черный', 'Бордовый', 'Бронзовый', 'Вишнево-Красный', 'Жемчужно-Белый', 'Зеленый', 'Золотисто-Коричневый', 'Золотисто-Охристый', 'Коричневый', 'Красный', 'Мальва', 'Многоцветный (Красный, Чёрный)', 'Мурена (Тёмно-Синий)', 'Оранжево-Красный', 'Оранжево-Черный', 'Оранжевый', 'Оранжевый Перламутровый', 'Оранжевый Черный', 'Перлам-Серебристый', 'Перламутрово-Серебристый', 'Светло-Коричневый', 'Светло-Серый', 'Светло-Синий', 'Серебристо-Белый', 'Серебристый', 'Серо Зеленый', 'Серо-Зеленый', 'Серо-Золотистый', 'Серо-Коричневый', 'Серо-Сине-Зеленый Металлик', 'Серо-Синий', 'Серый', 'Сине-Черный', 'Синий', 'Синий Темный', 'Скат', 'Средний Серо-Зеленый', 'Стальной', 'Темно Серый', 'Темно-Бордовый', 'Темно-Вишневый', 'Темно-Голубой', 'Темно-Зеленый', 'Темно-Серый', 'Темно-Синий', 'Черно-Серый', 'Черный', 'Черный Металлик']

class EquipmentAutotekaDriveModel28(_BaseModel):
    description: str
    title: str
    value: int

class EquipmentAutotekaEngineNumberModel29(_BaseModel):
    title: str
    value: str

class EquipmentAutotekaEngineTypeModel30(_BaseModel):
    title: str
    value: Literal['Бензин', 'Дизель', 'Электро', 'Газ', 'Гибрид', 'Бензиновый на сжиженном газе', 'Бензиновый на сжатом газе', 'Дизельный на сжиженном газе', 'Дизельный на сжатом газе', 'Электро-бензиновый', 'Электро-дизельный']

class EquipmentAutotekaEquipmentModel31(_BaseModel):
    title: str
    value: str

class EquipmentAutotekaHorsepowerModel32(_BaseModel):
    description: str
    title: str
    value: int

class EquipmentAutotekaMaxWeightModel33(_BaseModel):
    description: str
    title: str
    value: int

class EquipmentAutotekaModelModel34(_BaseModel):
    title: str
    value: str

class EquipmentAutotekaModificationModel35(_BaseModel):
    title: str
    value: str

class EquipmentAutotekaNetWeightModel36(_BaseModel):
    description: str
    title: str
    value: int

class EquipmentAutotekaTransmissionModel37(_BaseModel):
    description: str
    title: str
    value: int

class EquipmentAutotekaVehicleModel38(_BaseModel):
    description: str
    title: str
    value: int

class EquipmentAutotekaVehicleCategoryModel39(_BaseModel):
    title: str
    value: Literal['A', 'B', 'C', 'D', 'E', 'O', 'M1', 'M1G', 'N1']

class EquipmentAutotekaVehicleTypeModel40(_BaseModel):
    title: str
    value: Literal['Автобусы прочие', 'Грузовой бортовой', 'Грузовой прочий', 'Грузовой фургон', 'Грузовые автомобили бортовые', 'Грузовые автомобили фургоны', 'Легковое купе', 'Легковой прочий', 'Легковой седан', 'Легковой универсал', 'Легковой хэтчбек (комби)', 'Легковые автомобили кабриолет', 'Легковые автомобили комби (хэтчбек)', 'Легковые автомобили купе', 'Легковые автомобили прочие', 'Легковые автомобили седан', 'Легковые автомобили универсал', 'Мотоциклы']

class EquipmentAutotekaVolumeModel41(_BaseModel):
    description: str
    title: str
    value: int

class EquipmentAutotekaYearModel42(_BaseModel):
    title: str
    value: int

class EquipmentAutoteka(_BaseModel):
    body: EquipmentAutotekaBodyModel23
    body_number: EquipmentAutotekaBodyNumberModel24 | None = Field(alias='bodyNumber')
    brand: EquipmentAutotekaBrandModel25
    chasis_number: EquipmentAutotekaChasisNumberModel26 | None = Field(alias='chasisNumber')
    color: EquipmentAutotekaColorModel27
    drive: EquipmentAutotekaDriveModel28
    engine_number: EquipmentAutotekaEngineNumberModel29 | None = Field(alias='engineNumber')
    engine_type: EquipmentAutotekaEngineTypeModel30 = Field(alias='engineType')
    equipment: EquipmentAutotekaEquipmentModel31
    horsepower: EquipmentAutotekaHorsepowerModel32
    max_weight: EquipmentAutotekaMaxWeightModel33 = Field(alias='maxWeight')
    model: EquipmentAutotekaModelModel34
    modification: EquipmentAutotekaModificationModel35
    net_weight: EquipmentAutotekaNetWeightModel36 = Field(alias='netWeight')
    transmission: EquipmentAutotekaTransmissionModel37
    vehicle: EquipmentAutotekaVehicleModel38
    vehicle_category: EquipmentAutotekaVehicleCategoryModel39 = Field(alias='vehicleCategory')
    vehicle_type: EquipmentAutotekaVehicleTypeModel40 = Field(alias='vehicleType')
    volume: EquipmentAutotekaVolumeModel41
    year: EquipmentAutotekaYearModel42

class EventsAutotekaAvitoOnSaleModel43AdditionalInfoModel44(_BaseModel):
    date: int
    price: int
    title: str
    url: str

class EventsAutotekaAvitoOnSaleModel43(_BaseModel):
    additional_info: EventsAutotekaAvitoOnSaleModel43AdditionalInfoModel44 = Field(alias='additionalInfo')
    description: str
    type: str
    value: bool

class EventsAutotekaBodyRepairModel45(_BaseModel):
    description: str
    type: str
    value: bool

class EventsAutotekaCrashesModel46(_BaseModel):
    description: str
    type: str
    value: bool

class EventsAutotekaDealerDataAvailableModel47(_BaseModel):
    description: str
    type: str
    value: bool

class EventsAutotekaFirstSellDateModel48(_BaseModel):
    type: str
    value: str

class EventsAutotekaLastMileageRecordModel49(_BaseModel):
    description: str
    type: str
    value: int

class EventsAutotekaOwnersModel50(_BaseModel):
    description: str
    type: str
    value: int

class EventsAutotekaPledgeModel51(_BaseModel):
    description: str
    type: str
    value: bool

class EventsAutotekaPublicPersonModel52(_BaseModel):
    description: str
    type: str
    value: bool

class EventsAutoteka(_BaseModel):
    avito_on_sale: EventsAutotekaAvitoOnSaleModel43 = Field(alias='avitoOnSale')
    body_repair: EventsAutotekaBodyRepairModel45 = Field(alias='bodyRepair')
    crashes: EventsAutotekaCrashesModel46
    dealer_data_available: EventsAutotekaDealerDataAvailableModel47 = Field(alias='dealerDataAvailable')
    first_sell_date: EventsAutotekaFirstSellDateModel48 = Field(alias='firstSellDate')
    last_mileage_record: EventsAutotekaLastMileageRecordModel49 = Field(alias='lastMileageRecord')
    owners: EventsAutotekaOwnersModel50
    pledge: EventsAutotekaPledgeModel51
    public_person: EventsAutotekaPublicPersonModel52 = Field(alias='publicPerson')

class EventsOthersHistoryAutoteka(_BaseModel):
    date: int
    description: str
    event: str
    mileage: int
    operation_code_id: int | None = Field(default=None, alias='operationCodeId')
    source: str
    source_id: int | None = Field(default=None, alias='sourceId')
    type: str

class ExtendedSpecificationsParam(_BaseModel):
    id: int | None
    key: Literal['brand', 'brandId', 'model', 'modelId', 'body_type', 'kolichestvo_dverey', 'drive', 'wheel', 'generation', 'engine_type', 'transmission', 'complectation', 'modification', 'engine', 'capacity', 'year']
    name: Literal['Бренд', 'Идентификатор бренда', 'Модель', 'Идентификатор модели', 'Тип автомобиля', 'Количество дверей', 'Привод', 'Руль', 'Поколение', 'Тип двигателя', 'Коробка передач', 'Комплектация', 'Модификация', 'Мощность двигателя', 'Объем двигателя', 'Год выпуска']
    value: str
    value_id: int | None = Field(alias='valueId')

class ExtendedSpecifications(_BaseModel):
    events: list[ExtendedSpecificationsParam]
    request_time: int = Field(alias='requestTime')

class ExternalPlacementAutoteka(_BaseModel):
    city: str | None
    date: str
    is_crashed: bool = Field(alias='isCrashed')
    mileage: int | None
    price: int | None
    region: str | None
    url: str

class FineEventAutoteka(_BaseModel):
    created_at: int = Field(alias='createdAt')
    date_incident: int | None = Field(alias='dateIncident')
    koap_code: str = Field(alias='koapCode')
    koap_text: str = Field(alias='koapText')
    num_post: str | None = Field(alias='numPost')
    status: str
    sum: int

class FinesAutoteka(_BaseModel):
    events: list[FineEventAutoteka]
    recaps: list[RecapAutoteka]
    request_time: int | None = Field(default=None, alias='requestTime')

class HeadAutotekaRegNumbersHistoryItemModel53(_BaseModel):
    number: str

class HeadAutoteka(_BaseModel):
    brand: Literal['AUDI', 'BENTLEY', 'BMW', 'CADILLAC', 'CHERY', 'CHEVROLET', 'CHRYSLER', 'CITROEN', 'DACIA', 'DAEWOO', 'DAF', 'DATSUN', 'DODGE', 'FIAT', 'FORD', 'FREIGHTLINER', 'GAZ', 'GEELY', 'GENESIS', 'GREAT WALL', 'HONDA', 'HYUNDAI', 'Honda', 'INFINITI', 'ISUZU', 'IVECO', 'JEEP', 'Jaguar', 'KAMAZ', 'KIA', 'LADA', 'LEXUS', 'LIFAN', 'Land Rover', 'MAN', 'MAZ', 'MAZDA', 'MERCEDES', 'MERCEDES-BENZ', 'MINI', 'MITSUBISHI', 'NISSAN', 'OPEL', 'PEUGEOT', 'PORSCHE', 'RENAULT', 'ROVER', 'SEAZ', 'SKODA', 'SMART', 'SSANGYONG', 'SUBARU', 'Suzuki', 'TAGAZ', 'TOYOTA', 'UAZ', 'VAZ', 'VOLKSWAGEN', 'VOLVO', 'YAMAHA', 'ZAZ']
    created_at: int = Field(alias='createdAt')
    model: str
    reg_number: str | None = Field(default=None, alias='regNumber')
    reg_numbers_history: list[HeadAutotekaRegNumbersHistoryItemModel53] | None = Field(default=None, alias='regNumbersHistory')
    vehicle_identifier_type: Literal['vin', 'frame', 'unknown'] = Field(default=None, alias='vehicleIdentifierType')
    vin: str
    year: int

class Insights(_BaseModel):
    is_imported: bool | None = Field(alias='isImported')

class InsurancePaymentsItem(_BaseModel):
    company_name: str | None = Field(alias='companyName')
    is_court_payment: bool | None = Field(default=None, alias='isCourtPayment')
    is_for_victim: bool = Field(alias='isForVictim')
    month: int | None = None
    payment_amount: float = Field(alias='paymentAmount')
    year: int

class InsurancePayments(RootModel[list[InsurancePaymentsItem]]):
    pass

class InsurancePolicyEventAutoteka(_BaseModel):
    company_name: str = Field(alias='companyName')
    create_date: int = Field(alias='createDate')
    end_date: int = Field(alias='endDate')
    has_trailer: bool | None = Field(default=None, alias='hasTrailer')
    is_transit: bool | None = Field(default=None, alias='isTransit')
    kmb: float | None = None
    policy_is_restrict: bool | None = Field(default=None, alias='policyIsRestrict')
    policy_number: str | None = Field(default=None, alias='policyNumber')
    policy_serial: str | None = Field(default=None, alias='policySerial')
    restriction_count: int | None = Field(default=None, alias='restrictionCount')
    start_date: int = Field(alias='startDate')
    status: str | None = None
    usage_target: str | None = Field(default=None, alias='usageTarget')

class InsurancePoliciesAutoteka(_BaseModel):
    events: list[InsurancePolicyEventAutoteka]
    recaps: list[RecapAutoteka]

class LeasingContractsItemModel54(_BaseModel):
    contract_date: int | None = Field(default=None, alias='contractDate')
    end_date: int | None = Field(default=None, alias='endDate')
    lessee_name: str | None = Field(default=None, alias='lesseeName')
    lessor_name: str | None = Field(default=None, alias='lessorName')
    start_date: int | None = Field(default=None, alias='startDate')

class Leasing(_BaseModel):
    contracts: list[LeasingContractsItemModel54] = None

class MaxPosterPriceValuationAnalyticByActualSalesModel55(_BaseModel):
    avg_price_with_correction: int = Field(alias='avgPriceWithCorrection')
    max_price_with_correction: int = Field(alias='maxPriceWithCorrection')
    min_price_with_correction: int = Field(alias='minPriceWithCorrection')
    price_position: int = Field(alias='pricePosition')

class MaxPosterPriceValuationAnalyticByCompletedSalesModel56(_BaseModel):
    avg_days_in_sale: int = Field(alias='avgDaysInSale')
    avg_mileage: int = Field(alias='avgMileage')
    avg_price: int = Field(alias='avgPrice')
    avg_price_with_correction: int = Field(alias='avgPriceWithCorrection')
    avg_year: float = Field(alias='avgYear')
    max_price: int = Field(alias='maxPrice')
    max_price_with_correction: int = Field(alias='maxPriceWithCorrection')
    max_purchase_price: int | None = Field(alias='maxPurchasePrice')
    min_price: int = Field(alias='minPrice')
    min_price_with_correction: int = Field(alias='minPriceWithCorrection')
    min_purchase_price: int | None = Field(alias='minPurchasePrice')
    price_position: int = Field(alias='pricePosition')
    recommended_purchase_price: int | None = Field(alias='recommendedPurchasePrice')
    useful_sales_total: int = Field(alias='usefulSalesTotal')

class MaxPosterValuationLiquidityRating(_BaseModel):
    attention_code: str = Field(alias='attentionCode')
    rating: str
    rating_value: int = Field(alias='ratingValue')

class MaxPosterPriceValuationLiquidityModel57(_BaseModel):
    accident_rating: MaxPosterValuationLiquidityRating = Field(alias='accidentRating')
    actual_market_sales: int | None = Field(default=None, alias='actualMarketSales')
    average_days_in_sale: int = Field(alias='averageDaysInSale')
    average_market_mileage: int = Field(alias='averageMarketMileage')
    completed_market_sales: int | None = Field(default=None, alias='completedMarketSales')
    mileage_rating: MaxPosterValuationLiquidityRating = Field(alias='mileageRating')
    popularity_rating: MaxPosterValuationLiquidityRating = Field(alias='popularityRating')
    total_market_sales: int = Field(alias='totalMarketSales')
    total_rating: MaxPosterValuationLiquidityRating = Field(alias='totalRating')
    turnover_rating: MaxPosterValuationLiquidityRating = Field(alias='turnoverRating')

class MaxPosterPriceValuation(_BaseModel):
    analytic_by_actual_sales: MaxPosterPriceValuationAnalyticByActualSalesModel55 | None = Field(default=None, alias='analyticByActualSales')
    analytic_by_completed_sales: MaxPosterPriceValuationAnalyticByCompletedSalesModel56 = Field(alias='analyticByCompletedSales')
    liquidity: MaxPosterPriceValuationLiquidityModel57

class OtherAutoteka(_BaseModel):
    status: str
    text: str
    type: str

class OwnersHistoryAutoteka(_BaseModel):
    organisation_name: str | None = Field(default=None, alias='organisationName')
    owner: str
    period: str
    region: str
    title: str
    type: int

class PriceStatReportAutotekaPriceModel58(_BaseModel):
    average: int = None
    highest: int = None
    lowest: int = None

class PriceStatReportAutoteka(_BaseModel):
    adverts_count: int | None = Field(default=None, alias='advertsCount')
    average_mileage: int | None = Field(default=None, alias='averageMileage')
    average_owners_count: float | None = Field(default=None, alias='averageOwnersCount')
    price: PriceStatReportAutotekaPriceModel58 | None = None

class PriceStatAutoteka(_BaseModel):
    recaps: list[RecapAutoteka]
    report: PriceStatReportAutoteka
    status: Literal['incomplete', 'ok']
    type: str

class PriceStatForNewCarsAutotekaItemsItemModel59PricesItemModel60(_BaseModel):
    price: int
    pwt: str
    trim: str

class PriceStatForNewCarsAutotekaItemsItemModel59(_BaseModel):
    name: str
    prices: list[PriceStatForNewCarsAutotekaItemsItemModel59PricesItemModel60]

class PriceStatForNewCarsAutotekaPriceModel61(_BaseModel):
    highest: int = None
    lowest: int = None
    median: int = None

class PriceStatForNewCarsAutoteka(_BaseModel):
    items: list[PriceStatForNewCarsAutotekaItemsItemModel59] = None
    price: PriceStatForNewCarsAutotekaPriceModel61 = None

class PtsDataPtsModel62(_BaseModel):
    created_at: int | None = Field(default=None, alias='createdAt')
    organization: str | None = None
    pts_number: str = Field(default=None, alias='ptsNumber')
    request_time: int = Field(default=None, alias='requestTime')

class PtsDataStsModel63(_BaseModel):
    created_at: int | None = Field(default=None, alias='createdAt')
    request_time: int = Field(default=None, alias='requestTime')
    sts_number: str = Field(default=None, alias='stsNumber')

class PtsData(_BaseModel):
    pts: PtsDataPtsModel62 = None
    sts: PtsDataStsModel63 = None

class RecallItemCompleteInfoModel64(_BaseModel):
    city: str | None = None
    completed_at: str = Field(default=None, alias='completedAt')
    dealer_name: str | None = Field(default=None, alias='dealerName')
    mileage: int | None = None
    region: str | None = None

class RecallItem(_BaseModel):
    complaint_code: str | None = Field(default=None, alias='complaintCode')
    complete_info: RecallItemCompleteInfoModel64 | None = Field(default=None, alias='completeInfo')
    completeness_status: bool = Field(default=None, alias='completenessStatus')
    created_at: str = Field(alias='createdAt')
    link: str | None
    organization: str
    reason: str
    recommendation: str | None

class Recalls(RootModel[list[RecallItem]]):
    pass

class ReportDataAutotekaRegistrationActionsModel65(_BaseModel):
    owners_history: list[OwnersHistoryAutoteka] = Field(alias='ownersHistory')
    request_time: int | None = Field(alias='requestTime')

class RestrictionsAutotekaPledgeModel66HistoryModel67PledgesItemModel68(_BaseModel):
    closed_at: int | None = Field(alias='closedAt')
    contract_end: int | None = Field(alias='contractEnd')
    contract_start: int | None = Field(alias='contractStart')
    notification_id: str = Field(alias='notificationId')
    organization_name: str | None = Field(alias='organizationName')

class RestrictionsAutotekaPledgeModel66HistoryModel67(_BaseModel):
    pledges: list[RestrictionsAutotekaPledgeModel66HistoryModel67PledgesItemModel68] = None

class RestrictionsAutotekaPledgeModel66PledgeAdditionalDataItemModel69DataItemModel70(_BaseModel):
    date_from: int | None = Field(alias='dateFrom')
    date_to: int = Field(alias='dateTo')
    organization_name: str | None = Field(alias='organizationName')

class RestrictionsAutotekaPledgeModel66PledgeAdditionalDataItemModel69(_BaseModel):
    data: list[RestrictionsAutotekaPledgeModel66PledgeAdditionalDataItemModel69DataItemModel70]
    date_from: int | None = Field(default=None, alias='dateFrom')
    has_pledge: bool = Field(alias='hasPledge')
    organization_name: str | None = Field(default=None, alias='organizationName')
    source: str
    updated_at: int = Field(alias='updatedAt')

class RestrictionsAutotekaPledgeModel66(_BaseModel):
    history: RestrictionsAutotekaPledgeModel66HistoryModel67 | None
    pledge_additional_data: list[RestrictionsAutotekaPledgeModel66PledgeAdditionalDataItemModel69] = Field(alias='pledgeAdditionalData')
    request_time: int | None = Field(alias='requestTime')
    status: Literal['ok', 'warning', 'incomplete']
    text: str

class RestrictionsAutotekaRegistrationModel71AdditionalInfoItemModel72(_BaseModel):
    amount: float | None = None
    data: str
    document_type: str | None = Field(default=None, alias='documentType')
    event_date: str = Field(alias='eventDate')
    organisation_name: str = Field(alias='organisationName')
    reasons: str | None = None
    region: str
    restriction_name: str = Field(alias='restrictionName')
    source: str

class RestrictionsAutotekaRegistrationModel71(_BaseModel):
    additional_info: list[RestrictionsAutotekaRegistrationModel71AdditionalInfoItemModel72] = Field(alias='additionalInfo')
    request_time: int | None = Field(alias='requestTime')
    status: Literal['ok', 'warning', 'incomplete']
    text: str

class RestrictionsAutotekaStealingModel73AdditionalInfoItemModel74(_BaseModel):
    data: str
    source: str

class RestrictionsAutotekaStealingModel73(_BaseModel):
    additional_info: list[RestrictionsAutotekaStealingModel73AdditionalInfoItemModel74] = Field(alias='additionalInfo')
    request_time: int | None = Field(alias='requestTime')
    status: Literal['ok', 'warning', 'incomplete']
    text: str

class RestrictionsAutoteka(_BaseModel):
    pledge: RestrictionsAutotekaPledgeModel66
    registration: RestrictionsAutotekaRegistrationModel71
    stealing: RestrictionsAutotekaStealingModel73

class SalvageCarAuctionRecordsItemModel75(_BaseModel):
    auction: str
    date: str
    description: str | None = None
    images: list[str] = None
    mileage: int | None = None
    region: str | None = None

class SalvageCarAuctionRecords(RootModel[list[SalvageCarAuctionRecordsItemModel75]]):
    pass

class ServiceInfoAutotekaReportCompleteStatusModel76UnavailableSourcesItemModel77(_BaseModel):
    data_type: str = Field(alias='dataType')
    source: str

class ServiceInfoAutotekaReportCompleteStatusModel76(_BaseModel):
    status: str
    unavailable_sources: list[ServiceInfoAutotekaReportCompleteStatusModel76UnavailableSourcesItemModel77] = Field(alias='unavailableSources')

class ServiceInfoAutoteka(_BaseModel):
    report_complete_status: ServiceInfoAutotekaReportCompleteStatusModel76 = Field(alias='reportCompleteStatus')

class TaxiDataEventAutoteka(_BaseModel):
    date_from: int = Field(alias='dateFrom')
    date_to: int | None = Field(default=None, alias='dateTo')
    is_actual: bool = Field(alias='isActual')
    permit_number: str = Field(alias='permitNumber')
    region_name: str = Field(alias='regionName')

class TaxiDataAutoteka(_BaseModel):
    events: list[TaxiDataEventAutoteka]
    recaps: list[RecapAutoteka]
    request_time: int | None = Field(default=None, alias='requestTime')

class AutotekaTeaser(_BaseModel):
    has_regular_service: bool = Field(alias='hasRegularService')
    is_one_owner: bool = Field(alias='isOneOwner')
    is_real_mileage: bool = Field(alias='isRealMileage')
    without_crashes: bool = Field(alias='withoutCrashes')

class TechInspectionHistoryEvent(_BaseModel):
    card_number: str | None = Field(alias='cardNumber')
    end_date: int | None = Field(alias='endDate')
    mileage: int | None
    start_date: int = Field(alias='startDate')

class TechInspectionHistory(_BaseModel):
    events: list[TechInspectionHistoryEvent]

class VehicleSpecificationsParam(_BaseModel):
    key: Literal['mainModel', 'model', 'transmission', 'doors', 'manufactured']
    name: Literal['Обозначение модели', 'Код модели автомобиля', 'Тип коробки передач', 'Количество дверей', 'Модельный год']
    value: Literal['LEXUS NX200T/300H', 'AGZ15R-AWTLTW', '6-ступенч. АКПП ZF 6HP28', '4', '2008']

class VehicleSpecifications(_BaseModel):
    events: list[VehicleSpecificationsParam]
    request_time: int = Field(alias='requestTime')

class ReportDataAutoteka(_BaseModel):
    accidents: ReportDataAutotekaAccidentsModel16
    arbitration_cases: ArbitrationCases = Field(alias='arbitrationCases')
    avito_auctions: AvitoAuctions = Field(alias='avitoAuctions')
    avito_items: list[AvitoItemAutoteka] = Field(alias='avitoItems')
    avito_price_valuation: AvitoPriceValuation = Field(default=None, alias='avitoPriceValuation')
    car_image: CarImageAutoteka = Field(alias='carImage')
    carsharing_data: CarsharingDataAutoteka = Field(default=None, alias='carsharingData')
    crashes_history: list[CrashesHistoryAutoteka] = Field(alias='crashesHistory')
    customs: Customs
    diagnostics: Diagnostics
    epts: Epts = None
    equipment: EquipmentAutoteka
    events: EventsAutoteka
    events_others_history: list[EventsOthersHistoryAutoteka] = Field(alias='eventsOthersHistory')
    extended_specifications: ExtendedSpecifications = Field(default=None, alias='extendedSpecifications')
    external_placements: list[ExternalPlacementAutoteka] | None = Field(default=None, alias='externalPlacements')
    fines: FinesAutoteka = None
    head: HeadAutoteka
    insights: Insights = None
    insurance_payments: InsurancePayments = Field(alias='insurancePayments')
    insurance_policies: InsurancePoliciesAutoteka = Field(default=None, alias='insurancePolicies')
    leasing: Leasing
    max_poster_price_valuation: MaxPosterPriceValuation = Field(default=None, alias='maxPosterPriceValuation')
    other: list[OtherAutoteka]
    owners_history: list[OwnersHistoryAutoteka] = Field(alias='ownersHistory')
    paid_fines: FinesAutoteka = Field(default=None, alias='paidFines')
    price_stat: PriceStatAutoteka = Field(default=None, alias='priceStat')
    price_stat_for_new_cars: PriceStatForNewCarsAutoteka = Field(default=None, alias='priceStatForNewCars')
    pts_data: PtsData = Field(alias='ptsData')
    pts_type: str | None = Field(default=None, alias='ptsType')
    recalls: Recalls
    registration_actions: ReportDataAutotekaRegistrationActionsModel65 = Field(alias='registrationActions')
    restrictions: RestrictionsAutoteka
    salvage_car_auction_records: SalvageCarAuctionRecords = Field(alias='salvageCarAuctionRecords')
    service_info: ServiceInfoAutoteka = Field(alias='serviceInfo')
    taxi_data: TaxiDataAutoteka = Field(default=None, alias='taxiData')
    teaser: AutotekaTeaser = None
    tech_inspection_history: TechInspectionHistory = Field(alias='techInspectionHistory')
    vehicle_specifications: VehicleSpecifications = Field(default=None, alias='vehicleSpecifications')

class ReportAutotekaAsync(_BaseModel):
    data: ReportDataAutoteka = None
    pdf_link: str = Field(default=None, alias='pdfLink')
    report_id: int = Field(alias='reportId')
    status: Literal['success', 'processing']
    web_link: str = Field(default=None, alias='webLink')

class GetReportResultAsync(_BaseModel):
    report: ReportAutotekaAsync = None

class AutotekaApiGetReportResponse(_BaseModel):
    result: GetReportResultAsync = None

class AutotekaApiPostPreviewByExternalItemResponse(_BaseModel):
    result: RequestPreviewResponseDataAutoteka = None

class AutotekaApiPostPreviewByItemIdResponse(_BaseModel):
    result: RequestPreviewResponseDataAutoteka = None

class AutotekaApiPostPreviewByRegNumberResponse(_BaseModel):
    result: RequestPreviewResponseDataAutoteka = None

class ScoringIdResultAutoteka(_BaseModel):
    scoring_id: int = Field(alias='scoringId')

class CreateScoringResponseDataAutoteka(_BaseModel):
    scoring: ScoringIdResultAutoteka = None

class AutotekaApiScoringByVehicleIdResponse(_BaseModel):
    result: CreateScoringResponseDataAutoteka = None

class ScoringAccidents(_BaseModel):
    relevance_date: int = Field(alias='relevanceDate')
    value: bool

class ScoringDataAutotekaCarsharingModel78(_BaseModel):
    relevance_date: int = Field(alias='relevanceDate')
    value: bool

class ScoringDataAutotekaEptsModel79(_BaseModel):
    relevance_date: int = Field(alias='relevanceDate')
    status: str

class ScoringDataAutotekaImportModel80(_BaseModel):
    company: str | None = None
    from_country: str | None = Field(default=None, alias='fromCountry')
    import_date: int | None = Field(default=None, alias='importDate')
    owner_type: Literal['unknown', 'company', 'person'] | None = Field(default=None, alias='ownerType')
    relevance_date: int = Field(alias='relevanceDate')
    value: bool

class ScoringDataAutotekaLeasingModel81(_BaseModel):
    relevance_date: int = Field(alias='relevanceDate')
    value: bool

class ScoringPlacements(_BaseModel):
    is_active: bool | None = Field(default=None, alias='isActive')
    last_placement_date: int | None = Field(default=None, alias='lastPlacementDate')
    last_placement_is_crashed: bool | None = Field(default=None, alias='lastPlacementIsCrashed')
    last_placement_price: int | None = Field(default=None, alias='lastPlacementPrice')
    min_price: int | None = Field(default=None, alias='minPrice')
    number: int | None = None
    placements_with_crashes_number: int | None = Field(default=None, alias='placementsWithCrashesNumber')
    relevance_date: int = Field(alias='relevanceDate')

class ScoringDataAutotekaPledgesModel82(_BaseModel):
    relevance_date: int = Field(alias='relevanceDate')
    value: bool

class ScoringDataAutotekaPriceEvaluationModel83(_BaseModel):
    avg_market_price: int | None = Field(default=None, alias='avgMarketPrice')
    avg_mileage: int | None = Field(default=None, alias='avgMileage')
    avg_price_with_condition: int | None = Field(default=None, alias='avgPriceWithCondition')
    avg_year: float | None = Field(default=None, alias='avgYear')
    imv_url: str | None = Field(default=None, alias='imvUrl')
    items_count: int | None = Field(default=None, alias='itemsCount')
    max_price: int | None = Field(default=None, alias='maxPrice')
    min_price: int | None = Field(default=None, alias='minPrice')
    relevance_date: int = Field(alias='relevanceDate')

class ScoringDataAutotekaRegistrationsModel84(_BaseModel):
    is_actual: bool = Field(alias='isActual')
    owners: int
    relevance_date: int = Field(alias='relevanceDate')

class ScoringDataAutotekaRestrictionsModel85(_BaseModel):
    relevance_date: int = Field(alias='relevanceDate')
    value: bool

class ScoringSeriousDamageSalvageCarAuctionsModel86(_BaseModel):
    auctions_count: int = Field(alias='auctionsCount')
    last_auction_date: int = Field(alias='lastAuctionDate')
    relevance_date: int = Field(alias='relevanceDate')

class ScoringSeriousDamage(_BaseModel):
    relevance_date: int = Field(alias='relevanceDate')
    salvage_car_auctions: ScoringSeriousDamageSalvageCarAuctionsModel86 | None = Field(default=None, alias='salvageCarAuctions')
    value: bool

class ScoringDataAutotekaStealingModel87(_BaseModel):
    relevance_date: int = Field(alias='relevanceDate')
    value: bool

class ScoringDataAutotekaTaxiModel88(_BaseModel):
    is_actual: bool = Field(alias='isActual')
    relevance_date: int = Field(alias='relevanceDate')
    value: bool

class ScoringTechSpecificationBodyNumberModel89(_BaseModel):
    gibdd_value: str = Field(alias='gibddValue')

class ScoringNormalizedValue(_BaseModel):
    value: str
    value_id: int | None = Field(alias='valueId')

class ScoringTechSpecificationBrandModel90(_BaseModel):
    gibdd_value: str | None = Field(default=None, alias='gibddValue')
    normalized_value: ScoringNormalizedValue = Field(default=None, alias='normalizedValue')

class ScoringTechSpecificationChasisNumberModel91(_BaseModel):
    gibdd_value: str = Field(alias='gibddValue')

class ScoringTechSpecificationColorModel92(_BaseModel):
    gibdd_value: str = Field(default=None, alias='gibddValue')

class ScoringTechSpecificationEngineNumberModel93(_BaseModel):
    gibdd_value: str = Field(alias='gibddValue')

class ScoringTechSpecificationEngineTypeModel94(_BaseModel):
    gibdd_value: str | None = Field(default=None, alias='gibddValue')
    normalized_value: ScoringNormalizedValue = Field(default=None, alias='normalizedValue')

class ScoringTechSpecificationHorsepowerModel95(_BaseModel):
    gibdd_value: int | None = Field(default=None, alias='gibddValue')
    normalized_value: ScoringNormalizedValue = Field(default=None, alias='normalizedValue')

class ScoringTechSpecificationMaxWeightModel96(_BaseModel):
    gibdd_value: int = Field(default=None, alias='gibddValue')

class ScoringTechSpecificationModelModel97(_BaseModel):
    gibdd_value: str | None = Field(default=None, alias='gibddValue')
    normalized_value: ScoringNormalizedValue = Field(default=None, alias='normalizedValue')

class ScoringTechSpecificationNetWeightModel98(_BaseModel):
    gibdd_value: int = Field(default=None, alias='gibddValue')

class ScoringTechSpecificationVehicleCategoryModel99(_BaseModel):
    gibdd_value: Literal['A', 'B', 'C', 'D', 'E', 'O', 'M1', 'M1G', 'N1'] = Field(default=None, alias='gibddValue')

class ScoringTechSpecificationVehicleTypeModel100(_BaseModel):
    gibdd_value: Literal['Автобусы прочие', 'Грузовой бортовой', 'Грузовой прочий', 'Грузовой фургон', 'Грузовые автомобили бортовые', 'Грузовые автомобили фургоны', 'Легковое купе', 'Легковой прочий', 'Легковой седан', 'Легковой универсал', 'Легковой хэтчбек (комби)', 'Легковые автомобили кабриолет', 'Легковые автомобили комби (хэтчбек)', 'Легковые автомобили купе', 'Легковые автомобили прочие', 'Легковые автомобили седан', 'Легковые автомобили универсал', 'Мотоциклы'] | None = Field(default=None, alias='gibddValue')
    normalized_value: ScoringNormalizedValue = Field(default=None, alias='normalizedValue')

class ScoringTechSpecificationVolumeModel101(_BaseModel):
    gibdd_value: int | None = Field(alias='gibddValue')
    normalized_value: ScoringNormalizedValue = Field(default=None, alias='normalizedValue')

class ScoringTechSpecificationYearModel102(_BaseModel):
    gibdd_value: int | None = Field(alias='gibddValue')
    normalized_value: ScoringNormalizedValue = Field(default=None, alias='normalizedValue')

class ScoringTechSpecification(_BaseModel):
    body_number: ScoringTechSpecificationBodyNumberModel89 | None = Field(default=None, alias='bodyNumber')
    brand: ScoringTechSpecificationBrandModel90 | None = None
    chasis_number: ScoringTechSpecificationChasisNumberModel91 | None = Field(default=None, alias='chasisNumber')
    color: ScoringTechSpecificationColorModel92 | None = None
    engine_number: ScoringTechSpecificationEngineNumberModel93 | None = Field(default=None, alias='engineNumber')
    engine_type: ScoringTechSpecificationEngineTypeModel94 | None = Field(default=None, alias='engineType')
    horsepower: ScoringTechSpecificationHorsepowerModel95 | None = None
    max_weight: ScoringTechSpecificationMaxWeightModel96 | None = Field(default=None, alias='maxWeight')
    model: ScoringTechSpecificationModelModel97 | None = None
    net_weight: ScoringTechSpecificationNetWeightModel98 | None = Field(default=None, alias='netWeight')
    vehicle_category: ScoringTechSpecificationVehicleCategoryModel99 | None = Field(default=None, alias='vehicleCategory')
    vehicle_type: ScoringTechSpecificationVehicleTypeModel100 | None = Field(default=None, alias='vehicleType')
    volume: ScoringTechSpecificationVolumeModel101 | None = None
    year: ScoringTechSpecificationYearModel102 | None = None

class ScoringDataAutoteka(_BaseModel):
    accidents: ScoringAccidents = None
    carsharing: ScoringDataAutotekaCarsharingModel78 | None = None
    epts: ScoringDataAutotekaEptsModel79 | None = None
    import_: ScoringDataAutotekaImportModel80 | None = Field(default=None, alias='import')
    leasing: ScoringDataAutotekaLeasingModel81 | None = None
    placements: ScoringPlacements = None
    pledges: ScoringDataAutotekaPledgesModel82 | None = None
    price_evaluation: ScoringDataAutotekaPriceEvaluationModel83 | None = Field(default=None, alias='priceEvaluation')
    registrations: ScoringDataAutotekaRegistrationsModel84 | None = None
    restrictions: ScoringDataAutotekaRestrictionsModel85 | None = None
    serious_damage: ScoringSeriousDamage = Field(default=None, alias='seriousDamage')
    stealing: ScoringDataAutotekaStealingModel87 | None = None
    taxi: ScoringDataAutotekaTaxiModel88 | None = None
    tech_specification: ScoringTechSpecification = Field(default=None, alias='techSpecification')

class ScoringAutoteka(_BaseModel):
    created_at: int = Field(alias='createdAt')
    data: ScoringDataAutoteka = None
    is_completed: bool = Field(alias='isCompleted')
    scoring_id: int = Field(alias='scoringId')

class GetScoringResult(_BaseModel):
    risks_assessment: ScoringAutoteka = Field(default=None, alias='risksAssessment')

class AutotekaApiScoringGetByIdResponse(_BaseModel):
    result: GetScoringResult = None

class SpecificationIdResultAutoteka(_BaseModel):
    specification_id: int = Field(alias='specificationId')

class CreateSpecificationResponseDataAutoteka(_BaseModel):
    specification: SpecificationIdResultAutoteka = None

class AutotekaApiSpecificationByPlateNumberResponse(_BaseModel):
    result: CreateSpecificationResponseDataAutoteka = None

class AutotekaApiSpecificationByVehicleIdResponse(_BaseModel):
    result: CreateSpecificationResponseDataAutoteka = None

class DocumentsResultAutotekaPtsModel103(_BaseModel):
    date: str | None = None
    number: str | None = None
    organization: str | None = None

class DocumentsResultAutotekaStsModel104(_BaseModel):
    date: str | None = None
    number: str | None = None

class DocumentsResultAutoteka(_BaseModel):
    pts: DocumentsResultAutotekaPtsModel103 | None = None
    sts: DocumentsResultAutotekaStsModel104 | None = None

class NewCarValuation(_BaseModel):
    avg_price: int = Field(alias='avgPrice')
    body_type: str = Field(alias='bodyType')
    brand: str
    complectation: str
    drive: str
    engine_type: str = Field(alias='engineType')
    max_price: int = Field(alias='maxPrice')
    median_price: int = Field(alias='medianPrice')
    min_price: int = Field(alias='minPrice')
    model: str
    modification: str
    transmission: str
    year: int

class SpecificationEquipmentAutotekaBodyNumberModel105(_BaseModel):
    title: str
    value: str

class SpecificationEquipmentAutotekaBodyTypeModel106(_BaseModel):
    title: str
    value: Literal['Автобусы прочие', 'Грузовой бортовой', 'Грузовой прочий', 'Грузовой фургон', 'Грузовые автомобили бортовые', 'Грузовые автомобили фургоны', 'Легковое купе', 'Легковой прочий', 'Легковой седан', 'Легковой универсал', 'Легковой хэтчбек (комби)', 'Легковые автомобили кабриолет', 'Легковые автомобили комби (хэтчбек)', 'Легковые автомобили купе', 'Легковые автомобили прочие', 'Легковые автомобили седан', 'Легковые автомобили универсал', 'Мотоциклы']

class SpecificationEquipmentAutotekaBrandModel107(_BaseModel):
    title: str
    value: Literal['AUDI', 'BENTLEY', 'BMW', 'CADILLAC', 'CHERY', 'CHEVROLET', 'CHRYSLER', 'CITROEN', 'DACIA', 'DAEWOO', 'DAF', 'DATSUN', 'DODGE', 'FIAT', 'FORD', 'FREIGHTLINER', 'GAZ', 'GEELY', 'GENESIS', 'GREAT WALL', 'HONDA', 'HYUNDAI', 'Honda', 'INFINITI', 'ISUZU', 'IVECO', 'JEEP', 'Jaguar', 'KAMAZ', 'KIA', 'LADA', 'LEXUS', 'LIFAN', 'Land Rover', 'MAN', 'MAZ', 'MAZDA', 'MERCEDES', 'MERCEDES-BENZ', 'MINI', 'MITSUBISHI', 'NISSAN', 'OPEL', 'PEUGEOT', 'PORSCHE', 'RENAULT', 'ROVER', 'SEAZ', 'SKODA', 'SMART', 'SSANGYONG', 'SUBARU', 'Suzuki', 'TAGAZ', 'TOYOTA', 'UAZ', 'VAZ', 'VOLKSWAGEN', 'VOLVO', 'YAMAHA', 'ZAZ']

class SpecificationEquipmentAutotekaColorModel108(_BaseModel):
    description: str
    title: str
    value: Literal['Бежево-Серый', 'Бежевый', 'Белый', 'Белый Металлик', 'Белый Перламутр', 'Белый Черный', 'Белый-Желтый-Серый', 'Белый/Черный', 'Бордовый', 'Бронзовый', 'Вишнево-Красный', 'Жемчужно-Белый', 'Зеленый', 'Золотисто-Коричневый', 'Золотисто-Охристый', 'Коричневый', 'Красный', 'Мальва', 'Многоцветный (Красный, Чёрный)', 'Мурена (Тёмно-Синий)', 'Оранжево-Красный', 'Оранжево-Черный', 'Оранжевый', 'Оранжевый Перламутровый', 'Оранжевый Черный', 'Перлам-Серебристый', 'Перламутрово-Серебристый', 'Светло-Коричневый', 'Светло-Серый', 'Светло-Синий', 'Серебристо-Белый', 'Серебристый', 'Серо Зеленый', 'Серо-Зеленый', 'Серо-Золотистый', 'Серо-Коричневый', 'Серо-Сине-Зеленый Металлик', 'Серо-Синий', 'Серый', 'Сине-Черный', 'Синий', 'Синий Темный', 'Скат', 'Средний Серо-Зеленый', 'Стальной', 'Темно Серый', 'Темно-Бордовый', 'Темно-Вишневый', 'Темно-Голубой', 'Темно-Зеленый', 'Темно-Серый', 'Темно-Синий', 'Черно-Серый', 'Черный', 'Черный Металлик']

class SpecificationEquipmentAutotekaEngineNumberModel109(_BaseModel):
    title: str
    value: str

class SpecificationEquipmentAutotekaEngineTypeModel110(_BaseModel):
    title: str
    value: Literal['Бензин', 'Дизель', 'Электро', 'Газ', 'Гибрид', 'Бензиновый на сжиженном газе', 'Бензиновый на сжатом газе', 'Дизельный на сжиженном газе', 'Дизельный на сжатом газе', 'Электро-бензиновый', 'Электро-дизельный']

class SpecificationEquipmentAutotekaHorsepowerModel111(_BaseModel):
    description: str
    title: str
    value: int

class SpecificationEquipmentAutotekaMaxWeightModel112(_BaseModel):
    description: str
    title: str
    value: int

class SpecificationEquipmentAutotekaModelModel113(_BaseModel):
    title: str
    value: str

class SpecificationEquipmentAutotekaNetWeightModel114(_BaseModel):
    description: str
    title: str
    value: int

class SpecificationEquipmentAutotekaVehicleCategoryModel115(_BaseModel):
    title: str
    value: Literal['A', 'B', 'C', 'D', 'E', 'O', 'M1', 'M1G', 'N1']

class SpecificationEquipmentAutotekaVolumeModel116(_BaseModel):
    description: str
    title: str
    value: int

class SpecificationEquipmentAutotekaYearModel117(_BaseModel):
    title: str
    value: int

class SpecificationEquipmentAutoteka(_BaseModel):
    body_number: SpecificationEquipmentAutotekaBodyNumberModel105 | None = Field(alias='bodyNumber')
    body_type: SpecificationEquipmentAutotekaBodyTypeModel106 | None = Field(alias='bodyType')
    brand: SpecificationEquipmentAutotekaBrandModel107 | None
    color: SpecificationEquipmentAutotekaColorModel108 | None
    engine_number: SpecificationEquipmentAutotekaEngineNumberModel109 | None = Field(alias='engineNumber')
    engine_type: SpecificationEquipmentAutotekaEngineTypeModel110 | None = Field(alias='engineType')
    horsepower: SpecificationEquipmentAutotekaHorsepowerModel111 | None
    max_weight: SpecificationEquipmentAutotekaMaxWeightModel112 | None = Field(alias='maxWeight')
    model: SpecificationEquipmentAutotekaModelModel113 | None
    net_weight: SpecificationEquipmentAutotekaNetWeightModel114 | None = Field(alias='netWeight')
    vehicle_category: SpecificationEquipmentAutotekaVehicleCategoryModel115 | None = Field(alias='vehicleCategory')
    volume: SpecificationEquipmentAutotekaVolumeModel116 | None
    year: SpecificationEquipmentAutotekaYearModel117 | None

class SpecificationNormalizedSpecificationAutotekaBodyTypeModel118(_BaseModel):
    value: str
    value_id: int = Field(alias='valueId')

class SpecificationNormalizedSpecificationAutotekaBrandModel119(_BaseModel):
    value: str
    value_id: int = Field(alias='valueId')

class SpecificationNormalizedSpecificationAutotekaCapacityModel120(_BaseModel):
    value: float

class SpecificationNormalizedSpecificationAutotekaComplectationModel121(_BaseModel):
    value: str
    value_id: int = Field(alias='valueId')

class SpecificationNormalizedSpecificationAutotekaDoorsCountModel122(_BaseModel):
    value: int
    value_id: int = Field(alias='valueId')

class SpecificationNormalizedSpecificationAutotekaDriveModel123(_BaseModel):
    value: str
    value_id: int = Field(alias='valueId')

class SpecificationNormalizedSpecificationAutotekaEngineModel124(_BaseModel):
    value: float
    value_id: int = Field(alias='valueId')

class SpecificationNormalizedSpecificationAutotekaEngineTypeModel125(_BaseModel):
    value: str
    value_id: int = Field(alias='valueId')

class SpecificationNormalizedSpecificationAutotekaGenerationModel126(_BaseModel):
    value: str
    value_id: int = Field(alias='valueId')

class SpecificationNormalizedSpecificationAutotekaModelModel127(_BaseModel):
    value: str
    value_id: int = Field(alias='valueId')

class SpecificationNormalizedSpecificationAutotekaModificationModel128(_BaseModel):
    value: str
    value_id: int = Field(alias='valueId')

class SpecificationNormalizedSpecificationAutotekaTransmissionModel129(_BaseModel):
    value: str
    value_id: int = Field(alias='valueId')

class SpecificationNormalizedSpecificationAutotekaWheelModel130(_BaseModel):
    value: str

class SpecificationNormalizedSpecificationAutotekaYearModel131(_BaseModel):
    value: int
    value_id: int = Field(alias='valueId')

class SpecificationNormalizedSpecificationAutoteka(_BaseModel):
    body_type: SpecificationNormalizedSpecificationAutotekaBodyTypeModel118 | None = Field(alias='bodyType')
    brand: SpecificationNormalizedSpecificationAutotekaBrandModel119 | None
    capacity: SpecificationNormalizedSpecificationAutotekaCapacityModel120 | None
    complectation: SpecificationNormalizedSpecificationAutotekaComplectationModel121 | None
    doors_count: SpecificationNormalizedSpecificationAutotekaDoorsCountModel122 | None = Field(alias='doorsCount')
    drive: SpecificationNormalizedSpecificationAutotekaDriveModel123 | None
    engine: SpecificationNormalizedSpecificationAutotekaEngineModel124 | None
    engine_type: SpecificationNormalizedSpecificationAutotekaEngineTypeModel125 | None = Field(alias='engineType')
    generation: SpecificationNormalizedSpecificationAutotekaGenerationModel126 | None
    model: SpecificationNormalizedSpecificationAutotekaModelModel127 | None
    modification: SpecificationNormalizedSpecificationAutotekaModificationModel128 | None
    transmission: SpecificationNormalizedSpecificationAutotekaTransmissionModel129 | None
    wheel: SpecificationNormalizedSpecificationAutotekaWheelModel130 | None
    year: SpecificationNormalizedSpecificationAutotekaYearModel131 | None

class SpecificationResultAutoteka(_BaseModel):
    equipment: SpecificationEquipmentAutoteka
    normalized_specification: SpecificationNormalizedSpecificationAutoteka = Field(alias='normalizedSpecification')
    plate_number: str | None = Field(alias='plateNumber')
    specification_id: int = Field(alias='specificationId')
    status: str
    vehicle_id: str | None = Field(alias='vehicleId')

class GetSpecificationResponseDataAutoteka(_BaseModel):
    documents: DocumentsResultAutoteka = None
    new_car_valuations: list[NewCarValuation] | None = Field(default=None, alias='newCarValuations')
    specification: SpecificationResultAutoteka = None
    valuation: AvitoPriceValuation = None

class AutotekaApiSpecificationGetByIdResponse(_BaseModel):
    result: GetSpecificationResponseDataAutoteka = None

class ReportAutoteka(_BaseModel):
    data: ReportDataAutoteka = None
    pdf_link: str = Field(default=None, alias='pdfLink')
    report_id: int = Field(alias='reportId')
    status: Literal['success', 'processing', 'notFound']
    web_link: str = Field(default=None, alias='webLink')

class GetReportResult(_BaseModel):
    report: ReportAutoteka = None

class AutotekaApiPostSyncCreateReportByRegNumberResponse(_BaseModel):
    result: GetReportResult = None

class AutotekaApiPostSyncCreateReportByVinResponse(_BaseModel):
    result: GetReportResult = None

class TeaserWithoutDataAutoteka(_BaseModel):
    status: Literal['success', 'processing']
    teaser_id: int = Field(alias='teaserId')

class CreateTeaserResponseDataAutoteka(_BaseModel):
    teaser: TeaserWithoutDataAutoteka = None

class AutotekaApiPostTeaserResponse(_BaseModel):
    result: CreateTeaserResponseDataAutoteka = None

class TeaserAvailableInfoItemModel132(_BaseModel):
    index: int
    title: str
    values: list[str]

class TeaserAvitoPlacementsModel133(_BaseModel):
    photos_count: int = Field(alias='photosCount')
    placements_count: int = Field(alias='placementsCount')

class TeaserInsightsItemModel134(_BaseModel):
    index: int
    title: str

class TeaserMileageModel135(_BaseModel):
    is_real_mileage: bool = Field(alias='isRealMileage')

class TeaserOwnersModel136(_BaseModel):
    count: int

class TeaserServiceModel137(_BaseModel):
    records_count: int = Field(alias='recordsCount')
    records_first_date: str = Field(alias='recordsFirstDate')

class Teaser(_BaseModel):
    available_info: list[TeaserAvailableInfoItemModel132] = Field(alias='availableInfo')
    avito_placements: TeaserAvitoPlacementsModel133 = Field(alias='avitoPlacements')
    brand: str | None
    color: str | None
    insights: list[TeaserInsightsItemModel134]
    mileage: TeaserMileageModel135
    model: str | None
    owners: TeaserOwnersModel136
    service: TeaserServiceModel137
    year: int | None

class AutotekaApiGetTeaserResponse(_BaseModel):
    data: Teaser
    status: Literal['success', 'processing']
    teaser_id: int = Field(alias='teaserId')

class ValuationBySpecificationResultAutoteka(_BaseModel):
    brand: str
    mileage: int | None = None
    model: str
    new_car_valuations: list[NewCarValuation] | None = Field(default=None, alias='newCarValuations')
    owners_count: str = Field(alias='ownersCount')
    status: str
    valuation: AvitoPriceValuation
    vehicle_id: str | None = Field(alias='vehicleId')
    year: int

class AutotekaApiValuationBySpecificationResponse(_BaseModel):
    result: ValuationBySpecificationResultAutoteka = None

class AutotekaApiGetAccessTokenResponse(_BaseModel):
    access_token: str = None
    expires_in: float = None
    token_type: str = None

__all__ = ['CatalogsFieldAutotekaValuesItemModel1', 'CatalogsFieldAutoteka', 'CatalogsResolveResponseDataAutoteka', 'AutotekaApiCatalogsResolveResponse', 'AutotekaApiGetLeadsResponsePaginationModel2', 'AutotekaApiGetLeadsResponseResultItemModel3PayloadModel4ExtraPayloadModel5PriceAnalyticsModel6', 'AutotekaApiGetLeadsResponseResultItemModel3PayloadModel4ExtraPayloadModel5TeaserModel7', 'AutotekaApiGetLeadsResponseResultItemModel3PayloadModel4ExtraPayloadModel5', 'AutotekaApiGetLeadsResponseResultItemModel3PayloadModel4TriggerPayloadModel8LastEventsItemModel9', 'AutotekaApiGetLeadsResponseResultItemModel3PayloadModel4TriggerPayloadModel8', 'AutotekaApiGetLeadsResponseResultItemModel3PayloadModel4', 'AutotekaApiGetLeadsResponseResultItemModel3', 'AutotekaApiGetLeadsResponse', 'AutotekaApiMonitoringBucketAddResponseResultModel10InvalidVehiclesItemModel11', 'AutotekaApiMonitoringBucketAddResponseResultModel10', 'AutotekaApiMonitoringBucketAddResponse', 'AutotekaApiMonitoringBucketDeleteResponseResultModel12', 'AutotekaApiMonitoringBucketDeleteResponse', 'AutotekaApiMonitoringBucketRemoveResponseResultModel13InvalidVehiclesItemModel14', 'AutotekaApiMonitoringBucketRemoveResponseResultModel13', 'AutotekaApiMonitoringBucketRemoveResponse', 'ResponseMonitoringGetRegAction', 'AutotekaApiMonitoringGetRegActionsResponsePaginationModel15', 'AutotekaApiMonitoringGetRegActionsResponse', 'PackageAutoteka', 'GetActivePackageResponseDataAutoteka', 'AutotekaApiGetActivePackageResponse', 'PreviewIdOnlyAutoteka', 'RequestPreviewResponseDataAutoteka', 'AutotekaApiPostPreviewByVinResponse', 'PreviewDataAutoteka', 'PreviewAutoteka', 'GetPreviewResponseDataAutoteka', 'AutotekaApiGetPreviewResponse', 'ReportWithoutDataAutoteka', 'CreateReportResponseDataAutoteka', 'AutotekaApiPostReportResponse', 'AutotekaApiPostReportByVehicleIdResponse', 'ReportItemAutoteka', 'AutotekaApiGetReportListResponse', 'CrashesHistoryAutotekaDamageTypesItemModel17', 'CrashesHistoryAutoteka', 'ReportDataAutotekaAccidentsModel16', 'ArbitrationCasesCasesItemModel18', 'ArbitrationCases', 'AvitoAuctionsAuctionsItemModel19', 'AvitoAuctions', 'AvitoItemAutotekaImagesItemModel20', 'AvitoItemAutoteka', 'AvitoPriceValuationMarketNormalPriceRangeModel21', 'AvitoPriceValuation', 'CarImageAutoteka', 'CarsharingDataEventAutoteka', 'RecapAutoteka', 'CarsharingDataAutoteka', 'Customs', 'DiagnosticsEventConditionModel22', 'DiagnosticsEventDamage', 'DiagnosticsEventPhoto', 'DiagnosticsEvent', 'Diagnostics', 'Epts', 'EquipmentAutotekaBodyModel23', 'EquipmentAutotekaBodyNumberModel24', 'EquipmentAutotekaBrandModel25', 'EquipmentAutotekaChasisNumberModel26', 'EquipmentAutotekaColorModel27', 'EquipmentAutotekaDriveModel28', 'EquipmentAutotekaEngineNumberModel29', 'EquipmentAutotekaEngineTypeModel30', 'EquipmentAutotekaEquipmentModel31', 'EquipmentAutotekaHorsepowerModel32', 'EquipmentAutotekaMaxWeightModel33', 'EquipmentAutotekaModelModel34', 'EquipmentAutotekaModificationModel35', 'EquipmentAutotekaNetWeightModel36', 'EquipmentAutotekaTransmissionModel37', 'EquipmentAutotekaVehicleModel38', 'EquipmentAutotekaVehicleCategoryModel39', 'EquipmentAutotekaVehicleTypeModel40', 'EquipmentAutotekaVolumeModel41', 'EquipmentAutotekaYearModel42', 'EquipmentAutoteka', 'EventsAutotekaAvitoOnSaleModel43AdditionalInfoModel44', 'EventsAutotekaAvitoOnSaleModel43', 'EventsAutotekaBodyRepairModel45', 'EventsAutotekaCrashesModel46', 'EventsAutotekaDealerDataAvailableModel47', 'EventsAutotekaFirstSellDateModel48', 'EventsAutotekaLastMileageRecordModel49', 'EventsAutotekaOwnersModel50', 'EventsAutotekaPledgeModel51', 'EventsAutotekaPublicPersonModel52', 'EventsAutoteka', 'EventsOthersHistoryAutoteka', 'ExtendedSpecificationsParam', 'ExtendedSpecifications', 'ExternalPlacementAutoteka', 'FineEventAutoteka', 'FinesAutoteka', 'HeadAutotekaRegNumbersHistoryItemModel53', 'HeadAutoteka', 'Insights', 'InsurancePaymentsItem', 'InsurancePayments', 'InsurancePolicyEventAutoteka', 'InsurancePoliciesAutoteka', 'LeasingContractsItemModel54', 'Leasing', 'MaxPosterPriceValuationAnalyticByActualSalesModel55', 'MaxPosterPriceValuationAnalyticByCompletedSalesModel56', 'MaxPosterValuationLiquidityRating', 'MaxPosterPriceValuationLiquidityModel57', 'MaxPosterPriceValuation', 'OtherAutoteka', 'OwnersHistoryAutoteka', 'PriceStatReportAutotekaPriceModel58', 'PriceStatReportAutoteka', 'PriceStatAutoteka', 'PriceStatForNewCarsAutotekaItemsItemModel59PricesItemModel60', 'PriceStatForNewCarsAutotekaItemsItemModel59', 'PriceStatForNewCarsAutotekaPriceModel61', 'PriceStatForNewCarsAutoteka', 'PtsDataPtsModel62', 'PtsDataStsModel63', 'PtsData', 'RecallItemCompleteInfoModel64', 'RecallItem', 'Recalls', 'ReportDataAutotekaRegistrationActionsModel65', 'RestrictionsAutotekaPledgeModel66HistoryModel67PledgesItemModel68', 'RestrictionsAutotekaPledgeModel66HistoryModel67', 'RestrictionsAutotekaPledgeModel66PledgeAdditionalDataItemModel69DataItemModel70', 'RestrictionsAutotekaPledgeModel66PledgeAdditionalDataItemModel69', 'RestrictionsAutotekaPledgeModel66', 'RestrictionsAutotekaRegistrationModel71AdditionalInfoItemModel72', 'RestrictionsAutotekaRegistrationModel71', 'RestrictionsAutotekaStealingModel73AdditionalInfoItemModel74', 'RestrictionsAutotekaStealingModel73', 'RestrictionsAutoteka', 'SalvageCarAuctionRecordsItemModel75', 'SalvageCarAuctionRecords', 'ServiceInfoAutotekaReportCompleteStatusModel76UnavailableSourcesItemModel77', 'ServiceInfoAutotekaReportCompleteStatusModel76', 'ServiceInfoAutoteka', 'TaxiDataEventAutoteka', 'TaxiDataAutoteka', 'AutotekaTeaser', 'TechInspectionHistoryEvent', 'TechInspectionHistory', 'VehicleSpecificationsParam', 'VehicleSpecifications', 'ReportDataAutoteka', 'ReportAutotekaAsync', 'GetReportResultAsync', 'AutotekaApiGetReportResponse', 'AutotekaApiPostPreviewByExternalItemResponse', 'AutotekaApiPostPreviewByItemIdResponse', 'AutotekaApiPostPreviewByRegNumberResponse', 'ScoringIdResultAutoteka', 'CreateScoringResponseDataAutoteka', 'AutotekaApiScoringByVehicleIdResponse', 'ScoringAccidents', 'ScoringDataAutotekaCarsharingModel78', 'ScoringDataAutotekaEptsModel79', 'ScoringDataAutotekaImportModel80', 'ScoringDataAutotekaLeasingModel81', 'ScoringPlacements', 'ScoringDataAutotekaPledgesModel82', 'ScoringDataAutotekaPriceEvaluationModel83', 'ScoringDataAutotekaRegistrationsModel84', 'ScoringDataAutotekaRestrictionsModel85', 'ScoringSeriousDamageSalvageCarAuctionsModel86', 'ScoringSeriousDamage', 'ScoringDataAutotekaStealingModel87', 'ScoringDataAutotekaTaxiModel88', 'ScoringTechSpecificationBodyNumberModel89', 'ScoringNormalizedValue', 'ScoringTechSpecificationBrandModel90', 'ScoringTechSpecificationChasisNumberModel91', 'ScoringTechSpecificationColorModel92', 'ScoringTechSpecificationEngineNumberModel93', 'ScoringTechSpecificationEngineTypeModel94', 'ScoringTechSpecificationHorsepowerModel95', 'ScoringTechSpecificationMaxWeightModel96', 'ScoringTechSpecificationModelModel97', 'ScoringTechSpecificationNetWeightModel98', 'ScoringTechSpecificationVehicleCategoryModel99', 'ScoringTechSpecificationVehicleTypeModel100', 'ScoringTechSpecificationVolumeModel101', 'ScoringTechSpecificationYearModel102', 'ScoringTechSpecification', 'ScoringDataAutoteka', 'ScoringAutoteka', 'GetScoringResult', 'AutotekaApiScoringGetByIdResponse', 'SpecificationIdResultAutoteka', 'CreateSpecificationResponseDataAutoteka', 'AutotekaApiSpecificationByPlateNumberResponse', 'AutotekaApiSpecificationByVehicleIdResponse', 'DocumentsResultAutotekaPtsModel103', 'DocumentsResultAutotekaStsModel104', 'DocumentsResultAutoteka', 'NewCarValuation', 'SpecificationEquipmentAutotekaBodyNumberModel105', 'SpecificationEquipmentAutotekaBodyTypeModel106', 'SpecificationEquipmentAutotekaBrandModel107', 'SpecificationEquipmentAutotekaColorModel108', 'SpecificationEquipmentAutotekaEngineNumberModel109', 'SpecificationEquipmentAutotekaEngineTypeModel110', 'SpecificationEquipmentAutotekaHorsepowerModel111', 'SpecificationEquipmentAutotekaMaxWeightModel112', 'SpecificationEquipmentAutotekaModelModel113', 'SpecificationEquipmentAutotekaNetWeightModel114', 'SpecificationEquipmentAutotekaVehicleCategoryModel115', 'SpecificationEquipmentAutotekaVolumeModel116', 'SpecificationEquipmentAutotekaYearModel117', 'SpecificationEquipmentAutoteka', 'SpecificationNormalizedSpecificationAutotekaBodyTypeModel118', 'SpecificationNormalizedSpecificationAutotekaBrandModel119', 'SpecificationNormalizedSpecificationAutotekaCapacityModel120', 'SpecificationNormalizedSpecificationAutotekaComplectationModel121', 'SpecificationNormalizedSpecificationAutotekaDoorsCountModel122', 'SpecificationNormalizedSpecificationAutotekaDriveModel123', 'SpecificationNormalizedSpecificationAutotekaEngineModel124', 'SpecificationNormalizedSpecificationAutotekaEngineTypeModel125', 'SpecificationNormalizedSpecificationAutotekaGenerationModel126', 'SpecificationNormalizedSpecificationAutotekaModelModel127', 'SpecificationNormalizedSpecificationAutotekaModificationModel128', 'SpecificationNormalizedSpecificationAutotekaTransmissionModel129', 'SpecificationNormalizedSpecificationAutotekaWheelModel130', 'SpecificationNormalizedSpecificationAutotekaYearModel131', 'SpecificationNormalizedSpecificationAutoteka', 'SpecificationResultAutoteka', 'GetSpecificationResponseDataAutoteka', 'AutotekaApiSpecificationGetByIdResponse', 'ReportAutoteka', 'GetReportResult', 'AutotekaApiPostSyncCreateReportByRegNumberResponse', 'AutotekaApiPostSyncCreateReportByVinResponse', 'TeaserWithoutDataAutoteka', 'CreateTeaserResponseDataAutoteka', 'AutotekaApiPostTeaserResponse', 'TeaserAvailableInfoItemModel132', 'TeaserAvitoPlacementsModel133', 'TeaserInsightsItemModel134', 'TeaserMileageModel135', 'TeaserOwnersModel136', 'TeaserServiceModel137', 'Teaser', 'AutotekaApiGetTeaserResponse', 'ValuationBySpecificationResultAutoteka', 'AutotekaApiValuationBySpecificationResponse', 'AutotekaApiGetAccessTokenResponse']
