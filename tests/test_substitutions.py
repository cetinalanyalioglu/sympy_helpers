"""Tests for expression substitution helpers."""

import sympy as sp

from sympy_helpers.substitutions import substitute_expressions


def test_substitute_expressions_expands_chain_in_any_order() -> None:
    rho, u, p, T, h, ht = sp.symbols("rho u p T h ht", real=True)
    R, cp = sp.symbols("R c_p", real=True)

    variables = {"T": T, "h": h, "ht": ht}
    expressions = {
        "ht": h + u**2 / 2,
        "h": cp * T,
        "T": p / (rho * R),
    }

    result = substitute_expressions(expressions, variables)

    assert result["T"] == p / (rho * R)
    assert result["h"] == cp * p / (rho * R)
    assert result["ht"] == cp * p / (rho * R) + u**2 / 2


def test_substitute_expressions_expands_flux_expression() -> None:
    rho, u, p, T, h, ht = sp.symbols("rho u p T h ht", real=True)
    R, cp = sp.symbols("R c_p", real=True)

    variables = {"T": T, "h": h, "ht": ht}
    expressions = {
        "T": p / (rho * R),
        "h": cp * T,
        "ht": h + u**2 / 2,
        "energy_flux": rho * u * ht,
    }

    result = substitute_expressions(expressions, variables)

    assert result["energy_flux"] == rho * u * (cp * p / (rho * R) + u**2 / 2)


def test_substitute_expressions_ignore_keeps_intermediate_symbol() -> None:
    rho, u, p, T, h, ht = sp.symbols("rho u p T h ht", real=True)
    R, cp = sp.symbols("R c_p", real=True)

    variables = {"T": T, "h": h, "ht": ht}
    expressions = {
        "T": p / (rho * R),
        "h": cp * T,
        "ht": h + u**2 / 2,
    }

    result = substitute_expressions(expressions, variables, ignore=["h"])

    assert result["T"] == p / (rho * R)
    assert result["h"] == cp * p / (rho * R)
    assert result["ht"] == h + u**2 / 2


def test_substitute_expressions_ignore_blocks_downstream_expansion() -> None:
    rho, u, p, T, h, ht = sp.symbols("rho u p T h ht", real=True)
    R, cp = sp.symbols("R c_p", real=True)

    variables = {"T": T, "h": h, "ht": ht}
    expressions = {
        "T": p / (rho * R),
        "h": cp * T,
        "ht": h + u**2 / 2,
    }

    result = substitute_expressions(expressions, variables, ignore=["T"])

    assert result["T"] == p / (rho * R)
    assert result["h"] == cp * T
    assert result["ht"] == cp * T + u**2 / 2
