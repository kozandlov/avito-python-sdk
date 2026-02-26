# Примеры интеграции

## Переменные окружения

Скопируйте и заполните:

```bash
cp examples/.env.example .env
```

Минимально нужны:
- `AVITO_CLIENT_ID`
- `AVITO_CLIENT_SECRET`

## Список примеров

- `basic_user_info.py` — проверка доступа и получение профиля.
- `fastapi_app/main.py` — endpoint `/me` в FastAPI.
- `django_app/avito_client.py` — helper для Django.
- `celery_app/tasks.py` — Celery task для синхронизации профиля.
- `webhooks/fastapi_receiver.py` — прием webhook событий Avito.
- `webhooks/subscribe.py` — регистрация webhook URL через SDK.
- `webhooks/unsubscribe.py` — отключение webhook URL через SDK.

## Webhooks: быстрый сценарий

1. Заполните `AVITO_WEBHOOK_SECRET` и `AVITO_WEBHOOK_URL` в `.env`.
2. Поднимите receiver:

```bash
uvicorn examples.webhooks.fastapi_receiver:app --host 0.0.0.0 --port 8000
```

3. Подпишите URL:

```bash
python examples/webhooks/subscribe.py
```

4. Проверяйте события в receiver и логах приложения.
5. Отключите подписку при необходимости:

```bash
python examples/webhooks/unsubscribe.py
```
