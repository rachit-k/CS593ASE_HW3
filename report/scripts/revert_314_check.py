"""Part 2 diagnostic: would restoring Jinja 3.1.4's branch_update fix #2069?

Swaps 3.1.4's version of ``Symbols.branch_update`` into this checkout at
runtime (no source file is changed) and runs the relevant tests.

    .venv/bin/python report/scripts/revert_314_check.py
"""

import sys
import typing as t

import pytest

from jinja2 import idtracking
from jinja2.idtracking import VAR_LOAD_ALIAS
from jinja2.idtracking import VAR_LOAD_RESOLVE


def branch_update_314(self, branch_symbols):
    """Copied from Jinja 3.1.4 (git show 3.1.4:src/jinja2/idtracking.py)."""
    stores: t.Dict[str, int] = {}
    for branch in branch_symbols:
        for target in branch.stores:
            if target in self.stores:
                continue
            stores[target] = stores.get(target, 0) + 1

    for sym in branch_symbols:
        self.refs.update(sym.refs)
        self.loads.update(sym.loads)
        self.stores.update(sym.stores)

    for name, branch_count in stores.items():
        if branch_count == len(branch_symbols):
            continue

        target = self.find_ref(name)
        assert target is not None, "should not happen"

        if self.parent is not None:
            outer_target = self.parent.find_ref(name)
            if outer_target is not None:
                self.loads[target] = (VAR_LOAD_ALIAS, outer_target)
                continue
        self.loads[target] = (VAR_LOAD_RESOLVE, name)


idtracking.Symbols.branch_update = branch_update_314

sys.exit(
    pytest.main(
        [
            "-v",
            "-p",
            "no:cacheprovider",
            "tests/test_api.py::TestMeta",
            "tests/test_regression.py::test_load_parameter_when_set_in_all_if_branches",
            "tests/test_idtracking.py",
        ]
    )
)
