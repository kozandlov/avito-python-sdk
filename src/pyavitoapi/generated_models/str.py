"""Generated response models for slug: str."""

from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, ValidationError

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class StrApiPutBookingsInfoResponse(_BaseModel):
    result: Literal['success'] = None

class RealtyBookingContactModel1(_BaseModel):
    email: str
    name: str
    phone: str = None

class RealtyBookingSafeDepositModel2(_BaseModel):
    owner_amount: int = None
    tax: int = None
    total_amount: int = None

class RealtyBooking(_BaseModel):
    avito_booking_id: int = None
    base_price: int = None
    check_in: str = None
    check_out: str = None
    contact: RealtyBookingContactModel1 = None
    guest_count: int = None
    nights: int = None
    safe_deposit: RealtyBookingSafeDepositModel2 = None
    status: Literal['active', 'canceled', 'pending'] = None

class StrApiGetRealtyBookingsResponse(_BaseModel):
    bookings: list[RealtyBooking]

class StrApiPostRealtyPricesResponse(_BaseModel):
    result: Literal['success'] = None

class StrApiPutIntervalsResponse(_BaseModel):
    result: Literal['success'] = None

__all__ = ['StrApiPutBookingsInfoResponse', 'RealtyBookingContactModel1', 'RealtyBookingSafeDepositModel2', 'RealtyBooking', 'StrApiGetRealtyBookingsResponse', 'StrApiPostRealtyPricesResponse', 'StrApiPutIntervalsResponse']
