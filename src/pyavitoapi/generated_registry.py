"""Generated slug registry."""

from __future__ import annotations

from typing import Any

from pyavitoapi.generated.accounts_hierarchy import AccountsHierarchyApi
from pyavitoapi.generated.auction import AuctionApi
from pyavitoapi.generated.auth import AuthApi
from pyavitoapi.generated.autoload import AutoloadApi
from pyavitoapi.generated.autostrategy import AutostrategyApi
from pyavitoapi.generated.autoteka import AutotekaApi
from pyavitoapi.generated.calltracking import CalltrackingApi
from pyavitoapi.generated.cpa import CpaApi
from pyavitoapi.generated.cpxpromo import CpxpromoApi
from pyavitoapi.generated.delivery_sandbox import DeliverySandboxApi
from pyavitoapi.generated.item import ItemApi
from pyavitoapi.generated.job import JobApi
from pyavitoapi.generated.messenger import MessengerApi
from pyavitoapi.generated.order_management import OrderManagementApi
from pyavitoapi.generated.promotion import PromotionApi
from pyavitoapi.generated.ratings import RatingsApi
from pyavitoapi.generated.realty_reports import RealtyReportsApi
from pyavitoapi.generated.sbc_gateway import SbcGatewayApi
from pyavitoapi.generated.stock_management import StockManagementApi
from pyavitoapi.generated.str import StrApi
from pyavitoapi.generated.tariff import TariffApi
from pyavitoapi.generated.trxpromo import TrxpromoApi
from pyavitoapi.generated.user import UserApi

REGISTRY: dict[str, type[Any]] = {
    "accounts-hierarchy": AccountsHierarchyApi,
    "auction": AuctionApi,
    "auth": AuthApi,
    "autoload": AutoloadApi,
    "autostrategy": AutostrategyApi,
    "autoteka": AutotekaApi,
    "calltracking": CalltrackingApi,
    "cpa": CpaApi,
    "cpxpromo": CpxpromoApi,
    "delivery-sandbox": DeliverySandboxApi,
    "item": ItemApi,
    "job": JobApi,
    "messenger": MessengerApi,
    "order-management": OrderManagementApi,
    "promotion": PromotionApi,
    "ratings": RatingsApi,
    "realty-reports": RealtyReportsApi,
    "sbc-gateway": SbcGatewayApi,
    "stock-management": StockManagementApi,
    "str": StrApi,
    "tariff": TariffApi,
    "trxpromo": TrxpromoApi,
    "user": UserApi,
}
