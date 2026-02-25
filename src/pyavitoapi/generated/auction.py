"""Generated API module for slug: auction."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.auction import AuctionApiGetUserBidsResponse


class AuctionApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def get_user_bids(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AuctionApiGetUserBidsResponse:
        """Получение информации о действующих и доступных ставках"""
        payload = await self._transport.request(
            method="GET",
            path_template="/auction/1/bids",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AuctionApiGetUserBidsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for auction.get_user_bids (GET /auction/1/bids)",
                payload=payload,
                details={
                    "slug": "auction",
                    "operation_id": "getUserBids",
                    "python_method": "get_user_bids",
                    "http_method": "GET",
                    "path": "/auction/1/bids",
                    "errors": exc.errors(),
                },
            ) from exc

    async def save_item_bids(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:
        """Сохранение новых ставок"""
        payload = await self._transport.request(
            method="POST",
            path_template="/auction/1/bids",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        return None

__all__ = ["AuctionApi"]
