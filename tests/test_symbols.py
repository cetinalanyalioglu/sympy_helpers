"""Tests for symbol creation helpers."""

import sympy as sp

from sympy_helpers.symbols import create_mean_symbol, create_perturbation_symbol


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


def test_create_perturbation_symbol_uses_default_suffix() -> None:
    x = sp.Symbol("x")

    perturb_x = create_perturbation_symbol(x)

    assert isinstance(perturb_x, sp.Symbol)
    assert perturb_x.name == "x'"
    assert perturb_x.is_real is True


def test_create_perturbation_symbol_accepts_custom_suffix() -> None:
    x = sp.Symbol("x")

    perturb_x = create_perturbation_symbol(x, suffix="_tilde")

    assert perturb_x.name == "x_tilde"
