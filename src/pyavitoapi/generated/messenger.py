"""Generated API module for slug: messenger."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.messenger import MessengerApiChatReadResponse, MessengerApiDeleteMessageResponse, MessengerApiGetChatByIdV2Response, MessengerApiGetChatsV2Response, MessengerApiGetMessagesV3Response, MessengerApiGetSubscriptionsResponse, MessengerApiGetVoiceFilesResponse, MessengerApiPostSendImageMessageResponse, MessengerApiPostSendMessageResponse, MessengerApiPostWebhookUnsubscribeResponse, MessengerApiPostWebhookV3Response, MessengerApiUploadImagesResponse


class MessengerApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def post_send_message(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> MessengerApiPostSendMessageResponse:
        """Отправка сообщения"""
        payload = await self._transport.request(
            method="POST",
            path_template="/messenger/v1/accounts/{user_id}/chats/{chat_id}/messages",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return MessengerApiPostSendMessageResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for messenger.post_send_message (POST /messenger/v1/accounts/{user_id}/chats/{chat_id}/messages)",
                payload=payload,
                details={
                    "slug": "messenger",
                    "operation_id": "postSendMessage",
                    "python_method": "post_send_message",
                    "http_method": "POST",
                    "path": "/messenger/v1/accounts/{user_id}/chats/{chat_id}/messages",
                    "errors": exc.errors(),
                },
            ) from exc

    async def post_send_image_message(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> MessengerApiPostSendImageMessageResponse:
        """Отправка сообщения с изображением"""
        payload = await self._transport.request(
            method="POST",
            path_template="/messenger/v1/accounts/{user_id}/chats/{chat_id}/messages/image",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return MessengerApiPostSendImageMessageResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for messenger.post_send_image_message (POST /messenger/v1/accounts/{user_id}/chats/{chat_id}/messages/image)",
                payload=payload,
                details={
                    "slug": "messenger",
                    "operation_id": "postSendImageMessage",
                    "python_method": "post_send_image_message",
                    "http_method": "POST",
                    "path": "/messenger/v1/accounts/{user_id}/chats/{chat_id}/messages/image",
                    "errors": exc.errors(),
                },
            ) from exc

    async def delete_message(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> MessengerApiDeleteMessageResponse:
        """Удаление сообщения"""
        payload = await self._transport.request(
            method="POST",
            path_template="/messenger/v1/accounts/{user_id}/chats/{chat_id}/messages/{message_id}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return MessengerApiDeleteMessageResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for messenger.delete_message (POST /messenger/v1/accounts/{user_id}/chats/{chat_id}/messages/{message_id})",
                payload=payload,
                details={
                    "slug": "messenger",
                    "operation_id": "deleteMessage",
                    "python_method": "delete_message",
                    "http_method": "POST",
                    "path": "/messenger/v1/accounts/{user_id}/chats/{chat_id}/messages/{message_id}",
                    "errors": exc.errors(),
                },
            ) from exc

    async def chat_read(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> MessengerApiChatReadResponse:
        """Прочитать чат"""
        payload = await self._transport.request(
            method="POST",
            path_template="/messenger/v1/accounts/{user_id}/chats/{chat_id}/read",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return MessengerApiChatReadResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for messenger.chat_read (POST /messenger/v1/accounts/{user_id}/chats/{chat_id}/read)",
                payload=payload,
                details={
                    "slug": "messenger",
                    "operation_id": "chatRead",
                    "python_method": "chat_read",
                    "http_method": "POST",
                    "path": "/messenger/v1/accounts/{user_id}/chats/{chat_id}/read",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_voice_files(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> MessengerApiGetVoiceFilesResponse:
        """Получение голосовых сообщений"""
        payload = await self._transport.request(
            method="GET",
            path_template="/messenger/v1/accounts/{user_id}/getVoiceFiles",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return MessengerApiGetVoiceFilesResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for messenger.get_voice_files (GET /messenger/v1/accounts/{user_id}/getVoiceFiles)",
                payload=payload,
                details={
                    "slug": "messenger",
                    "operation_id": "getVoiceFiles",
                    "python_method": "get_voice_files",
                    "http_method": "GET",
                    "path": "/messenger/v1/accounts/{user_id}/getVoiceFiles",
                    "errors": exc.errors(),
                },
            ) from exc

    async def upload_images(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> MessengerApiUploadImagesResponse:
        """Загрузка изображений"""
        payload = await self._transport.request(
            method="POST",
            path_template="/messenger/v1/accounts/{user_id}/uploadImages",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return MessengerApiUploadImagesResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for messenger.upload_images (POST /messenger/v1/accounts/{user_id}/uploadImages)",
                payload=payload,
                details={
                    "slug": "messenger",
                    "operation_id": "uploadImages",
                    "python_method": "upload_images",
                    "http_method": "POST",
                    "path": "/messenger/v1/accounts/{user_id}/uploadImages",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_subscriptions(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> MessengerApiGetSubscriptionsResponse:
        """Получение подписок (webhooks)"""
        payload = await self._transport.request(
            method="POST",
            path_template="/messenger/v1/subscriptions",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return MessengerApiGetSubscriptionsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for messenger.get_subscriptions (POST /messenger/v1/subscriptions)",
                payload=payload,
                details={
                    "slug": "messenger",
                    "operation_id": "getSubscriptions",
                    "python_method": "get_subscriptions",
                    "http_method": "POST",
                    "path": "/messenger/v1/subscriptions",
                    "errors": exc.errors(),
                },
            ) from exc

    async def post_webhook_unsubscribe(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> MessengerApiPostWebhookUnsubscribeResponse:
        """Отключение уведомлений (webhooks)"""
        payload = await self._transport.request(
            method="POST",
            path_template="/messenger/v1/webhook/unsubscribe",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return MessengerApiPostWebhookUnsubscribeResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for messenger.post_webhook_unsubscribe (POST /messenger/v1/webhook/unsubscribe)",
                payload=payload,
                details={
                    "slug": "messenger",
                    "operation_id": "postWebhookUnsubscribe",
                    "python_method": "post_webhook_unsubscribe",
                    "http_method": "POST",
                    "path": "/messenger/v1/webhook/unsubscribe",
                    "errors": exc.errors(),
                },
            ) from exc

    async def post_blacklist_v2(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:
        """Добавление пользователя в blacklist"""
        payload = await self._transport.request(
            method="POST",
            path_template="/messenger/v2/accounts/{user_id}/blacklist",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        return None

    async def get_chats_v2(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> MessengerApiGetChatsV2Response:
        """Получение информации по чатам"""
        payload = await self._transport.request(
            method="GET",
            path_template="/messenger/v2/accounts/{user_id}/chats",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return MessengerApiGetChatsV2Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for messenger.get_chats_v2 (GET /messenger/v2/accounts/{user_id}/chats)",
                payload=payload,
                details={
                    "slug": "messenger",
                    "operation_id": "getChatsV2",
                    "python_method": "get_chats_v2",
                    "http_method": "GET",
                    "path": "/messenger/v2/accounts/{user_id}/chats",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_chat_by_id_v2(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> MessengerApiGetChatByIdV2Response:
        """Получение информации по чату"""
        payload = await self._transport.request(
            method="GET",
            path_template="/messenger/v2/accounts/{user_id}/chats/{chat_id}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return MessengerApiGetChatByIdV2Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for messenger.get_chat_by_id_v2 (GET /messenger/v2/accounts/{user_id}/chats/{chat_id})",
                payload=payload,
                details={
                    "slug": "messenger",
                    "operation_id": "getChatByIdV2",
                    "python_method": "get_chat_by_id_v2",
                    "http_method": "GET",
                    "path": "/messenger/v2/accounts/{user_id}/chats/{chat_id}",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_messages_v3(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> MessengerApiGetMessagesV3Response:
        """Получение списка сообщений V3"""
        payload = await self._transport.request(
            method="GET",
            path_template="/messenger/v3/accounts/{user_id}/chats/{chat_id}/messages/",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return MessengerApiGetMessagesV3Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for messenger.get_messages_v3 (GET /messenger/v3/accounts/{user_id}/chats/{chat_id}/messages/)",
                payload=payload,
                details={
                    "slug": "messenger",
                    "operation_id": "getMessagesV3",
                    "python_method": "get_messages_v3",
                    "http_method": "GET",
                    "path": "/messenger/v3/accounts/{user_id}/chats/{chat_id}/messages/",
                    "errors": exc.errors(),
                },
            ) from exc

    async def post_webhook_v3(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> MessengerApiPostWebhookV3Response:
        """Включение уведомлений V3 (webhooks)"""
        payload = await self._transport.request(
            method="POST",
            path_template="/messenger/v3/webhook",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return MessengerApiPostWebhookV3Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for messenger.post_webhook_v3 (POST /messenger/v3/webhook)",
                payload=payload,
                details={
                    "slug": "messenger",
                    "operation_id": "postWebhookV3",
                    "python_method": "post_webhook_v3",
                    "http_method": "POST",
                    "path": "/messenger/v3/webhook",
                    "errors": exc.errors(),
                },
            ) from exc

__all__ = ["MessengerApi"]
