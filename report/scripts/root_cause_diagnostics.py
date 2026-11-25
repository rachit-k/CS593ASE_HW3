"""Part 2 diagnostics: how Symbols.branch_update merges the branches of an if.

Wraps ``Symbols.branch_update`` to print each branch's ``stores`` and load
instruction for the variable of interest, and the merged result. Then prints
what ``find_undeclared_variables`` returns and what rendering produces.

    .venv/bin/python report/scripts/root_cause_diagnostics.py      # 3.1.6

    # Jinja 3.1.4 for comparison:
    mkdir -p /tmp/j3.1.4 && git archive 3.1.4 src | tar -x -C /tmp/j3.1.4
    PYTHONPATH=/tmp/j3.1.4/src .venv/bin/python report/scripts/root_cause_diagnostics.py
"""

from jinja2 import Environment
from jinja2 import meta
from jinja2.idtracking import Symbols

TRACKED = ("_a", "_y")
_original = Symbols.branch_update


def _fmt(loads):
    return {k: v[0] for k, v in loads.items() if k.endswith(TRACKED)}


def traced_branch_update(self, branch_symbols):
    parts = [
        f"b{i} stores={sorted(b.stores)} loads={_fmt(b.loads)}"
        for i, b in enumerate(branch_symbols)
    ]
    print("  branch_update: " + " | ".join(parts))
    _original(self, branch_symbols)
    print(f"    -> merged: {_fmt(self.loads)}")


Symbols.branch_update = traced_branch_update
env = Environment()

CASES = [
    (
        "#2069: if/elif/else, every branch sets y",
        "{% if c == 1 %}{% set y = 1 %}{% elif c == 2 %}{% set y = 2 %}"
        "{% else %}{% set y = 3 %}{% endif %}{{ y }}",
        {"c": 1, "y": "CTX"},
    ),
    (
        "#2069 variant: if/else, both branches set y",
        "{% if c %}{% set y = 1 %}{% else %}{% set y = 2 %}{% endif %}{{ y }}",
        {"c": True, "y": "CTX"},
    ),
    (
        "#1253: body reads a before setting it",
        "{% if True %}{{ a.b }}{% set a = 1 %}{% elif False %}{% set a = 2 %}"
        "{% else %}{% set a = 3 %}{% endif %}{{ a }}",
        {"a": {"b": 0}},
    ),
    (
        "two elifs, second elif does not set y (runs 'elif b')",
        "{% if x %}{% set y = 1 %}{% elif a %}{% set y = 2 %}"
        "{% elif b %}{% else %}{% set y = 3 %}{% endif %}{{ y }}",
        {"x": False, "a": False, "b": True, "y": "CTX"},
    ),
]

for name, source, context in CASES:
    print(f"== {name}")
    ast = env.parse(source)
    print("  find_undeclared_variables:", sorted(meta.find_undeclared_variables(ast)))
    Symbols.branch_update = _original  # keep the render quiet
    try:
        print(f"  render({context}): {env.from_string(source).render(context)!r}")
    except Exception as e:  # noqa: BLE001
        print(f"  render raised {type(e).__name__}: {e}")
    Symbols.branch_update = traced_branch_update
