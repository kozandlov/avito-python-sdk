"""Generated response models for slug: job."""

from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, ValidationError, Field, RootModel

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class JobApiApplicationsApplyActionsResponseAppliesItemModel1(_BaseModel):
    created_at: str = None
    id: str = None
    state: str = None
    updated_at: str = None

class JobApiApplicationsApplyActionsResponse(_BaseModel):
    applies: list[JobApiApplicationsApplyActionsResponseAppliesItemModel1] = None

class EducationLevel(RootModel[Literal['higher', 'unfinished-higher', 'secondary', 'special-secondary', None]]):
    pass

class JobApiApplicationsGetByIdsResponseAppliesItemModel2ApplicantModel3DataModel4FullNameModel5(_BaseModel):
    first_name: str = None
    last_name: str = None
    patronymic: str | None = None

class Gender(RootModel[Literal['female', 'male', None]]):
    pass

class JobApiApplicationsGetByIdsResponseAppliesItemModel2ApplicantModel3DataModel4(_BaseModel):
    birthday: str | None = None
    citizenship: str | None = None
    education: EducationLevel = None
    full_name: JobApiApplicationsGetByIdsResponseAppliesItemModel2ApplicantModel3DataModel4FullNameModel5 | None = None
    gender: Gender = None
    name: str | None = None

class JobApiApplicationsGetByIdsResponseAppliesItemModel2ApplicantModel3(_BaseModel):
    data: JobApiApplicationsGetByIdsResponseAppliesItemModel2ApplicantModel3DataModel4 = None
    id: str = None
    resume_id: str | None = None

class JobApiApplicationsGetByIdsResponseAppliesItemModel2ContactsModel6ChatModel7(_BaseModel):
    value: str = None

class JobApiApplicationsGetByIdsResponseAppliesItemModel2ContactsModel6PhonesItemModel8(_BaseModel):
    status: str | None = None
    value: str = None

class JobApiApplicationsGetByIdsResponseAppliesItemModel2ContactsModel6(_BaseModel):
    chat: JobApiApplicationsGetByIdsResponseAppliesItemModel2ContactsModel6ChatModel7 | None = None
    phones: list[JobApiApplicationsGetByIdsResponseAppliesItemModel2ContactsModel6PhonesItemModel8] = None

class EnrichedPropertyMatchingStatus(RootModel[Literal['no_criteria', 'matched', 'mismatched']]):
    pass

class EnrichedPropertiesAgeModel9(_BaseModel):
    matching_status: EnrichedPropertyMatchingStatus = None
    value: int | None = None

class EnrichedPropertiesCitizenshipModel10(_BaseModel):
    matching_status: EnrichedPropertyMatchingStatus = None
    value: str | None = None

class EnrichedPropertiesExperienceModel11(_BaseModel):
    matching_status: EnrichedPropertyMatchingStatus = None
    value: str | None = None

class EnrichedPropertiesFullNameModel12(_BaseModel):
    matching_status: EnrichedPropertyMatchingStatus = None
    value: str | None = None

class EnrichedPropertiesGenderModel13(_BaseModel):
    matching_status: EnrichedPropertyMatchingStatus = None
    value: str | None = None

class EnrichedPropertiesPhoneModel14(_BaseModel):
    matching_status: EnrichedPropertyMatchingStatus = None
    value: str | None = None

class EnrichedProperties(_BaseModel):
    age: EnrichedPropertiesAgeModel9 | None = None
    citizenship: EnrichedPropertiesCitizenshipModel10 | None = None
    experience: EnrichedPropertiesExperienceModel11 | None = None
    full_name: EnrichedPropertiesFullNameModel12 | None = None
    gender: EnrichedPropertiesGenderModel13 | None = None
    phone: EnrichedPropertiesPhoneModel14 | None = None
    status: Literal['in_progress', 'not_completed', 'completed_no_criteria', 'completed_matched', 'completed_mismatched'] = None

class PrevalidationAnswer(_BaseModel):
    label: str = None
    value: str = None
    variable: str = None

class JobApiApplicationsGetByIdsResponseAppliesItemModel2PrevalidationModel15(_BaseModel):
    status: str = None
    summary: list[PrevalidationAnswer] | None = None

class JobApiApplicationsGetByIdsResponseAppliesItemModel2PriceModel16(_BaseModel):
    bonus: int
    real: int
    total: int

