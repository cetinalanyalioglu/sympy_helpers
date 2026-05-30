"""Tests for display helpers."""

import sympy as sp

from sympy_helpers.display import format_symbol_dict
from sympy_helpers.symbols import create_mean_symbols, create_perturbation_symbols


def test_format_symbol_dict_renders_perturbation_values_in_latex() -> None:
    x, y = sp.symbols("x y")

    latex = format_symbol_dict(create_perturbation_symbols([x, y]))

    assert latex == r"\left\{ \text{'x'}: x', \text{'y'}: y' \right\}"


def test_format_symbol_dict_renders_mean_values_in_latex() -> None:
    x = sp.Symbol("x", real=True)

    latex = format_symbol_dict(create_mean_symbols([x]))

    assert latex == r"\left\{ \text{'x'}: \overline{x} \right\}"


def test_format_symbol_dict_handles_empty_mapping() -> None:
    assert format_symbol_dict({}) == r"\left\{ \right\}"


def test_format_symbol_dict_accepts_symbol_keys() -> None:
    x, y = sp.symbols("x y")
    expr = 2 * x + 3 * y + 1

    latex = format_symbol_dict({x: expr.coeff(x), y: expr.coeff(y)})

    assert latex == r"\left\{ \text{'x'}: 2, \text{'y'}: 3 \right\}"
