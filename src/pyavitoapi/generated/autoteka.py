"""Generated API module for slug: autoteka."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.autoteka import AutotekaApiCatalogsResolveResponse, AutotekaApiGetAccessTokenResponse, AutotekaApiGetActivePackageResponse, AutotekaApiGetLeadsResponse, AutotekaApiGetPreviewResponse, AutotekaApiGetReportListResponse, AutotekaApiGetReportResponse, AutotekaApiGetTeaserResponse, AutotekaApiMonitoringBucketAddResponse, AutotekaApiMonitoringBucketDeleteResponse, AutotekaApiMonitoringBucketRemoveResponse, AutotekaApiMonitoringGetRegActionsResponse, AutotekaApiPostPreviewByExternalItemResponse, AutotekaApiPostPreviewByItemIdResponse, AutotekaApiPostPreviewByRegNumberResponse, AutotekaApiPostPreviewByVinResponse, AutotekaApiPostReportByVehicleIdResponse, AutotekaApiPostReportResponse, AutotekaApiPostSyncCreateReportByRegNumberResponse, AutotekaApiPostSyncCreateReportByVinResponse, AutotekaApiPostTeaserResponse, AutotekaApiScoringByVehicleIdResponse, AutotekaApiScoringGetByIdResponse, AutotekaApiSpecificationByPlateNumberResponse, AutotekaApiSpecificationByVehicleIdResponse, AutotekaApiSpecificationGetByIdResponse, AutotekaApiValuationBySpecificationResponse


class AutotekaApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def catalogs_resolve(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiCatalogsResolveResponse:
        """Получение актуальных параметров Автокаталога
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoteka/v1/catalogs/resolve",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiCatalogsResolveResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.catalogs_resolve (POST /autoteka/v1/catalogs/resolve)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "catalogsResolve",
                    "python_method": "catalogs_resolve",
                    "http_method": "POST",
                    "path": "/autoteka/v1/catalogs/resolve",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_leads(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiGetLeadsResponse:
        """Получение событий сервиса Сигнал
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoteka/v1/get-leads/",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiGetLeadsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.get_leads (POST /autoteka/v1/get-leads/)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "getLeads",
                    "python_method": "get_leads",
                    "http_method": "POST",
                    "path": "/autoteka/v1/get-leads/",
                    "errors": exc.errors(),
                },
            ) from exc

    async def monitoring_bucket_add(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiMonitoringBucketAddResponse:
        """Добавить идентификаторы (vin/frame) на мониторинг
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoteka/v1/monitoring/bucket/add",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiMonitoringBucketAddResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.monitoring_bucket_add (POST /autoteka/v1/monitoring/bucket/add)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "monitoringBucketAdd",
                    "python_method": "monitoring_bucket_add",
                    "http_method": "POST",
                    "path": "/autoteka/v1/monitoring/bucket/add",
                    "errors": exc.errors(),
                },
            ) from exc

    async def monitoring_bucket_delete(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiMonitoringBucketDeleteResponse:
        """Полная очистка списка мониторинга
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoteka/v1/monitoring/bucket/delete",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiMonitoringBucketDeleteResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.monitoring_bucket_delete (POST /autoteka/v1/monitoring/bucket/delete)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "monitoringBucketDelete",
                    "python_method": "monitoring_bucket_delete",
                    "http_method": "POST",
                    "path": "/autoteka/v1/monitoring/bucket/delete",
                    "errors": exc.errors(),
                },
            ) from exc

    async def monitoring_bucket_remove(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiMonitoringBucketRemoveResponse:
        """Удаление идентификаторов из мониторинга (vin/frame)
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoteka/v1/monitoring/bucket/remove",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiMonitoringBucketRemoveResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.monitoring_bucket_remove (POST /autoteka/v1/monitoring/bucket/remove)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "monitoringBucketRemove",
                    "python_method": "monitoring_bucket_remove",
                    "http_method": "POST",
                    "path": "/autoteka/v1/monitoring/bucket/remove",
                    "errors": exc.errors(),
                },
            ) from exc

    async def monitoring_get_reg_actions(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiMonitoringGetRegActionsResponse:
        """Получение событий мониторинга
"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoteka/v1/monitoring/get-reg-actions/",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiMonitoringGetRegActionsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.monitoring_get_reg_actions (GET /autoteka/v1/monitoring/get-reg-actions/)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "monitoringGetRegActions",
                    "python_method": "monitoring_get_reg_actions",
                    "http_method": "GET",
                    "path": "/autoteka/v1/monitoring/get-reg-actions/",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_active_package(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiGetActivePackageResponse:
        """Запрос остатка отчётов пользователя
"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoteka/v1/packages/active_package",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiGetActivePackageResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.get_active_package (GET /autoteka/v1/packages/active_package)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "getActivePackage",
                    "python_method": "get_active_package",
                    "http_method": "GET",
                    "path": "/autoteka/v1/packages/active_package",
                    "errors": exc.errors(),
                },
            ) from exc

    async def post_preview_by_vin(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiPostPreviewByVinResponse:
        """Превью по VIN или номеру кузова
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoteka/v1/previews",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiPostPreviewByVinResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.post_preview_by_vin (POST /autoteka/v1/previews)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "postPreviewByVin",
                    "python_method": "post_preview_by_vin",
                    "http_method": "POST",
                    "path": "/autoteka/v1/previews",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_preview(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiGetPreviewResponse:
        """Получение превью по его ID
"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoteka/v1/previews/{previewId}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiGetPreviewResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.get_preview (GET /autoteka/v1/previews/{previewId})",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "getPreview",
                    "python_method": "get_preview",
                    "http_method": "GET",
                    "path": "/autoteka/v1/previews/{previewId}",
                    "errors": exc.errors(),
                },
            ) from exc

    async def post_report(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiPostReportResponse:
        """Отчет по превью
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoteka/v1/reports",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiPostReportResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.post_report (POST /autoteka/v1/reports)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "postReport",
                    "python_method": "post_report",
                    "http_method": "POST",
                    "path": "/autoteka/v1/reports",
                    "errors": exc.errors(),
                },
            ) from exc

    async def post_report_by_vehicle_id(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiPostReportByVehicleIdResponse:
        """Отчет по идентификатору авто (vin/frame)
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoteka/v1/reports-by-vehicle-id",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiPostReportByVehicleIdResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.post_report_by_vehicle_id (POST /autoteka/v1/reports-by-vehicle-id)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "postReportByVehicleId",
                    "python_method": "post_report_by_vehicle_id",
                    "http_method": "POST",
                    "path": "/autoteka/v1/reports-by-vehicle-id",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_report_list(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiGetReportListResponse:
        """Получение списка отчётов
"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoteka/v1/reports/list/",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiGetReportListResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.get_report_list (GET /autoteka/v1/reports/list/)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "getReportList",
                    "python_method": "get_report_list",
                    "http_method": "GET",
                    "path": "/autoteka/v1/reports/list/",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_report(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiGetReportResponse:
        """Получение отчета по его ID
"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoteka/v1/reports/{report_id}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiGetReportResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.get_report (GET /autoteka/v1/reports/{report_id})",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "getReport",
                    "python_method": "get_report",
                    "http_method": "GET",
                    "path": "/autoteka/v1/reports/{report_id}",
                    "errors": exc.errors(),
                },
            ) from exc

    async def post_preview_by_external_item(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiPostPreviewByExternalItemResponse:
        """Превью по ID объявления другой площадки
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoteka/v1/request-preview-by-external-item",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiPostPreviewByExternalItemResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.post_preview_by_external_item (POST /autoteka/v1/request-preview-by-external-item)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "postPreviewByExternalItem",
                    "python_method": "post_preview_by_external_item",
                    "http_method": "POST",
                    "path": "/autoteka/v1/request-preview-by-external-item",
                    "errors": exc.errors(),
                },
            ) from exc

    async def post_preview_by_item_id(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiPostPreviewByItemIdResponse:
        """Превью по ID объявления Авито"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoteka/v1/request-preview-by-item-id",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiPostPreviewByItemIdResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.post_preview_by_item_id (POST /autoteka/v1/request-preview-by-item-id)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "postPreviewByItemId",
                    "python_method": "post_preview_by_item_id",
                    "http_method": "POST",
                    "path": "/autoteka/v1/request-preview-by-item-id",
                    "errors": exc.errors(),
                },
            ) from exc

    async def post_preview_by_reg_number(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiPostPreviewByRegNumberResponse:
        """Превью по государственному номеру
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoteka/v1/request-preview-by-regnumber",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiPostPreviewByRegNumberResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.post_preview_by_reg_number (POST /autoteka/v1/request-preview-by-regnumber)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "postPreviewByRegNumber",
                    "python_method": "post_preview_by_reg_number",
                    "http_method": "POST",
                    "path": "/autoteka/v1/request-preview-by-regnumber",
                    "errors": exc.errors(),
                },
            ) from exc

    async def scoring_by_vehicle_id(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiScoringByVehicleIdResponse:
        """Скоринг рисков по идентификатору авто (vin/frame)
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoteka/v1/scoring/by-vehicle-id",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiScoringByVehicleIdResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.scoring_by_vehicle_id (POST /autoteka/v1/scoring/by-vehicle-id)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "scoringByVehicleId",
                    "python_method": "scoring_by_vehicle_id",
                    "http_method": "POST",
                    "path": "/autoteka/v1/scoring/by-vehicle-id",
                    "errors": exc.errors(),
                },
            ) from exc

    async def scoring_get_by_id(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiScoringGetByIdResponse:
        """Получение скоринга рисков по его ID
"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoteka/v1/scoring/{scoring_id}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiScoringGetByIdResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.scoring_get_by_id (GET /autoteka/v1/scoring/{scoring_id})",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "scoringGetById",
                    "python_method": "scoring_get_by_id",
                    "http_method": "GET",
                    "path": "/autoteka/v1/scoring/{scoring_id}",
                    "errors": exc.errors(),
                },
            ) from exc

    async def specification_by_plate_number(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiSpecificationByPlateNumberResponse:
        """Запрос характеристик по регистрационному номеру
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoteka/v1/specifications/by-plate-number",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiSpecificationByPlateNumberResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.specification_by_plate_number (POST /autoteka/v1/specifications/by-plate-number)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "specificationByPlateNumber",
                    "python_method": "specification_by_plate_number",
                    "http_method": "POST",
                    "path": "/autoteka/v1/specifications/by-plate-number",
                    "errors": exc.errors(),
                },
            ) from exc

    async def specification_by_vehicle_id(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiSpecificationByVehicleIdResponse:
        """Запрос характеристик по идентификатору авто (vin/frame)
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoteka/v1/specifications/by-vehicle-id",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiSpecificationByVehicleIdResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.specification_by_vehicle_id (POST /autoteka/v1/specifications/by-vehicle-id)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "specificationByVehicleId",
                    "python_method": "specification_by_vehicle_id",
                    "http_method": "POST",
                    "path": "/autoteka/v1/specifications/by-vehicle-id",
                    "errors": exc.errors(),
                },
            ) from exc

    async def specification_get_by_id(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiSpecificationGetByIdResponse:
        """Получение характеристик по ID запроса
"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoteka/v1/specifications/specification/{specificationID}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiSpecificationGetByIdResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.specification_get_by_id (GET /autoteka/v1/specifications/specification/{specificationID})",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "specificationGetById",
                    "python_method": "specification_get_by_id",
                    "http_method": "GET",
                    "path": "/autoteka/v1/specifications/specification/{specificationID}",
                    "errors": exc.errors(),
                },
            ) from exc

    async def post_sync_create_report_by_reg_number(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiPostSyncCreateReportByRegNumberResponse:
        """Синхронное создание отчета по ГРЗ
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoteka/v1/sync/create-by-regnumber",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiPostSyncCreateReportByRegNumberResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.post_sync_create_report_by_reg_number (POST /autoteka/v1/sync/create-by-regnumber)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "postSyncCreateReportByRegNumber",
                    "python_method": "post_sync_create_report_by_reg_number",
                    "http_method": "POST",
                    "path": "/autoteka/v1/sync/create-by-regnumber",
                    "errors": exc.errors(),
                },
            ) from exc

    async def post_sync_create_report_by_vin(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiPostSyncCreateReportByVinResponse:
        """Синхронное создание отчёта по VIN или номеру кузова
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoteka/v1/sync/create-by-vin",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiPostSyncCreateReportByVinResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.post_sync_create_report_by_vin (POST /autoteka/v1/sync/create-by-vin)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "postSyncCreateReportByVin",
                    "python_method": "post_sync_create_report_by_vin",
                    "http_method": "POST",
                    "path": "/autoteka/v1/sync/create-by-vin",
                    "errors": exc.errors(),
                },
            ) from exc

    async def post_teaser(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiPostTeaserResponse:
        """Тизер по идентификатору авто (vin/frame)
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoteka/v1/teasers",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiPostTeaserResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.post_teaser (POST /autoteka/v1/teasers)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "postTeaser",
                    "python_method": "post_teaser",
                    "http_method": "POST",
                    "path": "/autoteka/v1/teasers",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_teaser(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiGetTeaserResponse:
        """Получение тизера по ID тизера
"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoteka/v1/teasers/{teaser_id}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiGetTeaserResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.get_teaser (GET /autoteka/v1/teasers/{teaser_id})",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "getTeaser",
                    "python_method": "get_teaser",
                    "http_method": "GET",
                    "path": "/autoteka/v1/teasers/{teaser_id}",
                    "errors": exc.errors(),
                },
            ) from exc

    async def valuation_by_specification(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiValuationBySpecificationResponse:
        """Получение оценки по параметрам
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoteka/v1/valuation/by-specification",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiValuationBySpecificationResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.valuation_by_specification (POST /autoteka/v1/valuation/by-specification)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "valuationBySpecification",
                    "python_method": "valuation_by_specification",
                    "http_method": "POST",
                    "path": "/autoteka/v1/valuation/by-specification",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_access_token(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutotekaApiGetAccessTokenResponse:
        """Получение access token
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/token",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutotekaApiGetAccessTokenResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoteka.get_access_token (POST /token)",
                payload=payload,
                details={
                    "slug": "autoteka",
                    "operation_id": "getAccessToken",
                    "python_method": "get_access_token",
                    "http_method": "POST",
                    "path": "/token",
                    "errors": exc.errors(),
                },
            ) from exc

__all__ = ["AutotekaApi"]
