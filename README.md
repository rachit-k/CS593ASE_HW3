# CS593 ASE Homework 3: fixing Jinja #2069

This repository is Jinja 3.1.6 with a fix for
[pallets/jinja#2069](https://github.com/pallets/jinja/issues/2069):
`meta.find_undeclared_variables()` reported a variable as undeclared even when
every branch of an `{% if %}` assigned it. The reflection report is in
[report/reflection-report.md](report/reflection-report.md). Jinja's original
README follows below the line.

## What changed

The original Jinja 3.1.6 release commit (`15206881`) is preserved, and the
homework commits sit on top of it:

| Commit | Contents |
| --- | --- |
| `15206881` | Jinja 3.1.6 release, unchanged |
| `ba19111c`, `df1f79a6` | Part 1: reproduction tests in `tests/test_api.py`, report |
| `66508fc2`, `294d6093` | Part 2: root cause analysis, diagnostic scripts |
| `754020c0` | Part 3: the fix in `src/jinja2/idtracking.py`, additional tests, `CHANGES.rst` |
| latest | Part 4: this README and the reflection section of the report |

The release tags `3.1.4`, `3.1.5` and `3.1.6` are pushed too, since the
comparison commands below and the scripts in `report/scripts/` use them.

`git diff 15206881 -- src tests CHANGES.rst` shows every change to Jinja itself.

## Setup

Tested with Python 3.12.

```bash
git clone https://github.com/rachit-k/CS593ASE_HW3.git
cd CS593ASE_HW3
python3.12 -m venv .venv
.venv/bin/pip install -r requirements/tests.txt -e .
```

## Reproduce the original failure

Commit `df1f79a6` has the reproduction tests on top of unmodified 3.1.6 source.

```bash
git checkout df1f79a6
.venv/bin/python -m pytest tests/test_api.py::TestMeta -v
# 2 failed, 3 passed: both new tests get {'control', 'output'} instead of {'control'}
git switch hw3-fix-2069
```

## Run the tests on the fix

```bash
# the reproduction tests and the new tests
.venv/bin/python -m pytest tests/test_api.py::TestMeta \
    tests/test_core_tags.py::TestIfCondition tests/test_idtracking.py -v

# the full suite: 933 passed
.venv/bin/python -m pytest -q

# the same tests against untouched 3.1.6 source: 11 failed, 28 passed
mkdir -p /tmp/j3.1.6 && git archive 3.1.6 src | tar -x -C /tmp/j3.1.6
PYTHONPATH=/tmp/j3.1.6/src .venv/bin/python -m pytest -q tests/test_api.py::TestMeta \
    tests/test_core_tags.py::TestIfCondition tests/test_idtracking.py
```

The scripts used during the investigation are in `report/scripts/`. Each one
explains how to run it at the top of the file.

---

# Jinja

Jinja is a fast, expressive, extensible templating engine. Special
placeholders in the template allow writing code similar to Python
syntax. Then the template is passed data to render the final document.

It includes:

-   Template inheritance and inclusion.
-   Define and import macros within templates.
-   HTML templates can use autoescaping to prevent XSS from untrusted
    user input.
-   A sandboxed environment can safely render untrusted templates.
-   AsyncIO support for generating templates and calling async
    functions.
-   I18N support with Babel.
-   Templates are compiled to optimized Python code just-in-time and
    cached, or can be compiled ahead-of-time.
-   Exceptions point to the correct line in templates to make debugging
    easier.
-   Extensible filters, tests, functions, and even syntax.

Jinja's philosophy is that while application logic belongs in Python if
possible, it shouldn't make the template designer's job difficult by
restricting functionality too much.


## In A Nutshell

```jinja
{% extends "base.html" %}
{% block title %}Members{% endblock %}
{% block content %}
  <ul>
  {% for user in users %}
    <li><a href="{{ user.url }}">{{ user.username }}</a></li>
  {% endfor %}
  </ul>
{% endblock %}
```

## Donate

The Pallets organization develops and supports Jinja and other popular
packages. In order to grow the community of contributors and users, and
allow the maintainers to devote more time to the projects, [please
donate today][].

[please donate today]: https://palletsprojects.com/donate

## Contributing

See our [detailed contributing documentation][contrib] for many ways to
contribute, including reporting issues, requesting features, asking or answering
questions, and making PRs.

[contrib]: https://palletsprojects.com/contributing/
