"""Generated response models for slug: job."""

from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, ValidationError, Field, RootModel

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class EducationLevel(RootModel[Literal['higher', 'unfinished-higher', 'secondary', 'special-secondary', None]]):
    pass

class JobApiApplicationsGetByIdsResponseAppliesItemModel1ApplicantModel2DataModel3FullNameModel4(_BaseModel):
    first_name: str = None
    last_name: str = None
    patronymic: str | None = None

class JobApiApplicationsGetByIdsResponseAppliesItemModel1ApplicantModel2DataModel3(_BaseModel):
    birthday: str | None = None
    citizenship: str | None = None
    education: EducationLevel = None
    full_name: JobApiApplicationsGetByIdsResponseAppliesItemModel1ApplicantModel2DataModel3FullNameModel4 | None = None
    gender: str | None = None
    name: str | None = None

class JobApiApplicationsGetByIdsResponseAppliesItemModel1ApplicantModel2(_BaseModel):
    data: JobApiApplicationsGetByIdsResponseAppliesItemModel1ApplicantModel2DataModel3 = None
    id: str = None
    resume_id: str | None = None

class JobApiApplicationsGetByIdsResponseAppliesItemModel1ContactsModel5ChatModel6(_BaseModel):
    value: str = None

class JobApiApplicationsGetByIdsResponseAppliesItemModel1ContactsModel5PhonesItemModel7(_BaseModel):
    status: str | None = None
    value: str = None

class JobApiApplicationsGetByIdsResponseAppliesItemModel1ContactsModel5(_BaseModel):
    chat: JobApiApplicationsGetByIdsResponseAppliesItemModel1ContactsModel5ChatModel6 | None = None
    phones: list[JobApiApplicationsGetByIdsResponseAppliesItemModel1ContactsModel5PhonesItemModel7] = None

class EnrichedPropertyMatchingStatus(RootModel[Literal['no_criteria', 'matched', 'mismatched']]):
    pass

class EnrichedPropertiesAgeModel8(_BaseModel):
    matching_status: EnrichedPropertyMatchingStatus = None
    value: int | None = None

class EnrichedPropertiesCitizenshipModel9(_BaseModel):
    matching_status: EnrichedPropertyMatchingStatus = None
    value: str | None = None

class EnrichedPropertiesExperienceModel10(_BaseModel):
    matching_status: EnrichedPropertyMatchingStatus = None
    value: str | None = None

class EnrichedPropertiesFullNameModel11(_BaseModel):
    matching_status: EnrichedPropertyMatchingStatus = None
    value: str | None = None

class EnrichedPropertiesGenderModel12(_BaseModel):
    matching_status: EnrichedPropertyMatchingStatus = None
    value: str | None = None

class EnrichedPropertiesPhoneModel13(_BaseModel):
    matching_status: EnrichedPropertyMatchingStatus = None
    value: str | None = None

class EnrichedProperties(_BaseModel):
    age: EnrichedPropertiesAgeModel8 | None = None
    citizenship: EnrichedPropertiesCitizenshipModel9 | None = None
    experience: EnrichedPropertiesExperienceModel10 | None = None
    full_name: EnrichedPropertiesFullNameModel11 | None = None
    gender: EnrichedPropertiesGenderModel12 | None = None
    phone: EnrichedPropertiesPhoneModel13 | None = None
    status: Literal['in_progress', 'not_completed', 'completed_no_criteria', 'completed_matched', 'completed_mismatched'] = None

class PrevalidationAnswer(_BaseModel):
    label: str = None
    value: str = None
    variable: str = None

class JobApiApplicationsGetByIdsResponseAppliesItemModel1PrevalidationModel14(_BaseModel):
    status: str = None
    summary: list[PrevalidationAnswer] | None = None

class JobApiApplicationsGetByIdsResponseAppliesItemModel1PriceModel15(_BaseModel):
    bonus: int
    real: int
    total: int

class JobApiApplicationsGetByIdsResponseAppliesItemModel1(_BaseModel):
    applicant: JobApiApplicationsGetByIdsResponseAppliesItemModel1ApplicantModel2 = None
    contacts: JobApiApplicationsGetByIdsResponseAppliesItemModel1ContactsModel5 = None
    created_at: str = None
    employee_id: int | None = None
    enriched_properties: EnrichedProperties = None
    id: str = None
    is_viewed: bool = None
    negotiation_id: int | None = None
    prevalidation: JobApiApplicationsGetByIdsResponseAppliesItemModel1PrevalidationModel14 | None = None
    price: JobApiApplicationsGetByIdsResponseAppliesItemModel1PriceModel15 | None = None
    source: Literal['sbc_cold_flow'] = None
    state: str = None
    type: Literal['by_phone', 'by_chat'] = None
    updated_at: str = None
    vacancy_id: int = None

