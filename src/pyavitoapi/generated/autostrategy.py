"""Generated API module for slug: autostrategy."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.autostrategy import AutostrategyApiCreateAutostrategyCampaignResponse, AutostrategyApiEditAutostrategyCampaignResponse, AutostrategyApiGetAutostrategyBudgetResponse, AutostrategyApiGetAutostrategyCampaignInfoResponse, AutostrategyApiGetAutostrategyCampaignsResponse, AutostrategyApiGetAutostrategyStatResponse, AutostrategyApiStopAutostrategyCampaignResponse


class AutostrategyApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def get_autostrategy_budget(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutostrategyApiGetAutostrategyBudgetResponse:
        """Расчет бюджета кампании"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autostrategy/v1/budget",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutostrategyApiGetAutostrategyBudgetResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autostrategy.get_autostrategy_budget (POST /autostrategy/v1/budget)",
                payload=payload,
                details={
                    "slug": "autostrategy",
                    "operation_id": "getAutostrategyBudget",
                    "python_method": "get_autostrategy_budget",
                    "http_method": "POST",
                    "path": "/autostrategy/v1/budget",
                    "errors": exc.errors(),
                },
            ) from exc

    async def create_autostrategy_campaign(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutostrategyApiCreateAutostrategyCampaignResponse:
        """Создание новой кампании"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autostrategy/v1/campaign/create",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutostrategyApiCreateAutostrategyCampaignResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autostrategy.create_autostrategy_campaign (POST /autostrategy/v1/campaign/create)",
                payload=payload,
                details={
                    "slug": "autostrategy",
                    "operation_id": "createAutostrategyCampaign",
                    "python_method": "create_autostrategy_campaign",
                    "http_method": "POST",
                    "path": "/autostrategy/v1/campaign/create",
                    "errors": exc.errors(),
                },
            ) from exc

    async def edit_autostrategy_campaign(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutostrategyApiEditAutostrategyCampaignResponse:
        """Редактирование кампании"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autostrategy/v1/campaign/edit",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutostrategyApiEditAutostrategyCampaignResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autostrategy.edit_autostrategy_campaign (POST /autostrategy/v1/campaign/edit)",
                payload=payload,
                details={
                    "slug": "autostrategy",
                    "operation_id": "editAutostrategyCampaign",
                    "python_method": "edit_autostrategy_campaign",
                    "http_method": "POST",
                    "path": "/autostrategy/v1/campaign/edit",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_autostrategy_campaign_info(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutostrategyApiGetAutostrategyCampaignInfoResponse:
        """Получение полной информации о кампании"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autostrategy/v1/campaign/info",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutostrategyApiGetAutostrategyCampaignInfoResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autostrategy.get_autostrategy_campaign_info (POST /autostrategy/v1/campaign/info)",
                payload=payload,
                details={
                    "slug": "autostrategy",
                    "operation_id": "getAutostrategyCampaignInfo",
                    "python_method": "get_autostrategy_campaign_info",
                    "http_method": "POST",
                    "path": "/autostrategy/v1/campaign/info",
                    "errors": exc.errors(),
                },
            ) from exc

    async def stop_autostrategy_campaign(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutostrategyApiStopAutostrategyCampaignResponse:
        """Остановка кампании"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autostrategy/v1/campaign/stop",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutostrategyApiStopAutostrategyCampaignResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autostrategy.stop_autostrategy_campaign (POST /autostrategy/v1/campaign/stop)",
                payload=payload,
                details={
                    "slug": "autostrategy",
                    "operation_id": "stopAutostrategyCampaign",
                    "python_method": "stop_autostrategy_campaign",
                    "http_method": "POST",
                    "path": "/autostrategy/v1/campaign/stop",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_autostrategy_campaigns(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutostrategyApiGetAutostrategyCampaignsResponse:
        """Получение списка кампаний"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autostrategy/v1/campaigns",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutostrategyApiGetAutostrategyCampaignsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autostrategy.get_autostrategy_campaigns (POST /autostrategy/v1/campaigns)",
                payload=payload,
                details={
                    "slug": "autostrategy",
                    "operation_id": "getAutostrategyCampaigns",
                    "python_method": "get_autostrategy_campaigns",
                    "http_method": "POST",
                    "path": "/autostrategy/v1/campaigns",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_autostrategy_stat(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AutostrategyApiGetAutostrategyStatResponse:
        """Получение статистики по кампании"""
        payload = await self._transport.request(
            method="POST",
            path_template="/autostrategy/v1/stat",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AutostrategyApiGetAutostrategyStatResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for autostrategy.get_autostrategy_stat (POST /autostrategy/v1/stat)",
                payload=payload,
                details={
                    "slug": "autostrategy",
                    "operation_id": "getAutostrategyStat",
                    "python_method": "get_autostrategy_stat",
                    "http_method": "POST",
                    "path": "/autostrategy/v1/stat",
                    "errors": exc.errors(),
                },
            ) from exc

__all__ = ["AutostrategyApi"]
