"""Generated response models for slug: messenger."""

from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, ValidationError, Field, RootModel

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class MessengerApiPostSendMessageResponseContentModel1(_BaseModel):
    text: str = None

class MessengerApiPostSendMessageResponse(_BaseModel):
    content: MessengerApiPostSendMessageResponseContentModel1 = None
    created: int = None
    direction: str = None
    id: str = None
    type: str = None

class MessengerApiPostSendImageMessageResponseContentModel2ImageModel3(_BaseModel):
    sizes: dict[str, str] = None

class MessengerApiPostSendImageMessageResponseContentModel2(_BaseModel):
    image: MessengerApiPostSendImageMessageResponseContentModel2ImageModel3 = None

class MessengerApiPostSendImageMessageResponse(_BaseModel):
    author_id: int = None
    content: MessengerApiPostSendImageMessageResponseContentModel2 = None
    created: int = None
    direction: str = None
    id: str = None
    type: str = None

class MessengerApiDeleteMessageResponse(_BaseModel):
    pass

class MessengerApiChatReadResponse(_BaseModel):
    ok: bool = None

class MessengerApiGetVoiceFilesResponse(_BaseModel):
    voices_urls: dict[str, str] = None

class MessengerApiUploadImagesResponse(RootModel[dict[str, dict[str, str]]]):
    pass

class MessengerApiGetSubscriptionsResponseSubscriptionsItemModel4(_BaseModel):
    url: str
    version: str

class MessengerApiGetSubscriptionsResponse(_BaseModel):
    subscriptions: list[MessengerApiGetSubscriptionsResponseSubscriptionsItemModel4]

class MessengerApiPostWebhookUnsubscribeResponse(_BaseModel):
    ok: bool = None

class ChatContextModel5ValueModel6ImagesModel7MainModel8(_BaseModel):
    field_140x105: str = Field(default=None, alias='140x105')

class ChatContextModel5ValueModel6ImagesModel7(_BaseModel):
    count: int = None
    main: ChatContextModel5ValueModel6ImagesModel7MainModel8 = None

class ChatContextModel5ValueModel6(_BaseModel):
    id: int = None
    images: ChatContextModel5ValueModel6ImagesModel7 = None
    price_string: str = None
    status_id: int = None
    title: str = None
    url: str = None
    user_id: int = None

class ChatContextModel5(_BaseModel):
    type: str = None
    value: ChatContextModel5ValueModel6 = None

class MessageContentCallModel10(_BaseModel):
    status: Literal['missed'] = None
    target_user_id: int = None

class MessageContentImageModel11(_BaseModel):
    sizes: dict[str, Any] = None

class MessageContentItemModel12(_BaseModel):
    image_url: str = None
    item_url: str = None
    price_string: str | None = None
    title: str = None

class MessageContentLinkModel13PreviewModel14(_BaseModel):
    description: str = None
    domain: str = None
    images: dict[str, Any] | None = None
    title: str = None
    url: str = None

class MessageContentLinkModel13(_BaseModel):
    preview: MessageContentLinkModel13PreviewModel14 | None = None
    text: str = None
    url: str = None

class MessageContentLocationModel15(_BaseModel):
    kind: Literal['house', 'street', 'area', '...'] = None
    lat: float = None
    lon: float = None
    text: str = None
    title: str = None

class MessageContentVoiceModel16(_BaseModel):
    voice_id: str = None

class MessageContent(_BaseModel):
    call: MessageContentCallModel10 | None = None
    flow_id: str | None = None
    image: MessageContentImageModel11 | None = None
    item: MessageContentItemModel12 | None = None
    link: MessageContentLinkModel13 | None = None
    location: MessageContentLocationModel15 | None = None
    text: str | None = None
    voice: MessageContentVoiceModel16 | None = None

class ChatLastMessageModel9(_BaseModel):
    author_id: int = None
    content: MessageContent = None
    created: int = None
    direction: str = None
    id: str = None
    type: str = None

