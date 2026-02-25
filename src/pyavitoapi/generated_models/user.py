"""Generated response models for slug: user."""

from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, ValidationError, Field

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class ResponseOperationsHistoryItem(_BaseModel):
    amount_bonus: float = Field(default=None, alias='amountBonus')
    amount_rub: float = Field(default=None, alias='amountRub')
    amount_total: float = Field(default=None, alias='amountTotal')
    item_id: int = Field(default=None, alias='itemId')
    operation_name: str = Field(default=None, alias='operationName')
    operation_type: Literal['списание в счёт кредита', 'постоплата', 'внесение CPA аванса', 'возврат CPA аванса', 'аванс', 'возврат аванса', 'списание средств с кошелька в доход (не за оказанные услуги)', 'сжигание бонусов', 'резервирование под автостратегию', 'возврат зарезервированных средств под автостатегию на кошелек', 'резервирование средств под услугу', 'возврат зарзервированных средств на баланс кошелька', 'признание выручки', 'списание остатка', 'сторно', 'опротестовано', 'чарджбэк'] = Field(default=None, alias='operationType')
    paid_at: str = Field(default=None, alias='paidAt')
    service_id: int = Field(default=None, alias='serviceId')
    service_name: str = Field(default=None, alias='serviceName')
    service_type: Literal['vas', 'perf_vas', 'lf', 'cv', 'tariff', 'subscription', 'cpa', 'bundle'] = Field(default=None, alias='serviceType')
    updated_at: str = Field(default=None, alias='updatedAt')

class UserApiPostOperationsHistoryResponseResultModel1(_BaseModel):
    operations: list[ResponseOperationsHistoryItem] = None

class UserApiPostOperationsHistoryResponse(_BaseModel):
    result: UserApiPostOperationsHistoryResponseResultModel1 = None

class UserApiGetUserInfoSelfResponse(_BaseModel):
    email: str = None
    id: int = None
    name: str = None
    phone: str = None
    phones: list[str] = None
    profile_url: str = None

class UserApiGetUserBalanceResponse(_BaseModel):
    bonus: float = None
    real: float = None

__all__ = ['ResponseOperationsHistoryItem', 'UserApiPostOperationsHistoryResponseResultModel1', 'UserApiPostOperationsHistoryResponse', 'UserApiGetUserInfoSelfResponse', 'UserApiGetUserBalanceResponse']
