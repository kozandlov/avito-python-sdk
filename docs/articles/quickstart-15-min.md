# Интеграция Avito API за 15 минут с `avito-python-sdk`

## Что понадобится

- `AVITO_CLIENT_ID`
- `AVITO_CLIENT_SECRET`
- Python `3.11+`

## Установка

```bash
pip install avito-python-sdk
```

## Минимальный рабочий скрипт

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

## Что дальше

- Получить чаты: `client.messenger.get_chats_v2(...)`
- Отправить сообщение: `client.messenger.post_send_message(...)`
- Добавить retry/backoff для `429` ошибок.
