# pyAvitoApi

Асинхронная Python SDK-библиотека для Avito API с полным покрытием операций на основе официальных OpenAPI-снимков.

## Что входит

- Покрытие всех API-групп из `https://developers.avito.ru/web/1/openapi/list`.
- Генерация per-slug API-классов из нормализованных (`patched`) OpenAPI-спецификаций.
- Typed response models на Pydantic для всех сгенерированных методов.
- Детерминированный pipeline снимков и генерации.

## Структура проекта

- `specs/raw` — сырой snapshot OpenAPI.
- `specs/patched` — нормализованные спеки для генерации.
- `tools/fetch_specs.py` — загрузка snapshot + manifest.
- `tools/patch_specs.py` — нормализация известных дефектов OpenAPI.
- `tools/generate_clients.py` — генерация async API-модулей.
- `tools/build_coverage_report.py` — сборка отчета покрытия.
- `src/pyavitoapi/generated` — сгенерированные API-модули по slug.
- `src/pyavitoapi/generated_models` — сгенерированные typed response models.
- `src/pyavitoapi/client.py` — фасад `AvitoAsyncClient`.

## Быстрый старт

```python
from pyavitoapi import AvitoAsyncClient

async def main() -> None:
    async with AvitoAsyncClient(client_id="...", client_secret="...") as client:
        token = await client.auth.get_client_credentials_token()
        me = await client.user.get_user_info_self(path_params={}, query=None)
        print(token.access_token[:8], me.model_dump(exclude_none=True))
```

## Перегенерация

```bash
python tools/fetch_specs.py
python tools/patch_specs.py
python tools/generate_clients.py
python tools/build_coverage_report.py
```

## Тесты

```bash
pytest -q
```

## Примечания

- Метрика покрытия считается относительно `specs/patched` (нормализованные уникальные операции).
- Raw-спеки могут содержать дубликаты token-операций из-за известных upstream-особенностей.
- Сгенерированные методы валидируют ответы по typed-моделям и бросают
  `AvitoValidationError`, если payload не соответствует схеме.

## Документация

- Руководство по использованию: `docs/USAGE.md`
- Матрица endpoint-ов: `docs/endpoint-matrix.md`
- Известные особенности OpenAPI: `docs/known-quirks.md`
- Отчет покрытия: `docs/final-compliance-report.md`
- Карта typed-ответов: `docs/typed-response-map.json`
- История релизов: `RELEASE_NOTES.md`
