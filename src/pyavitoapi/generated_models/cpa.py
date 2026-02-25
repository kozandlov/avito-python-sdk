"""Generated response models for slug: cpa."""

from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, ValidationError, Field

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class OpenApiChatsBuyer(_BaseModel):
    buyer_id: int = Field(alias='buyerId')
    name: str
    url: str

class OpenApiChat(_BaseModel):
    action_id: int = Field(alias='actionId')
    channel_id: str = Field(alias='channelId')
    contact_type: str = Field(alias='contactType')
    date: str
    group: str
    message: str
    message_id: str = Field(alias='messageId')
    price_penny: int = Field(alias='pricePenny')
    status: str
    target_chat_type: str = Field(alias='targetChatType')

class OpenApiChatsItem(_BaseModel):
    item_id: int = Field(alias='itemId')
    price_penny: int = Field(alias='pricePenny')
    title: str
    url: str

class OpenApiChatsComposition(_BaseModel):
    buyer: OpenApiChatsBuyer
    chat: OpenApiChat
    is_arbitrage_available: bool = Field(alias='isArbitrageAvailable')
    item: OpenApiChatsItem

class CpaApiChatByActionIdResponse(_BaseModel):
    chat: OpenApiChatsComposition = None

class CpaApiChatsByTimeResponse(_BaseModel):
    chats: list[OpenApiChatsComposition] = None

class CpaError(_BaseModel):
    code: int = None
    message: str = None

class CpaApiPostCreateComplaintResponse(_BaseModel):
    error: CpaError = None
    success: bool = None

class CpaApiCreateComplaintByActionIdResponse(_BaseModel):
    error: CpaError = None
    success: bool = None

class OpenAPIPhonesInfoFromChatsOut(_BaseModel):
    date: str
    group: str
    id: int
    phone_number: str | None = None
    price_penny: int = Field(alias='pricePenny')
    url: str

class CpaApiPhonesInfoFromChatsResponse(_BaseModel):
    results: list[OpenAPIPhonesInfoFromChatsOut]
    total: int

class CpaApiBalanceInfoV2Response(_BaseModel):
    advance: int = None
    balance: int = None
    debt: int = None
    error: CpaError = None

class CallV2(_BaseModel):
    buyer_phone: str = Field(default=None, alias='buyerPhone')
    create_time: str = Field(default=None, alias='createTime')
    duration: int = None
    group_title: str = Field(default=None, alias='groupTitle')
    id: int = None
    is_arbitrage_available: bool = Field(default=None, alias='isArbitrageAvailable')
    item_id: int = Field(default=None, alias='itemId')
    price: int = None
    record_url: str = Field(default=None, alias='recordUrl')
    seller_phone: str = Field(default=None, alias='sellerPhone')
    start_time: str = Field(default=None, alias='startTime')
    status_id: Literal[0, 1, 2, 3] = Field(default=None, alias='statusId')
    virtual_phone: str = Field(default=None, alias='virtualPhone')
    waiting_duration: float = Field(default=None, alias='waitingDuration')

class CpaApiGetCallByIdV2Response(_BaseModel):
    calls: CallV2 = None
    error: CpaError = None

class CpaApiGetCallsByTimeV2Response(_BaseModel):
    calls: list[CallV2] = None
    error: CpaError = None

class CpaApiChatsByTime2Response(_BaseModel):
    chats: list[OpenApiChatsComposition] = None

class CpaApiBalanceInfoV3Response(_BaseModel):
    balance: int = None

__all__ = ['OpenApiChatsBuyer', 'OpenApiChat', 'OpenApiChatsItem', 'OpenApiChatsComposition', 'CpaApiChatByActionIdResponse', 'CpaApiChatsByTimeResponse', 'CpaError', 'CpaApiPostCreateComplaintResponse', 'CpaApiCreateComplaintByActionIdResponse', 'OpenAPIPhonesInfoFromChatsOut', 'CpaApiPhonesInfoFromChatsResponse', 'CpaApiBalanceInfoV2Response', 'CallV2', 'CpaApiGetCallByIdV2Response', 'CpaApiGetCallsByTimeV2Response', 'CpaApiChatsByTime2Response', 'CpaApiBalanceInfoV3Response']
