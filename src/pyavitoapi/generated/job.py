"""Generated API module for slug: job."""

from __future__ import annotations

from typing import Any, Optional
from pydantic import ValidationError

from pyavitoapi.transport.errors import AvitoValidationError
from pyavitoapi.transport.http import AvitoHttpTransport
from pyavitoapi.generated_models.job import JobApiApplicationsGetByIdsResponse, JobApiApplicationsGetIdsResponse, JobApiApplicationsSetIsViewedResponse, JobApiApplicationsWebhookDeleteResponse, JobApiApplicationsWebhookGetResponse, JobApiApplicationsWebhookPutResponse, JobApiApplicationsWebhooksGetResponse, JobApiGetDictByIdResponse, JobApiGetDictsResponse, JobApiResumeGetContactsResponse, JobApiResumeGetItemResponse, JobApiResumesGetResponse, JobApiSearchVacancyResponse, JobApiVacanciesGetByIdsResponse, JobApiVacancyCreateResponse, JobApiVacancyCreateV2Response, JobApiVacancyGetItemResponse, JobApiVacancyGetStatusesResponse, JobApiVacancyUpdateV2Response


class JobApi:
    """Generated async API client."""

    def __init__(self, transport: AvitoHttpTransport) -> None:
        self._transport = transport

    async def applications_get_by_ids(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> JobApiApplicationsGetByIdsResponse:
        """Получение списка откликов
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/job/v1/applications/get_by_ids",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return JobApiApplicationsGetByIdsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for job.applications_get_by_ids (POST /job/v1/applications/get_by_ids)",
                payload=payload,
                details={
                    "slug": "job",
                    "operation_id": "applicationsGetByIds",
                    "python_method": "applications_get_by_ids",
                    "http_method": "POST",
                    "path": "/job/v1/applications/get_by_ids",
                    "errors": exc.errors(),
                },
            ) from exc

    async def applications_get_ids(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> JobApiApplicationsGetIdsResponse:
        """Получение идентификаторов откликов
"""
        payload = await self._transport.request(
            method="GET",
            path_template="/job/v1/applications/get_ids",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return JobApiApplicationsGetIdsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for job.applications_get_ids (GET /job/v1/applications/get_ids)",
                payload=payload,
                details={
                    "slug": "job",
                    "operation_id": "applicationsGetIds",
                    "python_method": "applications_get_ids",
                    "http_method": "GET",
                    "path": "/job/v1/applications/get_ids",
                    "errors": exc.errors(),
                },
            ) from exc

    async def applications_set_is_viewed(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> JobApiApplicationsSetIsViewedResponse:
        """Изменение статуса отклика
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/job/v1/applications/set_is_viewed",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return JobApiApplicationsSetIsViewedResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for job.applications_set_is_viewed (POST /job/v1/applications/set_is_viewed)",
                payload=payload,
                details={
                    "slug": "job",
                    "operation_id": "applicationsSetIsViewed",
                    "python_method": "applications_set_is_viewed",
                    "http_method": "POST",
                    "path": "/job/v1/applications/set_is_viewed",
                    "errors": exc.errors(),
                },
            ) from exc

    async def applications_webhook_get(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> JobApiApplicationsWebhookGetResponse:
        """Получение информации о подписках (webhook)
"""
        payload = await self._transport.request(
            method="GET",
            path_template="/job/v1/applications/webhook",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return JobApiApplicationsWebhookGetResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for job.applications_webhook_get (GET /job/v1/applications/webhook)",
                payload=payload,
                details={
                    "slug": "job",
                    "operation_id": "applicationsWebhookGet",
                    "python_method": "applications_webhook_get",
                    "http_method": "GET",
                    "path": "/job/v1/applications/webhook",
                    "errors": exc.errors(),
                },
            ) from exc

    async def applications_webhook_put(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> JobApiApplicationsWebhookPutResponse:
        """Включение уведомлений по откликам (webhook)
"""
        payload = await self._transport.request(
            method="PUT",
            path_template="/job/v1/applications/webhook",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return JobApiApplicationsWebhookPutResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for job.applications_webhook_put (PUT /job/v1/applications/webhook)",
                payload=payload,
                details={
                    "slug": "job",
                    "operation_id": "applicationsWebhookPut",
                    "python_method": "applications_webhook_put",
                    "http_method": "PUT",
                    "path": "/job/v1/applications/webhook",
                    "errors": exc.errors(),
                },
            ) from exc

    async def applications_webhook_delete(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> JobApiApplicationsWebhookDeleteResponse:
        """Отключение уведомлений по откликам (webhook)
"""
        payload = await self._transport.request(
            method="DELETE",
            path_template="/job/v1/applications/webhook",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return JobApiApplicationsWebhookDeleteResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for job.applications_webhook_delete (DELETE /job/v1/applications/webhook)",
                payload=payload,
                details={
                    "slug": "job",
                    "operation_id": "applicationsWebhookDelete",
                    "python_method": "applications_webhook_delete",
                    "http_method": "DELETE",
                    "path": "/job/v1/applications/webhook",
                    "errors": exc.errors(),
                },
            ) from exc

    async def applications_webhooks_get(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> JobApiApplicationsWebhooksGetResponse:
        """Получение списка подписок (webhook)
"""
        payload = await self._transport.request(
            method="GET",
            path_template="/job/v1/applications/webhooks",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return JobApiApplicationsWebhooksGetResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for job.applications_webhooks_get (GET /job/v1/applications/webhooks)",
                payload=payload,
                details={
                    "slug": "job",
                    "operation_id": "applicationsWebhooksGet",
                    "python_method": "applications_webhooks_get",
                    "http_method": "GET",
                    "path": "/job/v1/applications/webhooks",
                    "errors": exc.errors(),
                },
            ) from exc

    async def resumes_get(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> JobApiResumesGetResponse:
        """Поиск резюме
"""
        payload = await self._transport.request(
            method="GET",
            path_template="/job/v1/resumes/",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return JobApiResumesGetResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for job.resumes_get (GET /job/v1/resumes/)",
                payload=payload,
                details={
                    "slug": "job",
                    "operation_id": "resumesGet",
                    "python_method": "resumes_get",
                    "http_method": "GET",
                    "path": "/job/v1/resumes/",
                    "errors": exc.errors(),
                },
            ) from exc

    async def resume_get_contacts(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> JobApiResumeGetContactsResponse:
        """Доступ к контактным данным соискателя
"""
        payload = await self._transport.request(
            method="GET",
            path_template="/job/v1/resumes/{resume_id}/contacts/",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return JobApiResumeGetContactsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for job.resume_get_contacts (GET /job/v1/resumes/{resume_id}/contacts/)",
                payload=payload,
                details={
                    "slug": "job",
                    "operation_id": "resumeGetContacts",
                    "python_method": "resume_get_contacts",
                    "http_method": "GET",
                    "path": "/job/v1/resumes/{resume_id}/contacts/",
                    "errors": exc.errors(),
                },
            ) from exc

    async def vacancy_create(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> JobApiVacancyCreateResponse:
        """Публикация вакансии"""
        payload = await self._transport.request(
            method="POST",
            path_template="/job/v1/vacancies",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return JobApiVacancyCreateResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for job.vacancy_create (POST /job/v1/vacancies)",
                payload=payload,
                details={
                    "slug": "job",
                    "operation_id": "vacancyCreate",
                    "python_method": "vacancy_create",
                    "http_method": "POST",
                    "path": "/job/v1/vacancies",
                    "errors": exc.errors(),
                },
            ) from exc

    async def vacancy_archive(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:
        """Остановка публикации вакансии"""
        payload = await self._transport.request(
            method="PUT",
            path_template="/job/v1/vacancies/archived/{vacancy_id}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        return None

    async def vacancy_update(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:
        """Редактирование вакансии"""
        payload = await self._transport.request(
            method="PUT",
            path_template="/job/v1/vacancies/{vacancy_id}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        return None

    async def vacancy_prolongate(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:
        """Реактивация вакансии"""
        payload = await self._transport.request(
            method="POST",
            path_template="/job/v1/vacancies/{vacancy_id}/prolongate",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        return None

    async def resume_get_item(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> JobApiResumeGetItemResponse:
        """Просмотр данных резюме
"""
        payload = await self._transport.request(
            method="GET",
            path_template="/job/v2/resumes/{resume_id}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return JobApiResumeGetItemResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for job.resume_get_item (GET /job/v2/resumes/{resume_id})",
                payload=payload,
                details={
                    "slug": "job",
                    "operation_id": "resumeGetItem",
                    "python_method": "resume_get_item",
                    "http_method": "GET",
                    "path": "/job/v2/resumes/{resume_id}",
                    "errors": exc.errors(),
                },
            ) from exc

    async def search_vacancy(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> JobApiSearchVacancyResponse:
        """Поиск вакансий
"""
        payload = await self._transport.request(
            method="GET",
            path_template="/job/v2/vacancies",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return JobApiSearchVacancyResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for job.search_vacancy (GET /job/v2/vacancies)",
                payload=payload,
                details={
                    "slug": "job",
                    "operation_id": "searchVacancy",
                    "python_method": "search_vacancy",
                    "http_method": "GET",
                    "path": "/job/v2/vacancies",
                    "errors": exc.errors(),
                },
            ) from exc

    async def vacancy_create_v2(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> JobApiVacancyCreateV2Response:
        """Публикация вакансии v2"""
        payload = await self._transport.request(
            method="POST",
            path_template="/job/v2/vacancies",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return JobApiVacancyCreateV2Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for job.vacancy_create_v2 (POST /job/v2/vacancies)",
                payload=payload,
                details={
                    "slug": "job",
                    "operation_id": "vacancyCreateV2",
                    "python_method": "vacancy_create_v2",
                    "http_method": "POST",
                    "path": "/job/v2/vacancies",
                    "errors": exc.errors(),
                },
            ) from exc

    async def vacancies_get_by_ids(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> JobApiVacanciesGetByIdsResponse:
        """Просмотр данных вакансий
"""
        payload = await self._transport.request(
            method="POST",
            path_template="/job/v2/vacancies/batch",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return JobApiVacanciesGetByIdsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for job.vacancies_get_by_ids (POST /job/v2/vacancies/batch)",
                payload=payload,
                details={
                    "slug": "job",
                    "operation_id": "vacanciesGetByIds",
                    "python_method": "vacancies_get_by_ids",
                    "http_method": "POST",
                    "path": "/job/v2/vacancies/batch",
                    "errors": exc.errors(),
                },
            ) from exc

    async def vacancy_get_statuses(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> JobApiVacancyGetStatusesResponse:
        """Получение статуса публикации вакансий V2"""
        payload = await self._transport.request(
            method="POST",
            path_template="/job/v2/vacancies/statuses",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return JobApiVacancyGetStatusesResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for job.vacancy_get_statuses (POST /job/v2/vacancies/statuses)",
                payload=payload,
                details={
                    "slug": "job",
                    "operation_id": "vacancyGetStatuses",
                    "python_method": "vacancy_get_statuses",
                    "http_method": "POST",
                    "path": "/job/v2/vacancies/statuses",
                    "errors": exc.errors(),
                },
            ) from exc

    async def vacancy_update_v2(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> JobApiVacancyUpdateV2Response:
        """Редактирование вакансии v2"""
        payload = await self._transport.request(
            method="POST",
            path_template="/job/v2/vacancies/update/{vacancy_uuid}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return JobApiVacancyUpdateV2Response.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for job.vacancy_update_v2 (POST /job/v2/vacancies/update/{vacancy_uuid})",
                payload=payload,
                details={
                    "slug": "job",
                    "operation_id": "vacancyUpdateV2",
                    "python_method": "vacancy_update_v2",
                    "http_method": "POST",
                    "path": "/job/v2/vacancies/update/{vacancy_uuid}",
                    "errors": exc.errors(),
                },
            ) from exc

    async def vacancy_get_item(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> JobApiVacancyGetItemResponse:
        """Просмотр данных вакансии
"""
        payload = await self._transport.request(
            method="GET",
            path_template="/job/v2/vacancies/{vacancy_id}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return JobApiVacancyGetItemResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for job.vacancy_get_item (GET /job/v2/vacancies/{vacancy_id})",
                payload=payload,
                details={
                    "slug": "job",
                    "operation_id": "vacancyGetItem",
                    "python_method": "vacancy_get_item",
                    "http_method": "GET",
                    "path": "/job/v2/vacancies/{vacancy_id}",
                    "errors": exc.errors(),
                },
            ) from exc

    async def vacancy_auto_renewal(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:
        """Автопродление вакансии v2"""
        payload = await self._transport.request(
            method="PUT",
            path_template="/job/v2/vacancies/{vacancy_uuid}/auto_renewal",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        return None

    async def get_dicts(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> JobApiGetDictsResponse:
        """Получение списка доступных словарей"""
        payload = await self._transport.request(
            method="GET",
            path_template="/job/v2/vacancy/dict",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return JobApiGetDictsResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for job.get_dicts (GET /job/v2/vacancy/dict)",
                payload=payload,
                details={
                    "slug": "job",
                    "operation_id": "getDicts",
                    "python_method": "get_dicts",
                    "http_method": "GET",
                    "path": "/job/v2/vacancy/dict",
                    "errors": exc.errors(),
                },
            ) from exc

    async def get_dict_by_id(
        self,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> JobApiGetDictByIdResponse:
        """Получение доступных значений списка по ID словаря"""
        payload = await self._transport.request(
            method="GET",
            path_template="/job/v2/vacancy/dict/{dictionary_id}",
            path_params=path_params,
            query=query,
            json_body=json_body,
            headers=headers,
        )
        try:
            return JobApiGetDictByIdResponse.model_validate(payload)
        except ValidationError as exc:
            raise AvitoValidationError(
                "Response validation failed for job.get_dict_by_id (GET /job/v2/vacancy/dict/{dictionary_id})",
                payload=payload,
                details={
                    "slug": "job",
                    "operation_id": "getDictByID",
                    "python_method": "get_dict_by_id",
                    "http_method": "GET",
                    "path": "/job/v2/vacancy/dict/{dictionary_id}",
                    "errors": exc.errors(),
                },
            ) from exc

__all__ = ["JobApi"]
