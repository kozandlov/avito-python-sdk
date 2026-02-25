"""Pagination helpers."""

from __future__ import annotations


def clamp_limit(limit: int, *, minimum: int = 1, maximum: int = 100) -> int:
    return max(minimum, min(maximum, limit))


def clamp_offset(offset: int, *, minimum: int = 0, maximum: int = 1000) -> int:
    return max(minimum, min(maximum, offset))
