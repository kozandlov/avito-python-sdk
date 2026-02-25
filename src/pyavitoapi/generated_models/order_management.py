"""Generated response models for slug: order-management."""

from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, ValidationError, Field

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class OrderManagementApiMarkingsResponseResultsItemModel1(_BaseModel):
    error: str | None = None
    item_id: str = Field(default=None, alias='itemId')
    order_id: str = Field(default=None, alias='orderId')
    success: bool = None

class OrderManagementApiMarkingsResponse(_BaseModel):
    results: list[OrderManagementApiMarkingsResponseResultsItemModel1] = None

class OrderManagementApiAcceptReturnOrderResponse(_BaseModel):
    success: bool = None

class OrderManagementApiApplyTransitionResponse(_BaseModel):
    success: bool = None

class OrderManagementApiCheckConfirmationCodeResponseDataModel2(_BaseModel):
    status: Literal['success', 'fail', 'expired', 'attempts'] = None

class OrderManagementApiCheckConfirmationCodeResponse(_BaseModel):
    data: OrderManagementApiCheckConfirmationCodeResponseDataModel2 = None

class OrderManagementApiCncSetDetailsResponseResultModel3(_BaseModel):
    success: bool = None

class OrderManagementApiCncSetDetailsResponse(_BaseModel):
    result: OrderManagementApiCncSetDetailsResponseResultModel3 = None
    status: str = None

class OrderManagementApiGetCourierDeliveryRangeResponseResultModel4DateOptionsItemModel5TimeIntervalsItemModel6(_BaseModel):
    end_date: str = Field(default=None, alias='endDate')
    start_date: str = Field(default=None, alias='startDate')
    title: str = None
    type: str = None

class OrderManagementApiGetCourierDeliveryRangeResponseResultModel4DateOptionsItemModel5(_BaseModel):
    date: str = None
    time_intervals: list[OrderManagementApiGetCourierDeliveryRangeResponseResultModel4DateOptionsItemModel5TimeIntervalsItemModel6] = Field(default=None, alias='timeIntervals')

class OrderManagementApiGetCourierDeliveryRangeResponseResultModel4(_BaseModel):
    address: str = None
    address_details: str = Field(default=None, alias='addressDetails')
    date_options: list[OrderManagementApiGetCourierDeliveryRangeResponseResultModel4DateOptionsItemModel5] = Field(alias='dateOptions')
    end_date: str = Field(default=None, alias='endDate')
    name: str = None
    phone: str = None
    start_date: str = Field(default=None, alias='startDate')

class OrderManagementApiGetCourierDeliveryRangeResponse(_BaseModel):
    result: OrderManagementApiGetCourierDeliveryRangeResponseResultModel4
    status: str

class OrderManagementApiSetCourierDeliveryRangeResponse(_BaseModel):
    success: bool = None

class OrderManagementApiSetOrderTrackingNumberResponseErrorModel7(_BaseModel):
    code: str
    message: str

class OrderManagementApiSetOrderTrackingNumberResponse(_BaseModel):
    error: OrderManagementApiSetOrderTrackingNumberResponseErrorModel7 = None
    success: bool = None

class Action(_BaseModel):
    name: Literal['setMarkings', 'setCNCDetails', 'setTrackNumber', 'fixTrackNumber', 'acceptReturnOrder', 'confirm', 'reject', 'perform', 'receive'] = None
    required: bool = None

class BuyerInfo(_BaseModel):
    full_name: str = Field(default=None, alias='fullName')
    phone_number: str = Field(default=None, alias='phoneNumber')

class CourierInfo(_BaseModel):
    address: str | None = None
    comment: str | None = None

class TerminalInfo(_BaseModel):
    address: str | None = None
    code: str | None = None

class Delivery(_BaseModel):
    buyer_info: BuyerInfo = Field(default=None, alias='buyerInfo')
    courier_info: CourierInfo = Field(default=None, alias='courierInfo')
    dispatch_number: str = Field(default=None, alias='dispatchNumber')
    service_name: str = Field(default=None, alias='serviceName')
    service_type: Literal['pvz', 'dbs', 'rdbs'] = Field(default=None, alias='serviceType')
    terminal_info: TerminalInfo = Field(default=None, alias='terminalInfo')
    tracking_number: str = Field(default=None, alias='trackingNumber')

