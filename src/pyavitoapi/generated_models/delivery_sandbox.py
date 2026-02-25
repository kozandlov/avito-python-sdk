"""Generated response models for slug: delivery-sandbox."""

from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, ValidationError, Field, RootModel

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class DeliverySandboxApiCancelAnnouncement3PlResponseDataModel1(_BaseModel):
    status: Literal['success'] = None

class DeliverySandboxApiCancelAnnouncement3PlResponseErrorModel2(_BaseModel):
    code: str = None
    message: str = None

class DeliverySandboxApiCancelAnnouncement3PlResponse(_BaseModel):
    data: DeliverySandboxApiCancelAnnouncement3PlResponseDataModel1 | None = None
    error: DeliverySandboxApiCancelAnnouncement3PlResponseErrorModel2 | None = None

class DeliverySandboxApiCreateAnnouncement3PlResponseDataModel3(_BaseModel):
    status: Literal['success'] = None

class DeliverySandboxApiCreateAnnouncement3PlResponseErrorModel4(_BaseModel):
    code: str = None
    message: str = None

class DeliverySandboxApiCreateAnnouncement3PlResponse(_BaseModel):
    data: DeliverySandboxApiCreateAnnouncement3PlResponseDataModel3 | None = None
    error: DeliverySandboxApiCreateAnnouncement3PlResponseErrorModel4 | None = None

class CreateParcelData(_BaseModel):
    barcodes: list[str] = None
    dispatch_number: str = Field(alias='dispatchNumber')
    tracking_number: str = Field(alias='trackingNumber')

class CreateParcelError(_BaseModel):
    code: Literal['VALIDATION_ERROR', 'UNSUPPORTED_PARAM_ERROR', 'TERMINAL_UNAVAILABLE', 'SORTING_CENTER_UNAVAILABLE']
    message: str

class DeliverySandboxApiCreateParcelResponse(_BaseModel):
    data: CreateParcelData = None
    error: CreateParcelError = None

class DeliverySandboxApiCreateAnnouncementResponseDataModel5(_BaseModel):
    status: Literal['success'] = None

class DeliverySandboxApiCreateAnnouncementResponseErrorModel6(_BaseModel):
    code: str = None
    message: str = None

class DeliverySandboxApiCreateAnnouncementResponse(_BaseModel):
    data: DeliverySandboxApiCreateAnnouncementResponseDataModel5 | None = None
    error: DeliverySandboxApiCreateAnnouncementResponseErrorModel6 | None = None

class DeliverySandboxApiTrackAnnouncementResponseDataModel7(_BaseModel):
    status: Literal['success'] = None

class DeliverySandboxApiTrackAnnouncementResponseErrorModel8(_BaseModel):
    code: str = None
    message: str = None

class DeliverySandboxApiTrackAnnouncementResponse(_BaseModel):
    data: DeliverySandboxApiTrackAnnouncementResponseDataModel7 | None = None
    error: DeliverySandboxApiTrackAnnouncementResponseErrorModel8 | None = None

class DeliverySandboxApiCustomAreaScheduleResponseDataModel9(_BaseModel):
    task_id: int = Field(default=None, alias='taskId')

class DeliverySandboxApiCustomAreaScheduleResponseErrorModel10(_BaseModel):
    code: str
    message: str

class DeliverySandboxApiCustomAreaScheduleResponse(_BaseModel):
    data: DeliverySandboxApiCustomAreaScheduleResponseDataModel9 | None = None
    error: DeliverySandboxApiCustomAreaScheduleResponseErrorModel10 | None = None

class DeliverySandboxApiCancelParcelResponseDataModel11(_BaseModel):
    status: Literal['OK'] = None

class DeliveryError(_BaseModel):
    code: str
    message: str

class DeliverySandboxApiCancelParcelResponse(_BaseModel):
    data: DeliverySandboxApiCancelParcelResponseDataModel11 | None = None
    error: DeliveryError = None

class DeliverySandboxApiCheckConfirmationCodeResponseDataModel12(_BaseModel):
    status: Literal['success', 'fail', 'expired', 'attempts'] = None

