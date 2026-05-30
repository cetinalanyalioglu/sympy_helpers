"""Tests for symbol creation helpers."""

import sympy as sp

from sympy_helpers.symbols import (
    create_mean_symbol,
    create_mean_symbols,
    create_perturbation_symbol,
    create_perturbation_symbols,
    create_subscripted_symbol,
    create_subscripted_symbols,
)


def test_create_mean_symbol_wraps_name_with_overline() -> None:
    x = sp.Symbol("x", real=True)

    mean_x = create_mean_symbol(x)

    assert isinstance(mean_x, sp.Symbol)
    assert mean_x.name == r"\overline{x}"
    assert mean_x.is_real is True


def test_create_mean_symbol_preserves_assumptions() -> None:
    rho = sp.Symbol(r"\rho", positive=True)

    mean_rho = create_mean_symbol(rho)

    assert mean_rho.name == r"\overline{\rho}"
    assert mean_rho.is_positive is True


def test_create_mean_symbols_returns_name_mapping() -> None:
    x, y = sp.symbols("x y", real=True)

    mean_symbols = create_mean_symbols([x, y])

    assert set(mean_symbols.keys()) == {"x", "y"}
    assert mean_symbols["x"].name == r"\overline{x}"
    assert mean_symbols["y"].name == r"\overline{y}"


def test_create_perturbation_symbol_uses_default_suffix() -> None:
    x = sp.Symbol("x")

    perturb_x = create_perturbation_symbol(x)

    assert isinstance(perturb_x, sp.Symbol)
    assert perturb_x.name == "x'"
    assert perturb_x.is_real is True


def test_create_perturbation_symbol_uses_latex_tilde_suffix() -> None:
    x = sp.Symbol("x")

    perturb_x = create_perturbation_symbol(x, suffix="tilde")

    assert perturb_x.name == r"\tilde{x}"


def test_create_perturbation_symbols_returns_name_mapping() -> None:
    x, y = sp.symbols("x y")

    perturbations = create_perturbation_symbols([x, y])

    assert set(perturbations.keys()) == {"x", "y"}
    assert perturbations["x"].name == "x'"
    assert perturbations["y"].name == "y'"


def test_create_subscripted_symbol_appends_subscript() -> None:
    x = sp.Symbol("x", real=True, positive=True)

    subscripted_x = create_subscripted_symbol(x, "0")

    assert subscripted_x.name == "x_0"
    assert subscripted_x.is_real is True
    assert subscripted_x.is_positive is True


def test_create_subscripted_symbols_returns_name_mapping() -> None:
    x, y = sp.symbols("x y")

    subscripted = create_subscripted_symbols([x, y], "0")

    assert set(subscripted.keys()) == {"x", "y"}
    assert subscripted["x"].name == "x_0"
    assert subscripted["y"].name == "y_0"


def test_create_subscripted_symbols_preserves_assumptions() -> None:
    x = sp.Symbol("x", real=True, positive=True)

    subscripted = create_subscripted_symbols([x], "1")

    assert subscripted["x"].is_real is True
    assert subscripted["x"].is_positive is True
