"""Generated API module for slug: ads."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.ads import AdsApiV1AddUserResponse, AdsApiV1ChangeBudgetResponse, AdsApiV1ChangePriceResponse, AdsApiV1CreateAccountResponse, AdsApiV1CreateAdvertiserResponse, AdsApiV1CreateContractResponse, AdsApiV1CreateNonPayerAccountResponse, AdsApiV1DeleteUserResponse, AdsApiV1GetAccountBalanceByIdResponse, AdsApiV1GetAccountByIdResponse, AdsApiV1GetAdvertisersListResponse, AdsApiV1GetCampaignStatisticResponse, AdsApiV1GetCampaignsListResponse, AdsApiV1GetChildAccountsListResponse, AdsApiV1GetChildAccountsWithBalancesListResponse, AdsApiV1GetContractsListResponse, AdsApiV1GetCreativesListResponse, AdsApiV1GetCreativesStatisticResponse, AdsApiV1GetGroupsListResponse, AdsApiV1GetGroupsStatisticResponse, AdsApiV1GetUsersListByAccountResponse, AdsApiV1SetUserRoleResponse, AdsApiV1TransferBonusResponse, AdsApiV1TransferFundsResponse


class AdsApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def v1_get_account_by_id(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1GetAccountByIdResponse:
        """Получить аккаунт по ID"""
        payload = await self._transport.request(
            method="GET",
            path_template="/ads/v1/account/{accountID}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1GetAccountByIdResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_get_account_by_id (GET /ads/v1/account/{accountID})",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1GetAccountByID",
                    "python_method": "v1_get_account_by_id",
                    "http_method": "GET",
                    "path": "/ads/v1/account/{accountID}",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_create_account(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1CreateAccountResponse:
        """Создать аккаунт в песочнице"""
        payload = await self._transport.request(
            method="POST",
            path_template="/ads/v1/account/{accountID}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1CreateAccountResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_create_account (POST /ads/v1/account/{accountID})",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1CreateAccount",
                    "python_method": "v1_create_account",
                    "http_method": "POST",
                    "path": "/ads/v1/account/{accountID}",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_add_user(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1AddUserResponse:
        """Добавить пользователя в аккаунт"""
        payload = await self._transport.request(
            method="POST",
            path_template="/ads/v1/account/{accountID}/add-user",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1AddUserResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_add_user (POST /ads/v1/account/{accountID}/add-user)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1AddUser",
                    "python_method": "v1_add_user",
                    "http_method": "POST",
                    "path": "/ads/v1/account/{accountID}/add-user",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_get_advertisers_list(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1GetAdvertisersListResponse:
        """Получить список рекламодателей по фильтрам"""
        payload = await self._transport.request(
            method="POST",
            path_template="/ads/v1/account/{accountID}/advertisers",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1GetAdvertisersListResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_get_advertisers_list (POST /ads/v1/account/{accountID}/advertisers)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1GetAdvertisersList",
                    "python_method": "v1_get_advertisers_list",
                    "http_method": "POST",
                    "path": "/ads/v1/account/{accountID}/advertisers",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_get_account_balance_by_id(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1GetAccountBalanceByIdResponse:
        """Получить баланс аккаунта по ID"""
        payload = await self._transport.request(
            method="GET",
            path_template="/ads/v1/account/{accountID}/balance",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1GetAccountBalanceByIdResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_get_account_balance_by_id (GET /ads/v1/account/{accountID}/balance)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1GetAccountBalanceByID",
                    "python_method": "v1_get_account_balance_by_id",
                    "http_method": "GET",
                    "path": "/ads/v1/account/{accountID}/balance",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_transfer_bonus(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1TransferBonusResponse:
        """Перевод бонусов между аккаунтом родителем и дочерними на одном договоре"""
        payload = await self._transport.request(
            method="POST",
            path_template="/ads/v1/account/{accountID}/bonus-transfer",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1TransferBonusResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_transfer_bonus (POST /ads/v1/account/{accountID}/bonus-transfer)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1TransferBonus",
                    "python_method": "v1_transfer_bonus",
                    "http_method": "POST",
                    "path": "/ads/v1/account/{accountID}/bonus-transfer",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_get_campaigns_list(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1GetCampaignsListResponse:
        """Получить список кампаний по фильтрам"""
        payload = await self._transport.request(
            method="POST",
            path_template="/ads/v1/account/{accountID}/campaigns",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1GetCampaignsListResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_get_campaigns_list (POST /ads/v1/account/{accountID}/campaigns)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1GetCampaignsList",
                    "python_method": "v1_get_campaigns_list",
                    "http_method": "POST",
                    "path": "/ads/v1/account/{accountID}/campaigns",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_get_creatives_statistic(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1GetCreativesStatisticResponse:
        """Получить статистику по креативам кампании"""
        payload = await self._transport.request(
            method="POST",
            path_template="/ads/v1/account/{accountID}/campaigns/{campaignID}/creatives/stats",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1GetCreativesStatisticResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_get_creatives_statistic (POST /ads/v1/account/{accountID}/campaigns/{campaignID}/creatives/stats)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1GetCreativesStatistic",
                    "python_method": "v1_get_creatives_statistic",
                    "http_method": "POST",
                    "path": "/ads/v1/account/{accountID}/campaigns/{campaignID}/creatives/stats",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_get_groups_statistic(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1GetGroupsStatisticResponse:
        """Получить статистику по группам кампании"""
        payload = await self._transport.request(
            method="POST",
            path_template="/ads/v1/account/{accountID}/campaigns/{campaignID}/groups/stats",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1GetGroupsStatisticResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_get_groups_statistic (POST /ads/v1/account/{accountID}/campaigns/{campaignID}/groups/stats)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1GetGroupsStatistic",
                    "python_method": "v1_get_groups_statistic",
                    "http_method": "POST",
                    "path": "/ads/v1/account/{accountID}/campaigns/{campaignID}/groups/stats",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_get_campaign_statistic(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1GetCampaignStatisticResponse:
        """Получить статистику по кампании"""
        payload = await self._transport.request(
            method="POST",
            path_template="/ads/v1/account/{accountID}/campaigns/{campaignID}/stats",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1GetCampaignStatisticResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_get_campaign_statistic (POST /ads/v1/account/{accountID}/campaigns/{campaignID}/stats)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1GetCampaignStatistic",
                    "python_method": "v1_get_campaign_statistic",
                    "http_method": "POST",
                    "path": "/ads/v1/account/{accountID}/campaigns/{campaignID}/stats",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_get_child_accounts_list(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1GetChildAccountsListResponse:
        """Получить список дочерних аккаунтов"""
        payload = await self._transport.request(
            method="GET",
            path_template="/ads/v1/account/{accountID}/children",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1GetChildAccountsListResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_get_child_accounts_list (GET /ads/v1/account/{accountID}/children)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1GetChildAccountsList",
                    "python_method": "v1_get_child_accounts_list",
                    "http_method": "GET",
                    "path": "/ads/v1/account/{accountID}/children",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_get_child_accounts_with_balances_list(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1GetChildAccountsWithBalancesListResponse:
        """Получить список дочерних аккаунтов с балансами"""
        payload = await self._transport.request(
            method="GET",
            path_template="/ads/v1/account/{accountID}/children-with-balances",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1GetChildAccountsWithBalancesListResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_get_child_accounts_with_balances_list (GET /ads/v1/account/{accountID}/children-with-balances)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1GetChildAccountsWithBalancesList",
                    "python_method": "v1_get_child_accounts_with_balances_list",
                    "http_method": "GET",
                    "path": "/ads/v1/account/{accountID}/children-with-balances",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_get_contracts_list(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1GetContractsListResponse:
        """Получить список договоров по фильтрам"""
        payload = await self._transport.request(
            method="POST",
            path_template="/ads/v1/account/{accountID}/contracts",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1GetContractsListResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_get_contracts_list (POST /ads/v1/account/{accountID}/contracts)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1GetContractsList",
                    "python_method": "v1_get_contracts_list",
                    "http_method": "POST",
                    "path": "/ads/v1/account/{accountID}/contracts",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_create_advertiser(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1CreateAdvertiserResponse:
        """Создать рекламодателя"""
        payload = await self._transport.request(
            method="POST",
            path_template="/ads/v1/account/{accountID}/create-advertiser",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1CreateAdvertiserResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_create_advertiser (POST /ads/v1/account/{accountID}/create-advertiser)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1CreateAdvertiser",
                    "python_method": "v1_create_advertiser",
                    "http_method": "POST",
                    "path": "/ads/v1/account/{accountID}/create-advertiser",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_create_contract(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1CreateContractResponse:
        """Создание изначального договора"""
        payload = await self._transport.request(
            method="POST",
            path_template="/ads/v1/account/{accountID}/create-contract",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1CreateContractResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_create_contract (POST /ads/v1/account/{accountID}/create-contract)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1CreateContract",
                    "python_method": "v1_create_contract",
                    "http_method": "POST",
                    "path": "/ads/v1/account/{accountID}/create-contract",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_create_non_payer_account(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1CreateNonPayerAccountResponse:
        """Создание дочернего аккаунта на договоре родителя"""
        payload = await self._transport.request(
            method="POST",
            path_template="/ads/v1/account/{accountID}/create-nonpayer-child-account",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1CreateNonPayerAccountResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_create_non_payer_account (POST /ads/v1/account/{accountID}/create-nonpayer-child-account)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1CreateNonPayerAccount",
                    "python_method": "v1_create_non_payer_account",
                    "http_method": "POST",
                    "path": "/ads/v1/account/{accountID}/create-nonpayer-child-account",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_get_creatives_list(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1GetCreativesListResponse:
        """Получить список креативов по фильтрам"""
        payload = await self._transport.request(
            method="POST",
            path_template="/ads/v1/account/{accountID}/creatives",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1GetCreativesListResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_get_creatives_list (POST /ads/v1/account/{accountID}/creatives)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1GetCreativesList",
                    "python_method": "v1_get_creatives_list",
                    "http_method": "POST",
                    "path": "/ads/v1/account/{accountID}/creatives",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_delete_user(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1DeleteUserResponse:
        """Удалить пользователя из аккаунта"""
        payload = await self._transport.request(
            method="DELETE",
            path_template="/ads/v1/account/{accountID}/delete-user/{userID}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1DeleteUserResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_delete_user (DELETE /ads/v1/account/{accountID}/delete-user/{userID})",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1DeleteUser",
                    "python_method": "v1_delete_user",
                    "http_method": "DELETE",
                    "path": "/ads/v1/account/{accountID}/delete-user/{userID}",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_transfer_funds(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1TransferFundsResponse:
        """Перевод денег между аккаунтом родителем и дочерними на одном договоре"""
        payload = await self._transport.request(
            method="POST",
            path_template="/ads/v1/account/{accountID}/funds-transfer",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1TransferFundsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_transfer_funds (POST /ads/v1/account/{accountID}/funds-transfer)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1TransferFunds",
                    "python_method": "v1_transfer_funds",
                    "http_method": "POST",
                    "path": "/ads/v1/account/{accountID}/funds-transfer",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_change_budget(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1ChangeBudgetResponse:
        """Изменить бюджет группы"""
        payload = await self._transport.request(
            method="POST",
            path_template="/ads/v1/account/{accountID}/group/{groupID}/change-budget",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1ChangeBudgetResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_change_budget (POST /ads/v1/account/{accountID}/group/{groupID}/change-budget)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1ChangeBudget",
                    "python_method": "v1_change_budget",
                    "http_method": "POST",
                    "path": "/ads/v1/account/{accountID}/group/{groupID}/change-budget",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_change_price(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1ChangePriceResponse:
        """Изменить цену группы"""
        payload = await self._transport.request(
            method="POST",
            path_template="/ads/v1/account/{accountID}/group/{groupID}/change-price",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1ChangePriceResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_change_price (POST /ads/v1/account/{accountID}/group/{groupID}/change-price)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1ChangePrice",
                    "python_method": "v1_change_price",
                    "http_method": "POST",
                    "path": "/ads/v1/account/{accountID}/group/{groupID}/change-price",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_get_groups_list(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1GetGroupsListResponse:
        """Получить список групп по фильтрам"""
        payload = await self._transport.request(
            method="POST",
            path_template="/ads/v1/account/{accountID}/groups",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1GetGroupsListResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_get_groups_list (POST /ads/v1/account/{accountID}/groups)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1GetGroupsList",
                    "python_method": "v1_get_groups_list",
                    "http_method": "POST",
                    "path": "/ads/v1/account/{accountID}/groups",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_set_user_role(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1SetUserRoleResponse:
        """Изменить роль пользователя в аккаунте"""
        payload = await self._transport.request(
            method="POST",
            path_template="/ads/v1/account/{accountID}/set-user-role",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1SetUserRoleResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_set_user_role (POST /ads/v1/account/{accountID}/set-user-role)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1SetUserRole",
                    "python_method": "v1_set_user_role",
                    "http_method": "POST",
                    "path": "/ads/v1/account/{accountID}/set-user-role",
                    "errors": exc.errors(),
                },
            ) from exc

    async def v1_get_users_list_by_account(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AdsApiV1GetUsersListByAccountResponse:
        """Получить список пользователей аккаунта"""
        payload = await self._transport.request(
            method="GET",
            path_template="/ads/v1/account/{accountID}/users",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AdsApiV1GetUsersListByAccountResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for ads.v1_get_users_list_by_account (GET /ads/v1/account/{accountID}/users)",
                payload=payload,
                details={
                    "slug": "ads",
                    "operation_id": "V1GetUsersListByAccount",
                    "python_method": "v1_get_users_list_by_account",
                    "http_method": "GET",
                    "path": "/ads/v1/account/{accountID}/users",
                    "errors": exc.errors(),
                },
            ) from exc

__all__ = ["AdsApi"]
