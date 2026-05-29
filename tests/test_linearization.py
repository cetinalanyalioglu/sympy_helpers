"""Tests for expression linearization."""

import pytest
import sympy as sp

from sympy_helpers.linearization import linearize
from sympy_helpers.symbols import create_mean_symbol, create_perturbation_symbol


def test_linearize_quadratic_returns_perturbation_terms_only() -> None:
    x = sp.Symbol("x")
    x_bar = create_mean_symbol(x)
    x_pert = create_perturbation_symbol(x)

    result = linearize(x**2, [x])

    assert result == 2 * x_bar * x_pert


def test_linearize_linear_expression_returns_constant_perturbation_slope() -> None:
    x = sp.Symbol("x")
    x_pert = create_perturbation_symbol(x)

    result = linearize(3 * x + 5, [x])

    assert result == 3 * x_pert


def test_linearize_includes_mean_value_when_requested() -> None:
    x = sp.Symbol("x")
    x_bar = create_mean_symbol(x)
    x_pert = create_perturbation_symbol(x)

    result = linearize(3 * x + 5, [x], remove_mean=False)

    assert result == 3 * x_bar + 5 + 3 * x_pert


def test_linearize_two_variables_builds_sum_of_partial_derivatives() -> None:
    x, y = sp.symbols("x y")
    x_bar = create_mean_symbol(x)
    y_bar = create_mean_symbol(y)
    x_pert = create_perturbation_symbol(x)
    y_pert = create_perturbation_symbol(y)

    result = linearize(x * y, [x, y])

    assert result == y_bar * x_pert + x_bar * y_pert


def test_linearize_strict_raises_for_missing_variable() -> None:
    x, y = sp.symbols("x y")

    with pytest.raises(ValueError):
        linearize(x**2, [y], strict=True)


def test_linearize_non_strict_warns_for_missing_variable() -> None:
    x, y = sp.symbols("x y")

    with pytest.warns(UserWarning, match="Variable y not found in expression"):
        result = linearize(x**2, [y], strict=False)

    assert result == 0


def test_linearize_raises_for_non_symbol_variable() -> None:
    x, y = sp.symbols("x y")

    with pytest.raises(ValueError):
        linearize(x * y, [x + y])
