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
