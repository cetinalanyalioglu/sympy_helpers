"""Display helpers for notebook-friendly output."""

from __future__ import annotations

from typing import Mapping, Union

import sympy as sp

SymbolDictKey = Union[str, sp.Symbol]


def _format_dict_key(key: SymbolDictKey) -> str:
    if isinstance(key, sp.Symbol):
        return key.name
    return str(key)


def format_symbol_dict(mapping: Mapping[SymbolDictKey, sp.Basic]) -> str:
    """Format a symbol dictionary as a LaTeX expression.

    Parameters
    ----------
    mapping : dict
        Dictionary mapping names (or symbols) to SymPy symbols or expressions

    Returns
    -------
    str
        LaTeX string representing the dictionary with rendered values
    """
    if not mapping:
        return r"\left\{ \right\}"

    items = ", ".join(rf"\text{{'{_format_dict_key(key)}'}}: {sp.latex(value)}" for key, value in mapping.items())
    return rf"\left\{{ {items} \right\}}"


def display_symbol_dict(mapping: Mapping[SymbolDictKey, sp.Basic]) -> None:
    """Display a symbol dictionary with LaTeX-rendered values.

    In Jupyter notebooks, values are rendered with LaTeX. Outside IPython,
    the formatted LaTeX string is printed.

    Parameters
    ----------
    mapping : dict
        Dictionary mapping names (or symbols) to SymPy symbols or expressions
    """
    latex = format_symbol_dict(mapping)

    try:
        from IPython.display import Math, display
    except ImportError:
        print(latex)
        return

    display(Math(latex))
