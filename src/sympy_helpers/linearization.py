"""Expression linearization helpers."""

from sympy_helpers.symbols import create_mean_symbol, create_perturbation_symbol


def linearize(expr, vars, remove_mean=True, strict=True):
    """Linearize a symbolic expression around mean values using Taylor series expansion.

    Parameters
    ----------
    expr : sympy.Expr
        The symbolic expression to linearize
    vars : list of sympy.Symbol
        List of variables to linearize with respect to
    remove_mean : bool, optional
        If True, returns only perturbation terms without mean value term.
        If False, includes mean value term. Default is True.
    suffix_perturb : str, optional
        Suffix to append to variable names for perturbation terms.
        Default is e.g. rho -> rho'

    Returns
    -------
    linearized : sympy.Expr
        The linearized expression

    Raises
    ------
    ValueError
        If any requested variable is not in the expression or
        if any variable has more than one free symbol
    """

    # Check if all requested variables appear in the expression (avoid typing errors)
    for var in vars:
        if var not in expr.free_symbols and strict:
            raise ValueError

    # Check if all variables are simple (e.g. only one free symbol)
    if not all([len(var.free_symbols) == 1 for var in vars]):
        raise ValueError

    # Define mean variables
    vars_mean = {var: create_mean_symbol(var) for var in vars}

    # Define perturbation variables
    vars_perturb = {var: create_perturbation_symbol(var) for var in vars}

    # Substitute mean variables
    linearized = 0 if remove_mean else expr.subs(vars_mean)

    for var, perturb in vars_perturb.items():
        linearized += expr.diff(var).subs(vars_mean) * perturb

    return linearized
