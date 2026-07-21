"""Generated API module for slug: avito-promo."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.avito_promo import AvitoPromoApiAgencyBalanceResponse, AvitoPromoApiAgencyClientsResponse, AvitoPromoApiAgencyClientsTargetCreateResponse, AvitoPromoApiAgencyClientsTargetResultResponse, AvitoPromoApiAgencyFinancesBalanceResponse, AvitoPromoApiAgencyFinancesTransactionsHistoryResponse, AvitoPromoApiAgencyTransactionResponse, AvitoPromoApiAgencyTransactionsResponse, AvitoPromoApiAgencyUsersInviteSendResponse, AvitoPromoApiAgencyUsersInviteStatusResponse, AvitoPromoApiAgencyUsersVerificationStatusResponse, AvitoPromoApiStatsAccountsItemsResponse, AvitoPromoApiStatsAccountsSpendingsResponse


class AvitoPromoApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def agency_balance(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AvitoPromoApiAgencyBalanceResponse:
        """Перевод средств на счёт клиента"""
        payload = await self._transport.request(
            method="POST",
            path_template="/agency/balance",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AvitoPromoApiAgencyBalanceResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for avito-promo.agency_balance (POST /agency/balance)",
                payload=payload,
                details={
                    "slug": "avito-promo",
                    "operation_id": "agencyBalance",
                    "python_method": "agency_balance",
                    "http_method": "POST",
                    "path": "/agency/balance",
                    "errors": exc.errors(),
                },
            ) from exc

    async def agency_transactions(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AvitoPromoApiAgencyTransactionsResponse:
        """Получение списка незавершённых транзакций"""
        payload = await self._transport.request(
            method="GET",
            path_template="/agency/transactions",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AvitoPromoApiAgencyTransactionsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for avito-promo.agency_transactions (GET /agency/transactions)",
                payload=payload,
                details={
                    "slug": "avito-promo",
                    "operation_id": "agencyTransactions",
                    "python_method": "agency_transactions",
                    "http_method": "GET",
                    "path": "/agency/transactions",
                    "errors": exc.errors(),
                },
            ) from exc

    async def agency_transaction(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AvitoPromoApiAgencyTransactionResponse:
        """Получение информации о транзакции"""
        payload = await self._transport.request(
            method="GET",
            path_template="/agency/transactions/{transaction_id}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AvitoPromoApiAgencyTransactionResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for avito-promo.agency_transaction (GET /agency/transactions/{transaction_id})",
                payload=payload,
                details={
                    "slug": "avito-promo",
                    "operation_id": "agencyTransaction",
                    "python_method": "agency_transaction",
                    "http_method": "GET",
                    "path": "/agency/transactions/{transaction_id}",
                    "errors": exc.errors(),
                },
            ) from exc

    async def agency_clients(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AvitoPromoApiAgencyClientsResponse:
        """Получение списка клиентов"""
        payload = await self._transport.request(
            method="POST",
            path_template="/api/1/agency/clients",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AvitoPromoApiAgencyClientsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for avito-promo.agency_clients (POST /api/1/agency/clients)",
                payload=payload,
                details={
                    "slug": "avito-promo",
                    "operation_id": "agencyClients",
                    "python_method": "agency_clients",
                    "http_method": "POST",
                    "path": "/api/1/agency/clients",
                    "errors": exc.errors(),
                },
            ) from exc

    async def agency_clients_target_create(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AvitoPromoApiAgencyClientsTargetCreateResponse:
        """Создание задачи на проверку ИНН клиентов"""
        payload = await self._transport.request(
            method="POST",
            path_template="/api/1/agency/clients/target/create",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AvitoPromoApiAgencyClientsTargetCreateResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for avito-promo.agency_clients_target_create (POST /api/1/agency/clients/target/create)",
                payload=payload,
                details={
                    "slug": "avito-promo",
                    "operation_id": "agencyClientsTargetCreate",
                    "python_method": "agency_clients_target_create",
                    "http_method": "POST",
                    "path": "/api/1/agency/clients/target/create",
                    "errors": exc.errors(),
                },
            ) from exc

    async def agency_clients_target_result(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AvitoPromoApiAgencyClientsTargetResultResponse:
        """Получение результата проверки ИНН клиентов"""
        payload = await self._transport.request(
            method="POST",
            path_template="/api/1/agency/clients/target/result",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AvitoPromoApiAgencyClientsTargetResultResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for avito-promo.agency_clients_target_result (POST /api/1/agency/clients/target/result)",
                payload=payload,
                details={
                    "slug": "avito-promo",
                    "operation_id": "agencyClientsTargetResult",
                    "python_method": "agency_clients_target_result",
                    "http_method": "POST",
                    "path": "/api/1/agency/clients/target/result",
                    "errors": exc.errors(),
                },
            ) from exc

    async def agency_finances_balance(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AvitoPromoApiAgencyFinancesBalanceResponse:
        """Получение баланса агентства"""
        payload = await self._transport.request(
            method="GET",
            path_template="/api/1/agency/finances/balance",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AvitoPromoApiAgencyFinancesBalanceResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for avito-promo.agency_finances_balance (GET /api/1/agency/finances/balance)",
                payload=payload,
                details={
                    "slug": "avito-promo",
                    "operation_id": "agencyFinancesBalance",
                    "python_method": "agency_finances_balance",
                    "http_method": "GET",
                    "path": "/api/1/agency/finances/balance",
                    "errors": exc.errors(),
                },
            ) from exc

    async def agency_finances_transactions_history(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AvitoPromoApiAgencyFinancesTransactionsHistoryResponse:
        """Получение всех операций с балансом агентства"""
        payload = await self._transport.request(
            method="POST",
            path_template="/api/1/agency/finances/transactionsHistory",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AvitoPromoApiAgencyFinancesTransactionsHistoryResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for avito-promo.agency_finances_transactions_history (POST /api/1/agency/finances/transactionsHistory)",
                payload=payload,
                details={
                    "slug": "avito-promo",
                    "operation_id": "agencyFinancesTransactionsHistory",
                    "python_method": "agency_finances_transactions_history",
                    "http_method": "POST",
                    "path": "/api/1/agency/finances/transactionsHistory",
                    "errors": exc.errors(),
                },
            ) from exc

    async def agency_users_invite_send(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AvitoPromoApiAgencyUsersInviteSendResponse:
        """Отправка приглашения нового клиента"""
        payload = await self._transport.request(
            method="POST",
            path_template="/api/1/agency/users/invite/send",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AvitoPromoApiAgencyUsersInviteSendResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for avito-promo.agency_users_invite_send (POST /api/1/agency/users/invite/send)",
                payload=payload,
                details={
                    "slug": "avito-promo",
                    "operation_id": "agencyUsersInviteSend",
                    "python_method": "agency_users_invite_send",
                    "http_method": "POST",
                    "path": "/api/1/agency/users/invite/send",
                    "errors": exc.errors(),
                },
            ) from exc

    async def agency_users_invite_status(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AvitoPromoApiAgencyUsersInviteStatusResponse:
        """Получение статуса приглашения нового клиента"""
        payload = await self._transport.request(
            method="POST",
            path_template="/api/1/agency/users/invite/status",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AvitoPromoApiAgencyUsersInviteStatusResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for avito-promo.agency_users_invite_status (POST /api/1/agency/users/invite/status)",
                payload=payload,
                details={
                    "slug": "avito-promo",
                    "operation_id": "agencyUsersInviteStatus",
                    "python_method": "agency_users_invite_status",
                    "http_method": "POST",
                    "path": "/api/1/agency/users/invite/status",
                    "errors": exc.errors(),
                },
            ) from exc

    async def agency_users_verification_status(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AvitoPromoApiAgencyUsersVerificationStatusResponse:
        """Получение статуса верификации нового клиента"""
        payload = await self._transport.request(
            method="POST",
            path_template="/api/1/agency/users/verificationStatus",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AvitoPromoApiAgencyUsersVerificationStatusResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for avito-promo.agency_users_verification_status (POST /api/1/agency/users/verificationStatus)",
                payload=payload,
                details={
                    "slug": "avito-promo",
                    "operation_id": "agencyUsersVerificationStatus",
                    "python_method": "agency_users_verification_status",
                    "http_method": "POST",
                    "path": "/api/1/agency/users/verificationStatus",
                    "errors": exc.errors(),
                },
            ) from exc

    async def stats_accounts_items(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AvitoPromoApiStatsAccountsItemsResponse:
        """Получение статистических показателей клиента"""
        payload = await self._transport.request(
            method="POST",
            path_template="/stats/v2/accounts/{user_id}/items",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AvitoPromoApiStatsAccountsItemsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for avito-promo.stats_accounts_items (POST /stats/v2/accounts/{user_id}/items)",
                payload=payload,
                details={
                    "slug": "avito-promo",
                    "operation_id": "statsAccountsItems",
                    "python_method": "stats_accounts_items",
                    "http_method": "POST",
                    "path": "/stats/v2/accounts/{user_id}/items",
                    "errors": exc.errors(),
                },
            ) from exc

    async def stats_accounts_spendings(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> AvitoPromoApiStatsAccountsSpendingsResponse:
        """Получение статистики расходов клиента"""
        payload = await self._transport.request(
            method="POST",
            path_template="/stats/v2/accounts/{user_id}/spendings",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return AvitoPromoApiStatsAccountsSpendingsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for avito-promo.stats_accounts_spendings (POST /stats/v2/accounts/{user_id}/spendings)",
                payload=payload,
                details={
                    "slug": "avito-promo",
                    "operation_id": "statsAccountsSpendings",
                    "python_method": "stats_accounts_spendings",
                    "http_method": "POST",
                    "path": "/stats/v2/accounts/{user_id}/spendings",
                    "errors": exc.errors(),
                },
            ) from exc

__all__ = ["AvitoPromoApi"]
