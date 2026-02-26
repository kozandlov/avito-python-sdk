# FAQ

## Как установить библиотеку?

```bash
pip install avito-python-sdk
```

## Какое имя в `requirements.txt`?

Используйте имя пакета из PyPI:

```text
avito-python-sdk==0.2.3
```

## Какой модуль импортировать в коде?

```python
from pyavitoapi import AvitoAsyncClient
```

## Почему `401 Unauthorized`?

Чаще всего не передан Bearer token в заголовках запроса.  
Получите заголовки так:

```python
headers = await client.auth.auth_header()
```

и передайте `headers=headers` в вызов метода.

## Почему получаю `AvitoValidationError`?

Ответ API не совпал с ожидаемой typed-моделью.  
Посмотрите подробности:

```python
except AvitoValidationError as e:
    print(e.details)
```

## Можно ли использовать синхронно?

SDK async-only. Для sync-кода используйте адаптеры (`asyncio.run`, `asgiref.sync.async_to_sync`).