class DeliverySandboxApiCheckConfirmationCodeResponse(_BaseModel):
    data: DeliverySandboxApiCheckConfirmationCodeResponseDataModel12 = None

class DeliverySandboxApiSetOrderPropertiesResponseDataModel13(_BaseModel):
    status: Literal['success', 'duplicate'] = None

class DeliverySandboxApiSetOrderPropertiesResponse(_BaseModel):
    data: DeliverySandboxApiSetOrderPropertiesResponseDataModel13 | None = None
    error: DeliveryError = None

class DeliverySandboxApiSetOrderRealAddressResponseDataModel14(_BaseModel):
    status: Literal['success', 'duplicate'] = None

class DeliverySandboxApiSetOrderRealAddressResponse(_BaseModel):
    data: DeliverySandboxApiSetOrderRealAddressResponseDataModel14 | None = None
    error: DeliveryError = None

class DeliverySetStatusDetails(_BaseModel):
    from_: str = Field(alias='from')

class DeliverySandboxApiTrackingResponseDataModel15(_BaseModel):
    details: DeliverySetStatusDetails = None
    status: Literal['success', 'forbidden'] = None

class DeliverySandboxApiTrackingResponse(_BaseModel):
    data: DeliverySandboxApiTrackingResponseDataModel15 | None = None
    error: DeliveryError = None

class DeliverySandboxApiProhibitOrderAcceptanceResponseDataModel16(_BaseModel):
    status: Literal['OK'] = None

class DeliverySandboxApiProhibitOrderAcceptanceResponse(_BaseModel):
    data: DeliverySandboxApiProhibitOrderAcceptanceResponseDataModel16 | None = None
    error: DeliveryError = None

class DeliveryZipCode(RootModel[str]):
    pass

class Address(_BaseModel):
    address_row: str = Field(default=None, alias='addressRow')
    building: str = None
    country: str = None
    fias: str
    floor: int = None
    house: str = None
    housing: str = None
    lat: float
    lng: float
    locality: str
    locality_type: str = Field(default=None, alias='localityType')
    porch: str = None
    region: str
    room: str = None
    street: str = None
    sub_region: str = Field(default=None, alias='subRegion')
    sub_region_type: str = Field(default=None, alias='subRegionType')
    zip_code: DeliveryZipCode = Field(alias='zipCode')

class SortingCenterID(_BaseModel):
    delivery_provider_id: str = Field(default=None, alias='deliveryProviderId')
    provider: str = None

class DeliveryPhones(RootModel[list[str]]):
    pass

class Restriction(_BaseModel):
    dimensional_factor: int = Field(default=None, alias='dimensionalFactor')
    max_declared_cost: int = Field(alias='maxDeclaredCost')
    max_dimensional_weight: int = Field(default=None, alias='maxDimensionalWeight')
    max_dimensions: list[int] = Field(alias='maxDimensions')
    max_weight: int = Field(alias='maxWeight')

class DeliveryDayTimeInterval(RootModel[str]):
    pass

class DeliveryDayTimeIntervals(RootModel[list[DeliveryDayTimeInterval]]):
    pass

class Schedule(_BaseModel):
    fri: DeliveryDayTimeIntervals
    mon: DeliveryDayTimeIntervals
    sat: DeliveryDayTimeIntervals
    sun: DeliveryDayTimeIntervals
    thu: DeliveryDayTimeIntervals
    tue: DeliveryDayTimeIntervals
    wed: DeliveryDayTimeIntervals

class SortingCenterGetData(_BaseModel):
    address: Address
    delivery_provider_id: SortingCenterID = Field(alias='deliveryProviderId')
    itinerary: str
    name: str
    phones: DeliveryPhones
    photos: list[str]
    restriction: Restriction
    schedule: Schedule

class DeliverySandboxApiGetSortingCenterResponseErrorModel17(_BaseModel):
    code: str
    message: str

class DeliverySandboxApiGetSortingCenterResponse(_BaseModel):
    data: list[SortingCenterGetData] | None = None
    error: DeliverySandboxApiGetSortingCenterResponseErrorModel17 = None

class DeliverySandboxApiAddSortingCenterResponseDataModel18(_BaseModel):
    task_id: int = Field(default=None, alias='taskId')

