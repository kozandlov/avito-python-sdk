"""Generated API module for slug: delivery-sandbox."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.delivery_sandbox import DeliverySandboxApiAddAreasSandboxResponse, DeliverySandboxApiAddSortingCenterResponse, DeliverySandboxApiAddTagsToSortingCenterResponse, DeliverySandboxApiAddTariffSandboxV2Response, DeliverySandboxApiAddTerminalsSandboxResponse, DeliverySandboxApiCancelAnnouncement3PlResponse, DeliverySandboxApiCancelParcelResponse, DeliverySandboxApiChangeParcelResultResponse, DeliverySandboxApiChangeParcelsResponse, DeliverySandboxApiCheckConfirmationCodeResponse, DeliverySandboxApiCreateAnnouncement3PlResponse, DeliverySandboxApiCreateAnnouncementResponse, DeliverySandboxApiCreateParcelResponse, DeliverySandboxApiCreateSandboxParcelV2Response, DeliverySandboxApiCustomAreaScheduleResponse, DeliverySandboxApiGetSortingCenterResponse, DeliverySandboxApiGetTaskResponse, DeliverySandboxApiProhibitOrderAcceptanceResponse, DeliverySandboxApiSetOrderPropertiesResponse, DeliverySandboxApiSetOrderRealAddressResponse, DeliverySandboxApiTrackAnnouncementResponse, DeliverySandboxApiTrackingResponse, DeliverySandboxApiUpdateTermsResponse, DeliverySandboxApiV1CancelParcelResponse, DeliverySandboxApiV1cancelAnnouncementResponse, DeliverySandboxApiV1changeParcelResponse, DeliverySandboxApiV1createAnnouncementResponse, DeliverySandboxApiV1getAnnouncementEventResponse, DeliverySandboxApiV1getChangeParcelInfoResponse, DeliverySandboxApiV1getParcelInfoResponse, DeliverySandboxApiV1getRegisteredParcelIdResponse


class DeliverySandboxApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def cancel_announcement3_pl(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiCancelAnnouncement3PlResponse:
        """Отмена анонса в СД"""
        payload = await self._transport.request(
            method="POST",
            path_template="/cancelAnnouncement",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiCancelAnnouncement3PlResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.cancel_announcement3_pl (POST /cancelAnnouncement)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "CancelAnnouncement3PL",
                    "python_method": "cancel_announcement3_pl",
                    "http_method": "POST",
                    "path": "/cancelAnnouncement",
                    "errors": exc.errors(),
                },
            ) from exc

    async def create_announcement3_pl(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiCreateAnnouncement3PlResponse:
        """Создание анонса в СД"""
        payload = await self._transport.request(
            method="POST",
            path_template="/createAnnouncement",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiCreateAnnouncement3PlResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.create_announcement3_pl (POST /createAnnouncement)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "CreateAnnouncement3PL",
                    "python_method": "create_announcement3_pl",
                    "http_method": "POST",
                    "path": "/createAnnouncement",
                    "errors": exc.errors(),
                },
            ) from exc

    async def create_parcel(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiCreateParcelResponse:
        """Создание посылки"""
        payload = await self._transport.request(
            method="POST",
            path_template="/createParcel",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiCreateParcelResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.create_parcel (POST /createParcel)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "createParcel",
                    "python_method": "create_parcel",
                    "http_method": "POST",
                    "path": "/createParcel",
                    "errors": exc.errors(),
                },
            ) from exc

    async def create_announcement(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiCreateAnnouncementResponse:
        """Создание анонса в Avito"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/announcements/create",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiCreateAnnouncementResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.create_announcement (POST /delivery-sandbox/announcements/create)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "CreateAnnouncement",
                    "python_method": "create_announcement",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/announcements/create",
                    "errors": exc.errors(),
                },
            ) from exc

    async def track_announcement(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiTrackAnnouncementResponse:
        """Трекинг анонсов"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/announcements/track",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiTrackAnnouncementResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.track_announcement (POST /delivery-sandbox/announcements/track)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "TrackAnnouncement",
                    "python_method": "track_announcement",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/announcements/track",
                    "errors": exc.errors(),
                },
            ) from exc

    async def custom_area_schedule(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiCustomAreaScheduleResponse:
        """Установка графика работы на определённый день"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/areas/custom-schedule",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiCustomAreaScheduleResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.custom_area_schedule (POST /delivery-sandbox/areas/custom-schedule)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "customAreaSchedule",
                    "python_method": "custom_area_schedule",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/areas/custom-schedule",
                    "errors": exc.errors(),
                },
            ) from exc

    async def cancel_parcel(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiCancelParcelResponse:
        """Отмена посылки"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/cancelParcel",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiCancelParcelResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.cancel_parcel (POST /delivery-sandbox/cancelParcel)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "cancelParcel",
                    "python_method": "cancel_parcel",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/cancelParcel",
                    "errors": exc.errors(),
                },
            ) from exc

    async def check_confirmation_code(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiCheckConfirmationCodeResponse:
        """Проверка кода подтверждения"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/order/checkConfirmationCode",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiCheckConfirmationCodeResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.check_confirmation_code (POST /delivery-sandbox/order/checkConfirmationCode)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "checkConfirmationCode",
                    "python_method": "check_confirmation_code",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/order/checkConfirmationCode",
                    "errors": exc.errors(),
                },
            ) from exc

    async def set_order_properties(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiSetOrderPropertiesResponse:
        """Добавление / изменение параметров доставки посылки"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/order/properties",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiSetOrderPropertiesResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.set_order_properties (POST /delivery-sandbox/order/properties)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "setOrderProperties",
                    "python_method": "set_order_properties",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/order/properties",
                    "errors": exc.errors(),
                },
            ) from exc

    async def set_order_real_address(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiSetOrderRealAddressResponse:
        """Фактический адрес приёма / возврата посылки"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/order/realAddress",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiSetOrderRealAddressResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.set_order_real_address (POST /delivery-sandbox/order/realAddress)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "setOrderRealAddress",
                    "python_method": "set_order_real_address",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/order/realAddress",
                    "errors": exc.errors(),
                },
            ) from exc

    async def tracking(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiTrackingResponse:
        """Трекинг"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/order/tracking",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiTrackingResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.tracking (POST /delivery-sandbox/order/tracking)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "tracking",
                    "python_method": "tracking",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/order/tracking",
                    "errors": exc.errors(),
                },
            ) from exc

    async def prohibit_order_acceptance(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiProhibitOrderAcceptanceResponse:
        """Запрет приёма посылки от отправителя"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/prohibitOrderAcceptance",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiProhibitOrderAcceptanceResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.prohibit_order_acceptance (POST /delivery-sandbox/prohibitOrderAcceptance)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "prohibitOrderAcceptance",
                    "python_method": "prohibit_order_acceptance",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/prohibitOrderAcceptance",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_sorting_center(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiGetSortingCenterResponse:
        """Получить список сортировочных центров"""
        payload = await self._transport.request(
            method="GET",
            path_template="/delivery-sandbox/sorting-center",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiGetSortingCenterResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.get_sorting_center (GET /delivery-sandbox/sorting-center)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "GetSortingCenter",
                    "python_method": "get_sorting_center",
                    "http_method": "GET",
                    "path": "/delivery-sandbox/sorting-center",
                    "errors": exc.errors(),
                },
            ) from exc

    async def add_sorting_center(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiAddSortingCenterResponse:
        """Загрузить сортировочные центры"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/tariffs/sorting-center",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiAddSortingCenterResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.add_sorting_center (POST /delivery-sandbox/tariffs/sorting-center)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "AddSortingCenter",
                    "python_method": "add_sorting_center",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/tariffs/sorting-center",
                    "errors": exc.errors(),
                },
            ) from exc

    async def add_areas_sandbox(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiAddAreasSandboxResponse:
        """Загрузить области доставки"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/tariffs/{tariff_id}/areas",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiAddAreasSandboxResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.add_areas_sandbox (POST /delivery-sandbox/tariffs/{tariff_id}/areas)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "AddAreasSandbox",
                    "python_method": "add_areas_sandbox",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/tariffs/{tariff_id}/areas",
                    "errors": exc.errors(),
                },
            ) from exc

    async def add_tags_to_sorting_center(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiAddTagsToSortingCenterResponse:
        """Установка тэгов своим и/или чужим сортировочным центрам"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/tariffs/{tariff_id}/tagged-sorting-centers",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiAddTagsToSortingCenterResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.add_tags_to_sorting_center (POST /delivery-sandbox/tariffs/{tariff_id}/tagged-sorting-centers)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "AddTagsToSortingCenter",
                    "python_method": "add_tags_to_sorting_center",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/tariffs/{tariff_id}/tagged-sorting-centers",
                    "errors": exc.errors(),
                },
            ) from exc

    async def add_terminals_sandbox(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiAddTerminalsSandboxResponse:
        """Загрузить терминалы"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/tariffs/{tariff_id}/terminals",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiAddTerminalsSandboxResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.add_terminals_sandbox (POST /delivery-sandbox/tariffs/{tariff_id}/terminals)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "AddTerminalsSandbox",
                    "python_method": "add_terminals_sandbox",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/tariffs/{tariff_id}/terminals",
                    "errors": exc.errors(),
                },
            ) from exc

    async def update_terms(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiUpdateTermsResponse:
        """Обновить сроки по тарифу"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/tariffs/{tariff_id}/terms",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiUpdateTermsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.update_terms (POST /delivery-sandbox/tariffs/{tariff_id}/terms)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "UpdateTerms",
                    "python_method": "update_terms",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/tariffs/{tariff_id}/terms",
                    "errors": exc.errors(),
                },
            ) from exc

    async def add_tariff_sandbox_v2(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiAddTariffSandboxV2Response:
        """Загрузить новый тариф v2"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/tariffsV2",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiAddTariffSandboxV2Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.add_tariff_sandbox_v2 (POST /delivery-sandbox/tariffsV2)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "AddTariffSandboxV2",
                    "python_method": "add_tariff_sandbox_v2",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/tariffsV2",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_task(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiGetTaskResponse:
        """Получение информации по задаче"""
        payload = await self._transport.request(
            method="GET",
            path_template="/delivery-sandbox/tasks/{task_id}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiGetTaskResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.get_task (GET /delivery-sandbox/tasks/{task_id})",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "GetTask",
                    "python_method": "get_task",
                    "http_method": "GET",
                    "path": "/delivery-sandbox/tasks/{task_id}",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1cancel_announcement(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiV1cancelAnnouncementResponse:
        """Отправка события об отмене тестового анонса"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/v1/cancelAnnouncement",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiV1cancelAnnouncementResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.v1cancel_announcement (POST /delivery-sandbox/v1/cancelAnnouncement)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "v1cancelAnnouncement",
                    "python_method": "v1cancel_announcement",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/v1/cancelAnnouncement",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_cancel_parcel(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiV1CancelParcelResponse:
        """Отмена тестовой посылки"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/v1/cancelParcel",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiV1CancelParcelResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.v1_cancel_parcel (POST /delivery-sandbox/v1/cancelParcel)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "v1CancelParcel",
                    "python_method": "v1_cancel_parcel",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/v1/cancelParcel",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1change_parcel(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiV1changeParcelResponse:
        """Создание заявки на изменение данных тестовой посылки"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/v1/changeParcel",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiV1changeParcelResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.v1change_parcel (POST /delivery-sandbox/v1/changeParcel)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "v1changeParcel",
                    "python_method": "v1change_parcel",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/v1/changeParcel",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1create_announcement(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiV1createAnnouncementResponse:
        """Создание тестового анонса"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/v1/createAnnouncement",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiV1createAnnouncementResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.v1create_announcement (POST /delivery-sandbox/v1/createAnnouncement)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "v1createAnnouncement",
                    "python_method": "v1create_announcement",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/v1/createAnnouncement",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1get_announcement_event(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiV1getAnnouncementEventResponse:
        """Получение последнего события тестового анонса"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/v1/getAnnouncementEvent",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiV1getAnnouncementEventResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.v1get_announcement_event (POST /delivery-sandbox/v1/getAnnouncementEvent)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "v1getAnnouncementEvent",
                    "python_method": "v1get_announcement_event",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/v1/getAnnouncementEvent",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1get_change_parcel_info(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiV1getChangeParcelInfoResponse:
        """Получение информации об изменении тестовой посылки"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/v1/getChangeParcelInfo",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiV1getChangeParcelInfoResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.v1get_change_parcel_info (POST /delivery-sandbox/v1/getChangeParcelInfo)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "v1getChangeParcelInfo",
                    "python_method": "v1get_change_parcel_info",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/v1/getChangeParcelInfo",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1get_parcel_info(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiV1getParcelInfoResponse:
        """Получение информации о тестовой посылке"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/v1/getParcelInfo",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiV1getParcelInfoResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.v1get_parcel_info (POST /delivery-sandbox/v1/getParcelInfo)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "v1getParcelInfo",
                    "python_method": "v1get_parcel_info",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/v1/getParcelInfo",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1get_registered_parcel_id(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiV1getRegisteredParcelIdResponse:
        """Получение ID зарегистрированной тестовой посылки"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/v1/getRegisteredParcelID",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiV1getRegisteredParcelIdResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.v1get_registered_parcel_id (POST /delivery-sandbox/v1/getRegisteredParcelID)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "v1getRegisteredParcelID",
                    "python_method": "v1get_registered_parcel_id",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/v1/getRegisteredParcelID",
                    "errors": exc.errors(),
                },
            ) from exc

    async def create_sandbox_parcel_v2(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiCreateSandboxParcelV2Response:
        """Создание тестовой посылки"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery-sandbox/v2/createParcel",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiCreateSandboxParcelV2Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.create_sandbox_parcel_v2 (POST /delivery-sandbox/v2/createParcel)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "CreateSandboxParcelV2",
                    "python_method": "create_sandbox_parcel_v2",
                    "http_method": "POST",
                    "path": "/delivery-sandbox/v2/createParcel",
                    "errors": exc.errors(),
                },
            ) from exc

    async def change_parcel_result(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiChangeParcelResultResponse:
        """Отправка результата исполнения заявки"""
        payload = await self._transport.request(
            method="POST",
            path_template="/delivery/order/changeParcelResult",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiChangeParcelResultResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.change_parcel_result (POST /delivery/order/changeParcelResult)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "ChangeParcelResult",
                    "python_method": "change_parcel_result",
                    "http_method": "POST",
                    "path": "/delivery/order/changeParcelResult",
                    "errors": exc.errors(),
                },
            ) from exc

    async def change_parcels(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> DeliverySandboxApiChangeParcelsResponse:
        """Обновление свойств посылок"""
        payload = await self._transport.request(
            method="POST",
            path_template="/sandbox/changeParcels",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return DeliverySandboxApiChangeParcelsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for delivery-sandbox.change_parcels (POST /sandbox/changeParcels)",
                payload=payload,
                details={
                    "slug": "delivery-sandbox",
                    "operation_id": "ChangeParcels",
                    "python_method": "change_parcels",
                    "http_method": "POST",
                    "path": "/sandbox/changeParcels",
                    "errors": exc.errors(),
                },
            ) from exc

__all__ = ["DeliverySandboxApi"]
