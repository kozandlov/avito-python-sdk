"""Unsubscribe webhook URL via avito-python-sdk."""

from __future__ import annotations

import asyncio
import os

from pyavitoapi import AvitoAsyncClient


async def main() -> None:
    webhook_url = os.environ["AVITO_WEBHOOK_URL"]

    async with AvitoAsyncClient(
        client_id=os.environ["AVITO_CLIENT_ID"],
        client_secret=os.environ["AVITO_CLIENT_SECRET"],
    ) as client:
        headers = await client.auth.auth_header()

        result = await client.messenger.post_webhook_unsubscribe(
            json_body={"url": webhook_url},
            headers=headers,
        )
        print("unsubscribe:", result.model_dump(exclude_none=True))


if __name__ == "__main__":
    asyncio.run(main())