class JobApiApplicationsGetByIdsResponseAppliesItemModel2(_BaseModel):
    applicant: JobApiApplicationsGetByIdsResponseAppliesItemModel2ApplicantModel3 = None
    contacts: JobApiApplicationsGetByIdsResponseAppliesItemModel2ContactsModel6 = None
    created_at: str = None
    employee_id: int | None = None
    enriched_properties: EnrichedProperties = None
    id: str = None
    is_viewed: bool = None
    negotiation_id: int | None = None
    prevalidation: JobApiApplicationsGetByIdsResponseAppliesItemModel2PrevalidationModel15 | None = None
    price: JobApiApplicationsGetByIdsResponseAppliesItemModel2PriceModel16 | None = None
    source: Literal['sbc_cold_flow'] = None
    state: str = None
    type: Literal['by_phone', 'by_chat'] = None
    updated_at: str = None
    vacancy_id: int = None

class JobApiApplicationsGetByIdsResponse(_BaseModel):
    applies: list[JobApiApplicationsGetByIdsResponseAppliesItemModel2] = None

class JobApiApplicationsGetIdsResponseAppliesItemModel17(_BaseModel):
    created_at: str = None
    id: str = None
    state: str = None
    updated_at: str = None

class JobApiApplicationsGetIdsResponse(_BaseModel):
    applies: list[JobApiApplicationsGetIdsResponseAppliesItemModel17] = None

class JobApiApplicationsGetStatesResponseStatesItemModel18(_BaseModel):
    description: str = None
    slug: str = None

class JobApiApplicationsGetStatesResponse(_BaseModel):
    states: list[JobApiApplicationsGetStatesResponseStatesItemModel18] = None

class JobApiApplicationsSetIsViewedResponseAppliesItemModel19(_BaseModel):
    id: str
    is_viewed: bool

class JobApiApplicationsSetIsViewedResponse(_BaseModel):
    applies: list[JobApiApplicationsSetIsViewedResponseAppliesItemModel19] = None

class JobApiApplicationsWebhookGetResponse(_BaseModel):
    secret: str
    url: str

class JobApiApplicationsWebhookPutResponse(_BaseModel):
    secret: str
    url: str

class JobApiApplicationsWebhookDeleteResponse(_BaseModel):
    ok: bool = None

class WebhookSubscribeRequestBody(_BaseModel):
    secret: str
    url: str

class JobApiApplicationsWebhooksGetResponse(_BaseModel):
    webhooks: list[WebhookSubscribeRequestBody]

class ResumeSearchMeta(_BaseModel):
    cursor: int = None
    page: int = None
    pages: int = None
    per_page: int = None

class Coordinates(_BaseModel):
    latitude: float
    longitude: float

class AddressDetails(_BaseModel):
    address: str | None = None
    coordinates: Coordinates = None
    district: str | None = None
    location: str | None = None
    metro: str | None = None

class DriverLicence(RootModel[Literal[True, False]]):
    pass

class DriverLicenceCategory(RootModel[list[Literal['a', 'b', 'be', 'c', 'ce', 'd', 'de', 'm', 'tm', 'tb']]]):
    pass

class DrivingExperience(RootModel[Literal['less-than-three-years', 'more-than-three-years']]):
    pass

class Location(_BaseModel):
    id: int = None
    title: str = None

class MedicalBook(RootModel[Literal[True, False]]):
    pass

class Citizenship(_BaseModel):
    id: int = None
    title: str = None

class OwnTransport(RootModel[Literal[False, 'car', 'cargo-car', 'bike', 'scooter']]):
    pass

class Specialization(_BaseModel):
    id: int = None
    title: str = None

class SimplifiedResume(_BaseModel):
    address_details: AddressDetails = None
    age: int = None
    created: str = None
    driver_licence: DriverLicence = None
    driver_licence_category: DriverLicenceCategory = None
    driving_experience: DrivingExperience = None
    education_level: EducationLevel = None
    gender: Gender = None
    id: int = None
    is_purchased: bool = None
    location: Location = None
    medical_book: MedicalBook = None
    nationality: Citizenship = None
    own_transport: OwnTransport = None
    salary: float = None
    specialization: Specialization = None
    title: str = None
    total_experience: int = None
    updated: str = None

