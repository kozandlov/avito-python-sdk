# Release Notes

## 0.2.0 (2026-02-25)

Typed response models rollout for generated API methods.

### Breaking changes

- Сгенерированные API-методы больше не возвращают raw JSON (`Any`).
- Для `2xx` с JSON-ответом методы возвращают typed Pydantic-модели.
- Для `204 No Content` методы возвращают `None`.
- При несоответствии payload схеме бросается `AvitoValidationError` c `details`.

### Что добавлено

- Генерация typed response models в `src/pyavitoapi/generated_models/*.py`.
- Валидация ответов в generated clients:
  - `Model.model_validate(payload)` для всех операций с JSON-ответом.
- Новая карта typed-ответов `docs/typed-response-map.json`.
- Расширенный `docs/final-compliance-report.md`:
  - `typed methods`
  - `Typed coverage vs patched`.

### Миграция с 0.1.x

- Если код ожидал `dict`/`list`, замените работу с raw JSON на:
  - `response.model_dump(exclude_none=True)` для словаря,
  - прямой доступ к typed полям модели (`response.field_name`).
- Обработка ошибок валидации:
  - добавьте `except AvitoValidationError` при необходимости.

## 0.1.0 (2026-02-25)

Первый публичный релиз библиотеки `pyAvitoApi`.

### Что добавлено

- Отдельный пакет `pyAvitoApi` (изолирован от основного проекта).
- Async-only SDK с фасадом `AvitoAsyncClient`.
- Поддержка всех официальных API-групп Avito из OpenAPI каталога (23 slug).
- Генерация per-slug модулей из `specs/patched`.
- Snapshot pipeline:
  - `tools/fetch_specs.py`
  - `tools/patch_specs.py`
  - `tools/generate_clients.py`
  - `tools/build_coverage_report.py`
- Typed transport errors:
  - `AvitoApiError`
  - `AvitoAuthError`
  - `AvitoRateLimitError`
  - `AvitoTransportError`
  - `AvitoValidationError`
- OAuth token manager (`client_credentials`) с кэшем и refresh-window.

### Качество и валидация

- Покрытие генерации:
  - `199/199` операций относительно `specs/patched` (`100%`).
  - `199/201` относительно `specs/raw` (`99%`) из-за известных дубликатов `/token` в raw-spec.
- Тесты: `7 passed`.
- Сборка дистрибутивов:
  - `pyavitoapi-0.1.0-py3-none-any.whl`
  - `pyavitoapi-0.1.0.tar.gz`

### Известные ограничения

- Публичный auth manager сейчас реализует `client_credentials` flow.
- Сгенерированные API-методы возвращают raw JSON (`Any`) без typed response models.
- Авторизационный заголовок передается явно через `headers` в вызовах API-методов.

### Известные особенности спецификаций

- `auth`: дубли `/token` с невидимыми unicode-символами в raw OpenAPI.
- `messenger`: неконсистентный `required` в `sendMessageRequestBody` в raw OpenAPI.
- Эти проблемы нормализуются в `tools/patch_specs.py`.

### Совместимость

- Python: `>=3.11`
- Основные зависимости:
  - `httpx>=0.27.0`
  - `pydantic>=2.7.0`
