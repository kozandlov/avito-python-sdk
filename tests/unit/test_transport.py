"""Unit tests for transport primitives."""

from pyavitoapi.utils.pagination import clamp_limit, clamp_offset


def test_clamp_limit() -> None:
    assert clamp_limit(0) == 1
    assert clamp_limit(50) == 50
    assert clamp_limit(200) == 100


def test_clamp_offset() -> None:
    assert clamp_offset(-10) == 0
    assert clamp_offset(10) == 10
    assert clamp_offset(2000) == 1000
