"""Tests for package-level exports."""

import sympy as sp

from sympy_helpers import (
    __all__,
    create_mean_symbol,
    create_perturbation_symbol,
    get_coefficients_of,
    linearize,
)


def test_public_api_exports() -> None:
    assert set(__all__) == {
        "create_mean_symbol",
        "create_mean_symbols",
        "create_perturbation_symbol",
        "create_perturbation_symbols",
        "create_subscripted_symbol",
        "create_subscripted_symbols",
        "display_symbol_dict",
        "format_symbol_dict",
        "get_coefficients_of",
        "linearize",
        "substitute_expressions",
    }


def test_public_api_usage_from_readme() -> None:
    x = sp.Symbol("x")
    expr = x**2

    linearized = linearize(expr, [x])
    mean_x = create_mean_symbol(x)
    perturb_x = create_perturbation_symbol(x)

    assert linearized == 2 * mean_x * perturb_x
    assert get_coefficients_of(2 * x + 1, [x])[x] == 2
