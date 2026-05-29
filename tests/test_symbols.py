"""Tests for symbol creation helpers."""

import sympy as sp

from sympy_helpers.symbols import create_mean_symbol


def test_create_mean_symbol_returns_named_real_symbol() -> None:
    symbol = create_mean_symbol("mu_x")

    assert isinstance(symbol, sp.Symbol)
    assert symbol.name == "mu_x"
    assert symbol.is_real is True


def test_create_mean_symbol_distinct_names_are_distinct() -> None:
    mu_x = create_mean_symbol("mu_x")
    mu_y = create_mean_symbol("mu_y")

    assert mu_x != mu_y
