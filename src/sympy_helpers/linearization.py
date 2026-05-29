"""Expression linearization helpers."""

from __future__ import annotations

from typing import Mapping, Sequence

import sympy as sp


def linearize(
    expr: sp.Expr,
    variables: Sequence[sp.Symbol],
    *,
    operating_point: Mapping[sp.Symbol, sp.Expr] | None = None,
) -> sp.Expr:
    """Return the first-order Taylor expansion of *expr* around *variables*."""
    if operating_point is None:
        operating_point = {var: sp.Integer(0) for var in variables}

    value_at_point = expr.subs(operating_point)
    linear_part = value_at_point
    for var in variables:
        slope = sp.diff(expr, var).subs(operating_point)
        linear_part += slope * (var - operating_point[var])

    return sp.expand(linear_part)