class JobApiResumesGetResponse(_BaseModel):
    meta: ResumeSearchMeta = None
    resumes: list[SimplifiedResume] = None

class ResumeContact(_BaseModel):
    type: Literal['e-mail', 'phone', 'chat_id'] = None
    value: str = None

class JobApiResumeGetContactsResponseFullNameModel20(_BaseModel):
    first_name: str = None
    last_name: str = None
    patronymic: str | None = None

class JobApiResumeGetContactsResponse(_BaseModel):
    already_bought: bool = None
    contacts: list[ResumeContact] = None
    full_name: JobApiResumeGetContactsResponseFullNameModel20 | None = None
    name: str = None

class JobApiVacancyCreateResponse(_BaseModel):
    id: str = None
    url: str = None
    uuid: str | None = None

class JobApiResumeGetItemResponseParamsModel21EducationListItemModel22(_BaseModel):
    education_stop: str | None = None
    institution: str | None = None
    specialty: str | None = None

class JobApiResumeGetItemResponseParamsModel21ExperienceListItemModel23(_BaseModel):
    company: str | None = None
    position: str | None = None
    responsibilities: str | None = None
    work_finish: str | None = None
    work_start: str | None = None

class JobApiResumeGetItemResponseParamsModel21LanguageListItemModel24(_BaseModel):
    language: str | None = None
    language_level: Literal['Начальный', 'Средний', 'Выше среднего', 'Свободное владение'] | None = None

class JobApiResumeGetItemResponseParamsModel21(_BaseModel):
    ability_to_business_trip: Literal['Не готов', 'Готов', 'Иногда'] | None = None
    address: str | None = None
    age: int | None = None
    business_area: Literal['IT, интернет, телеком', 'Автомобильный бизнес', 'Административная работа', 'Банки, инвестиции', 'Без опыта, студенты', 'Бухгалтерия, финансы', 'Высший менеджмент', 'Госслужба, НКО', 'Домашний персонал', 'ЖКХ, эксплуатация', 'Искусство, развлечения', 'Консультирование', 'Курьерская доставка', 'Маркетинг, реклама, PR', 'Медицина, фармацевтика', 'Образование, наука', 'Охрана, безопасность', 'Продажи', 'Производство, сырьё, с/х', 'Страхование', 'Строительство', 'Такси', 'Транспорт, логистика', 'Туризм, рестораны', 'Управление персоналом', 'Фитнес, салоны красоты', 'Юриспруденция'] | None = None
    driver_licence: Literal[True, False] | None = None
    driver_licence_category: list[Literal['a', 'b', 'be', 'c', 'ce', 'd', 'de', 'm', 'tm', 'tb']] | None = None
    education: Literal['Высшее', 'Незаконченное высшее', 'Среднее', 'Среднее специальное'] | None = None
    education_list: list[JobApiResumeGetItemResponseParamsModel21EducationListItemModel22] | None = None
    experience_list: list[JobApiResumeGetItemResponseParamsModel21ExperienceListItemModel23] | None = None
    language_list: list[JobApiResumeGetItemResponseParamsModel21LanguageListItemModel24] | None = None
    moving: Literal['Невозможен', 'Возможен'] | None = None
    nationality: str | None = None
    pol: Literal['Мужской', 'Женский'] | None = None
    razreshenie_na_rabotu_v_rossii: Literal['Да', 'Нет'] | None = None
    schedule: Literal['flyInFlyOut', 'partTime', 'fullDay', 'flexible', 'shift', 'remote', 'fiveDay', 'sixDay'] | None = None

class Photo(_BaseModel):
    url: str = None

class JobApiResumeGetItemResponse(_BaseModel):
    address_details: AddressDetails = None
    description: str = None
    id: int = None
    is_active: bool = None
    is_purchased: bool = None
    params: JobApiResumeGetItemResponseParamsModel21 = None
    photos: list[Photo] | None = None
    salary: int | None = None
    start_time: str = None
    title: str = None
    update_time: str = None
    url: str = None

class VacancySearchMeta(_BaseModel):
    page: int = None
    pages: int = None
    per_page: int = None

class SimplifiedVacancyAddressDetailsModel25(_BaseModel):
    address: str = None
    city: str = None

