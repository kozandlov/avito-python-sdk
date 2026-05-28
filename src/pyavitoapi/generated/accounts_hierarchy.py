"""Generated API module for slug: accounts-hierarchy."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.accounts_hierarchy import AccountsHierarchyApiCheckAhUserV1Response, AccountsHierarchyApiCheckAhUserV2Response, AccountsHierarchyApiGetAhInfoV1Response, AccountsHierarchyApiGetEmployeesV1Response, AccountsHierarchyApiListCompanyPhonesV1Response, AccountsHierarchyApiListItemsByEmployeeIdV1Response


class AccountsHierarchyApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def check_ah_user_v1(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AccountsHierarchyApiCheckAhUserV1Response:
        """Получение информации о статусе пользователя в ИА"""
        payload = await self._transport.request(
            method="GET",
            path_template="/checkAhUserV1",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AccountsHierarchyApiCheckAhUserV1Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for accounts-hierarchy.check_ah_user_v1 (GET /checkAhUserV1)",
                payload=payload,
                details={
                    "slug": "accounts-hierarchy",
                    "operation_id": "checkAhUserV1",
                    "python_method": "check_ah_user_v1",
                    "http_method": "GET",
                    "path": "/checkAhUserV1",
                    "errors": exc.errors(),
                },
            ) from exc

    async def check_ah_user_v2(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AccountsHierarchyApiCheckAhUserV2Response:
        """Получение информации о статусе пользователя в ИА"""
        payload = await self._transport.request(
            method="GET",
            path_template="/checkAhUserV2",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AccountsHierarchyApiCheckAhUserV2Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for accounts-hierarchy.check_ah_user_v2 (GET /checkAhUserV2)",
                payload=payload,
                details={
                    "slug": "accounts-hierarchy",
                    "operation_id": "checkAhUserV2",
                    "python_method": "check_ah_user_v2",
                    "http_method": "GET",
                    "path": "/checkAhUserV2",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_ah_info_v1(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AccountsHierarchyApiGetAhInfoV1Response:
        """Получение полной информации о статусе пользователя в ИА"""
        payload = await self._transport.request(
            method="GET",
            path_template="/getAhInfoV1",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AccountsHierarchyApiGetAhInfoV1Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for accounts-hierarchy.get_ah_info_v1 (GET /getAhInfoV1)",
                payload=payload,
                details={
                    "slug": "accounts-hierarchy",
                    "operation_id": "getAhInfoV1",
                    "python_method": "get_ah_info_v1",
                    "http_method": "GET",
                    "path": "/getAhInfoV1",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_employees_v1(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AccountsHierarchyApiGetEmployeesV1Response:
        """Получение списка сотрудников иерархии"""
        payload = await self._transport.request(
            method="GET",
            path_template="/getEmployeesV1",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AccountsHierarchyApiGetEmployeesV1Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for accounts-hierarchy.get_employees_v1 (GET /getEmployeesV1)",
                payload=payload,
                details={
                    "slug": "accounts-hierarchy",
                    "operation_id": "getEmployeesV1",
                    "python_method": "get_employees_v1",
                    "http_method": "GET",
                    "path": "/getEmployeesV1",
                    "errors": exc.errors(),
                },
            ) from exc

    async def link_items_v1(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:
        """Прикрепление сотрудника иерархии к объявлениям, перезакрепление объявлений между сотрудниками иерархии"""
        payload = await self._transport.request(
            method="POST",
            path_template="/linkItemsV1",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        return None

    async def list_company_phones_v1(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AccountsHierarchyApiListCompanyPhonesV1Response:
        """Получение списка телефонов компании"""
        payload = await self._transport.request(
            method="GET",
            path_template="/listCompanyPhonesV1",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AccountsHierarchyApiListCompanyPhonesV1Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for accounts-hierarchy.list_company_phones_v1 (GET /listCompanyPhonesV1)",
                payload=payload,
                details={
                    "slug": "accounts-hierarchy",
                    "operation_id": "listCompanyPhonesV1",
                    "python_method": "list_company_phones_v1",
                    "http_method": "GET",
                    "path": "/listCompanyPhonesV1",
                    "errors": exc.errors(),
                },
            ) from exc

    async def list_items_by_employee_id_v1(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AccountsHierarchyApiListItemsByEmployeeIdV1Response:
        """Получение списка объявлений по сотруднику"""
        payload = await self._transport.request(
            method="POST",
            path_template="/listItemsByEmployeeIdV1",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AccountsHierarchyApiListItemsByEmployeeIdV1Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for accounts-hierarchy.list_items_by_employee_id_v1 (POST /listItemsByEmployeeIdV1)",
                payload=payload,
                details={
                    "slug": "accounts-hierarchy",
                    "operation_id": "listItemsByEmployeeIdV1",
                    "python_method": "list_items_by_employee_id_v1",
                    "http_method": "POST",
                    "path": "/listItemsByEmployeeIdV1",
                    "errors": exc.errors(),
                },
            ) from exc

__all__ = ["AccountsHierarchyApi"]
