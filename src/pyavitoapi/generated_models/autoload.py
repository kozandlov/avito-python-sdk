"""Generated response models for slug: autoload."""

from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, ValidationError, RootModel

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class ExportScheduleItemModel1(_BaseModel):
    rate: int
    time_slots: list[int]
    weekdays: list[int]

class ExportSchedule(RootModel[list[ExportScheduleItemModel1]]):
    pass

class AutoloadApiGetProfileResponse(_BaseModel):
    autoload_enabled: bool
    report_email: str | None
    schedule: ExportSchedule
    upload_url: str | None

class APFieldsNodeAlert(_BaseModel):
    description: str = None
    title: str = None
    type: Literal['error', 'warning', 'info'] = None

class FieldValue(_BaseModel):
    description: str = None
    value: str = None

class APIDependencyPair(_BaseModel):
    clause: Literal['value', 'filled', 'empty'] = None
    source_field_tag: str = None
    values: list[str] = None

class APIDependency(_BaseModel):
    action: Literal['visible', 'required', 'hidden'] = None
    clause: Literal['or', 'and'] = None
    pairs: list[APIDependencyPair] = None

class FieldValueRange(_BaseModel):
    max: int | None = None
    min: int | None = None

class FieldWarning(_BaseModel):
    content: str
    title: str

class APIFieldContent(_BaseModel):
    data_type: Literal['string', 'integer', 'float']
    default: FieldValue = None
    dependencies: list[APIDependency] = None
    dependencies_text: list[str] = None
    field_type: Literal['input', 'select', 'checkbox']
    is_catalog: bool = None
    name_in_catalog: str | None = None
    required: bool
    required_by_dependency: bool
    values: list[FieldValue] = None
    values_link_json: str | None = None
    values_link_xml: str | None = None
    values_range: FieldValueRange = None
    warnings: list[FieldWarning] | None = None

class ChildAPIField(_BaseModel):
    content: list[APIFieldContent] = None
    descriptions: str = None
    feed_format: list[Literal['xml', 'excel']] = None
    label: str = None
    tag: str = None

class APIField(_BaseModel):
    children: list[ChildAPIField] = None
    content: list[APIFieldContent] = None
    descriptions: str = None
    feed_format: list[Literal['xml', 'excel']] = None
    label: str = None
    tag: str = None

class APIFieldsNode(_BaseModel):
    name: str
    slug: str

class AutoloadApiUserDocsNodeFieldsResponse(_BaseModel):
    alert: APFieldsNodeAlert = None
    fields: list[APIField]
    node: APIFieldsNode

class APICategoryNode(_BaseModel):
    name: str
    nested: list[dict[str, list[APICategoryNode]]] = None
    slug: str = None

class AutoloadApiUserDocsTreeResponse(_BaseModel):
    categories: list[APICategoryNode]

class AutoloadApiGetAdIdsByAvitoIdsResponseItemsItemModel2(_BaseModel):
    ad_id: str | None = None
    avito_id: int

class AutoloadApiGetAdIdsByAvitoIdsResponse(_BaseModel):
    items: list[AutoloadApiGetAdIdsByAvitoIdsResponseItemsItemModel2]

class AutoloadApiGetAvitoIdsByAdIdsResponseItemsItemModel3(_BaseModel):
    ad_id: str
    avito_id: int | None = None

class AutoloadApiGetAvitoIdsByAdIdsResponse(_BaseModel):
    items: list[AutoloadApiGetAvitoIdsByAdIdsResponseItemsItemModel3]

class FeedsDataItemModel4(_BaseModel):
    feed_name: str
    feed_url: str

class FeedsData(RootModel[list[FeedsDataItemModel4]]):
    pass

class AutoloadApiGetProfileV2Response(_BaseModel):
    autoload_enabled: bool
    feeds_data: FeedsData
    report_email: str | None
    schedule: ExportSchedule

class MetaReportsAutoloadV2(_BaseModel):
    page: int = None
    pages: int = None
    per_page: int = None
    total: int = None

class ReportShortAutoloadV2ItemModel5(_BaseModel):
    finished_at: str
    id: int
    started_at: str
    status: Literal['processing', 'success', 'success_warning', 'error']