class SimplifiedVacancy(_BaseModel):
    address_details: SimplifiedVacancyAddressDetailsModel25 = Field(default=None, alias='addressDetails')
    business_area: str = Field(default=None, alias='businessArea')
    company_name: str = Field(default=None, alias='companyName')
    link: str = None
    profession: str = None
    title: str = None

class JobApiSearchVacancyResponse(_BaseModel):
    meta: VacancySearchMeta = None
    vacancies: list[SimplifiedVacancy] = None

class JobApiVacancyCreateV2Response(_BaseModel):
    id: str = None

class Vacancy20AddressDetailsModel26CoordinatesModel27(_BaseModel):
    latitude: float = None
    longitude: float = None

class Vacancy20AddressDetailsModel26(_BaseModel):
    address: str = None
    city: str = None
    coordinates: Vacancy20AddressDetailsModel26CoordinatesModel27 = None
    province: str = None

class Vacancy20ContactsModel28(_BaseModel):
    email: str | None = None
    name: str | None = None

class Vacancy20HierarchyModel29(_BaseModel):
    employee_id: int | None = None

class Vacancy20ParamsModel30CoordinatesModel31(_BaseModel):
    latitude: float = None
    longitude: float = None

class DrivingLicenseCategory(RootModel[list[Literal['A', 'AI', 'AII', 'AIII', 'AIV', 'B', 'B1', 'BE', 'C', 'C1', 'C1E', 'CE', 'D', 'D1', 'D1E', 'DE', 'E', 'F', 'Tm', 'Tb', 'M']]]):
    pass

class Vacancy20ParamsModel30SalaryModel32(_BaseModel):
    from_: int | None = Field(default=None, alias='from')
    to: int | None = None

class Vacancy20ParamsModel30SalaryBaseRangeModel33(_BaseModel):
    from_: int | None = Field(default=None, alias='from')
    to: int | None = None

