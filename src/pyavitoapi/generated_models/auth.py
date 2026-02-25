"""Generated response models for slug: auth."""

from __future__ import annotations

from typing import Any
from pydantic import BaseModel, ConfigDict, ValidationError

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class AuthApiGetAccessTokenResponse(_BaseModel):
    access_token: str = None
    expires_in: float = None
    token_type: str = None

__all__ = ['AuthApiGetAccessTokenResponse']