class ReportShortAutoloadV2(RootModel[list[ReportShortAutoloadV2ItemModel5]]):
    pass

class AutoloadApiGetReportsV2Response(_BaseModel):
    meta: MetaReportsAutoloadV2 = None
    reports: ReportShortAutoloadV2 = None

class ItemInfoAutoloadV2FeeInfoModel6(_BaseModel):
    amount: int | None = None
    package_id: int | None = None
    type: Literal['single', 'package'] = None

class ItemInfoError(_BaseModel):
    code: int
    description: str
    title: str
    type: Literal['error', 'warning', 'info', 'alarm']
    updated_at: str

class ItemInfoAutoloadV2SectionModel7(_BaseModel):
    slug: str
    title: str

class ItemInfoAutoloadV2(_BaseModel):
    ad_id: str
    avito_date_end: str | None
    avito_id: int | None
    avito_status: Literal['active', 'old', 'blocked', 'rejected', 'archived', 'removed'] | None
    fee_info: ItemInfoAutoloadV2FeeInfoModel6 | None
    messages: list[ItemInfoError]
    processing_time: str | None
    section: ItemInfoAutoloadV2SectionModel7 = None
    url: str | None

class AutoloadApiGetAutoloadItemsInfoV2Response(_BaseModel):
    items: list[ItemInfoAutoloadV2]

class AutoloadApiGetLastCompletedReportResponseEventsItemModel8(_BaseModel):
    code: int
    description: str
    type: str

class AutoloadApiGetLastCompletedReportResponseListingFeesModel9PackagesItemModel10(_BaseModel):
    count: int = None
    package_id: int = None

class AutoloadApiGetLastCompletedReportResponseListingFeesModel9SingleModel11(_BaseModel):
    count: int = None
    total_amount: int = None

class AutoloadApiGetLastCompletedReportResponseListingFeesModel9(_BaseModel):
    packages: list[AutoloadApiGetLastCompletedReportResponseListingFeesModel9PackagesItemModel10]
    single: AutoloadApiGetLastCompletedReportResponseListingFeesModel9SingleModel11

class AutoloadApiGetLastCompletedReportResponseSectionStatsModel12SectionsItemModel13SectionsItemModel14(_BaseModel):
    count: int
    slug: str
    title: str

class AutoloadApiGetLastCompletedReportResponseSectionStatsModel12SectionsItemModel13(_BaseModel):
    count: int
    sections: list[AutoloadApiGetLastCompletedReportResponseSectionStatsModel12SectionsItemModel13SectionsItemModel14] = None
    slug: str
    title: str

class AutoloadApiGetLastCompletedReportResponseSectionStatsModel12(_BaseModel):
    count: int
    sections: list[AutoloadApiGetLastCompletedReportResponseSectionStatsModel12SectionsItemModel13] = None
    slug: str
    title: str

class AutoloadApiGetLastCompletedReportResponse(_BaseModel):
    events: list[AutoloadApiGetLastCompletedReportResponseEventsItemModel8]
    feed_url: str
    finished_at: str
    listing_fees: AutoloadApiGetLastCompletedReportResponseListingFeesModel9 = None
    report_id: int
    section_stats: AutoloadApiGetLastCompletedReportResponseSectionStatsModel12
    source: Literal['email', 'url', 'web', 'openapi']
    started_at: str
    status: Literal['processing', 'success', 'success_warning', 'error']

class AutoloadApiGetReportByIdV2ResponseEventsItemModel15(_BaseModel):
    code: int
    description: str
    type: str

class AutoloadApiGetReportByIdV2ResponseListingFeesModel16PackagesItemModel17(_BaseModel):
    count: int = None
    package_id: int = None

class AutoloadApiGetReportByIdV2ResponseListingFeesModel16SingleModel18(_BaseModel):
    count: int = None
    total_amount: int = None

class AutoloadApiGetReportByIdV2ResponseListingFeesModel16(_BaseModel):
    packages: list[AutoloadApiGetReportByIdV2ResponseListingFeesModel16PackagesItemModel17]
    single: AutoloadApiGetReportByIdV2ResponseListingFeesModel16SingleModel18

class AutoloadApiGetReportByIdV2ResponseSectionStatsModel19SectionsItemModel20SectionsItemModel21(_BaseModel):
    count: int
    slug: str
    title: str