class JobApiApplicationsGetByIdsResponse(_BaseModel):
    applies: list[JobApiApplicationsGetByIdsResponseAppliesItemModel1] = None

class JobApiApplicationsGetIdsResponseAppliesItemModel16(_BaseModel):
    created_at: str = None
    id: str = None
    state: str = None
    updated_at: str = None

class JobApiApplicationsGetIdsResponse(_BaseModel):
    applies: list[JobApiApplicationsGetIdsResponseAppliesItemModel16] = None

class JobApiApplicationsGetStatesResponseStatesItemModel17(_BaseModel):
    description: str = None
    slug: str = None

class JobApiApplicationsGetStatesResponse(_BaseModel):
    states: list[JobApiApplicationsGetStatesResponseStatesItemModel17] = None

class JobApiApplicationsSetIsViewedResponseAppliesItemModel18(_BaseModel):
    id: str
    is_viewed: bool

class JobApiApplicationsSetIsViewedResponse(_BaseModel):
    applies: list[JobApiApplicationsSetIsViewedResponseAppliesItemModel18] = None

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

class DriverLicence(RootModel[Literal['yes', 'no']]):
    pass

class DriverLicenceCategory(RootModel[list[Literal['a', 'b', 'be', 'c', 'ce', 'd', 'de', 'm', 'tm', 'tb']]]):
    pass

class DrivingExperience(RootModel[Literal['less-than-three-years', 'more-than-three-years']]):
    pass

class Gender(RootModel[Literal['female', 'male', None]]):
    pass

class Location(_BaseModel):
    id: int = None
    title: str = None

class MedicalBook(RootModel[Literal['yes', 'no']]):
    pass

class Citizenship(_BaseModel):
    id: int = None
    title: str = None

class OwnTransport(RootModel[Literal['no', 'car', 'cargo-car', 'bike', 'scooter']]):
    pass

class Specialization(_BaseModel):
    id: int = None
    title: str = None

class SimplifiedResume(_BaseModel):
    address_details: AddressDetails = None
    age: int = None
    created_at: str = None
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
    updated_at: str = None

class JobApiResumesGetResponse(_BaseModel):
    meta: ResumeSearchMeta = None
    resumes: list[SimplifiedResume] = None

class ResumeContact(_BaseModel):
    type: Literal['e-mail', 'phone', 'chat_id'] = None
    value: str = None

class JobApiResumeGetContactsResponseFullNameModel19(_BaseModel):
    first_name: str = None
    last_name: str = None
    patronymic: str | None = None

class JobApiResumeGetContactsResponse(_BaseModel):
    already_bought: bool = None
    contacts: list[ResumeContact] = None
    full_name: JobApiResumeGetContactsResponseFullNameModel19 | None = None
    name: str = None

class JobApiVacancyCreateResponse(_BaseModel):
    id: str = None
    url: str = None
    uuid: str | None = None

class JobApiResumeGetItemResponseParamsModel20EducationListItemModel21(_BaseModel):
    education_stop: str | None = None
    institution: str | None = None
    specialty: str | None = None

class JobApiResumeGetItemResponseParamsModel20ExperienceListItemModel22(_BaseModel):
    company: str | None = None
    position: str | None = None
    responsibilities: str | None = None
    work_finish: str | None = None
    work_start: str | None = None

class JobApiResumeGetItemResponseParamsModel20LanguageListItemModel23(_BaseModel):
    language: str | None = None
    language_level: Literal['Начальный', 'Средний', 'Выше среднего', 'Свободное владение'] | None = None

