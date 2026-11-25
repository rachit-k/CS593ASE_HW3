"""Run 14 template shapes through meta.find_undeclared_variables().

Used in Part 1 to compare Jinja 3.1.4, 3.1.5 and 3.1.6. From the repo root:

    .venv/bin/python report/scripts/version_matrix.py          # this checkout

    # another release, without touching the working tree:
    mkdir -p /tmp/j3.1.4 && git archive 3.1.4 src | tar -x -C /tmp/j3.1.4
    PYTHONPATH=/tmp/j3.1.4/src .venv/bin/python report/scripts/version_matrix.py

"Expected" is the set supported by rendering each template with a sentinel
value in the context (see report/reflection-report.md).
"""

from jinja2 import Environment, meta

env = Environment()
cases = [
 ("issue: if/elif/else, all assign", "{% if control == 1 %}{% set output = 1 %}{% elif control == 2 %}{% set output = 2 %}{% else %}{% set output = 3 %}{% endif %}{{ output }}", {"control"}),
 ("if/else, both assign",            "{% if x %}{% set y = 1 %}{% else %}{% set y = 2 %}{% endif %}{{ y }}", {"x"}),
 ("if only (no else)",               "{% if x %}{% set y = 1 %}{% endif %}{{ y }}", {"x","y"}),
 ("if/elif, no else",                "{% if x %}{% set y = 1 %}{% elif z %}{% set y = 2 %}{% endif %}{{ y }}", {"x","y","z"}),
 ("if/elif/else, elif misses",       "{% if x %}{% set y = 1 %}{% elif z %}{% else %}{% set y = 3 %}{% endif %}{{ y }}", {"x","y","z"}),
 ("nested if/else in both arms",     "{% if a %}{% if b %}{% set y = 1 %}{% else %}{% set y = 2 %}{% endif %}{% else %}{% set y = 3 %}{% endif %}{{ y }}", {"a","b"}),
 ("nested, inner arm misses",        "{% if a %}{% if b %}{% set y = 1 %}{% endif %}{% else %}{% set y = 3 %}{% endif %}{{ y }}", {"a","b","y"}),
 ("set before if, reassigned",       "{% set y = 0 %}{% if x %}{% set y = 1 %}{% endif %}{{ y }}", {"x"}),
 ("use inside the branch only",      "{% if x %}{% set y = 1 %}{{ y }}{% endif %}", {"x"}),
 ("if/else inside for loop",         "{% for i in items %}{% if i %}{% set y = 1 %}{% else %}{% set y = 2 %}{% endif %}{{ y }}{% endfor %}", {"items"}),
 ("if/else inside macro",            "{% macro m(a) %}{% if a %}{% set y = 1 %}{% else %}{% set y = 2 %}{% endif %}{{ y }}{% endmacro %}", set()),
 ("block set in both arms",          "{% if x %}{% set y %}a{% endset %}{% else %}{% set y %}b{% endset %}{% endif %}{{ y }}", {"x"}),
 ("tuple unpack in both arms",       "{% if x %}{% set y, z = 1, 2 %}{% else %}{% set y, z = 3, 4 %}{% endif %}{{ y }}{{ z }}", {"x"}),
 ("inline if expression",            "{% set y = 1 if x else 2 %}{{ y }}", {"x"}),
]
for name, src, exp in cases:
    got = meta.find_undeclared_variables(env.parse(src))
    print(f"{'OK  ' if got == exp else 'FAIL'} {name:32} expected={sorted(exp)} got={sorted(got)}")