class ChatUsersItemModel17PublicUserProfileModel18AvatarModel19ImagesModel20(_BaseModel):
    field_128x128: str = Field(default=None, alias='128x128')
    field_192x192: str = Field(default=None, alias='192x192')
    field_24x24: str = Field(default=None, alias='24x24')
    field_256x256: str = Field(default=None, alias='256x256')
    field_36x36: str = Field(default=None, alias='36x36')
    field_48x48: str = Field(default=None, alias='48x48')
    field_64x64: str = Field(default=None, alias='64x64')
    field_72x72: str = Field(default=None, alias='72x72')
    field_96x96: str = Field(default=None, alias='96x96')

class ChatUsersItemModel17PublicUserProfileModel18AvatarModel19(_BaseModel):
    default: str = None
    images: ChatUsersItemModel17PublicUserProfileModel18AvatarModel19ImagesModel20 = None

class ChatUsersItemModel17PublicUserProfileModel18(_BaseModel):
    avatar: ChatUsersItemModel17PublicUserProfileModel18AvatarModel19 = None
    item_id: int = None
    url: str = None
    user_id: int = None

class ChatUsersItemModel17(_BaseModel):
    id: int = None
    name: str = None
    public_user_profile: ChatUsersItemModel17PublicUserProfileModel18 = None

class Chat(_BaseModel):
    context: ChatContextModel5 = None
    created: int = None
    id: str = None
    last_message: ChatLastMessageModel9 = None
    updated: int = None
    users: list[ChatUsersItemModel17] = None

class MessengerApiGetChatsV2Response(_BaseModel):
    chats: list[Chat] = None

class MessengerApiGetChatByIdV2ResponseContextModel21ValueModel22ImagesModel23MainModel24(_BaseModel):
    field_140x105: str = Field(default=None, alias='140x105')

class MessengerApiGetChatByIdV2ResponseContextModel21ValueModel22ImagesModel23(_BaseModel):
    count: int = None
    main: MessengerApiGetChatByIdV2ResponseContextModel21ValueModel22ImagesModel23MainModel24 = None

class MessengerApiGetChatByIdV2ResponseContextModel21ValueModel22(_BaseModel):
    id: int = None
    images: MessengerApiGetChatByIdV2ResponseContextModel21ValueModel22ImagesModel23 = None
    price_string: str = None
    status_id: int = None
    title: str = None
    url: str = None
    user_id: int = None

class MessengerApiGetChatByIdV2ResponseContextModel21(_BaseModel):
    type: str = None
    value: MessengerApiGetChatByIdV2ResponseContextModel21ValueModel22 = None

class MessengerApiGetChatByIdV2ResponseLastMessageModel25(_BaseModel):
    author_id: int = None
    content: MessageContent = None
    created: int = None
    direction: str = None
    id: str = None
    type: str = None

class MessengerApiGetChatByIdV2ResponseUsersItemModel26PublicUserProfileModel27AvatarModel28ImagesModel29(_BaseModel):
    field_128x128: str = Field(default=None, alias='128x128')
    field_192x192: str = Field(default=None, alias='192x192')
    field_24x24: str = Field(default=None, alias='24x24')
    field_256x256: str = Field(default=None, alias='256x256')
    field_36x36: str = Field(default=None, alias='36x36')
    field_48x48: str = Field(default=None, alias='48x48')
    field_64x64: str = Field(default=None, alias='64x64')
    field_72x72: str = Field(default=None, alias='72x72')
    field_96x96: str = Field(default=None, alias='96x96')

class MessengerApiGetChatByIdV2ResponseUsersItemModel26PublicUserProfileModel27AvatarModel28(_BaseModel):
    default: str = None
    images: MessengerApiGetChatByIdV2ResponseUsersItemModel26PublicUserProfileModel27AvatarModel28ImagesModel29 = None

class MessengerApiGetChatByIdV2ResponseUsersItemModel26PublicUserProfileModel27(_BaseModel):
    avatar: MessengerApiGetChatByIdV2ResponseUsersItemModel26PublicUserProfileModel27AvatarModel28 = None
    item_id: int = None
    url: str = None
    user_id: int = None