class JobApiResumeGetItemResponseParamsModel20(_BaseModel):
    ability_to_business_trip: Literal['Не готов', 'Готов', 'Иногда'] | None = None
    address: str | None = None
    age: int | None = None
    business_area: Literal['IT, интернет, телеком', 'Автомобильный бизнес', 'Административная работа', 'Банки, инвестиции', 'Без опыта, студенты', 'Бухгалтерия, финансы', 'Высший менеджмент', 'Госслужба, НКО', 'Домашний персонал', 'ЖКХ, эксплуатация', 'Искусство, развлечения', 'Консультирование', 'Курьерская доставка', 'Маркетинг, реклама, PR', 'Медицина, фармацевтика', 'Образование, наука', 'Охрана, безопасность', 'Продажи', 'Производство, сырьё, с/х', 'Страхование', 'Строительство', 'Такси', 'Транспорт, логистика', 'Туризм, рестораны', 'Управление персоналом', 'Фитнес, салоны красоты', 'Юриспруденция'] | None = None
    driver_licence: Literal['Есть', 'Нет'] | None = None
    driver_licence_category: list[Literal['A', 'B', 'BE', 'C', 'CE', 'D', 'DE', 'M', 'Tm', 'Tb']] | None = None
    education: Literal['Высшее', 'Незаконченное высшее', 'Среднее', 'Среднее специальное'] | None = None
    education_list: list[JobApiResumeGetItemResponseParamsModel20EducationListItemModel21] | None = None
    experience: int | None = None
    experience_list: list[JobApiResumeGetItemResponseParamsModel20ExperienceListItemModel22] | None = None
    language_list: list[JobApiResumeGetItemResponseParamsModel20LanguageListItemModel23] | None = None
    moving: Literal['Невозможен', 'Возможен'] | None = None
    nationality: str | None = None
    pol: Literal['Мужской', 'Женский'] | None = None
    razreshenie_na_rabotu_v_rossii: Literal['Да', 'Нет'] | None = None
    schedule: Literal['Вахтовый метод', 'Неполный день', 'Полный день', 'Свободный график', 'Сменный график', 'Удалённая работа'] | None = None

class Photo(_BaseModel):
    url: str = None

class JobApiResumeGetItemResponse(_BaseModel):
    address_details: AddressDetails = None
    description: str = None
    id: int = None
    is_active: bool = None
    is_purchased: bool = None
    params: JobApiResumeGetItemResponseParamsModel20 = None
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

class SimplifiedVacancyAddressDetailsModel24(_BaseModel):
    address: str = None
    city: str = None

class SimplifiedVacancy(_BaseModel):
    address_details: SimplifiedVacancyAddressDetailsModel24 = Field(default=None, alias='addressDetails')
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

class Vacancy20AddressDetailsModel25CoordinatesModel26(_BaseModel):
    latitude: float = None
    longitude: float = None

class Vacancy20AddressDetailsModel25(_BaseModel):
    address: str = None
    area: str | None = None
    city: str = None
    coordinates: Vacancy20AddressDetailsModel25CoordinatesModel26 = None
    province: str = None

class Vacancy20ContactsModel27(_BaseModel):
    allow_calls: bool = None
    allow_messages: bool = None
    email: str | None = None
    name: str | None = None

class Vacancy20HierarchyModel28(_BaseModel):
    employee_id: int | None = None

class Vacancy20ParamsModel29CoordinatesModel30(_BaseModel):
    latitude: float = None
    longitude: float = None

class DrivingLicenseCategory(RootModel[list[Literal['A', 'AI', 'AII', 'AIII', 'AIV', 'B', 'B1', 'BE', 'C', 'C1', 'C1E', 'CE', 'D', 'D1', 'D1E', 'DE', 'E', 'F', 'Tm', 'Tb', 'M']]]):
    pass

class Vacancy20ParamsModel29SalaryModel31(_BaseModel):
    from_: int | None = Field(default=None, alias='from')
    to: int | None = None

class Vacancy20ParamsModel29SalaryBaseRangeModel32(_BaseModel):
    from_: int | None = Field(default=None, alias='from')
    to: int | None = None