class DeliverySandboxApiAddSortingCenterResponseErrorModel19(_BaseModel):
    code: str
    message: str

class DeliverySandboxApiAddSortingCenterResponse(_BaseModel):
    data: DeliverySandboxApiAddSortingCenterResponseDataModel18 | None = None
    error: DeliverySandboxApiAddSortingCenterResponseErrorModel19 | None = None

class DeliverySandboxApiAddAreasSandboxResponseDataModel20(_BaseModel):
    task_id: int = Field(default=None, alias='taskId')

class DeliverySandboxApiAddAreasSandboxResponse(_BaseModel):
    data: DeliverySandboxApiAddAreasSandboxResponseDataModel20 | None = None
    error: DeliveryError = None

class DeliverySandboxApiAddTagsToSortingCenterResponseDataModel21(_BaseModel):
    task_id: int = Field(default=None, alias='taskId')

class DeliverySandboxApiAddTagsToSortingCenterResponseErrorModel22(_BaseModel):
    code: str
    message: str

class DeliverySandboxApiAddTagsToSortingCenterResponse(_BaseModel):
    data: DeliverySandboxApiAddTagsToSortingCenterResponseDataModel21 | None = None
    error: DeliverySandboxApiAddTagsToSortingCenterResponseErrorModel22 | None = None

class DeliverySandboxApiAddTerminalsSandboxResponseDataModel23(_BaseModel):
    task_id: int = Field(default=None, alias='taskId')

class DeliverySandboxApiAddTerminalsSandboxResponse(_BaseModel):
    data: DeliverySandboxApiAddTerminalsSandboxResponseDataModel23 | None = None
    error: DeliveryError = None

class DeliverySandboxApiUpdateTermsResponseDataModel24(_BaseModel):
    task_id: int = Field(alias='taskId')

class DeliverySandboxApiUpdateTermsResponse(_BaseModel):
    data: DeliverySandboxApiUpdateTermsResponseDataModel24 = None
    error: DeliveryError = None

class DeliverySandboxApiAddTariffSandboxV2ResponseDataModel25(_BaseModel):
    task_id: int = Field(default=None, alias='taskId')

class DeliverySandboxApiAddTariffSandboxV2ResponseErrorModel26(_BaseModel):
    code: str
    message: str

class DeliverySandboxApiAddTariffSandboxV2Response(_BaseModel):
    data: DeliverySandboxApiAddTariffSandboxV2ResponseDataModel25 | None = None
    error: DeliverySandboxApiAddTariffSandboxV2ResponseErrorModel26 | None = None

class AreasTaskResult(_BaseModel):
    edited: str
    incoming: str

class AreasCustomScheduleTaskResult(_BaseModel):
    uploaded: str

class TerminalsTaskResult(_BaseModel):
    count: str = None
    deleted: str
    total: str
    upserted: str

class TariffTaskResult(_BaseModel):
    tariff_id: str = Field(alias='tariffId')

class SortingCentersTaskResult(_BaseModel):
    count: str

class SortingCentersTagsTaskResult(_BaseModel):
    count: str

class GetTaskData(_BaseModel):
    errors: list[DeliveryError] | None = None
    result: AreasTaskResult | AreasCustomScheduleTaskResult | TerminalsTaskResult | TariffTaskResult | SortingCentersTaskResult | SortingCentersTagsTaskResult | None = None
    state: str
    task_id: int = Field(alias='taskId')

class DeliverySandboxApiGetTaskResponse(_BaseModel):
    data: GetTaskData = None
    error: DeliveryError = None

class DeliverySandboxApiV1cancelAnnouncementResponseDataModel27(_BaseModel):
    status: Literal['success'] = None

class SandboxCancelAnnouncementError(_BaseModel):
    code: Literal['INTERNAL_ERROR', 'VALIDATION_ERROR', 'ANNOUNCEMENT_NOT_FOUND']
    message: str

class DeliverySandboxApiV1cancelAnnouncementResponse(_BaseModel):
    data: DeliverySandboxApiV1cancelAnnouncementResponseDataModel27 | None = None
    error: SandboxCancelAnnouncementError = None

