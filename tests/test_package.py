"""Tests for package-level exports."""

import sympy as sp

from sympy_helpers import __all__, create_mean_symbol, linearize


def test_public_api_exports() -> None:
    assert set(__all__) == {"create_mean_symbol", "linearize"}


def test_public_api_usage_from_readme() -> None:
    x = sp.Symbol("x")
    expr = x**2

    linearized = linearize(expr, [x])
    mean_symbol = create_mean_symbol("mu_x")

    assert sp.simplify(linearized) == 0
    assert mean_symbol.name == "mu_x"
