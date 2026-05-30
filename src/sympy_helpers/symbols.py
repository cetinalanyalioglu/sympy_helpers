"""Symbol creation helpers."""

import sympy as sp

_LATEX_PERTURBATION_SUFFIXES = {
    "tilde": r"\tilde{{{}}}",
    "_tilde": r"\tilde{{{}}}",
    r"\tilde": r"\tilde{{{}}}",
}


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


def create_mean_symbols(symbols):
    """Create mean symbols for a list of symbols.

    Parameters
    ----------
    symbols : list of sympy.Symbol
        Symbols to create mean symbols for

    Returns
    -------
    dict[str, sympy.Symbol]
        Mapping from original symbol names to mean symbols
    """
    return {sym.name: create_mean_symbol(sym) for sym in symbols}


def create_perturbation_symbol(sym, suffix="'"):
    """Create a perturbation symbol for a given symbol.

    Parameters
    ----------
    sym : sympy.Symbol
        Symbol to create perturbation symbol for
    suffix : str, optional
        Suffix to append to symbol name, by default '\''.
        Use ``"tilde"`` for a LaTeX tilde accent (``\\tilde{x}``).

    Returns
    -------
    sympy.Symbol
        Perturbation symbol for the given symbol
    """
    latex_template = _LATEX_PERTURBATION_SUFFIXES.get(suffix)
    if latex_template is not None:
        return sp.Symbol(latex_template.format(sym.name), real=True)

    return sp.Symbol(sym.name + suffix, real=True)


def create_perturbation_symbols(symbols, suffix="'"):
    """Create perturbation symbols for a list of symbols.

    Parameters
    ----------
    symbols : list of sympy.Symbol
        Symbols to create perturbation symbols for
    suffix : str, optional
        Suffix passed to :func:`create_perturbation_symbol`, by default '\''

    Returns
    -------
    dict[str, sympy.Symbol]
        Mapping from original symbol names to perturbation symbols
    """
    return {sym.name: create_perturbation_symbol(sym, suffix=suffix) for sym in symbols}


def create_subscripted_symbol(sym, subscript):
    """Create a subscripted symbol for a given symbol.

    Parameters
    ----------
    sym : sympy.Symbol
        Symbol to subscript
    subscript : str
        Subscript to append, e.g. "0" gives x_0 from x

    Returns
    -------
    sympy.Symbol
        Subscripted symbol
    """
    return sp.Symbol(f"{sym.name}_{subscript}", **sym.assumptions0)


def create_subscripted_symbols(symbols, subscript):
    """Create subscripted symbols for a list of symbols.

    Parameters
    ----------
    symbols : list of sympy.Symbol
        Symbols to subscript
    subscript : str
        Subscript to append, e.g. "0" gives x_0 from x

    Returns
    -------
    dict[str, sympy.Symbol]
        Mapping from original symbol names to subscripted symbols
    """
    return {sym.name: create_subscripted_symbol(sym, subscript) for sym in symbols}
