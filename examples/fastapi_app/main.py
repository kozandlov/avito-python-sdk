"""FastAPI integration example for avito-python-sdk."""

from __future__ import annotations

import os

from fastapi import FastAPI

from pyavitoapi import AvitoAsyncClient

app = FastAPI(title="Avito SDK FastAPI Example")


@app.get("/me")
async def get_me() -> dict:
    async with AvitoAsyncClient(
        client_id=os.environ["AVITO_CLIENT_ID"],
        client_secret=os.environ["AVITO_CLIENT_SECRET"],
    ) as client:
        headers = await client.auth.auth_header()
        me = await client.user.get_user_info_self(path_params={}, headers=headers)
        return me.model_dump(exclude_none=True)
