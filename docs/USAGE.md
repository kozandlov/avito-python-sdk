# pyAvitoApi Usage Guide

Руководство по практическому использованию библиотеки `pyAvitoApi`.

## 1) Установка

### Из исходников (локально)

```bash
cd pyAvitoApi
pip install -e .
```

### Для разработки

```bash
cd pyAvitoApi
pip install -e .[dev]
```

## 2) Базовый паттерн работы

`pyAvitoApi` использует async-клиент и контекстный менеджер:

```python
from pyavitoapi import AvitoAsyncClient

async def main() -> None:
    async with AvitoAsyncClient(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
    ) as client:
        print(client.available_apis)  # список доступных API-group (slug)
```

## 3) Авторизация

### Получить access token (`client_credentials`)

```python
token = await client.auth.get_client_credentials_token()
print(token.access_token, token.expires_in, token.token_type)
```

### Получить заголовок Authorization

```python
headers = await client.auth.auth_header()
# {'Authorization': 'Bearer ...'}
```

## 4) Вызов сгенерированных API-методов

Все методы сгенерированы в формате:

```python
await client.<api_group>.<method_name>(
    path_params={...},   # для {path} параметров
    query={...},         # query string
    json_body={...},     # JSON body
    headers={...},       # обычно Authorization
)
```

Возвращаемое значение:
- для `2xx` с JSON-ответом возвращается typed Pydantic-модель;
- для `204 No Content` метод возвращает `None`.

Важно:
- `api_group` — это slug с заменой `-` на `_`.
  - пример: `accounts-hierarchy` -> `client.accounts_hierarchy`
  - пример: `order-management` -> `client.order_management`
- `headers` передаются явно.

## 5) Практические примеры

### 5.1 Получить информацию о текущем пользователе

```python
headers = await client.auth.auth_header()

me = await client.user.get_user_info_self(
    path_params={},
    headers=headers,
)
print(type(me).__name__)
print(me.model_dump(exclude_none=True))
```

### 5.2 Получить баланс пользователя

```python
headers = await client.auth.auth_header()

balance = await client.user.get_user_balance(
    path_params={"user_id": 123456789},
    headers=headers,
)
print(balance.model_dump(exclude_none=True))
```

### 5.3 Получить список чатов Avito Messenger

```python
headers = await client.auth.auth_header()

chats = await client.messenger.get_chats_v2(
    path_params={"user_id": 123456789},
    query={"limit": 50, "offset": 0, "unread_only": True},
    headers=headers,
)
print(chats.model_dump(exclude_none=True))
```

### 5.4 Отправить текстовое сообщение в чат

```python
headers = await client.auth.auth_header()

result = await client.messenger.post_send_message(
    path_params={"user_id": 123456789, "chat_id": "CHAT_ID"},
    json_body={
        "type": "text",
        "message": {"text": "Здравствуйте!"},
    },
    headers=headers,
)
print(result.model_dump(exclude_none=True))
```

## 6) Webhook-интеграция Avito

Webhook-сценарий:
1. Регистрируем URL (подписка).
2. Получаем события на свой endpoint.
3. Быстро подтверждаем прием (`200 OK`) и обрабатываем событие в фоне.
4. Проверяем активные подписки.
5. При необходимости отключаем подписку.

### 6.1 Подписка на webhook V3

```python
headers = await client.auth.auth_header()

subscription = await client.messenger.post_webhook_v3(
    json_body={
        "url": "https://your-domain.com/avito/webhook?token=secret123",
    },
    headers=headers,
)
print(subscription.model_dump(exclude_none=True))
```

### 6.2 Проверка активных подписок

```python
headers = await client.auth.auth_header()

subscriptions = await client.messenger.get_subscriptions(
    headers=headers,
)
print(subscriptions.model_dump(exclude_none=True))
```

### 6.3 Отключение webhook-подписки

```python
headers = await client.auth.auth_header()

result = await client.messenger.post_webhook_unsubscribe(
    json_body={
        "url": "https://your-domain.com/avito/webhook?token=secret123",
    },
    headers=headers,
)
print(result.model_dump(exclude_none=True))
```

