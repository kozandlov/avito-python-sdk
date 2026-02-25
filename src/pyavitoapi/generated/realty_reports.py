"""Generated API module for slug: realty-reports."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.realty_reports import RealtyReportsApiCreateReportForClassifiedResponse, RealtyReportsApiMarketPriceCorrespondenceV1Response


class RealtyReportsApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def market_price_correspondence_v1(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> RealtyReportsApiMarketPriceCorrespondenceV1Response:
        """Получение соответствия переданной цены рыночной цене"""
        payload = await self._transport.request(
            method="GET",
            path_template="/realty/v1/marketPriceCorrespondence/{itemId}/{price}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return RealtyReportsApiMarketPriceCorrespondenceV1Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for realty-reports.market_price_correspondence_v1 (GET /realty/v1/marketPriceCorrespondence/{itemId}/{price})",
                payload=payload,
                details={
                    "slug": "realty-reports",
                    "operation_id": "market_price_correspondence_v1",
                    "python_method": "market_price_correspondence_v1",
                    "http_method": "GET",
                    "path": "/realty/v1/marketPriceCorrespondence/{itemId}/{price}",
                    "errors": exc.errors(),
                },
            ) from exc

    async def create_report_for_classified(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> RealtyReportsApiCreateReportForClassifiedResponse:
        """Получение аналитического отчета по недвижимости"""
        payload = await self._transport.request(
            method="POST",
            path_template="/realty/v1/report/create/{itemId}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return RealtyReportsApiCreateReportForClassifiedResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for realty-reports.create_report_for_classified (POST /realty/v1/report/create/{itemId})",
                payload=payload,
                details={
                    "slug": "realty-reports",
                    "operation_id": "CreateReportForClassified",
                    "python_method": "create_report_for_classified",
                    "http_method": "POST",
                    "path": "/realty/v1/report/create/{itemId}",
                    "errors": exc.errors(),
                },
            ) from exc

__all__ = ["RealtyReportsApi"]
