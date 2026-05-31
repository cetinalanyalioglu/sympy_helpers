"""Expression substitution helpers."""

from __future__ import annotations

from collections.abc import Iterable, Mapping

import sympy as sp


def substitute_expressions(
    expressions: Mapping[str, sp.Basic],
    variables: Mapping[str, sp.Symbol],
    ignore: Iterable[str] | None = None,
) -> dict[str, sp.Basic]:
    """Expand expressions using other entries defined in the same mapping.

    Each variable symbol is replaced by its corresponding expression from
    ``expressions``. The process repeats until no further replacements occur,
    so dictionary order does not need to follow dependency order.

    Parameters
    ----------
    expressions : dict[str, sympy.Basic]
        Named expressions. Keys must also exist in ``variables``.
    variables : dict[str, sympy.Symbol]
        Variable symbols corresponding to ``expressions`` keys.
    ignore : iterable of str, optional
        Keys to exclude from substitution. Ignored symbols are not replaced by
        their expressions when expanding other entries.

    Returns
    -------
    dict[str, sympy.Basic]
        Copy of ``expressions`` with internal dependencies substituted out.
    """
    result = dict(expressions)
    names = list(expressions)
    ignored = set(ignore or ())
    substitutable = [name for name in names if name in variables and name not in ignored]

    changed = True
    while changed:
        changed = False
        for name in names:
            subs = {variables[key]: result[key] for key in substitutable if key != name}
            expanded = result[name].xreplace(subs)
            if expanded != result[name]:
                result[name] = expanded
                changed = True

    return result