class Vacancy20ParamsModel29(_BaseModel):
    address: str | None = None
    administrator_organization_type: str | None = None
    age_preferences: list[Literal['от 14 лет', 'от 16 лет', 'старше 45 лет', 'для студентов', 'для пенсионеров', 'с нарушениями здоровья']] | None = None
    applies_filter: Literal['Любые', 'Только с резюме'] | None = None
    bonuses: list[Literal['Униформа', 'Проживание', 'Медицинская страховка', 'Питание', 'Оплата бензина', 'Парковка', 'Зоны отдыха', 'Транспорт до работы', 'Скидки в компании', 'Подарки детям на праздники', 'Оплата мобильной связи', 'Обучение', 'Компенсация проезда с работы', 'КАСКО', 'Смартфон', 'Услуги шиномонтажа']] | None = None
    business_area: str | None = None
    change: list[Literal['1 / 2', '1 / 3', '2 / 1', '2 / 2', '3 / 3', '3 / 2', '4 / 3', '5 / 2', '4 / 2', '6 / 1', 'Без выходных', 'Утренние', 'Дневные', 'Вечерние', 'Ночные', 'Плавающие выходные', 'Работа по выходным']] | None = None
    citizenship: list[str] | None = None
    construction_work_type: list[Literal['Малярные работы', 'Облицовка стен', 'Работы с плиткой', 'Монтаж и установка', 'Отделочные работы', 'Кровельные работы', 'Монтаж и настройка оборудования', 'Сварочные работы', 'Строительство фасадов', 'Формовка материалов', 'Бетонные и каменные работы', 'Ремонтные работы', 'Другие']] | None = None
    coordinates: Vacancy20ParamsModel29CoordinatesModel30 | None = None
    cuisine: list[Literal['Русская', 'Европейская', 'Кавказская', 'Итальянская', 'Японская', 'Турецкая', 'Другая']] | None = None
    delivery_method: list[Literal['На автомобиле', 'На велосипеде', 'На самокате', 'Пешком']] | None = None
    driving_experience: Literal['Нет опыта', 'Меньше года', '1-2 года', '3-5 лет', '6-10 лет', 'Больше 10 лет'] | None = None
    driving_license_category: DrivingLicenseCategory = None
    eatery_type: list[Literal['Кафе', 'Бар', 'Фастфуд', 'Ресторан', 'Столовая', 'Пекарня', 'Другой']] | None = None
    education_level: Literal['Не имеет значения', 'Среднее профессиональное', 'Высшее'] | None = None
    employment: str | None = None
    experience: Literal['Без опыта', 'Более 1 года', 'Более 3 лет', 'Более 5 лет', 'Более 10 лет'] | None = None
    facility_type: list[Literal['Производство', 'Логистический центр', 'Склад', 'Другое']] | None = None
    food_production_shop_type: list[Literal['Холодный', 'Горячий', 'Кондитерский', 'Заготовочный', 'Другой']] | None = None
    grade: str | None = None
    is_company_car: Literal['Да', 'Нет'] | None = None
    is_remote: Literal['Да', 'Нет'] | None = None
    is_side_job: Literal['Да', 'Нет'] | None = None
    job_responsibilities: str | None = None
    jobs_number: int | None = None
    medical_book: Literal['Должен оформить кандидат', 'Поможем оформить', 'Не нужна'] | None = None
    medical_specialization: list[str] | None = None
    paid_period: Literal['в месяц', 'в неделю', 'за смену', 'за час', 'сдельная оплата'] | None = None
    payout_frequency: Literal['Почасовая оплата', 'Каждый день', 'Дважды в месяц', 'Раз в неделю', 'Три раза в месяц', 'Раз в месяц'] | None = None
    profession: str | None = None
    registration_method: list[Literal['Трудовой договор', 'ГПХ с ИП', 'ГПХ с самозанятым', 'ГПХ с физическим лицом']] | None = None
    retail_equipment_type: list[Literal['Касса и POS-терминалы', 'Программы учёта товаров']] | None = None
    retail_shop_type: list[Literal['Гипермаркет или супермаркет', 'Продуктовый', 'Электроника и бытовая техника', 'Одежда и обувь', 'Парфюмерия и косметика', 'Строительство и хозтовары', 'Детские товары', 'Спортивные товары', 'Зоомагазин', 'Аптека', 'Другое']] | None = None
    salary: Vacancy20ParamsModel29SalaryModel31 | None = None
    salary_base_bonus: str | None = None
    salary_base_range: Vacancy20ParamsModel29SalaryBaseRangeModel32 | None = None
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
    address_details: Vacancy20AddressDetailsModel25 | None = Field(default=None, alias='addressDetails')
    auto_renewal: bool | None = None
    contacts: Vacancy20ContactsModel27 | None = None
    description: str = None
    hierarchy: Vacancy20HierarchyModel28 | None = None
    id: int = None
    is_active: bool = None
    params: Vacancy20ParamsModel29 = None
    salary: int | None = None
    start_time: str = None
    title: str = None
    update_time: str = None
    url: str = None
    uuid: str | None = None

class JobApiVacanciesGetByIdsResponse(RootModel[list[Vacancy20]]):
    pass

