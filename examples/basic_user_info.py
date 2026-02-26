"""Minimal example: fetch current user profile."""

from __future__ import annotations

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
