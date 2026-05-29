# sympy-helpers

Collection of utilities that offer higher-level functionality for SymPy-based symbolic algebra.

## Environment

This project uses the shared conda environment **`py310`** (Python 3.10).

```bash
conda activate py310
```

## Installation

Install from the project root in editable mode:

```bash
pip install -e .
```

For development (includes Black, Flake8, and pytest):

```bash
pip install -e ".[dev]"
```

## Examples

```python
import sympy as sp
from sympy_helpers import create_mean_symbol, linearize

x = sp.Symbol("x")
expr = x**2
linearized = linearize(expr, [x])  # 2*\\overline{x}*x'
mean_x = create_mean_symbol(x)
```