class JobApiVacancyGetStatusesResponseItemModel33LastActionModel34ErrorModel35(_BaseModel):
    code: int = None
    message: str = None

class JobApiVacancyGetStatusesResponseItemModel33LastActionModel34(_BaseModel):
    datetime: str = None
    error: JobApiVacancyGetStatusesResponseItemModel33LastActionModel34ErrorModel35 = None
    status: str = None

class JobApiVacancyGetStatusesResponseItemModel33VacancyModel36(_BaseModel):
    id: int = None
    moderation_status: Literal['in_progress', 'allowed', 'blocked', 'rejected'] | None = None
    reasons: list[str] | None = None
    status: Literal['created', 'activated', 'archived', 'blocked', 'closed', 'expired', 'rejected', 'unblocked'] = None
    url: str = None

class JobApiVacancyGetStatusesResponseItemModel33(_BaseModel):
    id: str = None
    last_action: JobApiVacancyGetStatusesResponseItemModel33LastActionModel34 = None
    vacancy: JobApiVacancyGetStatusesResponseItemModel33VacancyModel36 = None

class JobApiVacancyGetStatusesResponse(RootModel[list[JobApiVacancyGetStatusesResponseItemModel33]]):
    pass

class JobApiVacancyUpdateV2Response(_BaseModel):
    id: str = None

class JobApiVacancyGetItemResponseAddressDetailsModel37CoordinatesModel38(_BaseModel):
    latitude: float = None
    longitude: float = None

class JobApiVacancyGetItemResponseAddressDetailsModel37(_BaseModel):
    address: str = None
    area: str | None = None
    city: str = None
    coordinates: JobApiVacancyGetItemResponseAddressDetailsModel37CoordinatesModel38 = None
    province: str = None

class JobApiVacancyGetItemResponseContactsModel39(_BaseModel):
    allow_calls: bool = None
    allow_messages: bool = None
    email: str | None = None
    name: str | None = None

class JobApiVacancyGetItemResponseHierarchyModel40(_BaseModel):
    employee_id: int | None = None

class JobApiVacancyGetItemResponseParamsModel41CoordinatesModel42(_BaseModel):
    latitude: float = None
    longitude: float = None

class JobApiVacancyGetItemResponseParamsModel41SalaryModel43(_BaseModel):
    from_: int | None = Field(default=None, alias='from')
    to: int | None = None

class JobApiVacancyGetItemResponseParamsModel41SalaryBaseRangeModel44(_BaseModel):
    from_: int | None = Field(default=None, alias='from')
    to: int | None = None