class Vacancy20ParamsModel30(_BaseModel):
    address: str | None = None
    administrator_organization_type: str | None = None
    age_preferences: list[Literal['Соискатели старше 45 лет', 'Соискатели от 14 лет', 'Соискатели от 16 лет', 'С нарушениями здоровья', 'Для студентов', 'Для пенсионеров']] | None = None
    bonuses: list[Literal['Униформа', 'Проживание', 'Медицинская страховка', 'Питание', 'Оплата бензина', 'Парковка', 'Зоны отдыха', 'Транспорт до работы', 'Скидки в компании', 'Подарки детям на праздники', 'Оплата мобильной связи', 'Обучение', 'Компенсация проезда с работы', 'КАСКО', 'Смартфон', 'Услуги шиномонтажа']] | None = None
    business_area: str | None = None
    change: list[Literal['1 / 2', '1 / 3', '2 / 1', '2 / 2', '3 / 3', '3 / 2', '4 / 3', '5 / 2', '4 / 2', '6 / 1', 'Без выходных', 'Утренние', 'Дневные', 'Вечерние', 'Ночные', 'Плавающие выходные', 'Работа по выходным']] | None = None
    citizenship: list[str] | None = None
    construction_work_type: list[Literal['Малярные работы', 'Облицовка стен', 'Работы с плиткой', 'Монтаж и установка', 'Отделочные работы', 'Кровельные работы', 'Монтаж и настройка оборудования', 'Сварочные работы', 'Строительство фасадов', 'Формовка материалов', 'Бетонные и каменные работы', 'Ремонтные работы', 'Другие']] | None = None
    coordinates: Vacancy20ParamsModel30CoordinatesModel31 | None = None
    cuisine: list[Literal['Русская', 'Европейская', 'Кавказская', 'Итальянская', 'Японская', 'Турецкая', 'Другая']] | None = None
    delivery_method: list[Literal['На автомобиле', 'На велосипеде', 'На самокате', 'Пешком']] | None = None
    driving_experience: Literal['Нет опыта', 'Меньше года', '1-2 года', '3-5 лет', '6-10 лет', 'Больше 10 лет'] | None = None
    driving_license_category: DrivingLicenseCategory = None
    eatery_type: list[Literal['Кафе', 'Бар', 'Фастфуд', 'Ресторан', 'Столовая', 'Пекарня', 'Другой']] | None = None
    education_level: list[str] | None = None
    employment: str | None = None
    experience: Literal['Без опыта', 'Более 1 года', 'Более 3 лет', 'Более 5 лет', 'Более 10 лет'] | None = None
    facility_type: list[Literal['Производство', 'Логистический центр', 'Склад', 'Другое']] | None = None
    food_production_shop_type: list[Literal['Холодный', 'Горячий', 'Кондитерский', 'Заготовочный', 'Другой']] | None = None
    grade: str | None = None
    is_company_car: Literal['Да', 'Нет'] | None = None
    is_remote: Literal['Да', 'Нет'] | None = None
    is_side_job: Literal['Да', 'Нет'] | None = None
    medical_book: Literal['Должен оформить кандидат', 'Поможем оформить', 'Не нужна'] | None = None
    medical_specialization: list[str] | None = None
    paid_period: Literal['в месяц', 'в неделю', 'за смену', 'за час', 'сдельная оплата'] | None = None
    payout_frequency: Literal['почасовая оплата', 'каждый день', 'дважды в месяц', 'раз в неделю', 'три раза в месяц', 'раз в месяц'] | None = None
    profession: str | None = None
    registration_method: list[Literal['Трудовой договор', 'ГПХ с ИП', 'ГПХ с самозанятым', 'ГПХ с физическим лицом']] | None = None
    retail_equipment_type: list[Literal['Касса и POS-терминалы', 'Программы учёта товаров']] | None = None
    retail_shop_type: list[Literal['Гипермаркет или супермаркет', 'Продуктовый', 'Электроника и бытовая техника', 'Одежда и обувь', 'Парфюмерия и косметика', 'Строительство и хозтовары', 'Детские товары', 'Спортивные товары', 'Зоомагазин', 'Аптека', 'Другое']] | None = None
    salary: Vacancy20ParamsModel30SalaryModel32 | None = None
    salary_base_bonus: str | None = None
    salary_base_range: Vacancy20ParamsModel30SalaryBaseRangeModel33 | None = None
    schedule: Literal['5/2', '6/1', 'Вахта', 'Гибкий', 'Сменный', 'Полный день', 'Неполный день', 'Фиксированный', 'Удалённая работа'] | None = None
    shifts: list[str] | None = None
    taxes: Literal['До вычета налогов', 'На руки'] | None = None
    tools_availability: Literal['Нужны свои', 'Предоставляет работодатель'] | None = None
    vacancy_code: str | None = None
    vehicle_type: str | None = None
    work_days_per_week: list[str] | None = None
    work_format: list[str] | None = None
    work_hours_per_day: list[str] | None = None
    worker_class: list[Literal['1', '2', '3', '4', '5 и выше', 'Не требуется']] | None = None

class Vacancy20(_BaseModel):
    address_details: Vacancy20AddressDetailsModel26 | None = Field(default=None, alias='addressDetails')
    auto_renewal: bool | None = None
    contacts: Vacancy20ContactsModel28 | None = None
    description: str = None
    hierarchy: Vacancy20HierarchyModel29 | None = None
    id: int = None
    is_active: bool = None
    params: Vacancy20ParamsModel30 = None
    salary: int | None = None
    start_time: str = None
    title: str = None
    update_time: str = None
    url: str = None
    uuid: str | None = None

class JobApiVacanciesGetByIdsResponse(RootModel[list[Vacancy20]]):
    pass

class JobApiVacancyGetStatusesResponseItemModel34LastActionModel35ErrorModel36(_BaseModel):
    code: int = None
    message: str = None

class JobApiVacancyGetStatusesResponseItemModel34LastActionModel35(_BaseModel):
    datetime: str = None
    error: JobApiVacancyGetStatusesResponseItemModel34LastActionModel35ErrorModel36 = None
    status: str = None

class JobApiVacancyGetStatusesResponseItemModel34VacancyModel37(_BaseModel):
    id: int = None
    moderation_status: Literal['in_progress', 'allowed', 'blocked', 'rejected'] | None = None
    reasons: dict[str, Any] = None
    status: Literal['created', 'activated', 'archived', 'blocked', 'closed', 'expired', 'rejected', 'unblocked'] = None
    url: str = None

class JobApiVacancyGetStatusesResponseItemModel34(_BaseModel):
    id: str = None
    last_action: JobApiVacancyGetStatusesResponseItemModel34LastActionModel35 = None
    vacancy: JobApiVacancyGetStatusesResponseItemModel34VacancyModel37 = None

