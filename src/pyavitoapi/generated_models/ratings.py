"""Generated response models for slug: ratings."""

from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, ValidationError, Field

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class RatingsApiCreateReviewAnswerV1Response(_BaseModel):
    created_at: int = Field(alias='createdAt')
    id: int

class RatingsApiRemoveReviewAnswerV1Response(_BaseModel):
    success: bool

class Rating(_BaseModel):
    reviews_count: int = Field(alias='reviewsCount')
    reviews_with_score_count: int = Field(alias='reviewsWithScoreCount')
    score: float

class RatingsApiGetRatingsInfoV1Response(_BaseModel):
    is_enabled: bool = Field(alias='isEnabled')
    rating: Rating = None

class RejectReason(_BaseModel):
    id: int
    title: str

class ReviewAnswer(_BaseModel):
    created_at: int = Field(alias='createdAt')
    id: int
    reject_reasons: list[RejectReason] = None
    status: Literal['moderation', 'published', 'rejected']
    text: str

class ReviewExtraParamsModel1(_BaseModel):
    vin: str = None

class ReviewImageSize(_BaseModel):
    size: str
    url: str

class ReviewImage(_BaseModel):
    number: int
    sizes: list[ReviewImageSize]

class ReviewItem(_BaseModel):
    id: int = None
    title: str = None

class ReviewSender(_BaseModel):
    name: str

class Review(_BaseModel):
    answer: ReviewAnswer = None
    can_answer: bool = Field(alias='canAnswer')
    created_at: int = Field(alias='createdAt')
    extra_params: ReviewExtraParamsModel1 = Field(default=None, alias='extraParams')
    id: int
    images: list[ReviewImage] = None
    item: ReviewItem = None
    score: int
    sender: ReviewSender = None
    stage: Literal['done', 'fell_through', 'not_agree', 'not_communicate']
    text: str
    used_in_score: bool = Field(alias='usedInScore')

class RatingsApiGetReviewsV1Response(_BaseModel):
    reviews: list[Review]
    total: int

__all__ = ['RatingsApiCreateReviewAnswerV1Response', 'RatingsApiRemoveReviewAnswerV1Response', 'Rating', 'RatingsApiGetRatingsInfoV1Response', 'RejectReason', 'ReviewAnswer', 'ReviewExtraParamsModel1', 'ReviewImageSize', 'ReviewImage', 'ReviewItem', 'ReviewSender', 'Review', 'RatingsApiGetReviewsV1Response']
