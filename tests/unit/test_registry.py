"""Unit tests for generated registry presence."""

from pyavitoapi.generated_registry import REGISTRY


def test_registry_not_empty() -> None:
    assert len(REGISTRY) >= 20


def test_required_core_slugs_present() -> None:
    required = {"auth", "messenger", "user", "item"}
    assert required.issubset(REGISTRY.keys())