class DeliverySandboxApiV1CancelParcelResponseDataModel28(_BaseModel):
    status: str = None

class CancelSandboxParcelError(_BaseModel):
    code: Literal['VALIDATION_ERROR', 'INTERNAL_ERROR', 'UNKNOWN_PROVIDER']
    message: str = None

class DeliverySandboxApiV1CancelParcelResponse(_BaseModel):
    data: DeliverySandboxApiV1CancelParcelResponseDataModel28 | None = None
    error: CancelSandboxParcelError = None

class ChangeParcelReplyData(_BaseModel):
    application_id: str = Field(default=None, alias='applicationID')

class ChangeParcelError(_BaseModel):
    code: Literal['VALIDATION_ERROR', 'INTERNAL_ERROR', 'UNSUITABLE_PARCEL', 'PARCEL_NOT_FOUND']
    message: str = None

class DeliverySandboxApiV1changeParcelResponse(_BaseModel):
    data: ChangeParcelReplyData = None
    error: ChangeParcelError = None

class DeliverySandboxApiV1createAnnouncementResponseDataModel29(_BaseModel):
    status: Literal['success', 'failed'] = None

class SandboxCreateAnnouncementError(_BaseModel):
    code: Literal['VALIDATION_ERROR', 'INTERNAL_ERROR', 'OBJECT_EXISTS']
    message: str

class DeliverySandboxApiV1createAnnouncementResponse(_BaseModel):
    data: DeliverySandboxApiV1createAnnouncementResponseDataModel29 | None = None
    error: SandboxCreateAnnouncementError = None

class DeliverySandboxApiV1getAnnouncementEventResponseDataModel30(_BaseModel):
    announcement_event: str = Field(default=None, alias='announcementEvent')

class SandboxGetAnnouncementEventError(_BaseModel):
    code: Literal['INTERNAL_ERROR', 'VALIDATION_ERROR', 'ANNOUNCEMENT_NOT_FOUND']
    message: str

class DeliverySandboxApiV1getAnnouncementEventResponse(_BaseModel):
    data: DeliverySandboxApiV1getAnnouncementEventResponseDataModel30 | None = None
    error: SandboxGetAnnouncementEventError = None

class GetChangeParcelInfoReplyDataReceiverModel31(_BaseModel):
    name: str = None
    phones: list[str] = None

class GetChangeParcelInfoReplyData(_BaseModel):
    receiver: GetChangeParcelInfoReplyDataReceiverModel31 = None
    status: str = None

class GetChangeParcelInfoError(_BaseModel):
    code: Literal['VALIDATION_ERROR', 'INTERNAL_ERROR', 'APPLICATION_NOT_FOUND']
    message: str = None

class DeliverySandboxApiV1getChangeParcelInfoResponse(_BaseModel):
    data: GetChangeParcelInfoReplyData = None
    error: GetChangeParcelInfoError = None

class GetSandboxParcelInfoDimensions(_BaseModel):
    real_height: int | None = Field(default=None, alias='realHeight')
    real_length: int | None = Field(default=None, alias='realLength')
    real_weight: int | None = Field(default=None, alias='realWeight')
    real_width: int | None = Field(default=None, alias='realWidth')

class GetSandboxParcelInfoParcelHistory(_BaseModel):
    date: str = None
    event: str = None
    location: str | None = None
    status: str = None

class GetSandboxParcelInfoTerminals(_BaseModel):
    approximate: str = None
    real: str | None = None

class GetSandboxParcelInfoReplyDataReceiverModel32(_BaseModel):
    terminals: GetSandboxParcelInfoTerminals = None

class GetSandboxParcelInfoReplyDataSenderModel33(_BaseModel):
    terminals: GetSandboxParcelInfoTerminals = None

class GetSandboxParcelInfoReplyData(_BaseModel):
    dimensions: GetSandboxParcelInfoDimensions = None
    history: list[GetSandboxParcelInfoParcelHistory] = None
    receiver: GetSandboxParcelInfoReplyDataReceiverModel32 = None
    sender: GetSandboxParcelInfoReplyDataSenderModel33 = None
    status: str = None

