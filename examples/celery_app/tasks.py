"""Celery integration example for avito-python-sdk."""

from __future__ import annotations

import asyncio
import os

from celery import Celery

from pyavitoapi import AvitoAsyncClient

celery_app = Celery("avito_examples")


@celery_app.task
def sync_user_profile() -> dict:
    async def _run() -> dict:
        async with AvitoAsyncClient(
            client_id=os.environ["AVITO_CLIENT_ID"],
            client_secret=os.environ["AVITO_CLIENT_SECRET"],
        ) as client:
            headers = await client.auth.auth_header()
            me = await client.user.get_user_info_self(path_params={}, headers=headers)
            return me.model_dump(exclude_none=True)

    return asyncio.run(_run())
