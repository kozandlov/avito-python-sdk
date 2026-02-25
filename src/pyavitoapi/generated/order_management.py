"""Generated API module for slug: order-management."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.order_management import OrderManagementApiAcceptReturnOrderResponse, OrderManagementApiApplyTransitionResponse, OrderManagementApiCheckConfirmationCodeResponse, OrderManagementApiCncSetDetailsResponse, OrderManagementApiGenerateLabelsExtendedResponse, OrderManagementApiGenerateLabelsResponse, OrderManagementApiGetCourierDeliveryRangeResponse, OrderManagementApiGetOrdersResponse, OrderManagementApiMarkingsResponse, OrderManagementApiSetCourierDeliveryRangeResponse, OrderManagementApiSetOrderTrackingNumberResponse


class OrderManagementApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def markings(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> OrderManagementApiMarkingsResponse:
        """Передача честного знака"""
        payload = await self._transport.request(
            method="POST",
            path_template="/order-management/1/markings",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return OrderManagementApiMarkingsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for order-management.markings (POST /order-management/1/markings)",
                payload=payload,
                details={
                    "slug": "order-management",
                    "operation_id": "markings",
                    "python_method": "markings",
                    "http_method": "POST",
                    "path": "/order-management/1/markings",
                    "errors": exc.errors(),
                },
            ) from exc

    async def accept_return_order(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> OrderManagementApiAcceptReturnOrderResponse:
        """Выбор отделения отделения Почты России для получения возврата"""
        payload = await self._transport.request(
            method="POST",
            path_template="/order-management/1/order/acceptReturnOrder",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return OrderManagementApiAcceptReturnOrderResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for order-management.accept_return_order (POST /order-management/1/order/acceptReturnOrder)",
                payload=payload,
                details={
                    "slug": "order-management",
                    "operation_id": "acceptReturnOrder",
                    "python_method": "accept_return_order",
                    "http_method": "POST",
                    "path": "/order-management/1/order/acceptReturnOrder",
                    "errors": exc.errors(),
                },
            ) from exc

    async def apply_transition(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> OrderManagementApiApplyTransitionResponse:
        """Изменение статуса заказа"""
        payload = await self._transport.request(
            method="POST",
            path_template="/order-management/1/order/applyTransition",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return OrderManagementApiApplyTransitionResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for order-management.apply_transition (POST /order-management/1/order/applyTransition)",
                payload=payload,
                details={
                    "slug": "order-management",
                    "operation_id": "applyTransition",
                    "python_method": "apply_transition",
                    "http_method": "POST",
                    "path": "/order-management/1/order/applyTransition",
                    "errors": exc.errors(),
                },
            ) from exc

    async def check_confirmation_code(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> OrderManagementApiCheckConfirmationCodeResponse:
        """Метод для проверки кода подтверждения заказа."""
        payload = await self._transport.request(
            method="POST",
            path_template="/order-management/1/order/checkConfirmationCode",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return OrderManagementApiCheckConfirmationCodeResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for order-management.check_confirmation_code (POST /order-management/1/order/checkConfirmationCode)",
                payload=payload,
                details={
                    "slug": "order-management",
                    "operation_id": "checkConfirmationCode",
                    "python_method": "check_confirmation_code",
                    "http_method": "POST",
                    "path": "/order-management/1/order/checkConfirmationCode",
                    "errors": exc.errors(),
                },
            ) from exc

    async def cnc_set_details(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> OrderManagementApiCncSetDetailsResponse:
        """Метод для подготовки заказа с самовывозом"""
        payload = await self._transport.request(
            method="POST",
            path_template="/order-management/1/order/cncSetDetails",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return OrderManagementApiCncSetDetailsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for order-management.cnc_set_details (POST /order-management/1/order/cncSetDetails)",
                payload=payload,
                details={
                    "slug": "order-management",
                    "operation_id": "cncSetDetails",
                    "python_method": "cnc_set_details",
                    "http_method": "POST",
                    "path": "/order-management/1/order/cncSetDetails",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_courier_delivery_range(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> OrderManagementApiGetCourierDeliveryRangeResponse:
        """Метод получения доступных временных промежутков приезда курьера"""
        payload = await self._transport.request(
            method="GET",
            path_template="/order-management/1/order/getCourierDeliveryRange",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return OrderManagementApiGetCourierDeliveryRangeResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for order-management.get_courier_delivery_range (GET /order-management/1/order/getCourierDeliveryRange)",
                payload=payload,
                details={
                    "slug": "order-management",
                    "operation_id": "getCourierDeliveryRange",
                    "python_method": "get_courier_delivery_range",
                    "http_method": "GET",
                    "path": "/order-management/1/order/getCourierDeliveryRange",
                    "errors": exc.errors(),
                },
            ) from exc

    async def set_courier_delivery_range(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> OrderManagementApiSetCourierDeliveryRangeResponse:
        """Метод выбора определённого доступного временного промежутка для приезда курьера"""
        payload = await self._transport.request(
            method="POST",
            path_template="/order-management/1/order/setCourierDeliveryRange",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return OrderManagementApiSetCourierDeliveryRangeResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for order-management.set_courier_delivery_range (POST /order-management/1/order/setCourierDeliveryRange)",
                payload=payload,
                details={
                    "slug": "order-management",
                    "operation_id": "setCourierDeliveryRange",
                    "python_method": "set_courier_delivery_range",
                    "http_method": "POST",
                    "path": "/order-management/1/order/setCourierDeliveryRange",
                    "errors": exc.errors(),
                },
            ) from exc

    async def set_order_tracking_number(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> OrderManagementApiSetOrderTrackingNumberResponse:
        """Передача трек-номера"""
        payload = await self._transport.request(
            method="POST",
            path_template="/order-management/1/order/setTrackingNumber",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return OrderManagementApiSetOrderTrackingNumberResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for order-management.set_order_tracking_number (POST /order-management/1/order/setTrackingNumber)",
                payload=payload,
                details={
                    "slug": "order-management",
                    "operation_id": "setOrderTrackingNumber",
                    "python_method": "set_order_tracking_number",
                    "http_method": "POST",
                    "path": "/order-management/1/order/setTrackingNumber",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_orders(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> OrderManagementApiGetOrdersResponse:
        """Получение информации о заказах"""
        payload = await self._transport.request(
            method="GET",
            path_template="/order-management/1/orders",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return OrderManagementApiGetOrdersResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for order-management.get_orders (GET /order-management/1/orders)",
                payload=payload,
                details={
                    "slug": "order-management",
                    "operation_id": "getOrders",
                    "python_method": "get_orders",
                    "http_method": "GET",
                    "path": "/order-management/1/orders",
                    "errors": exc.errors(),
                },
            ) from exc

    async def generate_labels(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> OrderManagementApiGenerateLabelsResponse:
        """Создать задачу на генерацию этикеток (до 100)."""
        payload = await self._transport.request(
            method="POST",
            path_template="/order-management/1/orders/labels",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return OrderManagementApiGenerateLabelsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for order-management.generate_labels (POST /order-management/1/orders/labels)",
                payload=payload,
                details={
                    "slug": "order-management",
                    "operation_id": "generateLabels",
                    "python_method": "generate_labels",
                    "http_method": "POST",
                    "path": "/order-management/1/orders/labels",
                    "errors": exc.errors(),
                },
            ) from exc

    async def generate_labels_extended(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> OrderManagementApiGenerateLabelsExtendedResponse:
        """Создать задачу на генерацию этикеток (до 1000)."""
        payload = await self._transport.request(
            method="POST",
            path_template="/order-management/1/orders/labels/extended",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return OrderManagementApiGenerateLabelsExtendedResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for order-management.generate_labels_extended (POST /order-management/1/orders/labels/extended)",
                payload=payload,
                details={
                    "slug": "order-management",
                    "operation_id": "generateLabelsExtended",
                    "python_method": "generate_labels_extended",
                    "http_method": "POST",
                    "path": "/order-management/1/orders/labels/extended",
                    "errors": exc.errors(),
                },
            ) from exc

    async def download_label(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:
        """Скачать сгенерированный PDF-файл (этикетку)."""
        payload = await self._transport.request(
            method="GET",
            path_template="/order-management/1/orders/labels/{taskID}/download",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        return None

__all__ = ["OrderManagementApi"]
