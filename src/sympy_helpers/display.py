"""Display helpers for notebook-friendly output."""

from __future__ import annotations

from typing import Mapping, Union

import sympy as sp

SymbolDictKey = Union[str, sp.Symbol]


def _format_dict_key(key: SymbolDictKey) -> str:
    if isinstance(key, sp.Symbol):
        return key.name
    return str(key)


def _format_dict_key_latex(key: SymbolDictKey) -> str:
    if isinstance(key, sp.Symbol):
        return sp.latex(key)

    return rf"\mathrm{{{_format_dict_key(key)}}}"


def _format_dict_value(value: sp.Basic, latex_values: bool) -> str:
    if latex_values:
        return sp.latex(value)

    return str(value)


def format_symbol_dict(
    mapping: Mapping[SymbolDictKey, sp.Basic],
    *,
    latex_values: bool = True,
) -> str:
    """Format a symbol dictionary as a LaTeX expression.

    Parameters
    ----------
    mapping : dict
        Dictionary mapping names (or symbols) to SymPy symbols or expressions
    latex_values : bool, optional
        If True (default), render values with LaTeX. If False, use plain text.

    Returns
    -------
    str
        LaTeX string representing the dictionary with rendered keys
    """
    if not mapping:
        return r"\left\{ \right\}"

    items = ", ".join(
        rf"{_format_dict_key_latex(key)}: {_format_dict_value(value, latex_values)}" for key, value in mapping.items()
    )
    return rf"\left\{{ {items} \right\}}"


def display_symbol_dict(
    mapping: Mapping[SymbolDictKey, sp.Basic],
    *,
    latex_values: bool = True,
) -> None:
    """Display a symbol dictionary with LaTeX-rendered keys.

    In Jupyter notebooks, keys are always rendered with LaTeX. Values are
    rendered with LaTeX by default and can be shown as plain text when
    ``latex_values=False``. Outside IPython, the formatted string is printed.

    Parameters
    ----------
    mapping : dict
        Dictionary mapping names (or symbols) to SymPy symbols or expressions
    latex_values : bool, optional
        If True (default), render values with LaTeX. If False, use plain text.
    """
    latex = format_symbol_dict(mapping, latex_values=latex_values)

    try:
        from IPython.display import Math, display
    except ImportError:
        print(latex)
        return

    display(Math(latex))
