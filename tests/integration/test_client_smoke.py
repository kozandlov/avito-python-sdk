"""Integration smoke tests with mocked transport."""

from __future__ import annotations

import pytest

from pyavitoapi import AvitoAsyncClient
from pyavitoapi.transport.errors import AvitoValidationError


@pytest.mark.asyncio
async def test_client_exposes_generated_groups() -> None:
    async with AvitoAsyncClient(client_id="id", client_secret="secret") as client:
        assert "auth" in client.available_apis
        assert "messenger" in client.available_apis
        assert "user" in client.available_apis


@pytest.mark.asyncio
async def test_generated_method_calls_transport(monkeypatch) -> None:
    calls: list[tuple[str, str]] = []

    async def fake_request(**kwargs):
        calls.append((kwargs["method"], kwargs["path_template"]))
        return {}

    async with AvitoAsyncClient(client_id="id", client_secret="secret") as client:
        monkeypatch.setattr(client._transport, "request", fake_request)  # noqa: SLF001
        result = await client.user.get_user_info_self(path_params={})

    assert hasattr(result, "model_dump")
    assert result.model_dump(exclude_none=True) == {}
    assert calls == [("GET", "/core/v1/accounts/self")]


@pytest.mark.asyncio
async def test_generated_method_raises_validation_error(monkeypatch) -> None:
    async def fake_request(**kwargs):
        return "not-an-object"

    async with AvitoAsyncClient(client_id="id", client_secret="secret") as client:
        monkeypatch.setattr(client._transport, "request", fake_request)  # noqa: SLF001
        with pytest.raises(AvitoValidationError) as exc_info:
            await client.user.get_user_info_self(path_params={})

    err = exc_info.value
    assert err.details is not None
    assert err.details.get("slug") == "user"
