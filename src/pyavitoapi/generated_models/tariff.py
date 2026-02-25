"""Generated response models for slug: tariff."""

from __future__ import annotations

from typing import Any
from pydantic import BaseModel, ConfigDict, ValidationError, Field

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class TariffContractPackageCategoriesItemModel1(_BaseModel):
    name: str = None
    sub_categories: list[str] = Field(default=None, alias='subCategories')

class TariffContractPackagePriceConditionsItemModel2(_BaseModel):
    category_name: str = Field(default=None, alias='categoryName')
    original_price: float = Field(default=None, alias='originalPrice')
    price: float = None
    sort: int = None
    total: int = None

class TariffContractPackage(_BaseModel):
    categories: list[TariffContractPackageCategoriesItemModel1] = None
    locations: list[str] = None
    price_conditions: list[TariffContractPackagePriceConditionsItemModel2] = Field(default=None, alias='priceConditions')
    remain: int = None
    total: int = None

class TariffContractPriceModel3(_BaseModel):
    original_price: float = Field(default=None, alias='originalPrice')
    price: float = None

class TariffContract(_BaseModel):
    bonus: int = None
    close_time: int = Field(default=None, alias='closeTime')
    is_active: bool = Field(default=None, alias='isActive')
    level: str = None
    packages: list[TariffContractPackage] = None
    price: TariffContractPriceModel3 = None
    start_time: int = Field(default=None, alias='startTime')

class TariffApiGetTariffInfoResponse(_BaseModel):
    current: TariffContract = None
    scheduled: TariffContract = None

__all__ = ['TariffContractPackageCategoriesItemModel1', 'TariffContractPackagePriceConditionsItemModel2', 'TariffContractPackage', 'TariffContractPriceModel3', 'TariffContract', 'TariffApiGetTariffInfoResponse']
