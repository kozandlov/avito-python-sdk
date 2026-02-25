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

class AccountsHierarchyApiGetEmployeesV1ResponseItemModel1(_BaseModel):
    email: str | None = None
    employee_id: int = Field(alias='employeeId')
    is_chief: bool = Field(default=None, alias='isChief')
    name: str | None = None
    phones: list[str] = None

class AccountsHierarchyApiGetEmployeesV1Response(RootModel[list[AccountsHierarchyApiGetEmployeesV1ResponseItemModel1]]):
    pass

class AccountsHierarchyApiListCompanyPhonesV1ResponseResultModel2(_BaseModel):
    phones: list[str] = None

class AccountsHierarchyApiListCompanyPhonesV1Response(_BaseModel):
    result: AccountsHierarchyApiListCompanyPhonesV1ResponseResultModel2 = None

class AccountsHierarchyApiListItemsByEmployeeIdV1Response(_BaseModel):
    has_next: bool = Field(alias='hasNext')
    items: list[int]

__all__ = ['AccountsHierarchyApiCheckAhUserV1Response', 'AccountsHierarchyApiGetEmployeesV1ResponseItemModel1', 'AccountsHierarchyApiGetEmployeesV1Response', 'AccountsHierarchyApiListCompanyPhonesV1ResponseResultModel2', 'AccountsHierarchyApiListCompanyPhonesV1Response', 'AccountsHierarchyApiListItemsByEmployeeIdV1Response']
