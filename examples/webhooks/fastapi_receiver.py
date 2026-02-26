"""Webhook receiver example for Avito messenger webhooks."""

from __future__ import annotations

import os

from fastapi import FastAPI, HTTPException, Request

app = FastAPI(title="Avito Webhook Receiver Example")
WEBHOOK_SECRET = os.getenv("AVITO_WEBHOOK_SECRET", "change-me")


@app.get("/health")
async def health() -> dict[str, bool]:
    return {"ok": True}


@app.post("/avito/webhook")
async def avito_webhook(request: Request) -> dict[str, bool]:
    token = request.query_params.get("token")
    if token != WEBHOOK_SECRET:
        raise HTTPException(status_code=403, detail="forbidden")

    event = await request.json()
    # Store/deduplicate and enqueue event for async processing.
    # Example: await queue.publish(event)
    _ = event

    return {"ok": True}
