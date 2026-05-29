"""Tests for coefficient extraction."""

import sympy as sp

from sympy_helpers.coefficients import get_coefficients_of


def test_get_coefficients_of_linear_expression() -> None:
    x, y = sp.symbols("x y")
    expr = 2 * x + 3 * y + 1

    coefficients = get_coefficients_of(expr, [x, y])

    assert coefficients[x] == 2
    assert coefficients[y] == 3


def test_get_coefficients_of_expanded_polynomial() -> None:
    x = sp.Symbol("x")
    expr = (x + 1) ** 2

    coefficients = get_coefficients_of(expr, [x])

    assert coefficients[x] == 2
