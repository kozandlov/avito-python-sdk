# Частые ошибки при работе с Avito API и как их исправить

## 401 Unauthorized

Проверьте:
- валидность `client_id/client_secret`;
- передачу `headers=await client.auth.auth_header()`.

## 429 Too Many Requests

Используйте `retry_after` из `AvitoRateLimitError` и backoff.

## AvitoValidationError

SDK валидирует ответы по typed моделям.  
Смотрите `e.details["errors"]` и обновляйте SDK до актуальной версии.

## Ошибки публикации PyPI

Проверьте:
- совпадение версии тега и `pyproject.toml`;
- Trusted Publishing;
- успешность workflow `Publish To PyPI`.