class JobApiVacancyGetStatusesResponse(RootModel[list[JobApiVacancyGetStatusesResponseItemModel34]]):
    pass

class JobApiVacancyUpdateV2Response(_BaseModel):
    id: str = None

class JobApiVacancyGetItemResponseAddressDetailsModel38CoordinatesModel39(_BaseModel):
    latitude: float = None
    longitude: float = None

class JobApiVacancyGetItemResponseAddressDetailsModel38(_BaseModel):
    address: str = None
    city: str = None
    coordinates: JobApiVacancyGetItemResponseAddressDetailsModel38CoordinatesModel39 = None
    province: str = None

class JobApiVacancyGetItemResponseContactsModel40(_BaseModel):
    email: str | None = None
    name: str | None = None

class JobApiVacancyGetItemResponseHierarchyModel41(_BaseModel):
    employee_id: int | None = None

class JobApiVacancyGetItemResponseParamsModel42CoordinatesModel43(_BaseModel):
    latitude: float = None
    longitude: float = None

class JobApiVacancyGetItemResponseParamsModel42SalaryModel44(_BaseModel):
    from_: int | None = Field(default=None, alias='from')
    to: int | None = None

class JobApiVacancyGetItemResponseParamsModel42SalaryBaseRangeModel45(_BaseModel):
    from_: int | None = Field(default=None, alias='from')
    to: int | None = None

class JobApiVacancyGetItemResponseParamsModel42(_BaseModel):
    address: str | None = None
    administrator_organization_type: str | None = None
    age_preferences: list[Literal['Соискатели старше 45 лет', 'Соискатели от 14 лет', 'Соискатели от 16 лет', 'С нарушениями здоровья', 'Для студентов', 'Для пенсионеров']] | None = None
    bonuses: list[Literal['Униформа', 'Проживание', 'Медицинская страховка', 'Питание', 'Оплата бензина', 'Парковка', 'Зоны отдыха', 'Транспорт до работы', 'Скидки в компании', 'Подарки детям на праздники', 'Оплата мобильной связи', 'Обучение', 'Компенсация проезда с работы', 'КАСКО', 'Смартфон', 'Услуги шиномонтажа']] | None = None
    business_area: str | None = None
    change: list[Literal['1 / 2', '1 / 3', '2 / 1', '2 / 2', '3 / 3', '3 / 2', '4 / 3', '5 / 2', '4 / 2', '6 / 1', 'Без выходных', 'Утренние', 'Дневные', 'Вечерние', 'Ночные', 'Плавающие выходные', 'Работа по выходным']] | None = None
    citizenship: list[str] | None = None
    construction_work_type: list[Literal['Малярные работы', 'Облицовка стен', 'Работы с плиткой', 'Монтаж и установка', 'Отделочные работы', 'Кровельные работы', 'Монтаж и настройка оборудования', 'Сварочные работы', 'Строительство фасадов', 'Формовка материалов', 'Бетонные и каменные работы', 'Ремонтные работы', 'Другие']] | None = None
    coordinates: JobApiVacancyGetItemResponseParamsModel42CoordinatesModel43 | None = None
    cuisine: list[Literal['Русская', 'Европейская', 'Кавказская', 'Итальянская', 'Японская', 'Турецкая', 'Другая']] | None = None
    delivery_method: list[Literal['На автомобиле', 'На велосипеде', 'На самокате', 'Пешком']] | None = None
    driving_experience: Literal['Нет опыта', 'Меньше года', '1-2 года', '3-5 лет', '6-10 лет', 'Больше 10 лет'] | None = None
    driving_license_category: DrivingLicenseCategory = None
    eatery_type: list[Literal['Кафе', 'Бар', 'Фастфуд', 'Ресторан', 'Столовая', 'Пекарня', 'Другой']] | None = None
    education_level: list[str] | None = None
    employment: str | None = None
    experience: Literal['Без опыта', 'Более 1 года', 'Более 3 лет', 'Более 5 лет', 'Более 10 лет'] | None = None
    facility_type: list[Literal['Производство', 'Логистический центр', 'Склад', 'Другое']] | None = None
    food_production_shop_type: list[Literal['Холодный', 'Горячий', 'Кондитерский', 'Заготовочный', 'Другой']] | None = None
    grade: str | None = None
    is_company_car: Literal['Да', 'Нет'] | None = None
    is_remote: Literal['Да', 'Нет'] | None = None
    is_side_job: Literal['Да', 'Нет'] | None = None
    medical_book: Literal['Должен оформить кандидат', 'Поможем оформить', 'Не нужна'] | None = None
    medical_specialization: list[str] | None = None
    paid_period: Literal['в месяц', 'в неделю', 'за смену', 'за час', 'сдельная оплата'] | None = None
    payout_frequency: Literal['почасовая оплата', 'каждый день', 'дважды в месяц', 'раз в неделю', 'три раза в месяц', 'раз в месяц'] | None = None
    profession: str | None = None
    registration_method: list[Literal['Трудовой договор', 'ГПХ с ИП', 'ГПХ с самозанятым', 'ГПХ с физическим лицом']] | None = None
    retail_equipment_type: list[Literal['Касса и POS-терминалы', 'Программы учёта товаров']] | None = None
    retail_shop_type: list[Literal['Гипермаркет или супермаркет', 'Продуктовый', 'Электроника и бытовая техника', 'Одежда и обувь', 'Парфюмерия и косметика', 'Строительство и хозтовары', 'Детские товары', 'Спортивные товары', 'Зоомагазин', 'Аптека', 'Другое']] | None = None
    salary: JobApiVacancyGetItemResponseParamsModel42SalaryModel44 | None = None
    salary_base_bonus: str | None = None
    salary_base_range: JobApiVacancyGetItemResponseParamsModel42SalaryBaseRangeModel45 | None = None
    schedule: Literal['5/2', '6/1', 'Вахта', 'Гибкий', 'Сменный', 'Полный день', 'Неполный день', 'Фиксированный', 'Удалённая работа'] | None = None
    shifts: list[str] | None = None
    taxes: Literal['До вычета налогов', 'На руки'] | None = None
    tools_availability: Literal['Нужны свои', 'Предоставляет работодатель'] | None = None
    vacancy_code: str | None = None
    vehicle_type: str | None = None
    work_days_per_week: list[str] | None = None
    work_format: list[str] | None = None
    work_hours_per_day: list[str] | None = None
    worker_class: list[Literal['1', '2', '3', '4', '5 и выше', 'Не требуется']] | None = None

