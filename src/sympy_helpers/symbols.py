"""Symbol creation helpers."""

from collections.abc import Mapping, Sequence
from typing import Union

import sympy as sp

_LATEX_PERTURBATION_SUFFIXES = {
    "tilde": r"\tilde{{{}}}",
    "_tilde": r"\tilde{{{}}}",
    r"\tilde": r"\tilde{{{}}}",
}

SymbolCollection = Union[Sequence[sp.Symbol], Mapping[str, sp.Symbol]]


def _symbol_items(symbols: SymbolCollection):
    """Yield ``(key, symbol)`` pairs from a symbol list or mapping."""
    if isinstance(symbols, Mapping):
        return symbols.items()

    return ((sym.name, sym) for sym in symbols)


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


def create_mean_symbols(symbols: SymbolCollection):
    """Create mean symbols for a list or mapping of symbols.

    Parameters
    ----------
    symbols : list or dict[str, sympy.Symbol]
        Symbols to create mean symbols for. When a mapping is given, output keys
        match the mapping keys (e.g. ``"rho"`` for ``Symbol("\\\\rho")``).

    Returns
    -------
    dict[str, sympy.Symbol]
        Mapping from keys to mean symbols
    """
    return {key: create_mean_symbol(sym) for key, sym in _symbol_items(symbols)}


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


def create_perturbation_symbols(symbols: SymbolCollection, suffix="'"):
    """Create perturbation symbols for a list or mapping of symbols.

    Parameters
    ----------
    symbols : list or dict[str, sympy.Symbol]
        Symbols to create perturbation symbols for. When a mapping is given,
        output keys match the mapping keys.
    suffix : str, optional
        Suffix passed to :func:`create_perturbation_symbol`, by default '\''

    Returns
    -------
    dict[str, sympy.Symbol]
        Mapping from keys to perturbation symbols
    """
    return {key: create_perturbation_symbol(sym, suffix=suffix) for key, sym in _symbol_items(symbols)}


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


def create_subscripted_symbols(symbols: SymbolCollection, subscript):
    """Create subscripted symbols for a list or mapping of symbols.

    Parameters
    ----------
    symbols : list or dict[str, sympy.Symbol]
        Symbols to subscript. When a mapping is given, output keys match the
        mapping keys.
    subscript : str
        Subscript to append, e.g. "0" gives x_0 from x

    Returns
    -------
    dict[str, sympy.Symbol]
        Mapping from keys to subscripted symbols
    """
    return {key: create_subscripted_symbol(sym, subscript) for key, sym in _symbol_items(symbols)}
