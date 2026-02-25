"""Generated API module for slug: autoload."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.autoload import AutoloadApiGetAdIdsByAvitoIdsResponse, AutoloadApiGetAutoloadItemsInfoV2Response, AutoloadApiGetAvitoIdsByAdIdsResponse, AutoloadApiGetLastCompletedReportResponse, AutoloadApiGetLastCompletedReportV3Response, AutoloadApiGetProfileResponse, AutoloadApiGetProfileV2Response, AutoloadApiGetReportByIdV2Response, AutoloadApiGetReportByIdV3Response, AutoloadApiGetReportItemsByIdResponse, AutoloadApiGetReportItemsFeesByIdResponse, AutoloadApiGetReportsV2Response, AutoloadApiUserDocsNodeFieldsResponse, AutoloadApiUserDocsTreeResponse


class AutoloadApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def get_profile(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutoloadApiGetProfileResponse:
        """Получение профиля пользователя автозагрузки (deprecated)"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoload/v1/profile",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutoloadApiGetProfileResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoload.get_profile (GET /autoload/v1/profile)",
                payload=payload,
                details={
                    "slug": "autoload",
                    "operation_id": "getProfile",
                    "python_method": "get_profile",
                    "http_method": "GET",
                    "path": "/autoload/v1/profile",
                    "errors": exc.errors(),
                },
            ) from exc

    async def create_or_update_profile(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:
        """Создание/редактирование настроек профиля пользователя автозагрузки (deprecated)"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoload/v1/profile",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        return None

    async def upload(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:
        """Загрузка файла по ссылке"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoload/v1/upload",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        return None

    async def user_docs_node_fields(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutoloadApiUserDocsNodeFieldsResponse:
        """Получения полей категории"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoload/v1/user-docs/node/{node_slug}/fields",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutoloadApiUserDocsNodeFieldsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoload.user_docs_node_fields (GET /autoload/v1/user-docs/node/{node_slug}/fields)",
                payload=payload,
                details={
                    "slug": "autoload",
                    "operation_id": "userDocsNodeFields",
                    "python_method": "user_docs_node_fields",
                    "http_method": "GET",
                    "path": "/autoload/v1/user-docs/node/{node_slug}/fields",
                    "errors": exc.errors(),
                },
            ) from exc

    async def user_docs_tree(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutoloadApiUserDocsTreeResponse:
        """Получение дерева категорий"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoload/v1/user-docs/tree",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutoloadApiUserDocsTreeResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoload.user_docs_tree (GET /autoload/v1/user-docs/tree)",
                payload=payload,
                details={
                    "slug": "autoload",
                    "operation_id": "userDocsTree",
                    "python_method": "user_docs_tree",
                    "http_method": "GET",
                    "path": "/autoload/v1/user-docs/tree",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_ad_ids_by_avito_ids(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutoloadApiGetAdIdsByAvitoIdsResponse:
        """ID объявлений из файла"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoload/v2/items/ad_ids",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutoloadApiGetAdIdsByAvitoIdsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoload.get_ad_ids_by_avito_ids (GET /autoload/v2/items/ad_ids)",
                payload=payload,
                details={
                    "slug": "autoload",
                    "operation_id": "getAdIdsByAvitoIds",
                    "python_method": "get_ad_ids_by_avito_ids",
                    "http_method": "GET",
                    "path": "/autoload/v2/items/ad_ids",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_avito_ids_by_ad_ids(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutoloadApiGetAvitoIdsByAdIdsResponse:
        """ID объявлений на Авито"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoload/v2/items/avito_ids",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutoloadApiGetAvitoIdsByAdIdsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoload.get_avito_ids_by_ad_ids (GET /autoload/v2/items/avito_ids)",
                payload=payload,
                details={
                    "slug": "autoload",
                    "operation_id": "getAvitoIdsByAdIds",
                    "python_method": "get_avito_ids_by_ad_ids",
                    "http_method": "GET",
                    "path": "/autoload/v2/items/avito_ids",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_profile_v2(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutoloadApiGetProfileV2Response:
        """Получение профиля пользователя автозагрузки"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoload/v2/profile",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutoloadApiGetProfileV2Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoload.get_profile_v2 (GET /autoload/v2/profile)",
                payload=payload,
                details={
                    "slug": "autoload",
                    "operation_id": "getProfileV2",
                    "python_method": "get_profile_v2",
                    "http_method": "GET",
                    "path": "/autoload/v2/profile",
                    "errors": exc.errors(),
                },
            ) from exc

    async def create_or_update_profile_v2(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:
        """Создание/редактирование настроек профиля пользователя автозагрузки"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autoload/v2/profile",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        return None

    async def get_reports_v2(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutoloadApiGetReportsV2Response:
        """Список отчётов автозагрузки"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoload/v2/reports",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutoloadApiGetReportsV2Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoload.get_reports_v2 (GET /autoload/v2/reports)",
                payload=payload,
                details={
                    "slug": "autoload",
                    "operation_id": "getReportsV2",
                    "python_method": "get_reports_v2",
                    "http_method": "GET",
                    "path": "/autoload/v2/reports",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_autoload_items_info_v2(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutoloadApiGetAutoloadItemsInfoV2Response:
        """Объявления по ID в автозагрузке"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoload/v2/reports/items",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutoloadApiGetAutoloadItemsInfoV2Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoload.get_autoload_items_info_v2 (GET /autoload/v2/reports/items)",
                payload=payload,
                details={
                    "slug": "autoload",
                    "operation_id": "getAutoloadItemsInfoV2",
                    "python_method": "get_autoload_items_info_v2",
                    "http_method": "GET",
                    "path": "/autoload/v2/reports/items",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_last_completed_report(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutoloadApiGetLastCompletedReportResponse:
        """Статистика по последней выгрузке (deprecated)"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoload/v2/reports/last_completed_report",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutoloadApiGetLastCompletedReportResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoload.get_last_completed_report (GET /autoload/v2/reports/last_completed_report)",
                payload=payload,
                details={
                    "slug": "autoload",
                    "operation_id": "getLastCompletedReport",
                    "python_method": "get_last_completed_report",
                    "http_method": "GET",
                    "path": "/autoload/v2/reports/last_completed_report",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_report_by_id_v2(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutoloadApiGetReportByIdV2Response:
        """Статистика по конкретной выгрузке (deprecated)"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoload/v2/reports/{report_id}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutoloadApiGetReportByIdV2Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoload.get_report_by_id_v2 (GET /autoload/v2/reports/{report_id})",
                payload=payload,
                details={
                    "slug": "autoload",
                    "operation_id": "getReportByIdV2",
                    "python_method": "get_report_by_id_v2",
                    "http_method": "GET",
                    "path": "/autoload/v2/reports/{report_id}",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_report_items_by_id(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutoloadApiGetReportItemsByIdResponse:
        """Все объявления из конкретной выгрузки"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoload/v2/reports/{report_id}/items",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutoloadApiGetReportItemsByIdResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoload.get_report_items_by_id (GET /autoload/v2/reports/{report_id}/items)",
                payload=payload,
                details={
                    "slug": "autoload",
                    "operation_id": "getReportItemsById",
                    "python_method": "get_report_items_by_id",
                    "http_method": "GET",
                    "path": "/autoload/v2/reports/{report_id}/items",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_report_items_fees_by_id(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutoloadApiGetReportItemsFeesByIdResponse:
        """Списания за объявления в конкретной выгрузке"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoload/v2/reports/{report_id}/items/fees",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutoloadApiGetReportItemsFeesByIdResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoload.get_report_items_fees_by_id (GET /autoload/v2/reports/{report_id}/items/fees)",
                payload=payload,
                details={
                    "slug": "autoload",
                    "operation_id": "getReportItemsFeesById",
                    "python_method": "get_report_items_fees_by_id",
                    "http_method": "GET",
                    "path": "/autoload/v2/reports/{report_id}/items/fees",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_last_completed_report_v3(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutoloadApiGetLastCompletedReportV3Response:
        """Статистика по последней выгрузке"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoload/v3/reports/last_completed_report",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutoloadApiGetLastCompletedReportV3Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoload.get_last_completed_report_v3 (GET /autoload/v3/reports/last_completed_report)",
                payload=payload,
                details={
                    "slug": "autoload",
                    "operation_id": "getLastCompletedReportV3",
                    "python_method": "get_last_completed_report_v3",
                    "http_method": "GET",
                    "path": "/autoload/v3/reports/last_completed_report",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_report_by_id_v3(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutoloadApiGetReportByIdV3Response:
        """Статистика по конкретной выгрузке"""
        payload = await self._transport.request(
            method="GET",
            path_template="/autoload/v3/reports/{report_id}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutoloadApiGetReportByIdV3Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autoload.get_report_by_id_v3 (GET /autoload/v3/reports/{report_id})",
                payload=payload,
                details={
                    "slug": "autoload",
                    "operation_id": "getReportByIdV3",
                    "python_method": "get_report_by_id_v3",
                    "http_method": "GET",
                    "path": "/autoload/v3/reports/{report_id}",
                    "errors": exc.errors(),
                },
            ) from exc

__all__ = ["AutoloadApi"]