class AutoloadApiGetReportByIdV2ResponseSectionStatsModel19SectionsItemModel20(_BaseModel):
    count: int
    sections: list[AutoloadApiGetReportByIdV2ResponseSectionStatsModel19SectionsItemModel20SectionsItemModel21] = None
    slug: str
    title: str

class AutoloadApiGetReportByIdV2ResponseSectionStatsModel19(_BaseModel):
    count: int
    sections: list[AutoloadApiGetReportByIdV2ResponseSectionStatsModel19SectionsItemModel20] = None
    slug: str
    title: str

class AutoloadApiGetReportByIdV2Response(_BaseModel):
    events: list[AutoloadApiGetReportByIdV2ResponseEventsItemModel15]
    feed_url: str
    finished_at: str
    listing_fees: AutoloadApiGetReportByIdV2ResponseListingFeesModel16 = None
    report_id: int
    section_stats: AutoloadApiGetReportByIdV2ResponseSectionStatsModel19
    source: Literal['email', 'url', 'web', 'openapi']
    started_at: str
    status: Literal['processing', 'success', 'success_warning', 'error']

class ItemInfoVas(_BaseModel):
    price: int
    slug: Literal['xl', 'highlight', 'x2_1', 'x2_7', 'x5_1', 'x5_7', 'x10_1', 'x10_7', 'x15_1', 'x15_7', 'x20_1', 'x20_7']
    title: str

class ItemInfoReportAutoloadV2SectionModel22(_BaseModel):
    slug: str
    title: str

class ItemInfoReportAutoloadV2(_BaseModel):
    ad_id: str
    applied_vas: list[ItemInfoVas] = None
    avito_date_end: str | None
    avito_id: int | None
    avito_status: Literal['active', 'old', 'blocked', 'rejected', 'archived', 'removed'] | None
    feed_name: str | None = None
    messages: list[ItemInfoError]
    section: ItemInfoReportAutoloadV2SectionModel22
    url: str | None

class MetaReportItemsAutoloadV2(_BaseModel):
    page: int = None
    pages: int = None
    per_page: int = None
    total: int = None

class AutoloadApiGetReportItemsByIdResponse(_BaseModel):
    items: list[ItemInfoReportAutoloadV2]
    meta: MetaReportItemsAutoloadV2
    report_id: int

class ItemFeesInfoReportAutoloadV2(_BaseModel):
    ad_id: str
    avito_id: int
    fees_amount: int
    fees_package_id: int | None = None
    fees_type: Literal['single', 'package']

class AutoloadApiGetReportItemsFeesByIdResponseMetaModel23(_BaseModel):
    page: int = None
    pages: int = None
    per_page: int = None
    total: int = None

class AutoloadApiGetReportItemsFeesByIdResponse(_BaseModel):
    fees: list[ItemFeesInfoReportAutoloadV2] = None
    meta: AutoloadApiGetReportItemsFeesByIdResponseMetaModel23
    report_id: int

class AutoloadApiGetLastCompletedReportV3ResponseEventsItemModel24(_BaseModel):
    code: int
    description: str
    type: str

class AutoloadApiGetLastCompletedReportV3ResponseFeedsUrlsItemModel25(_BaseModel):
    name: str = None
    url: str = None

class AutoloadApiGetLastCompletedReportV3ResponseListingFeesModel26PackagesItemModel27(_BaseModel):
    count: int = None
    package_id: int = None

class AutoloadApiGetLastCompletedReportV3ResponseListingFeesModel26SingleModel28(_BaseModel):
    count: int = None
    total_amount: int = None

class AutoloadApiGetLastCompletedReportV3ResponseListingFeesModel26(_BaseModel):
    packages: list[AutoloadApiGetLastCompletedReportV3ResponseListingFeesModel26PackagesItemModel27]
    single: AutoloadApiGetLastCompletedReportV3ResponseListingFeesModel26SingleModel28

class AutoloadApiGetLastCompletedReportV3ResponseSectionStatsModel29SectionsItemModel30SectionsItemModel31(_BaseModel):
    count: int
    slug: str
    title: str

