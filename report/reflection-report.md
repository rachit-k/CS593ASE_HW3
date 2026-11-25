# Homework 3 Reflection Report: Fixing Jinja #2069 with a Coding Agent

Rachit · CS593 ASE · Repository: [rachit-k/CS593ASE_HW3](https://github.com/rachit-k/CS593ASE_HW3) · Branch `hw3-fix-2069`, created from tag `3.1.6`

I used Claude Code (Claude Opus 5.5, VS Code extension) for the whole assignment, plus the graphify skill to build a knowledge graph of the repository. "The agent" below always means Claude Code.

---

## 1. Repository Understanding and Bug Reproduction

### 1.1 The bug

[Issue #2069](https://github.com/pallets/jinja/issues/2069) is about `jinja2.meta.find_undeclared_variables()`, which is supposed to return the variables a caller has to pass into `render()`. For this template it also returns `output`, even though every branch of the `if` sets it:

```jinja
{% if control == 1 %}{% set output = 1 %}
{% elif control == 2 %}{% set output = 2 %}
{% else %}{% set output = 3 %}{% endif %}
{{ output }}
```

| | Result |
| --- | --- |
| Expected | `{'control'}` |
| Observed (3.1.5, 3.1.6) | `{'control', 'output'}` |

Whichever branch runs, `output` is set before it's printed, so the caller never needs to supply it. Reporting it is a false positive.

The issue says what the answer should be but not why, so I had the agent check it by rendering. It passed a decoy `output='FROM_CONTEXT'` and rendered with `control` set to 1, 2, 3 and 99. The output was `1`, `2`, `3` and `3`; the decoy never showed up. Remove the `else` and that changes: `{% if x %}{% set y = 1 %}{% endif %}{{ y }}` prints `FROM_CONTEXT` when `x` is false. There `y` really does come from the context and has to stay in the result.

The issue title blames 3.1.5, but a commenter said plain `if/else` breaks on 3.1.4 too. So the agent ran the same templates on 3.1.4, 3.1.5 and 3.1.6 (`report/scripts/version_matrix.py`):

| Template shape | Expected | 3.1.4 | 3.1.5 and 3.1.6 |
| --- | --- | --- | --- |
| `if / elif / else`, every branch assigns (the issue) | `control` | correct | adds `output` |
| `if / else`, both branches assign | `x` | adds `y` | adds `y` |
| Nested `if / else`, every path assigns | `a, b` | adds `y` | adds `y` |
| Same, inside a `for` loop or a macro | loop var / none | adds `y` | adds `y` |
| `if` with no `else` | `x, y` | correct | correct |
| `if / elif / else` where one branch skips the assignment | `x, y, z` | correct | correct |

The bug isn't about `elif`, and 3.1.5 didn't create it. It shows up whenever every path through an `if` that has an `else` assigns the name. 3.1.5 only broke the `elif` form, which 3.1.4 happened to get right. The last two rows matter just as much as the first four. When some path skips the assignment, reporting the name is correct, so a fix can't just ignore assignments inside conditionals.

### 1.2 Relevant components

`find_undeclared_variables()` doesn't analyze templates on its own. It runs Jinja's real code generator in a mode that writes nothing and records every name the generated code would look up in the context. Three files matter:

- `meta.py` holds `TrackingCodeGenerator`, a `CodeGenerator` subclass. Its `enter_frame()` collects every symbol whose load action is `resolve` ("look it up in the context"). That set is what the function returns.
- `compiler.py` builds a `Frame` for each scope: the template body, a `for` loop, a macro. For the issue's template the generated code opens with `l_0_output = resolve('output')`, so the extra lookup is the compiler's own decision and `meta.py` is just reporting it.
- `idtracking.py` decides those load actions. `FrameSymbolVisitor.visit_If()` analyzes each branch of an `if`, and `Symbols.branch_update()` merges the results back into the enclosing scope. Part 2 starts here.

To find these, the agent ran `/graphify` on the repo (about 2,800 nodes) and followed the call and inheritance edges from `find_undeclared_variables` down to `branch_update`. After that it only needed to read those three files. It also caught a mistake of mine. I had told it the clone was on 3.1.6, but `git describe` showed `main`, 164 commits later. It moved the work to a new branch made from the `3.1.6` tag before writing any tests.

### 1.3 Reproduction tests

I added two tests to the existing `TestMeta` class in `tests/test_api.py`, where the other `find_undeclared_variables` tests already live. They use the suite's `env` fixture and follow the existing test's style.

| Test | Template | What it checks | Why it is there |
| --- | --- | --- | --- |
| `test_find_undeclared_variables_set_in_if_elif_else` | `if / elif / else` on `control`, each branch sets `output` | The result is exactly `{'control'}` | The scenario from the issue |
| `test_find_undeclared_variables_set_in_if_else` | `if control / else`, both branches set `output` | The result is exactly `{'control'}` | The commenter's variant: not specific to `elif`, and fails on 3.1.4 too |

Both tests assert that the result *equals* `{'control'}`, not just that `'output'` is missing. That way each one checks two things: the always-assigned variable is gone, and the variable used in the condition is still there. A "fix" that dropped every variable near an `if` would still fail.

I left out the cases where a variable must still be reported (no `else`, a branch that skips the assignment, nested ifs). They already pass on 3.1.6, so they can't demonstrate the bug. They come back in Part 3 as guards. Three existing tests in `tests/test_idtracking.py` already cover the no-`else` case at the symbol-table level.

### 1.4 How to reproduce

The branch was created with `git switch -c hw3-fix-2069 3.1.6`. Commit `df1f79a6` ("Part 1") has the new tests on top of unmodified 3.1.6 source, so that's where the original failure shows:

```bash
git clone https://github.com/rachit-k/CS593ASE_HW3.git && cd CS593ASE_HW3
python3.12 -m venv .venv
.venv/bin/pip install -r requirements/tests.txt -e .
git checkout df1f79a6                    # Jinja 3.1.6 source + the reproduction tests
.venv/bin/python -m pytest tests/test_api.py::TestMeta -v
git switch hw3-fix-2069                  # back to the fixed version
```

Both new tests fail and the rest pass:

```
tests/test_api.py::TestMeta::test_find_undeclared_variables PASSED
tests/test_api.py::TestMeta::test_find_undeclared_variables_set_in_if_elif_else FAILED
tests/test_api.py::TestMeta::test_find_undeclared_variables_set_in_if_else FAILED
tests/test_api.py::TestMeta::test_find_refererenced_templates PASSED
tests/test_api.py::TestMeta::test_find_included_templates PASSED
E       AssertionError: assert {'control', 'output'} == {'control'}
E         Extra items in the left set:
E         'output'
```

The full suite at that commit gives 2 failed, 909 passed. Before I added the tests it was 909 passed.

![The two reproduction tests failing on Jinja 3.1.6](images/FailingTests.png)

*Figure 1. The two reproduction tests failing on unmodified Jinja 3.1.6.*

---

## 2. Bug Localization and Root Cause Analysis

### 2.1 Root cause

The bug isn't in `meta.py`, which reports exactly what the compiler decided. The wrong decision happens in `Symbols.branch_update()` (`src/jinja2/idtracking.py`, L123–145). That function merges the symbol tables of an `if` statement's branches back into the surrounding scope. In 3.1.6 it marks every name assigned in *any* branch as `resolve` and never checks whether every path assigns the name before reading it.

```python
def branch_update(self, branch_symbols):          # idtracking.py, 3.1.6
    stores = set()
    for branch in branch_symbols:
        stores.update(branch.stores)              # names assigned in ANY branch
    stores.difference_update(self.stores)         # ...that weren't defined before the if
    for sym in branch_symbols:
        self.refs.update(sym.refs)
        self.loads.update(sym.loads)              # per-branch loads: last branch wins
        self.stores.update(sym.stores)
    for name in stores:                           # every such name ->
        ...                                       #   alias (if an outer scope has it)
        self.loads[target] = (VAR_LOAD_RESOLVE, name)   # or resolve
```

For each `resolve`, the compiler emits a context lookup like `l_0_output = resolve('output')`, and `meta.py` reports it. Rendering is fine, because every branch overwrites the value before it's printed; the lookup is just wasted. That's probably why nobody noticed until someone called `find_undeclared_variables()`.

The tempting fix is to put back what 3.1.4 did. 3.1.4 skipped names stored in all branches, and commit `66587ce9` ("Fix bug where set would sometimes fail within if", for #1253, released in 3.1.5) removed that shortcut. But the old rule was wrong in three separate ways, which also explains the odd results in Section 1.1:

1. **Merging was last-branch-wins.** Each branch's table already holds the right answer for that branch: `undefined` if it assigns the name before reading it, `resolve` if it reads it first. But `self.loads.update(sym.loads)` lets a later branch overwrite an earlier one. In #1253 the `if` body read `a` before setting it (`resolve`). The `else` branch's `undefined` overwrote that, and rendering crashed with `UndefinedError`. The 3.1.5 fix stopped the crash by forcing `resolve` for every conditionally assigned name, and that's what produced #2069.
2. **An `if` was always analyzed as three branches:** the body, all the `elif`s together, and the `else`, with empty tables for missing ones. A plain `if/else` therefore had an empty `elif` slot that looked like a path assigning nothing. The variable counted as stored in 2 of 3 branches and got `resolve`, which is why `if/else` already failed on 3.1.4.
3. **All the `elif`s shared one table.** The parser stores each `elif` as a nested `If` node with no `elif` or `else` of its own, and `visit_If` walked them one after another in the same copy. An assignment in the first `elif` then hides a later `elif` that assigns nothing. On 3.1.4, `{% if x %}{% set y=1 %}{% elif a %}{% set y=2 %}{% elif b %}{% else %}{% set y=3 %}{% endif %}{{ y }}` renders `''` instead of the context value when `elif b` runs, and the function misses `y`. 3.1.6 only gets this right because it marks everything `resolve`.

Put simply, the symbol tracker has no way to say "every path through this `if` assigns the name before anyone reads it." 3.1.5 replaced a check that was wrong in both directions with the safest possible answer, `resolve`, and `meta` reports it faithfully.

| `branch_update` rule | #2069 `if/elif/else` | `if/else` | #1253 read-before-set | two `elif`s, one skips |
| --- | --- | --- | --- | --- |
| 3.1.4: skip names stored in all 3 slots | correct (by luck) | false positive | render crash | wrong render, `y` missed |
| 3.1.5+: every stored name → `resolve` | false positive | false positive | correct | correct |
| Required | `y` not reported | `y` not reported | `a` reported | `y` reported |

That gave the fix its spec. A name assigned inside an `if` can be left out only if every real path assigns it (the body, each `elif` on its own, and an `else` that actually exists) and no path reads it first. The #1253 regression test (`test_regression.py::test_load_parameter_when_set_in_all_if_branches`) and the branching tests in `tests/test_idtracking.py` have to keep passing.

### 2.2 How the agent investigated

The agent worked through three hypotheses and tested each by running something, not by arguing from the code.

| # | Hypothesis | How it was tested | Result |
| --- | --- | --- | --- |
| H1 | The extra name comes from the compiler's symbol table, not from `meta.py` | Wrapped `Symbols.branch_update` to print each branch's stores and loads and the merged result (`report/scripts/root_cause_diagnostics.py`) | Confirmed: every branch says `undefined`, the merge outputs `resolve` |
| H2 | 3.1.5 removed a correct check, so restoring it fixes the bug | Found `66587ce9` in the 3.1.4 → 3.1.5 history of `idtracking.py`, swapped the 3.1.4 function into 3.1.6 at runtime and ran the tests (`report/scripts/revert_314_check.py`) | Rejected: the issue's test passes, but the `if/else` test still fails and the #1253 test breaks again |
| H3 | The fixed three slots and the shared `elif` table distort the "all branches" count | Inspected the parsed AST (each `elif` is a nested `If`), rendered a two-`elif` template on 3.1.4 and 3.1.6 | Confirmed: 3.1.4 renders `''` instead of the context value |

H2 is the one I'd point to. The issue blames 3.1.5, and a revert looks like a two-minute fix. The agent swapped the old function in and ran the tests before suggesting anything. Had it trusted the issue's framing, I would probably have been handed that revert as "the fix".

### 2.3 Assumptions, detours and guidance

It stayed on relevant code: `idtracking.py`, the scope handling in `compiler.py`, and the git history of `idtracking.py`. It never opened the lexer or the runtime.

One thing to flag given the no-copying rule: the agent read the 3.1.4 → 3.1.5 diff of `idtracking.py`. That diff is the change that *caused* the regression, not a fix for #2069, so I treat it as ordinary bug localization, the same commit `git bisect` would have pointed to. The 3.1.4 code was only used as a diagnostic and isn't part of the patch.

I didn't have to steer it here. My whole prompt for this part was "let's move on to part 2".

---

## 3. Patch Implementation and Validation

### 3.1 The patch

The logic change is entirely in `src/jinja2/idtracking.py` (+23/−4 lines), plus a `CHANGES.rst` entry. `meta.py` and the compiler are untouched. Once the symbol table is right, both `find_undeclared_variables()` and the generated code follow from it.

The first change is in `FrameSymbolVisitor.visit_If`. It now passes one branch per real path: the body, each `elif` on its own (with that `elif`'s test, which only runs on that path), and the `else`. A missing `else` becomes an empty branch, because "nothing matched" is a real path that assigns nothing. The empty `elif` slot from 3.1.4 is gone.

```python
branch_symbols = [inner_visit(node.body)]
branch_symbols.extend(
    inner_visit([elif_.test, *elif_.body]) for elif_ in node.elif_
)
branch_symbols.append(inner_visit(node.else_ or ()))
self.symbols.branch_update(branch_symbols)
```

The second change is in `Symbols.branch_update`. Before falling back to `resolve`, it checks whether every branch recorded the name as `undefined`, meaning every branch assigns it before reading it. If so, the earlier value can never be used, so the name stays `undefined` and no lookup is emitted.

```python
if all(
    branch.loads.get(target) == (VAR_LOAD_UNDEFINED, None)
    for branch in branch_symbols
):
    self.loads[target] = (VAR_LOAD_UNDEFINED, None)
    continue
self.loads[target] = (VAR_LOAD_RESOLVE, name)
```

This works where the 3.1.4 rule didn't because it asks every branch for its own answer instead of counting stores or trusting whichever branch was merged last. Any one of these keeps the name as `resolve`: a branch that never assigns it (including a missing `else`), a branch that reads it first (#1253, or a read in an `elif` test), or a nested `if` that only sometimes assigns it. Names visible from an outer scope still become `alias`, as before. And because the check runs over the real list of paths, it handles any number of `elif`s, nesting, loops and macros, and every way of assigning a name: `set`, `set` blocks, tuple unpacking, macros and imports.

### 3.2 How the agent produced the patch

The agent wrote the patch straight from the spec at the end of Part 2, and the first version passed the whole suite. There was no failed patch to fix. I think that's mostly down to Part 2. By then it had already ruled out the revert and knew exactly which two places were wrong.

It didn't stop at green tests, either. It tried 13 more templates the tests didn't cover yet and checked both the `meta` result and the rendered output: a read in an `elif` test, a read before the `if`, a read before the assignment in the `else`, `is defined`, `include`, an outer variable in a `for` loop, async rendering. All 13 came out right. Then it ran the new tests against unpatched 3.1.6 and against 3.1.4 to show they can tell a correct fix from a wrong one (Section 3.3).

The one hiccup was linting. The newest `ruff` wanted to reformat code the patch never touched. The agent noticed the repo pins `ruff` 0.8.4 in `.pre-commit-config.yaml`, reran with that version, and everything passed. `mypy` reports no issues in `idtracking.py`.

### 3.3 Test results

The new tests work at three levels: what `find_undeclared_variables()` returns (`TestMeta.test_find_undeclared_variables_if_branches`, 15 cases), whether rendering still falls back to the context when it should (`TestIfCondition.test_set_in_branches_context_fallback`, 5 cases), and the symbol table itself (`test_if_branching_stores_all_branches` and `test_if_branching_stores_elif_missing`).

They split into two groups. Bug cases are names assigned on every path, which must not be reported: many `elif`s, nested `if`s that cover every path, `set` blocks, tuple unpacking, reading after assigning, and an `if` inside a `for` or a macro. These fail before the patch. Guard cases are names that must still be reported or still come from the context: no `else`, an `elif` that skips the assignment, a nested `if` without `else`, a read before the assignment, a read in an `elif` test, a read before the `if`. These pass before and after. They're there to catch a fix that hides too much.

| Tests | 3.1.6 (before) | 3.1.6 + patch | 3.1.4 (wrong the other way) |
| --- | --- | --- | --- |
| Reproduction tests (Part 1), 2 tests | 2 fail | pass | 1 fails (`if/else`) |
| New `meta` tests, 15 cases | 8 bug cases fail, 7 guards pass | all pass | 9 fail, incl. guards `one-elif-skips` and `read-in-elif-test` |
| New render tests, 5 cases | pass | pass | 2 guards fail (`elif-path-skips`, `elif-test-reads`) |
| New symbol-table tests, 2 tests | 1 fails | pass | pass |
| #1253 regression test (existing) | pass | pass | fails |
| Full suite | 2 failed, 909 passed | 933 passed | — |

Before the patch, exactly the bug cases fail. After it, everything passes. On 3.1.4, which was wrong in the other direction, the guards and the #1253 test fail. So the tests reject both the current behavior and a revert to 3.1.4.

To check it yourself from the repo root, after the setup in Section 1.4:

```bash
.venv/bin/python -m pytest -q                                   # 933 passed
.venv/bin/python -m pytest tests/test_api.py::TestMeta \
    tests/test_core_tags.py::TestIfCondition tests/test_idtracking.py -v
mkdir -p /tmp/j3.1.6 && git archive 3.1.6 src | tar -x -C /tmp/j3.1.6
PYTHONPATH=/tmp/j3.1.6/src .venv/bin/python -m pytest -q \
    tests/test_api.py::TestMeta tests/test_core_tags.py::TestIfCondition \
    tests/test_idtracking.py                                    # 11 failed, 28 passed
```

### 3.4 Remaining limitations

The patch leaves one false positive in place on purpose. In `{% if x %}{% set y = 1 %}{{ y }}{% endif %}`, `y` is only used inside the branch that sets it, so it never comes from the context, yet it's still reported. When `x` is false, `y` is left unassigned after the `if`, and Jinja doesn't track whether `y` is used later. Fixing that needs a "used after this point" analysis, which is a much bigger change than #2069. 3.1.4 behaved the same way.

You can see it in the Part 1 template set. On the patched code 13 of the 14 shapes print `OK`, and this is the only failure:

```bash
.venv/bin/python report/scripts/version_matrix.py
```

```
FAIL use inside the branch only       expected=['x'] got=['x', 'y']
```

And this shows why:

```bash
.venv/bin/python -c "
from jinja2 import Environment, meta
env = Environment()
src = '{% if x %}{% set y = 1 %}{{ y }}{% endif %}'
print(sorted(meta.find_undeclared_variables(env.parse(src))))
print([env.from_string(src).render(x=x, y='CTX') for x in (True, False)])
print([l.strip() for l in env.compile(src, raw=True).splitlines() if 'resolve(' in l])
"
```

```
['x', 'y']
['1', '']
["l_0_x = resolve('x')", "l_0_y = resolve('y')"]
```

The second line shows the context value `'CTX'` never gets printed, so reporting `y` is wrong. The third line is the cause. Next to the expected lookup for `x`, the compiler still emits one for `y`, and `meta` reports it. It's an unused lookup, never a wrong render.

Two smaller points. For names assigned on every path, the compiler now emits `l_0_y = missing` instead of a context lookup. Rendering output doesn't change (the render tests check this), but a custom `Context` subclass that counts or logs lookups would see one fewer. And the `CHANGES.rst` entry sits under an unreleased 3.1.7, which is my guess, since the assignment has me starting from 3.1.6.

---

## 4. Reflection on Coding Agent Performance

### 4.1 What it did well

The agent was at its best when it could run something. Almost every claim in this report came from a command it executed: the version matrix, the decoy renders, the `branch_update` traces, the revert experiment, the before/after test runs. Twice the starting assumption was wrong. The issue called it a 3.1.5 regression, and I said the clone was on 3.1.6. Both times, running code is what exposed it.

It also knew what a test should prove. It asserted equality with `{'control'}` instead of "`output` is not in the result", wrote guard tests that pass both before and after the fix, and ran the new tests against two older versions to show they actually discriminate.

Localization was quick. The graph took it from the public function to `branch_update` without detours, and in Part 2 it read only the three files that mattered.

### 4.2 Where it struggled

Most of its mistakes were small, but they're the kind that end up in a submitted report if nobody checks:

- It built the knowledge graph before checking which version was checked out, so the first graph described `main` and had to be rebuilt. The doc-extraction part of that build cost about 365k tokens and contributed almost nothing to this bug. A code-only graph would have been enough.
- Two tools broke. `graphify query` crashed on a missing `anyio` package and `gh` wasn't installed. It worked around both, reading `graph.json` directly and fetching the issue through a subagent, but the fetch only returned a summary of the issue. The first reproduction test's template is rebuilt from that summary rather than copied.
- It sometimes wrote results down before checking them. In Part 1 it listed the names of the passing `TestMeta` tests from memory and verified them afterwards; they happened to be right. In Part 3 the expected output it wrote for the limitation example (Section 3.4) was missing the `resolve('x')` line. It only caught that when I asked for the example to be runnable and it ran the snippet exactly as written.
- Its writing ran long. The first Part 1 report had a full exploration log, a call-path diagram, a screenshot checklist, and lines like "Part 1 is complete" in a document meant for a grader. I had to ask for 2–4 pages focused on the bug and the tests. It also kept proposing figures, and I removed four of them.
- The reproduction steps used `git switch hw3-fix-2069` without saying the branch already existed on the remote. I had to ask why it was switching instead of branching.

### 4.3 Incorrect fixes and premature claims

It never committed a wrong fix. The closest it came was the 3.1.4 revert, which it tested and rejected on its own before ever suggesting it. The premature claims were all in the write-up, not the code: the unchecked test names, the wrong expected output in Section 3.4, and "Part 1 is complete". The agent caught the first one itself. I caught the other two by reading what it produced and asking it to run or cut things.

### 4.4 How much I intervened

Very little on the technical side. Over the whole session I sent 13 prompts, and none of them corrected its analysis or its patch. They were about scope ("focus on what the bug is and how to reproduce it", "keep it 2–4 pages"), presentation (which figures to keep), and publishing (the repo URL, commit, push). I took the failing-test screenshot myself. The prompts that changed the outcome most were questions: "why are we switching here?", "why do we even need figure 2?", and asking for a way to *see* the limitation. Each one made the agent justify or demonstrate something it had only asserted.

### 4.5 What this says about coding agents

For a bug like this one, in a mature project with a fast test suite, the agent did the bulk of the real work. It found the code, explained the history, rejected the wrong fix, and wrote a correct one with tests that prove it.

It still needed someone checking its output, and mostly not the code. The code was backed by tests, and the tests were backed by runs against three versions. The weak spots were the things that weren't tied to an execution: details written from memory, how much to write, and what a reader actually needs. My takeaway is that you can trust an agent about as far as its claims trace back to something it ran. Everything else needs a person to read it.
