# avito-python-sdk

Асинхронная Python SDK-библиотека для Avito API.

Пакет в `pip`: `avito-python-sdk`  
Импорт в коде: `pyavitoapi`

## Установка

### Из PyPI

```bash
pip install avito-python-sdk
```

### Установка конкретной версии

```bash
pip install avito-python-sdk==0.2.3
```

### Использование в `requirements.txt`

```text
avito-python-sdk==0.2.3
```

Установка зависимостей проекта:

```bash
pip install -r requirements.txt
```

### Для разработки SDK

```bash
pip install -e .[dev]
```

## Быстрый старт

```python
import asyncio

from pyavitoapi import AvitoAsyncClient


async def main() -> None:
    async with AvitoAsyncClient(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
    ) as client:
        me = await client.user.get_user_info_self(path_params={})
        print(me.model_dump(exclude_none=True))


if __name__ == "__main__":
    asyncio.run(main())
```

## Примеры использования SDK

### 1) Получение access token

```python
token = await client.auth.get_client_credentials_token()
print(token.access_token, token.expires_in)
```

### 2) Получение `Authorization` заголовка

```python
headers = await client.auth.auth_header()
# {'Authorization': 'Bearer ...'}
```

### 3) Информация о текущем пользователе

```python
me = await client.user.get_user_info_self(path_params={})
print(me.id, me.name)
```

### 4) Баланс пользователя

```python
balance = await client.user.get_user_balance(path_params={"user_id": 123456789})
print(balance.real, balance.bonus)
```

### 5) Список чатов (Messenger)

```python
chats = await client.messenger.get_chats_v2(
    path_params={"user_id": 123456789},
    query={"limit": 50, "offset": 0},
)
print(chats.model_dump(exclude_none=True))
```

### 6) Отправка сообщения в чат

```python
result = await client.messenger.post_send_message(
    path_params={"user_id": 123456789, "chat_id": "CHAT_ID"},
    json_body={
        "type": "text",
        "message": {"text": "Здравствуйте!"},
    },
)
print(result.model_dump(exclude_none=True))
```

### 7) Доступные API-группы

```python
print(client.available_apis)
```

## Typed response models

Сгенерированные методы возвращают Pydantic-модели.

```python
user = await client.user.get_user_info_self(path_params={})

# доступ к typed полям
print(user.id, user.email)

# преобразование в dict
payload = user.model_dump(exclude_none=True)
print(payload)
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
    data = await client.user.get_user_info_self(path_params={})
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

## Полезные ссылки

- Руководство по использованию: `docs/USAGE.md`
- Endpoint matrix: `docs/endpoint-matrix.md`
- Known quirks: `docs/known-quirks.md`
- Coverage report: `docs/final-compliance-report.md`
- Typed response map: `docs/typed-response-map.json`
- Release notes: `RELEASE_NOTES.md`
- License: `AGPL-3.0-only`
