"""Generated API module for slug: calltracking."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport


class CalltrackingApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def get_call_by_id(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:
        """Звонок по идентификатору"""
        payload = await self._transport.request(
            method="POST",
            path_template="/calltracking/v1/getCallById/",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        return None

    async def get_calls(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:
        """Звонки по времени"""
        payload = await self._transport.request(
            method="POST",
            path_template="/calltracking/v1/getCalls/",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        return None

    async def get_record_by_call_id(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:
        """Получение аудиозаписи звонка по идентификатору"""
        payload = await self._transport.request(
            method="GET",
            path_template="/calltracking/v1/getRecordByCallId/",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        return None

__all__ = ["CalltrackingApi"]
