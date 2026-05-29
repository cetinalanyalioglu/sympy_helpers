"""Coefficient extraction helpers."""


def get_coefficients_of(expr, vars):
    """Get coefficients of variables in an expression.

    Parameters
    ----------
    expr : sympy.Expr
        Expression to get coefficients from
    vars : list
        List of variables to get coefficients for

    Returns
    -------
    dict
        Dictionary mapping variables to their coefficients in the expanded expression
    """
    return {var: expr.expand().coeff(var) for var in vars}