class Discount(_BaseModel):
    id: str = None
    type: Literal['promocode'] = None
    value: float = None

class ItemPrices(_BaseModel):
    commission: float = None
    discount_sum: float = Field(default=None, alias='discountSum')
    price: float = None
    total: float = None

class Item(_BaseModel):
    avito_id: str = Field(alias='avitoId')
    chat_id: str = Field(default=None, alias='chatId')
    count: int
    discounts: list[Discount] = None
    id: str = None
    location: str = None
    prices: ItemPrices
    title: str

class OrderPrices(_BaseModel):
    commission: float = None
    delivery: float = None
    discount: float = None
    price: float = None
    total: float = None

class ReturnPolicy(_BaseModel):
    return_status: Literal['in_transit', 'ready_to_pickup', 'self_return'] = Field(default=None, alias='returnStatus')
    tracking_number: str = Field(default=None, alias='trackingNumber')

class Schedules(_BaseModel):
    confirm_till: str | None = Field(default=None, alias='confirmTill')
    delivery_date: str | None = Field(default=None, alias='deliveryDate')
    delivery_date_ma: str | None = Field(default=None, alias='deliveryDateMaх')
    delivery_date_min: str | None = Field(default=None, alias='deliveryDateMin')
    set_tracking_number_till: str | None = Field(default=None, alias='setTrackingNumberTill')
    ship_till: str | None = Field(default=None, alias='shipTill')

class Order(_BaseModel):
    available_actions: list[Action] | None = Field(default=None, alias='availableActions')
    created_at: str = Field(alias='createdAt')
    delivery: Delivery
    id: str
    items: list[Item]
    marketplace_id: str | None = Field(default=None, alias='marketplaceId')
    prices: OrderPrices
    return_policy: ReturnPolicy = Field(default=None, alias='returnPolicy')
    schedules: Schedules
    status: str
    updated_at: str = Field(alias='updatedAt')

class OrderManagementApiGetOrdersResponse(_BaseModel):
    has_more: bool = Field(alias='hasMore')
    orders: list[Order]

class OrderManagementApiGenerateLabelsResponse(_BaseModel):
    task_id: str = Field(alias='taskID')

class OrderManagementApiGenerateLabelsExtendedResponse(_BaseModel):
    task_id: str = Field(alias='taskID')

__all__ = ['OrderManagementApiMarkingsResponseResultsItemModel1', 'OrderManagementApiMarkingsResponse', 'OrderManagementApiAcceptReturnOrderResponse', 'OrderManagementApiApplyTransitionResponse', 'OrderManagementApiCheckConfirmationCodeResponseDataModel2', 'OrderManagementApiCheckConfirmationCodeResponse', 'OrderManagementApiCncSetDetailsResponseResultModel3', 'OrderManagementApiCncSetDetailsResponse', 'OrderManagementApiGetCourierDeliveryRangeResponseResultModel4DateOptionsItemModel5TimeIntervalsItemModel6', 'OrderManagementApiGetCourierDeliveryRangeResponseResultModel4DateOptionsItemModel5', 'OrderManagementApiGetCourierDeliveryRangeResponseResultModel4', 'OrderManagementApiGetCourierDeliveryRangeResponse', 'OrderManagementApiSetCourierDeliveryRangeResponse', 'OrderManagementApiSetOrderTrackingNumberResponseErrorModel7', 'OrderManagementApiSetOrderTrackingNumberResponse', 'Action', 'BuyerInfo', 'CourierInfo', 'TerminalInfo', 'Delivery', 'Discount', 'ItemPrices', 'Item', 'OrderPrices', 'ReturnPolicy', 'Schedules', 'Order', 'OrderManagementApiGetOrdersResponse', 'OrderManagementApiGenerateLabelsResponse', 'OrderManagementApiGenerateLabelsExtendedResponse']
