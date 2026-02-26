# avito-python-sdk

[![PyPI version](https://img.shields.io/pypi/v/avito-python-sdk.svg)](https://pypi.org/project/avito-python-sdk/)
[![Python versions](https://img.shields.io/pypi/pyversions/avito-python-sdk.svg)](https://pypi.org/project/avito-python-sdk/)
[![CI](https://github.com/kozandlov/avito-python-sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/kozandlov/avito-python-sdk/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-AGPLv3-blue.svg)](LICENSE)

Асинхронная Python SDK-библиотека для Avito API с typed response models.

- Пакет в `pip`: `avito-python-sdk`
- Импорт в коде: `pyavitoapi`
- Лицензия: `AGPL-3.0-only`

## Установка

### Через `pip`

```bash
pip install avito-python-sdk
```

### С фиксацией версии

```bash
pip install avito-python-sdk==0.2.3
```

### Через `requirements.txt`

```text
avito-python-sdk==0.2.3
```

```bash
pip install -r requirements.txt
```

### Для разработки

```bash
pip install -e .[dev]
```

## Быстрый старт (до 5 минут)

```python
import asyncio
import os

from pyavitoapi import AvitoAsyncClient


async def main() -> None:
    async with AvitoAsyncClient(
        client_id=os.environ["AVITO_CLIENT_ID"],
        client_secret=os.environ["AVITO_CLIENT_SECRET"],
    ) as client:
        headers = await client.auth.auth_header()
        me = await client.user.get_user_info_self(path_params={}, headers=headers)
        print(me.model_dump(exclude_none=True))


if __name__ == "__main__":
    asyncio.run(main())
```

## Готовые сценарии

### 1) Профиль пользователя

```python
headers = await client.auth.auth_header()
me = await client.user.get_user_info_self(path_params={}, headers=headers)
print(me.id, me.name, me.email)
```

### 2) Чаты Avito Messenger

```python
headers = await client.auth.auth_header()
chats = await client.messenger.get_chats_v2(
    path_params={"user_id": 123456789},
    query={"limit": 50, "offset": 0},
    headers=headers,
)
print(chats.model_dump(exclude_none=True))
```

### 3) Отправка сообщения

```python
headers = await client.auth.auth_header()
result = await client.messenger.post_send_message(
    path_params={"user_id": 123456789, "chat_id": "CHAT_ID"},
    json_body={"type": "text", "message": {"text": "Здравствуйте!"}},
    headers=headers,
)
print(result.model_dump(exclude_none=True))
```

## Webhooks Avito (быстрый старт)

Webhook flow:

1. Поднимите публичный `HTTPS` endpoint в вашей системе.
2. Подпишите URL через `client.messenger.post_webhook_v3(...)`.
3. На входящем endpoint быстро возвращайте `200 OK` и обрабатывайте payload асинхронно.
4. Проверяйте подписки через `client.messenger.get_subscriptions(...)`.
5. При необходимости отключайте подписку `client.messenger.post_webhook_unsubscribe(...)`.

Пример подписки:

```python
headers = await client.auth.auth_header()
response = await client.messenger.post_webhook_v3(
    json_body={"url": "https://your-domain.com/avito/webhook?token=secret123"},
    headers=headers,
)
print(response.model_dump(exclude_none=True))
```

Минимальный webhook endpoint (FastAPI):

```python
from fastapi import FastAPI, HTTPException, Request

app = FastAPI()

@app.post("/avito/webhook")
async def avito_webhook(request: Request):
    if request.query_params.get("token") != "secret123":
        raise HTTPException(status_code=403, detail="forbidden")
    event = await request.json()
    # TODO: push event to queue and return quickly
    return {"ok": True}
```

## Typed response models

```python
headers = await client.auth.auth_header()
user = await client.user.get_user_info_self(path_params={}, headers=headers)

print(user.id, user.email)
print(user.model_dump(exclude_none=True))
```

## Обработка ошибок

```python
from pyavitoapi.transport.errors import (
    AvitoApiError,
    AvitoAuthError,
    AvitoRateLimitError,
    AvitoTransportError,
    AvitoValidationError,
)

try:
    headers = await client.auth.auth_header()
    await client.user.get_user_info_self(path_params={}, headers=headers)
except AvitoRateLimitError as e:
    print("retry_after:", e.retry_after)
except AvitoValidationError as e:
    print("schema errors:", e.details)
except AvitoAuthError as e:
    print("auth error:", e)
except AvitoTransportError as e:
    print("network error:", e)
except AvitoApiError as e:
    print("api error:", e.status_code, e.payload)
```

## Интеграционные примеры

Готовые шаблоны лежат в директории `examples/`:

- `examples/basic_user_info.py`
- `examples/fastapi_app/main.py`
- `examples/django_app/avito_client.py`
- `examples/celery_app/tasks.py`
- `examples/webhooks/fastapi_receiver.py`
- `examples/webhooks/subscribe.py`
- `examples/webhooks/unsubscribe.py`
- `examples/.env.example`

## Перегенерация SDK

```bash
python tools/fetch_specs.py
python tools/patch_specs.py
python tools/generate_clients.py
python tools/build_coverage_report.py
```

## Тесты и сборка

```bash
pytest -q
python -m build
```

## Релиз и публикация

- `Release Bump And Tag`:
  - автоматически увеличивает patch-версию,
  - создает commit и тег `vX.Y.Z`,
  - автоматически запускает `Publish To PyPI`.
- `Publish To PyPI`:
  - собирает wheel/sdist,
  - публикует пакет в PyPI через Trusted Publishing (OIDC).

## Поддержка и вклад

- Bug/Feature шаблоны: `.github/ISSUE_TEMPLATE/`
- PR шаблон: `.github/pull_request_template.md`
- Руководство для контрибьюторов: `CONTRIBUTING.md`
- Политика безопасности: `SECURITY.md`
- FAQ: `docs/FAQ.md`
- Troubleshooting: `docs/TROUBLESHOOTING.md`

## Полезные ссылки

- Примеры интеграции: `examples/README.md`
- Growth metrics: `docs/GROWTH_METRICS.md`
- Материалы для анонсов: `docs/articles/`
- Руководство по использованию: `docs/USAGE.md`
- Endpoint matrix: `docs/endpoint-matrix.md`
- Known quirks: `docs/known-quirks.md`
- Coverage report: `docs/final-compliance-report.md`
- Typed response map: `docs/typed-response-map.json`
- Release notes: `RELEASE_NOTES.md`
