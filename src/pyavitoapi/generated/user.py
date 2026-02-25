"""Generated API module for slug: user."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.user import UserApiGetUserBalanceResponse, UserApiGetUserInfoSelfResponse, UserApiPostOperationsHistoryResponse


class UserApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def post_operations_history(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> UserApiPostOperationsHistoryResponse:
        """Получение истории операций пользователя"""
        payload = await self._transport.request(
            method="POST",
            path_template="/core/v1/accounts/operations_history/",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return UserApiPostOperationsHistoryResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for user.post_operations_history (POST /core/v1/accounts/operations_history/)",
                payload=payload,
                details={
                    "slug": "user",
                    "operation_id": "postOperationsHistory",
                    "python_method": "post_operations_history",
                    "http_method": "POST",
                    "path": "/core/v1/accounts/operations_history/",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_user_info_self(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> UserApiGetUserInfoSelfResponse:
        """Получение информации об авторизованном пользователе"""
        payload = await self._transport.request(
            method="GET",
            path_template="/core/v1/accounts/self",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return UserApiGetUserInfoSelfResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for user.get_user_info_self (GET /core/v1/accounts/self)",
                payload=payload,
                details={
                    "slug": "user",
                    "operation_id": "getUserInfoSelf",
                    "python_method": "get_user_info_self",
                    "http_method": "GET",
                    "path": "/core/v1/accounts/self",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_user_balance(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> UserApiGetUserBalanceResponse:
        """Получение баланса кошелька пользователя"""
        payload = await self._transport.request(
            method="GET",
            path_template="/core/v1/accounts/{user_id}/balance/",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return UserApiGetUserBalanceResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for user.get_user_balance (GET /core/v1/accounts/{user_id}/balance/)",
                payload=payload,
                details={
                    "slug": "user",
                    "operation_id": "getUserBalance",
                    "python_method": "get_user_balance",
                    "http_method": "GET",
                    "path": "/core/v1/accounts/{user_id}/balance/",
                    "errors": exc.errors(),
                },
            ) from exc

__all__ = ["UserApi"]
