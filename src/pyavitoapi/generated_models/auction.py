"""Generated response models for slug: auction."""

from __future__ import annotations

from typing import Any
from pydantic import BaseModel, ConfigDict, ValidationError, Field

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class AuctionApiGetUserBidsResponseItemsItemModel1AvailablePricesItemModel2(_BaseModel):
    goodness: int
    price_penny: int = Field(alias='pricePenny')

class AuctionApiGetUserBidsResponseItemsItemModel1(_BaseModel):
    available_prices: list[AuctionApiGetUserBidsResponseItemsItemModel1AvailablePricesItemModel2] = Field(alias='availablePrices')
    expiration_time: str = Field(alias='expirationTime')
    item_id: int = Field(alias='itemID')
    price_penny: int = Field(alias='pricePenny')

class AuctionApiGetUserBidsResponse(_BaseModel):
    items: list[AuctionApiGetUserBidsResponseItemsItemModel1] = None

__all__ = ['AuctionApiGetUserBidsResponseItemsItemModel1AvailablePricesItemModel2', 'AuctionApiGetUserBidsResponseItemsItemModel1', 'AuctionApiGetUserBidsResponse']
