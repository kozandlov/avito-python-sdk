"""Django integration example for avito-python-sdk."""

from __future__ import annotations

from asgiref.sync import async_to_sync
from django.conf import settings

from pyavitoapi import AvitoAsyncClient


async def _fetch_me() -> dict:
    async with AvitoAsyncClient(
        client_id=settings.AVITO_CLIENT_ID,
        client_secret=settings.AVITO_CLIENT_SECRET,
    ) as client:
        headers = await client.auth.auth_header()
        me = await client.user.get_user_info_self(path_params={}, headers=headers)
        return me.model_dump(exclude_none=True)


def fetch_me_sync() -> dict:
    return async_to_sync(_fetch_me)()