class JobApiVacancyGetItemResponseParamsModel41(_BaseModel):
    address: str | None = None
    administrator_organization_type: str | None = None
    age_preferences: list[Literal['от 14 лет', 'от 16 лет', 'старше 45 лет', 'для студентов', 'для пенсионеров', 'с нарушениями здоровья']] | None = None
    applies_filter: Literal['Любые', 'Только с резюме'] | None = None
    bonuses: list[Literal['Униформа', 'Проживание', 'Медицинская страховка', 'Питание', 'Оплата бензина', 'Парковка', 'Зоны отдыха', 'Транспорт до работы', 'Скидки в компании', 'Подарки детям на праздники', 'Оплата мобильной связи', 'Обучение', 'Компенсация проезда с работы', 'КАСКО', 'Смартфон', 'Услуги шиномонтажа']] | None = None
    business_area: str | None = None
    change: list[Literal['1 / 2', '1 / 3', '2 / 1', '2 / 2', '3 / 3', '3 / 2', '4 / 3', '5 / 2', '4 / 2', '6 / 1', 'Без выходных', 'Утренние', 'Дневные', 'Вечерние', 'Ночные', 'Плавающие выходные', 'Работа по выходным']] | None = None
    citizenship: list[str] | None = None
    construction_work_type: list[Literal['Малярные работы', 'Облицовка стен', 'Работы с плиткой', 'Монтаж и установка', 'Отделочные работы', 'Кровельные работы', 'Монтаж и настройка оборудования', 'Сварочные работы', 'Строительство фасадов', 'Формовка материалов', 'Бетонные и каменные работы', 'Ремонтные работы', 'Другие']] | None = None
    coordinates: JobApiVacancyGetItemResponseParamsModel41CoordinatesModel42 | None = None
    cuisine: list[Literal['Русская', 'Европейская', 'Кавказская', 'Итальянская', 'Японская', 'Турецкая', 'Другая']] | None = None
    delivery_method: list[Literal['На автомобиле', 'На велосипеде', 'На самокате', 'Пешком']] | None = None
    driving_experience: Literal['Нет опыта', 'Меньше года', '1-2 года', '3-5 лет', '6-10 лет', 'Больше 10 лет'] | None = None
    driving_license_category: DrivingLicenseCategory = None
    eatery_type: list[Literal['Кафе', 'Бар', 'Фастфуд', 'Ресторан', 'Столовая', 'Пекарня', 'Другой']] | None = None
    education_level: Literal['Не имеет значения', 'Среднее профессиональное', 'Высшее'] | None = None
    employment: str | None = None
    experience: Literal['Без опыта', 'Более 1 года', 'Более 3 лет', 'Более 5 лет', 'Более 10 лет'] | None = None
    facility_type: list[Literal['Производство', 'Логистический центр', 'Склад', 'Другое']] | None = None
    food_production_shop_type: list[Literal['Холодный', 'Горячий', 'Кондитерский', 'Заготовочный', 'Другой']] | None = None
    grade: str | None = None
    is_company_car: Literal['Да', 'Нет'] | None = None
    is_remote: Literal['Да', 'Нет'] | None = None
    is_side_job: Literal['Да', 'Нет'] | None = None
    job_responsibilities: str | None = None
    jobs_number: int | None = None
    medical_book: Literal['Должен оформить кандидат', 'Поможем оформить', 'Не нужна'] | None = None
    medical_specialization: list[str] | None = None
    paid_period: Literal['в месяц', 'в неделю', 'за смену', 'за час', 'сдельная оплата'] | None = None
    payout_frequency: Literal['Почасовая оплата', 'Каждый день', 'Дважды в месяц', 'Раз в неделю', 'Три раза в месяц', 'Раз в месяц'] | None = None
    profession: str | None = None
    registration_method: list[Literal['Трудовой договор', 'ГПХ с ИП', 'ГПХ с самозанятым', 'ГПХ с физическим лицом']] | None = None
    retail_equipment_type: list[Literal['Касса и POS-терминалы', 'Программы учёта товаров']] | None = None
    retail_shop_type: list[Literal['Гипермаркет или супермаркет', 'Продуктовый', 'Электроника и бытовая техника', 'Одежда и обувь', 'Парфюмерия и косметика', 'Строительство и хозтовары', 'Детские товары', 'Спортивные товары', 'Зоомагазин', 'Аптека', 'Другое']] | None = None
    salary: JobApiVacancyGetItemResponseParamsModel41SalaryModel43 | None = None
    salary_base_bonus: str | None = None
    salary_base_range: JobApiVacancyGetItemResponseParamsModel41SalaryBaseRangeModel44 | None = None
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
    address_details: JobApiVacancyGetItemResponseAddressDetailsModel37 | None = Field(default=None, alias='addressDetails')
    auto_renewal: bool | None = None
    contacts: JobApiVacancyGetItemResponseContactsModel39 | None = None
    description: str = None
    hierarchy: JobApiVacancyGetItemResponseHierarchyModel40 | None = None
    id: int = None
    is_active: bool = None
    params: JobApiVacancyGetItemResponseParamsModel41 = None
    salary: int | None = None
    start_time: str = None
    title: str = None
    update_time: str = None
    url: str = None
    uuid: str | None = None

class JobApiGetDictsResponseItemModel45(_BaseModel):
    description: str = None
    id: str = None

class JobApiGetDictsResponse(RootModel[list[JobApiGetDictsResponseItemModel45]]):
    pass

class JobApiGetDictByIdResponseItemModel46(_BaseModel):
    deprecated: bool = None
    id: int = None
    name: str = None

class JobApiGetDictByIdResponse(RootModel[list[JobApiGetDictByIdResponseItemModel46]]):
    pass

