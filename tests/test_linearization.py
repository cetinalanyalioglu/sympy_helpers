"""Tests for expression linearization."""

import sympy as sp

from sympy_helpers.linearization import linearize


def _assert_expr_equal(actual: sp.Expr, expected: sp.Expr) -> None:
    assert sp.simplify(actual - expected) == 0


def test_linearize_quadratic_at_origin_is_zero() -> None:
    x = sp.Symbol("x")

    result = linearize(x**2, [x])

    _assert_expr_equal(result, sp.Integer(0))


def test_linearize_linear_expression_is_unchanged() -> None:
    x = sp.Symbol("x")
    expr = 3 * x + 5

    result = linearize(expr, [x])

    _assert_expr_equal(result, expr)


def test_linearize_at_nonzero_operating_point() -> None:
    x = sp.Symbol("x")
    operating_point = {x: sp.Integer(2)}

    result = linearize(x**2, [x], operating_point=operating_point)

    _assert_expr_equal(result, 4 * x - 4)


def test_linearize_two_variables_at_operating_point() -> None:
    x, y = sp.symbols("x y")
    operating_point = {x: sp.Integer(1), y: sp.Integer(2)}

    result = linearize(x * y, [x, y], operating_point=operating_point)

    _assert_expr_equal(result, 2 * x + y - 2)
