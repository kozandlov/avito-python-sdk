"""Generated response models for slug: realty-reports."""

from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, ValidationError, Field

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class Error(_BaseModel):
    code: int
    is_temporary: bool | None = Field(default=None, alias='isTemporary')
    message: str

class RealtyReportsApiMarketPriceCorrespondenceV1Response(_BaseModel):
    correspondence: Literal['below', 'normal', 'above'] = None
    error: Error = None

class RealtyReportsApiCreateReportForClassifiedResponseSuccessModel1ErrorsModel2(_BaseModel):
    access_denied: bool = Field(default=None, alias='accessDenied')
    feature_disabled: bool = Field(default=None, alias='featureDisabled')
    invalid_item: bool = Field(default=None, alias='invalidItem')
    message: str = None

class RealtyReportsApiCreateReportForClassifiedResponseSuccessModel1SuccessModel3(_BaseModel):
    report_link: str = Field(alias='reportLink')

class RealtyReportsApiCreateReportForClassifiedResponseSuccessModel1(_BaseModel):
    errors: RealtyReportsApiCreateReportForClassifiedResponseSuccessModel1ErrorsModel2 = None
    success: RealtyReportsApiCreateReportForClassifiedResponseSuccessModel1SuccessModel3 = None

class RealtyReportsApiCreateReportForClassifiedResponse(_BaseModel):
    success: RealtyReportsApiCreateReportForClassifiedResponseSuccessModel1

__all__ = ['Error', 'RealtyReportsApiMarketPriceCorrespondenceV1Response', 'RealtyReportsApiCreateReportForClassifiedResponseSuccessModel1ErrorsModel2', 'RealtyReportsApiCreateReportForClassifiedResponseSuccessModel1SuccessModel3', 'RealtyReportsApiCreateReportForClassifiedResponseSuccessModel1', 'RealtyReportsApiCreateReportForClassifiedResponse']
