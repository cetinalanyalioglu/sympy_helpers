"""Symbol creation helpers."""

from __future__ import annotations

import sympy as sp


def create_mean_symbol(name: str) -> sp.Symbol:
    """Create a SymPy symbol representing a mean (operating-point) value."""
    return sp.Symbol(name, real=True)
