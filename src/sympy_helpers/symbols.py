"""Symbol creation helpers."""

import sympy as sp


def create_mean_symbol(sym: sp.Symbol) -> sp.Symbol:
    """Create a mean symbol for a given symbol.

    Use "\\" prefix for greek symbols in order to render them correctly, e.g. "\\rho" for rho.

    Parameters
    ----------
    sym : sympy.Symbol
        Symbol to create mean symbol for

    Returns
    -------
    sympy.Symbol
        Mean symbol for the given symbol
    """
    return sp.Symbol(f"\\overline{{{sym.name}}}", **sym.assumptions0)


def create_perturbation_symbol(sym, suffix="'"):
    """Create a perturbation symbol for a given symbol.

    Parameters
    ----------
    sym : sympy.Symbol
        Symbol to create perturbation symbol for
    suffix : str, optional
        Suffix to append to symbol name, by default '\''

    Returns
    -------
    sympy.Symbol
        Perturbation symbol for the given symbol
    """

    return sp.Symbol(sym.name + suffix, real=True)
