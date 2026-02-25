"""Generated API module for slug: ratings."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.ratings import RatingsApiCreateReviewAnswerV1Response, RatingsApiGetRatingsInfoV1Response, RatingsApiGetReviewsV1Response, RatingsApiRemoveReviewAnswerV1Response


class RatingsApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def create_review_answer_v1(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> RatingsApiCreateReviewAnswerV1Response:
        """Отправка ответа на отзыв"""
        payload = await self._transport.request(
            method="POST",
            path_template="/ratings/v1/answers",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return RatingsApiCreateReviewAnswerV1Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ratings.create_review_answer_v1 (POST /ratings/v1/answers)",
                payload=payload,
                details={
                    "slug": "ratings",
                    "operation_id": "createReviewAnswerV1",
                    "python_method": "create_review_answer_v1",
                    "http_method": "POST",
                    "path": "/ratings/v1/answers",
                    "errors": exc.errors(),
                },
            ) from exc

    async def remove_review_answer_v1(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> RatingsApiRemoveReviewAnswerV1Response:
        """Запрос на удаление ответа на отзыв"""
        payload = await self._transport.request(
            method="DELETE",
            path_template="/ratings/v1/answers/{answer_id}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return RatingsApiRemoveReviewAnswerV1Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ratings.remove_review_answer_v1 (DELETE /ratings/v1/answers/{answer_id})",
                payload=payload,
                details={
                    "slug": "ratings",
                    "operation_id": "removeReviewAnswerV1",
                    "python_method": "remove_review_answer_v1",
                    "http_method": "DELETE",
                    "path": "/ratings/v1/answers/{answer_id}",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_ratings_info_v1(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> RatingsApiGetRatingsInfoV1Response:
        """Получение информации о рейтинге пользователя"""
        payload = await self._transport.request(
            method="GET",
            path_template="/ratings/v1/info",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return RatingsApiGetRatingsInfoV1Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ratings.get_ratings_info_v1 (GET /ratings/v1/info)",
                payload=payload,
                details={
                    "slug": "ratings",
                    "operation_id": "getRatingsInfoV1",
                    "python_method": "get_ratings_info_v1",
                    "http_method": "GET",
                    "path": "/ratings/v1/info",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_reviews_v1(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> RatingsApiGetReviewsV1Response:
        """Получение списка активных отзывов на пользователя с пагинацией"""
        payload = await self._transport.request(
            method="GET",
            path_template="/ratings/v1/reviews",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return RatingsApiGetReviewsV1Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ratings.get_reviews_v1 (GET /ratings/v1/reviews)",
                payload=payload,
                details={
                    "slug": "ratings",
                    "operation_id": "getReviewsV1",
                    "python_method": "get_reviews_v1",
                    "http_method": "GET",
                    "path": "/ratings/v1/reviews",
                    "errors": exc.errors(),
                },
            ) from exc

__all__ = ["RatingsApi"]
