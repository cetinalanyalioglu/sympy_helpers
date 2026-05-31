"""Tests for display helpers."""

import sympy as sp

from sympy_helpers.display import format_symbol_dict
from sympy_helpers.symbols import create_mean_symbols, create_perturbation_symbols


def test_format_symbol_dict_renders_perturbation_values_in_latex() -> None:
    x, y = sp.symbols("x y")

    latex = format_symbol_dict(create_perturbation_symbols([x, y]))

    assert latex == r"\left\{ \mathrm{x}: x', \mathrm{y}: y' \right\}"


def test_format_symbol_dict_renders_mean_values_in_latex() -> None:
    x = sp.Symbol("x", real=True)

    latex = format_symbol_dict(create_mean_symbols([x]))

    assert latex == r"\left\{ \mathrm{x}: \overline{x} \right\}"


def test_format_symbol_dict_handles_empty_mapping() -> None:
    assert format_symbol_dict({}) == r"\left\{ \right\}"


def test_format_symbol_dict_accepts_symbol_keys() -> None:
    x, y = sp.symbols("x y")
    expr = 2 * x + 3 * y + 1

    latex = format_symbol_dict({x: expr.coeff(x), y: expr.coeff(y)})

    assert latex == r"\left\{ x: 2, y: 3 \right\}"


def test_format_symbol_dict_can_render_plain_text_values() -> None:
    x, y = sp.symbols("x y")

    latex = format_symbol_dict(create_perturbation_symbols([x, y]), latex_values=False)

    assert latex == r"\left\{ \mathrm{x}: x', \mathrm{y}: y' \right\}"