class JobApiVacancyGetItemResponse(_BaseModel):
    address_details: JobApiVacancyGetItemResponseAddressDetailsModel38 | None = Field(default=None, alias='addressDetails')
    auto_renewal: bool | None = None
    contacts: JobApiVacancyGetItemResponseContactsModel40 | None = None
    description: str = None
    hierarchy: JobApiVacancyGetItemResponseHierarchyModel41 | None = None
    id: int = None
    is_active: bool = None
    params: JobApiVacancyGetItemResponseParamsModel42 = None
    salary: int | None = None
    start_time: str = None
    title: str = None
    update_time: str = None
    url: str = None
    uuid: str | None = None

class JobApiGetDictsResponseItemModel46(_BaseModel):
    description: str = None
    id: str = None

class JobApiGetDictsResponse(RootModel[list[JobApiGetDictsResponseItemModel46]]):
    pass

class JobApiGetDictByIdResponseItemModel47(_BaseModel):
    deprecated: bool = None
    id: int = None
    name: str = None

class JobApiGetDictByIdResponse(RootModel[list[JobApiGetDictByIdResponseItemModel47]]):
    pass

__all__ = ['JobApiApplicationsApplyActionsResponseAppliesItemModel1', 'JobApiApplicationsApplyActionsResponse', 'EducationLevel', 'JobApiApplicationsGetByIdsResponseAppliesItemModel2ApplicantModel3DataModel4FullNameModel5', 'Gender', 'JobApiApplicationsGetByIdsResponseAppliesItemModel2ApplicantModel3DataModel4', 'JobApiApplicationsGetByIdsResponseAppliesItemModel2ApplicantModel3', 'JobApiApplicationsGetByIdsResponseAppliesItemModel2ContactsModel6ChatModel7', 'JobApiApplicationsGetByIdsResponseAppliesItemModel2ContactsModel6PhonesItemModel8', 'JobApiApplicationsGetByIdsResponseAppliesItemModel2ContactsModel6', 'EnrichedPropertyMatchingStatus', 'EnrichedPropertiesAgeModel9', 'EnrichedPropertiesCitizenshipModel10', 'EnrichedPropertiesExperienceModel11', 'EnrichedPropertiesFullNameModel12', 'EnrichedPropertiesGenderModel13', 'EnrichedPropertiesPhoneModel14', 'EnrichedProperties', 'PrevalidationAnswer', 'JobApiApplicationsGetByIdsResponseAppliesItemModel2PrevalidationModel15', 'JobApiApplicationsGetByIdsResponseAppliesItemModel2PriceModel16', 'JobApiApplicationsGetByIdsResponseAppliesItemModel2', 'JobApiApplicationsGetByIdsResponse', 'JobApiApplicationsGetIdsResponseAppliesItemModel17', 'JobApiApplicationsGetIdsResponse', 'JobApiApplicationsGetStatesResponseStatesItemModel18', 'JobApiApplicationsGetStatesResponse', 'JobApiApplicationsSetIsViewedResponseAppliesItemModel19', 'JobApiApplicationsSetIsViewedResponse', 'JobApiApplicationsWebhookGetResponse', 'JobApiApplicationsWebhookPutResponse', 'JobApiApplicationsWebhookDeleteResponse', 'WebhookSubscribeRequestBody', 'JobApiApplicationsWebhooksGetResponse', 'ResumeSearchMeta', 'Coordinates', 'AddressDetails', 'DriverLicence', 'DriverLicenceCategory', 'DrivingExperience', 'Location', 'MedicalBook', 'Citizenship', 'OwnTransport', 'Specialization', 'SimplifiedResume', 'JobApiResumesGetResponse', 'ResumeContact', 'JobApiResumeGetContactsResponseFullNameModel20', 'JobApiResumeGetContactsResponse', 'JobApiVacancyCreateResponse', 'JobApiResumeGetItemResponseParamsModel21EducationListItemModel22', 'JobApiResumeGetItemResponseParamsModel21ExperienceListItemModel23', 'JobApiResumeGetItemResponseParamsModel21LanguageListItemModel24', 'JobApiResumeGetItemResponseParamsModel21', 'Photo', 'JobApiResumeGetItemResponse', 'VacancySearchMeta', 'SimplifiedVacancyAddressDetailsModel25', 'SimplifiedVacancy', 'JobApiSearchVacancyResponse', 'JobApiVacancyCreateV2Response', 'Vacancy20AddressDetailsModel26CoordinatesModel27', 'Vacancy20AddressDetailsModel26', 'Vacancy20ContactsModel28', 'Vacancy20HierarchyModel29', 'Vacancy20ParamsModel30CoordinatesModel31', 'DrivingLicenseCategory', 'Vacancy20ParamsModel30SalaryModel32', 'Vacancy20ParamsModel30SalaryBaseRangeModel33', 'Vacancy20ParamsModel30', 'Vacancy20', 'JobApiVacanciesGetByIdsResponse', 'JobApiVacancyGetStatusesResponseItemModel34LastActionModel35ErrorModel36', 'JobApiVacancyGetStatusesResponseItemModel34LastActionModel35', 'JobApiVacancyGetStatusesResponseItemModel34VacancyModel37', 'JobApiVacancyGetStatusesResponseItemModel34', 'JobApiVacancyGetStatusesResponse', 'JobApiVacancyUpdateV2Response', 'JobApiVacancyGetItemResponseAddressDetailsModel38CoordinatesModel39', 'JobApiVacancyGetItemResponseAddressDetailsModel38', 'JobApiVacancyGetItemResponseContactsModel40', 'JobApiVacancyGetItemResponseHierarchyModel41', 'JobApiVacancyGetItemResponseParamsModel42CoordinatesModel43', 'JobApiVacancyGetItemResponseParamsModel42SalaryModel44', 'JobApiVacancyGetItemResponseParamsModel42SalaryBaseRangeModel45', 'JobApiVacancyGetItemResponseParamsModel42', 'JobApiVacancyGetItemResponse', 'JobApiGetDictsResponseItemModel46', 'JobApiGetDictsResponse', 'JobApiGetDictByIdResponseItemModel47', 'JobApiGetDictByIdResponse']