class MessengerApiGetChatByIdV2ResponseUsersItemModel26(_BaseModel):
    id: int = None
    name: str = None
    public_user_profile: MessengerApiGetChatByIdV2ResponseUsersItemModel26PublicUserProfileModel27 = None

class MessengerApiGetChatByIdV2Response(_BaseModel):
    context: MessengerApiGetChatByIdV2ResponseContextModel21 = None
    created: int = None
    id: str = None
    last_message: MessengerApiGetChatByIdV2ResponseLastMessageModel25 = None
    updated: int = None
    users: list[MessengerApiGetChatByIdV2ResponseUsersItemModel26] = None

class MessageQuote(_BaseModel):
    author_id: int = None
    content: MessageContent = None
    created: int = None
    id: str = None
    type: Literal['text', 'image', 'link', 'item', 'location', 'call', 'deleted', 'voice', 'system'] = None

class MessengerApiGetMessagesV3ResponseItemModel30(_BaseModel):
    author_id: int = None
    content: MessageContent = None
    created: int = None
    direction: Literal['in', 'out'] = None
    id: str = None
    is_read: bool = None
    quote: MessageQuote = None
    read: int | None = None
    type: Literal['text', 'image', 'link', 'item', 'location', 'call', 'deleted', 'voice', 'system'] = None

class MessengerApiGetMessagesV3Response(RootModel[list[MessengerApiGetMessagesV3ResponseItemModel30]]):
    pass

class MessengerApiPostWebhookV3Response(_BaseModel):
    ok: bool = None

__all__ = ['MessengerApiPostSendMessageResponseContentModel1', 'MessengerApiPostSendMessageResponse', 'MessengerApiPostSendImageMessageResponseContentModel2ImageModel3', 'MessengerApiPostSendImageMessageResponseContentModel2', 'MessengerApiPostSendImageMessageResponse', 'MessengerApiDeleteMessageResponse', 'MessengerApiChatReadResponse', 'MessengerApiGetVoiceFilesResponse', 'MessengerApiUploadImagesResponse', 'MessengerApiGetSubscriptionsResponseSubscriptionsItemModel4', 'MessengerApiGetSubscriptionsResponse', 'MessengerApiPostWebhookUnsubscribeResponse', 'ChatContextModel5ValueModel6ImagesModel7MainModel8', 'ChatContextModel5ValueModel6ImagesModel7', 'ChatContextModel5ValueModel6', 'ChatContextModel5', 'MessageContentCallModel10', 'MessageContentImageModel11', 'MessageContentItemModel12', 'MessageContentLinkModel13PreviewModel14', 'MessageContentLinkModel13', 'MessageContentLocationModel15', 'MessageContentVoiceModel16', 'MessageContent', 'ChatLastMessageModel9', 'ChatUsersItemModel17PublicUserProfileModel18AvatarModel19ImagesModel20', 'ChatUsersItemModel17PublicUserProfileModel18AvatarModel19', 'ChatUsersItemModel17PublicUserProfileModel18', 'ChatUsersItemModel17', 'Chat', 'MessengerApiGetChatsV2Response', 'MessengerApiGetChatByIdV2ResponseContextModel21ValueModel22ImagesModel23MainModel24', 'MessengerApiGetChatByIdV2ResponseContextModel21ValueModel22ImagesModel23', 'MessengerApiGetChatByIdV2ResponseContextModel21ValueModel22', 'MessengerApiGetChatByIdV2ResponseContextModel21', 'MessengerApiGetChatByIdV2ResponseLastMessageModel25', 'MessengerApiGetChatByIdV2ResponseUsersItemModel26PublicUserProfileModel27AvatarModel28ImagesModel29', 'MessengerApiGetChatByIdV2ResponseUsersItemModel26PublicUserProfileModel27AvatarModel28', 'MessengerApiGetChatByIdV2ResponseUsersItemModel26PublicUserProfileModel27', 'MessengerApiGetChatByIdV2ResponseUsersItemModel26', 'MessengerApiGetChatByIdV2Response', 'MessageQuote', 'MessengerApiGetMessagesV3ResponseItemModel30', 'MessengerApiGetMessagesV3Response', 'MessengerApiPostWebhookV3Response']