class AutoloadApiGetLastCompletedReportV3ResponseSectionStatsModel29SectionsItemModel30(_BaseModel):
    count: int
    sections: list[AutoloadApiGetLastCompletedReportV3ResponseSectionStatsModel29SectionsItemModel30SectionsItemModel31] = None
    slug: str
    title: str

class AutoloadApiGetLastCompletedReportV3ResponseSectionStatsModel29(_BaseModel):
    count: int
    sections: list[AutoloadApiGetLastCompletedReportV3ResponseSectionStatsModel29SectionsItemModel30] = None
    slug: str
    title: str

class AutoloadApiGetLastCompletedReportV3Response(_BaseModel):
    events: list[AutoloadApiGetLastCompletedReportV3ResponseEventsItemModel24]
    feeds_urls: list[AutoloadApiGetLastCompletedReportV3ResponseFeedsUrlsItemModel25] = None
    finished_at: str
    listing_fees: AutoloadApiGetLastCompletedReportV3ResponseListingFeesModel26 = None
    report_id: int
    section_stats: AutoloadApiGetLastCompletedReportV3ResponseSectionStatsModel29
    source: Literal['email', 'url', 'web', 'openapi']
    started_at: str
    status: Literal['processing', 'success', 'success_warning', 'error']

class AutoloadApiGetReportByIdV3ResponseEventsItemModel32(_BaseModel):
    code: int
    description: str
    type: str

class AutoloadApiGetReportByIdV3ResponseFeedsUrlsItemModel33(_BaseModel):
    name: str = None
    url: str = None

class AutoloadApiGetReportByIdV3ResponseListingFeesModel34PackagesItemModel35(_BaseModel):
    count: int = None
    package_id: int = None

class AutoloadApiGetReportByIdV3ResponseListingFeesModel34SingleModel36(_BaseModel):
    count: int = None
    total_amount: int = None

class AutoloadApiGetReportByIdV3ResponseListingFeesModel34(_BaseModel):
    packages: list[AutoloadApiGetReportByIdV3ResponseListingFeesModel34PackagesItemModel35]
    single: AutoloadApiGetReportByIdV3ResponseListingFeesModel34SingleModel36

class AutoloadApiGetReportByIdV3ResponseSectionStatsModel37SectionsItemModel38SectionsItemModel39(_BaseModel):
    count: int
    slug: str
    title: str

class AutoloadApiGetReportByIdV3ResponseSectionStatsModel37SectionsItemModel38(_BaseModel):
    count: int
    sections: list[AutoloadApiGetReportByIdV3ResponseSectionStatsModel37SectionsItemModel38SectionsItemModel39] = None
    slug: str
    title: str

class AutoloadApiGetReportByIdV3ResponseSectionStatsModel37(_BaseModel):
    count: int
    sections: list[AutoloadApiGetReportByIdV3ResponseSectionStatsModel37SectionsItemModel38] = None
    slug: str
    title: str

class AutoloadApiGetReportByIdV3Response(_BaseModel):
    events: list[AutoloadApiGetReportByIdV3ResponseEventsItemModel32]
    feeds_urls: list[AutoloadApiGetReportByIdV3ResponseFeedsUrlsItemModel33] = None
    finished_at: str
    listing_fees: AutoloadApiGetReportByIdV3ResponseListingFeesModel34 = None
    report_id: int
    section_stats: AutoloadApiGetReportByIdV3ResponseSectionStatsModel37
    source: Literal['email', 'url', 'web', 'openapi']
    started_at: str
    status: Literal['processing', 'success', 'success_warning', 'error']