### 6.4 Пример приемника webhook (FastAPI)

```python
from fastapi import FastAPI, HTTPException, Request

app = FastAPI()
WEBHOOK_TOKEN = "secret123"


@app.post("/avito/webhook")
async def avito_webhook(request: Request):
    token = request.query_params.get("token")
    if token != WEBHOOK_TOKEN:
        raise HTTPException(status_code=403, detail="forbidden")

    event = await request.json()
    # Быстрый ACK; тяжелую обработку отправляйте в очередь
    # queue.publish(event)
    return {"ok": True}
```

### 6.5 Production-рекомендации

- Endpoint должен быть публичным по `HTTPS`.
- Возвращайте `200 OK` в пределах ~2 секунд.
- Делайте дедупликацию событий по `id` (идемпотентность).
- Храните raw payload для аудита и повторной обработки.
- Переносите обработку в очередь (Celery/RQ/Kafka).
- Добавляйте retry/backoff и метрики (ошибки, latency, throughput).
- Защитите endpoint shared-secret токеном (query/header).

## 7) Доступные API-group (slug -> property)

- `accounts-hierarchy` -> `client.accounts_hierarchy`
- `auction` -> `client.auction`
- `auth` -> зарезервировано под `client.auth` (token manager), см. примечание ниже
- `autoload` -> `client.autoload`
- `autostrategy` -> `client.autostrategy`
- `autoteka` -> `client.autoteka`
- `calltracking` -> `client.calltracking`
- `cpa` -> `client.cpa`
- `cpxpromo` -> `client.cpxpromo`
- `delivery-sandbox` -> `client.delivery_sandbox`
- `item` -> `client.item`
- `job` -> `client.job`
- `messenger` -> `client.messenger`
- `order-management` -> `client.order_management`
- `promotion` -> `client.promotion`
- `ratings` -> `client.ratings`
- `realty-reports` -> `client.realty_reports`
- `sbc-gateway` -> `client.sbc_gateway`
- `stock-management` -> `client.stock_management`
- `str` -> `client.str`
- `tariff` -> `client.tariff`
- `trxpromo` -> `client.trxpromo`
- `user` -> `client.user`

Примечание по `auth`:
- для токенов используйте `client.auth` (token manager),
- сгенерированный `AuthApi` можно использовать напрямую:
  `from pyavitoapi.generated.auth import AuthApi`,
  но обычно это не нужно.

## 8) Обработка ошибок

В transport/core используются typed exceptions:

- `AvitoApiError` — HTTP ошибки API (`status_code`, `payload`)
- `AvitoRateLimitError` — 429 + `retry_after`
- `AvitoTransportError` — сетевые/транспортные ошибки
- `AvitoAuthError` — проблемы получения/разбора токена
- `AvitoValidationError` — ответ API не прошел валидацию по typed response model

Пример:

```python
from pyavitoapi.transport.errors import AvitoApiError, AvitoRateLimitError, AvitoValidationError

try:
    headers = await client.auth.auth_header()
    data = await client.user.get_user_info_self(path_params={}, headers=headers)
except AvitoRateLimitError as e:
    print("Rate limited, retry_after=", e.retry_after)
except AvitoValidationError as e:
    print("Schema mismatch:", e.details)
except AvitoApiError as e:
    print("API error:", e.status_code, e.payload)
```

## 9) Перегенерация SDK при обновлении API

```bash
python tools/fetch_specs.py
python tools/patch_specs.py
python tools/generate_clients.py
python tools/build_coverage_report.py
```

После перегенерации:
1. проверьте `docs/final-compliance-report.md`,
2. прогоните `pytest -q`,
3. соберите пакет `python -m build`.

## 10) Где смотреть детали

- Endpoint matrix: `docs/endpoint-matrix.md`
- Known quirks: `docs/known-quirks.md`
- Coverage report: `docs/final-compliance-report.md`
- Release notes: `RELEASE_NOTES.md`
