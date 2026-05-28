"""Generated response models for slug: accounts-hierarchy."""

from __future__ import annotations

from typing import Any
from pydantic import BaseModel, ConfigDict, ValidationError, Field, RootModel

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class AccountsHierarchyApiCheckAhUserV1Response(_BaseModel):
    avito_company_id: int | None = Field(default=None, alias='avitoCompanyId')
    is_chief: bool = Field(default=None, alias='isChief')
    is_company: bool = Field(default=None, alias='isCompany')
    is_employee: bool = Field(default=None, alias='isEmployee')

class AccountsHierarchyApiCheckAhUserV2Response(_BaseModel):
    avito_company_id: int | None = Field(default=None, alias='avitoCompanyId')
    is_chief: bool = Field(default=None, alias='isChief')
    is_company: bool = Field(default=None, alias='isCompany')
    is_employee: bool = Field(default=None, alias='isEmployee')

class AccountsHierarchyApiGetAhInfoV1ResponseCompanyModel1(_BaseModel):
    is_company: bool = Field(alias='isCompany')

class AccountsHierarchyApiGetAhInfoV1ResponseEmployeesItemModel2(_BaseModel):
    avito_company_id: int | None = Field(default=None, alias='avitoCompanyId')
    employee_id: int | None = Field(default=None, alias='employeeId')
    is_chief: bool = Field(alias='isChief')

class AccountsHierarchyApiGetAhInfoV1Response(_BaseModel):
    company: AccountsHierarchyApiGetAhInfoV1ResponseCompanyModel1
    employees: list[AccountsHierarchyApiGetAhInfoV1ResponseEmployeesItemModel2]

class AccountsHierarchyApiGetEmployeesV1ResponseItemModel3(_BaseModel):
    email: str | None = None
    employee_id: int = Field(alias='employeeId')
    is_chief: bool = Field(default=None, alias='isChief')
    name: str | None = None
    phones: list[str] = None

class AccountsHierarchyApiGetEmployeesV1Response(RootModel[list[AccountsHierarchyApiGetEmployeesV1ResponseItemModel3]]):
    pass

class AccountsHierarchyApiListCompanyPhonesV1ResponseResultModel4(_BaseModel):
    cursor: str | None = None
    phones: list[str] = None

class AccountsHierarchyApiListCompanyPhonesV1Response(_BaseModel):
    result: AccountsHierarchyApiListCompanyPhonesV1ResponseResultModel4 = None

class AccountsHierarchyApiListItemsByEmployeeIdV1Response(_BaseModel):
    has_next: bool = Field(alias='hasNext')
    items: list[int]

__all__ = ['AccountsHierarchyApiCheckAhUserV1Response', 'AccountsHierarchyApiCheckAhUserV2Response', 'AccountsHierarchyApiGetAhInfoV1ResponseCompanyModel1', 'AccountsHierarchyApiGetAhInfoV1ResponseEmployeesItemModel2', 'AccountsHierarchyApiGetAhInfoV1Response', 'AccountsHierarchyApiGetEmployeesV1ResponseItemModel3', 'AccountsHierarchyApiGetEmployeesV1Response', 'AccountsHierarchyApiListCompanyPhonesV1ResponseResultModel4', 'AccountsHierarchyApiListCompanyPhonesV1Response', 'AccountsHierarchyApiListItemsByEmployeeIdV1Response']
