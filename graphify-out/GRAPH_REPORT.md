# Graph Report - jinja  (2026-11-23)

## Corpus Check
- 73 files · ~103,285 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 13 file(s) not represented in the graph (top: .in 5, (none) 4, .bat 1)

## Summary
- 2835 nodes · 5557 edges · 168 communities (81 shown, 87 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 693 edges (avg confidence: 0.87)
- Token cost: 365,098 input · 0 output

## Graph Freshness
- Built from commit: `15206881`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Filter Test Suite
- AST Node Classes
- Lexer and Stdlib Imports
- TemplateNotFound
- Parser Statement Parsing
- Regression Tests and Undefined
- Any
- Changelog and README Concepts
- internalcode
- Expression AST Nodes
- Any
- Token Stream Handling
- Async Filter Tests
- Native Types
- Eval Context and Constants
- Syntax Parsing Tests
- Node Visitor and Optimizer
- Built-in Filters Core
- Code Generator Core
- Publish Workflow CI
- Tests Workflow CI
- Runtime Context and Modules
- Lstrip Blocks Tests
- .writeline
- ._make_node
- Any
- Async For Loop Tests
- i18n Extension
- For Loop Tests
- Inheritance Tests
- .visit_Output
- Lexer and Parser Tests
- UndeclaredNameVisitor
- Extension Base Classes
- Loader Test Fixtures
- Environment
- Async Filter Variants
- TestInternationalization
- Loop Context Runtime
- Async Native Tests
- pickle
- Sandbox Attribute Safety
- Builtin Tests Suite
- Lock Workflow CI
- .parse_subscript
- InternationalizationExtension
- conftest.py
- Namespace Utility
- Undefined
- Async-aware Filter Decorators
- FilterArgumentError
- Attribute and Text Filters
- LRU Cache
- API Reference Docs
- tests.py
- Undefined API Tests
- Set Tag Tests
- Newstyle i18n Tests
- Trim Blocks Tests
- Intro and FAQ Concepts
- .visit_Block
- Sandbox String Format
- LRU Cache Tests
- Extended API Tests
- test_runtime.py
- Undefined Types Docs
- Extensions Docs
- Bucket
- make_logging_undefined
- .wrap_str_format
- If and With Tests
- Macro Tests
- Context and Meta Docs
- Sorting and Default Filters
- Template Streaming
- .call_method
- FileSystemLoader
- Loader Uptodate Checks
- Block and Template References
- utils.py
- Extension Tests
- Loader Tests
- ModuleLoader Tests
- environment.py
- Example Extension Tests
- TestParser
- Select and Reject Filters
- Sandbox Security Tests
- Template Control Structures Docs
- ModuleLoader
- Meta Tracking Generator
- Loop Render Runtime
- Immutable Sandbox
- Any
- nativetypes.py
- i18n Integration Docs
- jinja2/__init__.py
- TemplateModule
- Escaping and JSON Filters
- Async Loop Context
- Cycler Utility
- Async Function Tests
- Debug Tests
- Import Tests
- _make_unop
- Autoescape Extension Tests
- Assignments and Escaping Docs
- Macros and Autoescape Docs
- TestBugFix
- test_mock_not_pass_arg_marker
- CompilerExit
- test_async.py
- Async Include Tests
- TestCorner
- Loader Docs
- Exception Hierarchy Docs
- Template Inheritance Docs
- Loops Docs
- .readthedocs.yaml
- Attribute Getter Sorting
- Meta Module
- Autoescape Selection
- Async Import Tests
- Variables and Tests Docs
- Global Functions Docs
- Include and Import Docs
- Issue Template Config
- Pre-commit Config
- Filter Magic Fixture B
- Integration and Tricks Docs
- Built-in Extensions Docs
- Async Iterator Adapter
- InternalName Node
- .compile_expression
- Low-level API Tests
- Streaming Tests
- Safe Range
- Sandbox SecurityError
- URL Encoding Filter
- Groupby Tuple
- NodeType Metaclass
- Open If Exists
- Extension Scope Tests
- GitHub Issue Templates
- Devcontainer Setup Script
- TestIncludes
- Clear Caches Doc
- Count Newlines Doc
- Impossible Exception Doc
- Raw Block Doc
- Active Menu Trick
- Jinja2 Package Metadata

## God Nodes (most connected - your core abstractions)
1. `CodeGenerator` - 106 edges
2. `TestFilter` - 102 edges
3. `Environment` - 85 edges
4. `Frame` - 84 edges
5. `Parser` - 60 edges
6. `Expr` - 55 edges
7. `Undefined` - 54 edges
8. `TestBug` - 51 edges
9. `Node` - 47 edges
10. `EvalContext` - 46 edges

## Surprising Connections (you probably didn't know these)
- `test_undefined_native_return()` --uses--> `Undefined`  [INFERRED]
  tests/test_nativetypes.py → src/jinja2/runtime.py
- `tests broken.html fixture (calls fail())` --semantically_similar_to--> `broken.html example template`  [INFERRED] [semantically similar]
  tests/res/templates/broken.html → examples/basic/templates/broken.html
- `customfilter()` --calls--> `auto_aiter()`  [EXTRACTED]
  tests/test_async_filters.py → src/jinja2/async_utils.py
- `test_async_iteration_in_templates_extended()` --calls--> `auto_aiter()`  [EXTRACTED]
  tests/test_async.py → src/jinja2/async_utils.py
- `TestLowLevel` --uses--> `CodeGenerator`  [INFERRED]
  tests/test_api.py → src/jinja2/compiler.py

## Import Cycles
- 2-file cycle: `src/jinja2/__init__.py -> src/jinja2/environment.py -> src/jinja2/__init__.py`
- 3-file cycle: `src/jinja2/__init__.py -> src/jinja2/environment.py -> src/jinja2/compiler.py -> src/jinja2/__init__.py`
- 3-file cycle: `src/jinja2/__init__.py -> src/jinja2/environment.py -> src/jinja2/parser.py -> src/jinja2/__init__.py`
- 4-file cycle: `src/jinja2/__init__.py -> src/jinja2/environment.py -> src/jinja2/compiler.py -> src/jinja2/idtracking.py -> src/jinja2/__init__.py`
- 4-file cycle: `src/jinja2/__init__.py -> src/jinja2/environment.py -> src/jinja2/compiler.py -> src/jinja2/optimizer.py -> src/jinja2/__init__.py`

## Hyperedges (group relationships)
- **HTML Escaping System** — docs_templates_html_escaping, docs_templates_manual_escaping, docs_templates_automatic_escaping, docs_templates_markupsafe_markup, docs_templates_safe_filter, docs_templates_autoescape_overrides [EXTRACTED 1.00]
- **Template Inheritance Mechanism** — docs_templates_template_inheritance, docs_templates_extends_tag, docs_templates_block_tag, docs_templates_super_blocks, docs_templates_scoped_blocks, docs_templates_required_blocks, docs_templates_self_variable [EXTRACTED 1.00]
- **pass_* decorators supplying runtime objects to filters and tests** — docs_api_pass_context, docs_api_pass_eval_context, docs_api_pass_environment, docs_api_context, docs_api_evalcontext, docs_api_environment [EXTRACTED 1.00]
- **Built-in Template Loaders** — docs_api_packageloader, docs_api_filesystemloader, docs_api_dictloader, docs_api_functionloader, docs_api_prefixloader, docs_api_choiceloader, docs_api_moduleloader, docs_api_baseloader [EXTRACTED 1.00]
- **Templates that deliberately fail to exercise error reporting** — examples_basic_templates_broken_broken_template, examples_basic_templates_subbroken_may_break, tests_res_templates_broken_broken_template, tests_res_templates_syntaxerror_syntaxerror_template, changes_traceback_rewriting [INFERRED 0.75]
- **Scope Management Constructs** — docs_templates_assignments, docs_templates_namespace, docs_templates_with_statement, docs_templates_scoped_blocks, docs_templates_import_context_behavior [INFERRED 0.85]
- **Contribution workflow documents** — _github_issue_template_bug_report_bug_report_template, _github_issue_template_feature_request_feature_request_template, _github_pull_request_template_pull_request_template, changes_jinja_changelog [INFERRED 0.85]
- **Extension parsing pipeline: Extension -> Parser -> TokenStream -> Token -> AST nodes** — docs_extensions_extension, docs_extensions_parser, docs_extensions_tokenstream, docs_extensions_token, docs_extensions_ast_nodes [INFERRED 0.85]
- **tests/res/templates loader test fixtures** — tests_res_templates_test_test_template, tests_res_templates_foo_test_foo_template, tests_res_templates_mojibake_mojibake_fixture, tests_res_templates_broken_broken_template, tests_res_templates_syntaxerror_syntaxerror_template [INFERRED 0.85]

## Communities (168 total, 87 thin omitted)

### Community 1 - "AST Node Classes"
Cohesion: 0.05
Nodes (31): Add, And, Assign, AssignBlock, BinExpr, Block, Break, CallBlock (+23 more)

### Community 2 - "Lexer and Stdlib Imports"
Cohesion: 0.05
Nodes (13): InlineGettext, TemplateAssertionError, TemplateError, TemplateSyntaxError, compile_rules(), count_newlines(), describe_token_expr(), _describe_token_type() (+5 more)

### Community 3 - "TemplateNotFound"
Cohesion: 0.08
Nodes (7): TemplateNotFound, BaseLoader, ChoiceLoader, FunctionLoader, _get_zipimporter_files(), PrefixLoader, TestByteCodeCache

### Community 4 - "Parser Statement Parsing"
Cohesion: 0.08
Nodes (4): describe_token(), NSRef, Parser, parse()

### Community 5 - "Regression Tests and Undefined"
Cohesion: 0.04
Nodes (3): test_unicode_whitespace(), TestBug, test()

### Community 6 - "Any"
Cohesion: 0.12
Nodes (3): Macro, markup_join(), str_join()

### Community 7 - "Changelog and README Concepts"
Cohesion: 0.06
Nodes (45): Pull request template, Async mode (enable_async), Bytecode cache system, FileSystemLoader, i18n extension ({% trans %}, gettext/pgettext), Jinja Changelog (CHANGES.rst), MarkupSafe dependency, NativeEnvironment / NativeTemplate (+37 more)

### Community 9 - "Expression AST Nodes"
Cohesion: 0.07
Nodes (16): Call, Compare, Concat, CondExpr, DerivedContextReference, EnvironmentAttribute, Expr, ExtensionAttribute (+8 more)

### Community 10 - "Any"
Cohesion: 0.07
Nodes (4): get_spontaneous_environment(), Template, to_list(), TemplateExpression

### Community 11 - "Token Stream Handling"
Cohesion: 0.08
Nodes (5): Token, TokenStream, TokenStreamIterator, StreamFilterExtension, TestTokenStream

### Community 12 - "Async Filter Tests"
Cohesion: 0.08
Nodes (33): _asyncio_run(), closing_factory(), closing(), env_async(), make_aiter(), mark_dualiter(), decorator(), run_async_fn() (+25 more)

### Community 13 - "Native Types"
Cohesion: 0.08
Nodes (5): env(), test_booleans(), test_no_intermediate_eval(), test_spontaneous_env(), test_undefined_native_return()

### Community 14 - "Eval Context and Constants"
Cohesion: 0.13
Nodes (5): args_as_const(), EvalContext, get_eval_context(), Impossible, const()

### Community 16 - "Node Visitor and Optimizer"
Cohesion: 0.08
Nodes (4): write_expr2(), Node, _dump(), VisitCallable

### Community 17 - "Built-in Filters Core"
Cohesion: 0.05
Nodes (18): do_batch(), do_capitalize(), do_center(), do_filesizeformat(), do_float(), do_indent(), do_int(), do_lower() (+10 more)

### Community 18 - "Code Generator Core"
Cohesion: 0.10
Nodes (5): CodeGenerator, Frame, optimizeconst(), Filter, Test

### Community 19 - "Publish Workflow CI"
Cohesion: 0.05
Nodes (44): outputs, runs-on, steps, needs, permissions, runs-on, steps, GH_TOKEN (+36 more)

### Community 20 - "Tests Workflow CI"
Cohesion: 0.06
Nodes (33): name, os, python, tox, jobs, tests, typing, include (+25 more)

### Community 21 - "Runtime Context and Modules"
Cohesion: 0.09
Nodes (5): get_template_locals(), DebugExtension, Context, _dict_method_all(), f_all()

### Community 24 - "._make_node"
Cohesion: 0.10
Nodes (10): Const, ContextReference, Helper, Keyword, MarkSafeIfAutoescape, Mod, Operand, Output (+2 more)

### Community 25 - "Any"
Cohesion: 0.05
Nodes (11): DependencyFinderVisitor, find_symbols(), FrameSymbolVisitor, RootVisitor, Symbols, symbols_for_node(), test_basics(), test_complex() (+3 more)

### Community 27 - "i18n Extension"
Cohesion: 0.16
Nodes (10): _make_new_gettext(), gettext(), _make_new_ngettext(), ngettext(), _make_new_npgettext(), npgettext(), _make_new_pgettext(), pgettext() (+2 more)

### Community 33 - "Extension Base Classes"
Cohesion: 0.13
Nodes (3): ExprStmtExtension, Extension, LoopControlExtension

### Community 34 - "Loader Test Fixtures"
Cohesion: 0.12
Nodes (8): package_dir_loader(), package_file_loader(), package_zip_loader(), test_package_dir_list(), test_package_file_list(), test_package_loader_no_dir(), test_package_zip_list(), test_pep_451_import_hook()

### Community 35 - "Environment"
Cohesion: 0.11
Nodes (8): Environment, test_block_set_vars_unpacking_deterministic(), test_filters_deterministic(), test_import_as_with_context_deterministic(), test_loop_set_vars_unpacking_deterministic(), test_top_level_set_vars_unpacking_deterministic(), test_undefined_import_curly_name(), test_env()

### Community 36 - "Async Filter Variants"
Cohesion: 0.19
Nodes (19): async_variant(), auto_aiter(), auto_to_list(), async_select_or_reject(), do_first(), do_groupby(), do_join(), do_list() (+11 more)

### Community 37 - "TestInternationalization"
Cohesion: 0.05
Nodes (5): babel_extract(), _CommentFinder, TestMeta, TestInternationalization, test_template_hash()

### Community 38 - "Loop Context Runtime"
Cohesion: 0.16
Nodes (4): LoopContext, test_loopcontext0(), test_loopcontext1(), test_loopcontext2()

### Community 39 - "Async Native Tests"
Cohesion: 0.20
Nodes (8): run_async_fn(), test_async_blocks(), test_async_extend(), test_basic_async(), func(), test_basic_generate_async(), test_blocks_generate_async(), test_include_generate_async()

### Community 40 - "pickle"
Cohesion: 0.22
Nodes (3): fs_env(), test_environment(), test_pickle_missing()

### Community 43 - "Lock Workflow CI"
Cohesion: 0.11
Nodes (18): concurrency, group, jobs, lock, runs-on, steps, name, on (+10 more)

### Community 44 - ".parse_subscript"
Cohesion: 0.11
Nodes (8): Dict, Getattr, Getitem, List, Literal, Slice, TemplateData, Tuple

### Community 45 - "InternationalizationExtension"
Cohesion: 0.12
Nodes (3): extract_from_ast(), _gettext_alias(), InternationalizationExtension

### Community 46 - "conftest.py"
Cohesion: 0.19
Nodes (7): choice_loader(), dict_loader(), env(), filesystem_loader(), function_loader(), package_loader(), prefix_loader()

### Community 49 - "Undefined"
Cohesion: 0.06
Nodes (10): copy_cache(), create_cache(), _environment_config_check(), load_extensions(), ChainableUndefined, StrictUndefined, Undefined, import_string() (+2 more)

### Community 50 - "Async-aware Filter Decorators"
Cohesion: 0.17
Nodes (7): decorator(), is_async(), wrapper(), do_replace(), do_xmlattr(), sync_do_join(), pass_eval_context()

### Community 51 - "FilterArgumentError"
Cohesion: 0.11
Nodes (8): FilterArgumentError, do_format(), do_reverse(), do_round(), do_urlize(), prepare_select_or_reject(), urlize(), TestEscapeUrlizeTarget

### Community 52 - "Attribute and Text Filters"
Cohesion: 0.10
Nodes (11): do_attr(), do_last(), do_max(), do_min(), do_truncate(), do_wordwrap(), _min_or_max(), sync_do_first() (+3 more)

### Community 54 - "API Reference Docs"
Cohesion: 0.17
Nodes (14): Jinja API Reference, Bucket (jinja2.bccache.Bucket), BytecodeCache, Environment, FileSystemBytecodeCache, MemcachedBytecodeCache, PackageLoader, Template (+6 more)

### Community 55 - "tests.py"
Cohesion: 0.05
Nodes (21): test_boolean(), test_defined(), test_divisibleby(), test_escaped(), test_even(), test_false(), test_float(), test_in() (+13 more)

### Community 60 - "Intro and FAQ Concepts"
Cohesion: 0.15
Nodes (10): select_autoescape, Changes (changelog), Why is it called Jinja, Jinja Documentation Index, Flask, Babel (optional dependency), Installation, Jinja Templating Engine (+2 more)

### Community 62 - "Sandbox String Format"
Cohesion: 0.23
Nodes (3): SandboxedEnvironment, TestStringFormat, TestStringFormatMap

### Community 65 - "test_runtime.py"
Cohesion: 0.14
Nodes (9): build_pattern(), collapse_ranges(), get_characters(), main(), test_iterator_not_advanced_early(), test_undefined_copy(), test_undefined_deepcopy(), test_undefined_pickle() (+1 more)

### Community 66 - "Undefined Types Docs"
Cohesion: 0.16
Nodes (12): ChainableUndefined, DebugUndefined, is_undefined, make_logging_undefined, StrictUndefined, Undefined, ImmutableSandboxedEnvironment, is_internal_attribute (+4 more)

### Community 67 - "Extensions Docs"
Cohesion: 0.20
Nodes (13): AST Nodes (jinja2.nodes.Node), Autoescape Extension (jinja2.ext.autoescape), cachelib, Debug Extension (jinja2.ext.debug), Expression Statement Extension (jinja2.ext.do), Extension (jinja2.ext.Extension), Jinja Extensions, FragmentCacheExtension (cache tag example) (+5 more)

### Community 68 - "Bucket"
Cohesion: 0.05
Nodes (8): Bucket, BytecodeCache, FileSystemBytecodeCache, MemcachedBytecodeCache, env(), MockMemcached, Error, TestMemcachedBytecodeCache

### Community 69 - "make_logging_undefined"
Cohesion: 0.19
Nodes (6): make_logging_undefined(), __bool__(), _fail_with_undefined_error(), __iter__(), _log_message(), __str__()

### Community 71 - "If and With Tests"
Cohesion: 0.14
Nodes (3): env_trim(), TestIfCondition, TestWith

### Community 73 - "Context and Meta Docs"
Cohesion: 0.19
Nodes (12): Context (jinja2.runtime.Context), Custom Filters, Custom Tests, EvalContext (Evaluation Context), jinja2.meta.find_referenced_templates, jinja2.meta.find_undeclared_variables, Low Level API, Meta API (+4 more)

### Community 74 - "Sorting and Default Filters"
Cohesion: 0.18
Nodes (6): do_default(), do_dictsort(), sort_func(), do_items(), ignore_case(), sync_do_sum()

### Community 78 - "Loader Uptodate Checks"
Cohesion: 0.21
Nodes (6): PackageLoader, split_template_path(), test_package_dir_source(), test_package_file_source(), test_package_zip_omit_curdir(), test_package_zip_source()

### Community 80 - "utils.py"
Cohesion: 0.07
Nodes (8): consume(), generate_lorem_ipsum(), Joiner, _MissingType, Magic, test_consume(), test_missing(), TestLoremIpsum

### Community 84 - "environment.py"
Cohesion: 0.10
Nodes (10): auto_await(), TemplateRuntimeError, TemplatesNotFound, UndefinedError, optimize(), Optimizer, new_context(), _PassArg (+2 more)

### Community 85 - "Example Extension Tests"
Cohesion: 0.24
Nodes (8): DerivedExampleExtension, ExampleExtension, _get_with_context(), gettext(), ngettext(), npgettext(), pgettext(), PreprocessorExtension

### Community 87 - "Select and Reject Filters"
Cohesion: 0.19
Nodes (7): do_random(), select_or_reject(), sync_do_reject(), sync_do_rejectattr(), sync_do_select(), sync_do_selectattr(), pass_context()

### Community 88 - "Sandbox Security Tests"
Cohesion: 0.17
Nodes (3): unsafe(), PrivateStuff, PublicStuff

### Community 89 - "Template Control Structures Docs"
Cohesion: 0.24
Nodes (11): Comments, Comparison and Logic Operators, Control Structures, Template Delimiters ({% %}, {{ }}, {# #}), Expressions, Inline if Expression, if Statement, Literals (strings, numbers, lists, tuples, dicts, booleans) (+3 more)

### Community 93 - "Immutable Sandbox"
Cohesion: 0.22
Nodes (4): ImmutableSandboxedEnvironment, TestSandbox, disable_op(), disable_op()

### Community 95 - "nativetypes.py"
Cohesion: 0.16
Nodes (4): has_safe_repr(), fake_traceback(), rewrite_traceback_stack(), NativeEnvironment

### Community 96 - "i18n Integration Docs"
Cohesion: 0.24
Nodes (9): Policies, Environment.extract_translations, i18n Extension (jinja2.ext.i18n), Inline gettext Extension example, Environment.install_gettext_callables, Environment.install_gettext_translations, Environment.install_null_translations, i18n Whitespace Trimming (+1 more)

### Community 97 - "jinja2/__init__.py"
Cohesion: 0.06
Nodes (8): _MemcachedClient, clear_caches(), env(), test_adding_undefined_native_return(), test_is_filter(), test_is_test(), test_name_undefined(), test_name_undefined_in_if()

### Community 99 - "Escaping and JSON Filters"
Cohesion: 0.20
Nodes (4): do_forceescape(), do_mark_safe(), do_tojson(), htmlsafe_json_dumps()

### Community 102 - "Async Function Tests"
Cohesion: 0.27
Nodes (7): test_await_and_macros(), func(), test_await_on_calls(), async_func(), func(), normal_func(), test_await_on_calls_normal_render()

### Community 106 - "_make_unop"
Cohesion: 0.50
Nodes (4): _make_binop(), visitor(), _make_unop(), visitor()

### Community 108 - "Assignments and Escaping Docs"
Cohesion: 0.25
Nodes (8): Assignments (set tag), Block Assignments (set ... endset), List of Builtin Filters (DEFAULT_FILTERS), filter Sections, Filters, HTML Escaping, Manual Escaping (|e filter), with Statement

### Community 109 - "Macros and Autoescape Docs"
Cohesion: 0.32
Nodes (8): Autoescape Overrides (autoescape tag), Automatic Escaping, call Block, Macro Special Variables (varargs, kwargs, caller), Macros, markupsafe.Markup, safe Filter, Template File Extension (.jinja)

### Community 114 - "test_async.py"
Cohesion: 0.12
Nodes (9): async_native_env(), test_async_iteration_in_templates(), test_async_iteration_in_templates_extended(), test_chainable_undefined_aiter(), test_env_async(), test_namespace_awaitable(), _test(), test_native_async() (+1 more)

### Community 117 - "Loader Docs"
Cohesion: 0.29
Nodes (7): BaseLoader, ChoiceLoader, DictLoader, FileSystemLoader, FunctionLoader, ModuleLoader, PrefixLoader

### Community 118 - "Exception Hierarchy Docs"
Cohesion: 0.29
Nodes (7): TemplateAssertionError, TemplateError, TemplateNotFound, TemplateRuntimeError, TemplatesNotFound, TemplateSyntaxError, UndefinedError

### Community 119 - "Template Inheritance Docs"
Cohesion: 0.29
Nodes (7): block Tag, Required Blocks, Scoped Blocks, self Variable (self.BLOCKNAME), Super Blocks (super(), super.super()), Template Inheritance, TemplateRuntimeError

### Community 120 - "Loops Docs"
Cohesion: 0.33
Nodes (7): jinja2.Environment, for Loop, Line Statements and Line Comments, Loop Controls (break, continue), Loop Filtering, Recursive Loops, Whitespace Control (trim_blocks, lstrip_blocks, +/- modifiers)

### Community 121 - ".readthedocs.yaml"
Cohesion: 0.14
Nodes (13): build, os, tools, method, path, requirements, python, install (+5 more)

### Community 123 - "Attribute Getter Sorting"
Cohesion: 0.20
Nodes (6): do_sort(), make_attrgetter(), attrgetter(), make_multi_attrgetter(), _prepare_attribute_parts(), sync_do_unique()

### Community 125 - "Autoescape Selection"
Cohesion: 0.17
Nodes (4): DebugUndefined, object_type_repr(), select_autoescape(), TestHelpers

### Community 128 - "Variables and Tests Docs"
Cohesion: 0.40
Nodes (5): List of Builtin Tests (DEFAULT_TESTS), Other Operators (in, is, |, ~, (), ., []), Tests (is operator), Undefined Value, Template Variables

### Community 129 - "Global Functions Docs"
Cohesion: 0.40
Nodes (6): cycler, debug Statement, Global Functions (range, lipsum, dict), joiner, Special loop Variable (index, cycle, depth, previtem, changed), namespace

### Community 130 - "Include and Import Docs"
Cohesion: 0.47
Nodes (5): extends Tag, FileSystemLoader, import / from-import Tag, include Tag, Template Objects in extends/include/import

### Community 131 - "Issue Template Config"
Cohesion: 0.33
Nodes (5): blank_issues_enabled, contact_links, about, name, url

### Community 132 - "Pre-commit Config"
Cohesion: 0.25
Nodes (7): ci, autoupdate_schedule, id, repos, hooks, repo, rev

### Community 136 - "Integration and Tricks Docs"
Cohesion: 0.40
Nodes (5): Django integration, loop.cycle (replacement for Django cycle tag), Switching from Django Templates, Accessing the Parent Loop, Alternating Rows

### Community 137 - "Built-in Extensions Docs"
Cohesion: 0.40
Nodes (5): Expression Statement (do tag), Built-in Template Extensions, gettext / ngettext / pgettext / npgettext, i18n trans Block, Newstyle gettext

## Knowledge Gaps
- **69 isolated node(s):** `Jinja2`, `List of Builtin Filters (DEFAULT_FILTERS)`, `Autoescape Overrides (autoescape tag)`, `Template File Extension (.jinja)`, `ChoiceLoader` (+64 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1149 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **87 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Environment` connect `Environment` to `Filter Test Suite`, `AST Node Classes`, `Lexer and Stdlib Imports`, `TemplateNotFound`, `Parser Statement Parsing`, `internalcode`, `Any`, `Token Stream Handling`, `Eval Context and Constants`, `.compile_expression`, `Built-in Filters Core`, `Code Generator Core`, `Runtime Context and Modules`, `Extension Base Classes`, `TestInternationalization`, `InternationalizationExtension`, `conftest.py`, `Undefined`, `TestIncludes`, `tests.py`, `Sandbox String Format`, `.wrap_str_format`, `.call_method`, `environment.py`, `ModuleLoader`, `nativetypes.py`, `jinja2/__init__.py`?**
  _High betweenness centrality (0.191) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `CodeGenerator` (e.g. with `TemplateAssertionError` and `EvalContext`) actually correct?**
  _`CodeGenerator` has 5 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Jinja2`, `List of Builtin Filters (DEFAULT_FILTERS)`, `Autoescape Overrides (autoescape tag)` to the rest of the system?**
  _69 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Filter Test Suite` be split into smaller, more focused modules?**
  _Cohesion score 0.03766042499474016 - nodes in this community are weakly interconnected._
- **Why does `CodeGenerator` connect `Code Generator Core` to `Lexer and Stdlib Imports`, `Environment`, `Eval Context and Constants`, `.newline`, `Node Visitor and Optimizer`, `Low-level API Tests`, `environment.py`, `nativetypes.py`, `.writeline`, `.mark_parameter_stored`, `Meta Tracking Generator`, `.visit_Block`, `.visit_Output`, `.push_parameter_definitions`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Are the 25 inferred relationships involving `Environment` (e.g. with `CodeGenerator` and `TemplateNotFound`) actually correct?**
  _`Environment` has 25 INFERRED edges - model-reasoned connections that need verification._
- **Should `AST Node Classes` be split into smaller, more focused modules?**
  _Cohesion score 0.04971751412429379 - nodes in this community are weakly interconnected._