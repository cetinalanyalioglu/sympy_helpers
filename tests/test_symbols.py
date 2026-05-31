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


def _example_symbol_mapping() -> dict[str, sp.Symbol]:
    return {
        "rho": sp.Symbol(r"\rho", real=True, positive=True),
        "u": sp.Symbol("u", real=True),
        "p": sp.Symbol("p", real=True, positive=True),
        "cp": sp.Symbol("c_p", real=True),
    }


def test_create_mean_symbols_accepts_symbol_mapping() -> None:
    symbols = _example_symbol_mapping()

    mean_symbols = create_mean_symbols(symbols)

    assert set(mean_symbols.keys()) == set(symbols.keys())
    assert mean_symbols["rho"].name == r"\overline{\rho}"
    assert mean_symbols["cp"].name == r"\overline{c_p}"
    assert mean_symbols["rho"].is_positive is True


def test_create_perturbation_symbols_accepts_symbol_mapping() -> None:
    symbols = _example_symbol_mapping()

    perturbations = create_perturbation_symbols(symbols)

    assert set(perturbations.keys()) == set(symbols.keys())
    assert perturbations["rho"].name == r"\rho'"
    assert perturbations["cp"].name == r"c_p'"


def test_create_subscripted_symbols_accepts_symbol_mapping() -> None:
    symbols = _example_symbol_mapping()

    subscripted = create_subscripted_symbols(symbols, "0")

    assert set(subscripted.keys()) == set(symbols.keys())
    assert subscripted["rho"].name == r"\rho_0"
    assert subscripted["cp"].name == r"c_p_0"


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