__all__ = ['EducationLevel', 'JobApiApplicationsGetByIdsResponseAppliesItemModel1ApplicantModel2DataModel3FullNameModel4', 'JobApiApplicationsGetByIdsResponseAppliesItemModel1ApplicantModel2DataModel3', 'JobApiApplicationsGetByIdsResponseAppliesItemModel1ApplicantModel2', 'JobApiApplicationsGetByIdsResponseAppliesItemModel1ContactsModel5ChatModel6', 'JobApiApplicationsGetByIdsResponseAppliesItemModel1ContactsModel5PhonesItemModel7', 'JobApiApplicationsGetByIdsResponseAppliesItemModel1ContactsModel5', 'EnrichedPropertyMatchingStatus', 'EnrichedPropertiesAgeModel8', 'EnrichedPropertiesCitizenshipModel9', 'EnrichedPropertiesExperienceModel10', 'EnrichedPropertiesFullNameModel11', 'EnrichedPropertiesGenderModel12', 'EnrichedPropertiesPhoneModel13', 'EnrichedProperties', 'PrevalidationAnswer', 'JobApiApplicationsGetByIdsResponseAppliesItemModel1PrevalidationModel14', 'JobApiApplicationsGetByIdsResponseAppliesItemModel1PriceModel15', 'JobApiApplicationsGetByIdsResponseAppliesItemModel1', 'JobApiApplicationsGetByIdsResponse', 'JobApiApplicationsGetIdsResponseAppliesItemModel16', 'JobApiApplicationsGetIdsResponse', 'JobApiApplicationsGetStatesResponseStatesItemModel17', 'JobApiApplicationsGetStatesResponse', 'JobApiApplicationsSetIsViewedResponseAppliesItemModel18', 'JobApiApplicationsSetIsViewedResponse', 'JobApiApplicationsWebhookGetResponse', 'JobApiApplicationsWebhookPutResponse', 'JobApiApplicationsWebhookDeleteResponse', 'WebhookSubscribeRequestBody', 'JobApiApplicationsWebhooksGetResponse', 'ResumeSearchMeta', 'Coordinates', 'AddressDetails', 'DriverLicence', 'DriverLicenceCategory', 'DrivingExperience', 'Gender', 'Location', 'MedicalBook', 'Citizenship', 'OwnTransport', 'Specialization', 'SimplifiedResume', 'JobApiResumesGetResponse', 'ResumeContact', 'JobApiResumeGetContactsResponseFullNameModel19', 'JobApiResumeGetContactsResponse', 'JobApiVacancyCreateResponse', 'JobApiResumeGetItemResponseParamsModel20EducationListItemModel21', 'JobApiResumeGetItemResponseParamsModel20ExperienceListItemModel22', 'JobApiResumeGetItemResponseParamsModel20LanguageListItemModel23', 'JobApiResumeGetItemResponseParamsModel20', 'Photo', 'JobApiResumeGetItemResponse', 'VacancySearchMeta', 'SimplifiedVacancyAddressDetailsModel24', 'SimplifiedVacancy', 'JobApiSearchVacancyResponse', 'JobApiVacancyCreateV2Response', 'Vacancy20AddressDetailsModel25CoordinatesModel26', 'Vacancy20AddressDetailsModel25', 'Vacancy20ContactsModel27', 'Vacancy20HierarchyModel28', 'Vacancy20ParamsModel29CoordinatesModel30', 'DrivingLicenseCategory', 'Vacancy20ParamsModel29SalaryModel31', 'Vacancy20ParamsModel29SalaryBaseRangeModel32', 'Vacancy20ParamsModel29', 'Vacancy20', 'JobApiVacanciesGetByIdsResponse', 'JobApiVacancyGetStatusesResponseItemModel33LastActionModel34ErrorModel35', 'JobApiVacancyGetStatusesResponseItemModel33LastActionModel34', 'JobApiVacancyGetStatusesResponseItemModel33VacancyModel36', 'JobApiVacancyGetStatusesResponseItemModel33', 'JobApiVacancyGetStatusesResponse', 'JobApiVacancyUpdateV2Response', 'JobApiVacancyGetItemResponseAddressDetailsModel37CoordinatesModel38', 'JobApiVacancyGetItemResponseAddressDetailsModel37', 'JobApiVacancyGetItemResponseContactsModel39', 'JobApiVacancyGetItemResponseHierarchyModel40', 'JobApiVacancyGetItemResponseParamsModel41CoordinatesModel42', 'JobApiVacancyGetItemResponseParamsModel41SalaryModel43', 'JobApiVacancyGetItemResponseParamsModel41SalaryBaseRangeModel44', 'JobApiVacancyGetItemResponseParamsModel41', 'JobApiVacancyGetItemResponse', 'JobApiGetDictsResponseItemModel45', 'JobApiGetDictsResponse', 'JobApiGetDictByIdResponseItemModel46', 'JobApiGetDictByIdResponse']