__all__ = ['ExportScheduleItemModel1', 'ExportSchedule', 'AutoloadApiGetProfileResponse', 'APFieldsNodeAlert', 'FieldValue', 'APIDependencyPair', 'APIDependency', 'FieldValueRange', 'FieldWarning', 'APIFieldContent', 'ChildAPIField', 'APIField', 'APIFieldsNode', 'AutoloadApiUserDocsNodeFieldsResponse', 'APICategoryNode', 'AutoloadApiUserDocsTreeResponse', 'AutoloadApiGetAdIdsByAvitoIdsResponseItemsItemModel2', 'AutoloadApiGetAdIdsByAvitoIdsResponse', 'AutoloadApiGetAvitoIdsByAdIdsResponseItemsItemModel3', 'AutoloadApiGetAvitoIdsByAdIdsResponse', 'FeedsDataItemModel4', 'FeedsData', 'AutoloadApiGetProfileV2Response', 'MetaReportsAutoloadV2', 'ReportShortAutoloadV2ItemModel5', 'ReportShortAutoloadV2', 'AutoloadApiGetReportsV2Response', 'ItemInfoAutoloadV2FeeInfoModel6', 'ItemInfoError', 'ItemInfoAutoloadV2SectionModel7', 'ItemInfoAutoloadV2', 'AutoloadApiGetAutoloadItemsInfoV2Response', 'AutoloadApiGetLastCompletedReportResponseEventsItemModel8', 'AutoloadApiGetLastCompletedReportResponseListingFeesModel9PackagesItemModel10', 'AutoloadApiGetLastCompletedReportResponseListingFeesModel9SingleModel11', 'AutoloadApiGetLastCompletedReportResponseListingFeesModel9', 'AutoloadApiGetLastCompletedReportResponseSectionStatsModel12SectionsItemModel13SectionsItemModel14', 'AutoloadApiGetLastCompletedReportResponseSectionStatsModel12SectionsItemModel13', 'AutoloadApiGetLastCompletedReportResponseSectionStatsModel12', 'AutoloadApiGetLastCompletedReportResponse', 'AutoloadApiGetReportByIdV2ResponseEventsItemModel15', 'AutoloadApiGetReportByIdV2ResponseListingFeesModel16PackagesItemModel17', 'AutoloadApiGetReportByIdV2ResponseListingFeesModel16SingleModel18', 'AutoloadApiGetReportByIdV2ResponseListingFeesModel16', 'AutoloadApiGetReportByIdV2ResponseSectionStatsModel19SectionsItemModel20SectionsItemModel21', 'AutoloadApiGetReportByIdV2ResponseSectionStatsModel19SectionsItemModel20', 'AutoloadApiGetReportByIdV2ResponseSectionStatsModel19', 'AutoloadApiGetReportByIdV2Response', 'ItemInfoVas', 'ItemInfoReportAutoloadV2SectionModel22', 'ItemInfoReportAutoloadV2', 'MetaReportItemsAutoloadV2', 'AutoloadApiGetReportItemsByIdResponse', 'ItemFeesInfoReportAutoloadV2', 'AutoloadApiGetReportItemsFeesByIdResponseMetaModel23', 'AutoloadApiGetReportItemsFeesByIdResponse', 'AutoloadApiGetLastCompletedReportV3ResponseEventsItemModel24', 'AutoloadApiGetLastCompletedReportV3ResponseFeedsUrlsItemModel25', 'AutoloadApiGetLastCompletedReportV3ResponseListingFeesModel26PackagesItemModel27', 'AutoloadApiGetLastCompletedReportV3ResponseListingFeesModel26SingleModel28', 'AutoloadApiGetLastCompletedReportV3ResponseListingFeesModel26', 'AutoloadApiGetLastCompletedReportV3ResponseSectionStatsModel29SectionsItemModel30SectionsItemModel31', 'AutoloadApiGetLastCompletedReportV3ResponseSectionStatsModel29SectionsItemModel30', 'AutoloadApiGetLastCompletedReportV3ResponseSectionStatsModel29', 'AutoloadApiGetLastCompletedReportV3Response', 'AutoloadApiGetReportByIdV3ResponseEventsItemModel32', 'AutoloadApiGetReportByIdV3ResponseFeedsUrlsItemModel33', 'AutoloadApiGetReportByIdV3ResponseListingFeesModel34PackagesItemModel35', 'AutoloadApiGetReportByIdV3ResponseListingFeesModel34SingleModel36', 'AutoloadApiGetReportByIdV3ResponseListingFeesModel34', 'AutoloadApiGetReportByIdV3ResponseSectionStatsModel37SectionsItemModel38SectionsItemModel39', 'AutoloadApiGetReportByIdV3ResponseSectionStatsModel37SectionsItemModel38', 'AutoloadApiGetReportByIdV3ResponseSectionStatsModel37', 'AutoloadApiGetReportByIdV3Response']
