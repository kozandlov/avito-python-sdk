"""Generated API module for slug: cpa."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.cpa import CpaApiBalanceInfoV2Response, CpaApiBalanceInfoV3Response, CpaApiChatByActionIdResponse, CpaApiChatsByTime2Response, CpaApiChatsByTimeResponse, CpaApiCreateComplaintByActionIdResponse, CpaApiGetCallByIdV2Response, CpaApiGetCallsByTimeV2Response, CpaApiPhonesInfoFromChatsResponse, CpaApiPostCreateComplaintResponse


class CpaApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def get_call(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:
        """Запись звонка (deprecated)"""
        payload = await self._transport.request(
            method="GET",
            path_template="/cpa/v1/call/{call_id}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        return None

    async def chat_by_action_id(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> CpaApiChatByActionIdResponse:
        """Чат"""
        payload = await self._transport.request(
            method="GET",
            path_template="/cpa/v1/chatByActionId/{actionId}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return CpaApiChatByActionIdResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for cpa.chat_by_action_id (GET /cpa/v1/chatByActionId/{actionId})",
                payload=payload,
                details={
                    "slug": "cpa",
                    "operation_id": "chatByActionId",
                    "python_method": "chat_by_action_id",
                    "http_method": "GET",
                    "path": "/cpa/v1/chatByActionId/{actionId}",
                    "errors": exc.errors(),
                },
            ) from exc

    async def chats_by_time(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> CpaApiChatsByTimeResponse:
        """Чаты по времени (deprecated)"""
        payload = await self._transport.request(
            method="POST",
            path_template="/cpa/v1/chatsByTime",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return CpaApiChatsByTimeResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for cpa.chats_by_time (POST /cpa/v1/chatsByTime)",
                payload=payload,
                details={
                    "slug": "cpa",
                    "operation_id": "chatsByTime",
                    "python_method": "chats_by_time",
                    "http_method": "POST",
                    "path": "/cpa/v1/chatsByTime",
                    "errors": exc.errors(),
                },
            ) from exc

    async def post_create_complaint(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> CpaApiPostCreateComplaintResponse:
        """Создание жалобы для звонков"""
        payload = await self._transport.request(
            method="POST",
            path_template="/cpa/v1/createComplaint",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return CpaApiPostCreateComplaintResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for cpa.post_create_complaint (POST /cpa/v1/createComplaint)",
                payload=payload,
                details={
                    "slug": "cpa",
                    "operation_id": "postCreateComplaint",
                    "python_method": "post_create_complaint",
                    "http_method": "POST",
                    "path": "/cpa/v1/createComplaint",
                    "errors": exc.errors(),
                },
            ) from exc

    async def create_complaint_by_action_id(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> CpaApiCreateComplaintByActionIdResponse:
        """Создание жалобы для звонков/чатов"""
        payload = await self._transport.request(
            method="POST",
            path_template="/cpa/v1/createComplaintByActionId",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return CpaApiCreateComplaintByActionIdResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for cpa.create_complaint_by_action_id (POST /cpa/v1/createComplaintByActionId)",
                payload=payload,
                details={
                    "slug": "cpa",
                    "operation_id": "createComplaintByActionId",
                    "python_method": "create_complaint_by_action_id",
                    "http_method": "POST",
                    "path": "/cpa/v1/createComplaintByActionId",
                    "errors": exc.errors(),
                },
            ) from exc

    async def phones_info_from_chats(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> CpaApiPhonesInfoFromChatsResponse:
        """Информация по номерам телефонов из целевых чатов"""
        payload = await self._transport.request(
            method="POST",
            path_template="/cpa/v1/phonesInfoFromChats",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return CpaApiPhonesInfoFromChatsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for cpa.phones_info_from_chats (POST /cpa/v1/phonesInfoFromChats)",
                payload=payload,
                details={
                    "slug": "cpa",
                    "operation_id": "phonesInfoFromChats",
                    "python_method": "phones_info_from_chats",
                    "http_method": "POST",
                    "path": "/cpa/v1/phonesInfoFromChats",
                    "errors": exc.errors(),
                },
            ) from exc

    async def balance_info_v2(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> CpaApiBalanceInfoV2Response:
        """Баланс (deprecated)"""
        payload = await self._transport.request(
            method="POST",
            path_template="/cpa/v2/balanceInfo",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return CpaApiBalanceInfoV2Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for cpa.balance_info_v2 (POST /cpa/v2/balanceInfo)",
                payload=payload,
                details={
                    "slug": "cpa",
                    "operation_id": "balanceInfoV2",
                    "python_method": "balance_info_v2",
                    "http_method": "POST",
                    "path": "/cpa/v2/balanceInfo",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_call_by_id_v2(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> CpaApiGetCallByIdV2Response:
        """Звонок"""
        payload = await self._transport.request(
            method="POST",
            path_template="/cpa/v2/callById",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return CpaApiGetCallByIdV2Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for cpa.get_call_by_id_v2 (POST /cpa/v2/callById)",
                payload=payload,
                details={
                    "slug": "cpa",
                    "operation_id": "getCallByIdV2",
                    "python_method": "get_call_by_id_v2",
                    "http_method": "POST",
                    "path": "/cpa/v2/callById",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_calls_by_time_v2(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> CpaApiGetCallsByTimeV2Response:
        """Звонки по времени"""
        payload = await self._transport.request(
            method="POST",
            path_template="/cpa/v2/callsByTime",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return CpaApiGetCallsByTimeV2Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for cpa.get_calls_by_time_v2 (POST /cpa/v2/callsByTime)",
                payload=payload,
                details={
                    "slug": "cpa",
                    "operation_id": "getCallsByTimeV2",
                    "python_method": "get_calls_by_time_v2",
                    "http_method": "POST",
                    "path": "/cpa/v2/callsByTime",
                    "errors": exc.errors(),
                },
            ) from exc

    async def chats_by_time_2(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> CpaApiChatsByTime2Response:
        """Чаты по времени"""
        payload = await self._transport.request(
            method="POST",
            path_template="/cpa/v2/chatsByTime",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return CpaApiChatsByTime2Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for cpa.chats_by_time_2 (POST /cpa/v2/chatsByTime)",
                payload=payload,
                details={
                    "slug": "cpa",
                    "operation_id": "chatsByTime_2",
                    "python_method": "chats_by_time_2",
                    "http_method": "POST",
                    "path": "/cpa/v2/chatsByTime",
                    "errors": exc.errors(),
                },
            ) from exc

    async def balance_info_v3(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> CpaApiBalanceInfoV3Response:
        """Баланс"""
        payload = await self._transport.request(
            method="POST",
            path_template="/cpa/v3/balanceInfo",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return CpaApiBalanceInfoV3Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for cpa.balance_info_v3 (POST /cpa/v3/balanceInfo)",
                payload=payload,
                details={
                    "slug": "cpa",
                    "operation_id": "balanceInfoV3",
                    "python_method": "balance_info_v3",
                    "http_method": "POST",
                    "path": "/cpa/v3/balanceInfo",
                    "errors": exc.errors(),
                },
            ) from exc

__all__ = ["CpaApi"]