class GetSandboxParcelInfoError(_BaseModel):
    code: Literal['VALIDATION_ERROR', 'INTERNAL_ERROR', 'UNKNOWN_PROVIDER', 'NOT_FOUND']
    message: str = None

class DeliverySandboxApiV1getParcelInfoResponse(_BaseModel):
    data: GetSandboxParcelInfoReplyData = None
    error: GetSandboxParcelInfoError = None

class DeliverySandboxApiV1getRegisteredParcelIdResponseDataModel34(_BaseModel):
    parcel_id: str = Field(default=None, alias='parcelID')

class GetRegisteredParcelIDError(_BaseModel):
    code: Literal['NOT_FOUND', 'NOT_REGISTERED', 'VALIDATION_ERROR', 'INTERNAL_ERROR']
    message: str = None

class DeliverySandboxApiV1getRegisteredParcelIdResponse(_BaseModel):
    data: DeliverySandboxApiV1getRegisteredParcelIdResponseDataModel34 | None = None
    error: GetRegisteredParcelIDError = None

class DeliverySandboxApiCreateSandboxParcelV2ResponseDataModel35(_BaseModel):
    order_id: str = Field(default=None, alias='orderID')

class DeliverySandboxApiCreateSandboxParcelV2Response(_BaseModel):
    data: DeliverySandboxApiCreateSandboxParcelV2ResponseDataModel35 | None = None
    error: CreateParcelError = None

class DeliverySandboxApiChangeParcelResultResponseErrorModel36(_BaseModel):
    code: Literal['ID_INVALID', 'NOT_FOUND', 'STATUS_INVALID', 'FAILED_REASON_MISSES', 'PARCEL_CLOSED']
    message: str

class DeliverySandboxApiChangeParcelResultResponse(_BaseModel):
    data: dict[str, Any] | None = None
    error: DeliverySandboxApiChangeParcelResultResponseErrorModel36 | None = None

class ChangeParcelsData(_BaseModel):
    status: Literal['ok']

class ChangeParcelsError(_BaseModel):
    code: Literal['VALIDATION_ERROR', 'UNSUPPORTED_PARAM_ERROR']
    message: str

class DeliverySandboxApiChangeParcelsResponse(_BaseModel):
    data: ChangeParcelsData = None
    error: ChangeParcelsError = None

