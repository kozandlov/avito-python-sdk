# Troubleshooting

## 1) `401 Unauthorized`

Причины:
- неверные `AVITO_CLIENT_ID` / `AVITO_CLIENT_SECRET`;
- не передан `Authorization` в API-вызов.

Проверьте:

```python
headers = await client.auth.auth_header()
await client.user.get_user_info_self(path_params={}, headers=headers)
```

## 2) `429 Too Many Requests`

SDK бросает `AvitoRateLimitError`.

Рекомендуется:
- читать `retry_after`,
- добавлять backoff/retry на уровне приложения.

## 3) `AvitoValidationError`

Проблема: структура ответа не совпала со схемой typed response model.

Проверьте:
- `e.details["errors"]`,
- актуальность версии SDK.

## 4) Ошибка публикации в PyPI

Проверьте:
- Trusted Publishing настроен для репозитория и workflow `publish-pypi.yml`;
- тег и версия в `pyproject.toml` совпадают;
- workflow `Publish To PyPI` запускается на `v*`.

## 5) Workflow не запускается после push тега

В GitHub push тега из workflow через `GITHUB_TOKEN` может не триггерить другой workflow.  
В проекте это решено явным `workflow_dispatch`-триггером из `Release Bump And Tag`.