__all__ = ['DeliverySandboxApiCancelAnnouncement3PlResponseDataModel1', 'DeliverySandboxApiCancelAnnouncement3PlResponseErrorModel2', 'DeliverySandboxApiCancelAnnouncement3PlResponse', 'DeliverySandboxApiCreateAnnouncement3PlResponseDataModel3', 'DeliverySandboxApiCreateAnnouncement3PlResponseErrorModel4', 'DeliverySandboxApiCreateAnnouncement3PlResponse', 'CreateParcelData', 'CreateParcelError', 'DeliverySandboxApiCreateParcelResponse', 'DeliverySandboxApiCreateAnnouncementResponseDataModel5', 'DeliverySandboxApiCreateAnnouncementResponseErrorModel6', 'DeliverySandboxApiCreateAnnouncementResponse', 'DeliverySandboxApiTrackAnnouncementResponseDataModel7', 'DeliverySandboxApiTrackAnnouncementResponseErrorModel8', 'DeliverySandboxApiTrackAnnouncementResponse', 'DeliverySandboxApiCustomAreaScheduleResponseDataModel9', 'DeliverySandboxApiCustomAreaScheduleResponseErrorModel10', 'DeliverySandboxApiCustomAreaScheduleResponse', 'DeliverySandboxApiCancelParcelResponseDataModel11', 'DeliveryError', 'DeliverySandboxApiCancelParcelResponse', 'DeliverySandboxApiCheckConfirmationCodeResponseDataModel12', 'DeliverySandboxApiCheckConfirmationCodeResponse', 'DeliverySandboxApiSetOrderPropertiesResponseDataModel13', 'DeliverySandboxApiSetOrderPropertiesResponse', 'DeliverySandboxApiSetOrderRealAddressResponseDataModel14', 'DeliverySandboxApiSetOrderRealAddressResponse', 'DeliverySetStatusDetails', 'DeliverySandboxApiTrackingResponseDataModel15', 'DeliverySandboxApiTrackingResponse', 'DeliverySandboxApiProhibitOrderAcceptanceResponseDataModel16', 'DeliverySandboxApiProhibitOrderAcceptanceResponse', 'DeliveryZipCode', 'Address', 'SortingCenterID', 'DeliveryPhones', 'Restriction', 'DeliveryDayTimeInterval', 'DeliveryDayTimeIntervals', 'Schedule', 'SortingCenterGetData', 'DeliverySandboxApiGetSortingCenterResponseErrorModel17', 'DeliverySandboxApiGetSortingCenterResponse', 'DeliverySandboxApiAddSortingCenterResponseDataModel18', 'DeliverySandboxApiAddSortingCenterResponseErrorModel19', 'DeliverySandboxApiAddSortingCenterResponse', 'DeliverySandboxApiAddAreasSandboxResponseDataModel20', 'DeliverySandboxApiAddAreasSandboxResponse', 'DeliverySandboxApiAddTagsToSortingCenterResponseDataModel21', 'DeliverySandboxApiAddTagsToSortingCenterResponseErrorModel22', 'DeliverySandboxApiAddTagsToSortingCenterResponse', 'DeliverySandboxApiAddTerminalsSandboxResponseDataModel23', 'DeliverySandboxApiAddTerminalsSandboxResponse', 'DeliverySandboxApiUpdateTermsResponseDataModel24', 'DeliverySandboxApiUpdateTermsResponse', 'DeliverySandboxApiAddTariffSandboxV2ResponseDataModel25', 'DeliverySandboxApiAddTariffSandboxV2ResponseErrorModel26', 'DeliverySandboxApiAddTariffSandboxV2Response', 'AreasTaskResult', 'AreasCustomScheduleTaskResult', 'TerminalsTaskResult', 'TariffTaskResult', 'SortingCentersTaskResult', 'SortingCentersTagsTaskResult', 'GetTaskData', 'DeliverySandboxApiGetTaskResponse', 'DeliverySandboxApiV1cancelAnnouncementResponseDataModel27', 'SandboxCancelAnnouncementError', 'DeliverySandboxApiV1cancelAnnouncementResponse', 'DeliverySandboxApiV1CancelParcelResponseDataModel28', 'CancelSandboxParcelError', 'DeliverySandboxApiV1CancelParcelResponse', 'ChangeParcelReplyData', 'ChangeParcelError', 'DeliverySandboxApiV1changeParcelResponse', 'DeliverySandboxApiV1createAnnouncementResponseDataModel29', 'SandboxCreateAnnouncementError', 'DeliverySandboxApiV1createAnnouncementResponse', 'DeliverySandboxApiV1getAnnouncementEventResponseDataModel30', 'SandboxGetAnnouncementEventError', 'DeliverySandboxApiV1getAnnouncementEventResponse', 'GetChangeParcelInfoReplyDataReceiverModel31', 'GetChangeParcelInfoReplyData', 'GetChangeParcelInfoError', 'DeliverySandboxApiV1getChangeParcelInfoResponse', 'GetSandboxParcelInfoDimensions', 'GetSandboxParcelInfoParcelHistory', 'GetSandboxParcelInfoTerminals', 'GetSandboxParcelInfoReplyDataReceiverModel32', 'GetSandboxParcelInfoReplyDataSenderModel33', 'GetSandboxParcelInfoReplyData', 'GetSandboxParcelInfoError', 'DeliverySandboxApiV1getParcelInfoResponse', 'DeliverySandboxApiV1getRegisteredParcelIdResponseDataModel34', 'GetRegisteredParcelIDError', 'DeliverySandboxApiV1getRegisteredParcelIdResponse', 'DeliverySandboxApiCreateSandboxParcelV2ResponseDataModel35', 'DeliverySandboxApiCreateSandboxParcelV2Response', 'DeliverySandboxApiChangeParcelResultResponseErrorModel36', 'DeliverySandboxApiChangeParcelResultResponse', 'ChangeParcelsData', 'ChangeParcelsError', 'DeliverySandboxApiChangeParcelsResponse']
