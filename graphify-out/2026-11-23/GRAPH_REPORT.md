# Graph Report - jinja  (2026-11-23)

## Corpus Check
- 99 files · ~102,996 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 4, .bat 1, .typed 1)

## Summary
- 2848 nodes · 5549 edges · 190 communities (86 shown, 104 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 697 edges (avg confidence: 0.87)
- Token cost: 365,098 input · 0 output

## Community Hubs (Navigation)
- Filter Test Suite
- AST Node Classes
- Lexer and Stdlib Imports
- Loaders and Examples
- Parser Statement Parsing
- Regression Tests and Undefined
- Runtime Errors and Macros
- Changelog and README Concepts
- Environment and Formatters
- Expression AST Nodes
- Template Object and Utils
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
- Compiler Loop and Identifiers
- Literal and Helper Nodes
- Frame Symbol Visitor
- Async For Loop Tests
- i18n Extension
- For Loop Tests
- Inheritance Tests
- Compiler Frames and Finalize
- Lexer and Parser Tests
- Compiler Helpers
- Extension Base Classes
- Loader Test Fixtures
- Environment Compile Helpers
- Async Filter Variants
- i18n Babel Tests
- Loop Context Runtime
- Async Native Tests
- Bytecode Cache Tests
- Sandbox Attribute Safety
- Builtin Tests Suite
- Lock Workflow CI
- Pre-commit Workflow CI
- Symbol Tracking
- Test Conftest Fixtures
- Namespace Utility
- Environment Cache and Config
- Async-aware Filter Decorators
- Format and Map Filters
- Attribute and Text Filters
- LRU Cache
- API Reference Docs
- Builtin Test Functions
- Undefined API Tests
- Set Tag Tests
- Newstyle i18n Tests
- Trim Blocks Tests
- Intro and FAQ Concepts
- Macro References
- Sandbox String Format
- LRU Cache Tests
- Extended API Tests
- Runtime Tests
- Undefined Types Docs
- Extensions Docs
- Bytecode Bucket
- Filter and Test Nodes
- Dependency Finder Visitor
- If and With Tests
- Macro Tests
- Context and Meta Docs
- Sorting and Default Filters
- Template Streaming
- Lexer Rules
- FileSystemLoader
- Loader Uptodate Checks
- Block and Template References
- Lorem Ipsum Generator
- Extension Tests
- Loader Tests
- ModuleLoader Tests
- Async Utilities
- Example Extension Tests
- Select and Reject Filters
- Sandbox Security Tests
- Template Control Structures Docs
- Pickle and Missing Tests
- Meta Tracking Generator
- Loop Render Runtime
- Immutable Sandbox
- Object Tests
- Traceback Rewriting
- i18n Integration Docs
- Memcached Bytecode Client
- Meta API Tests
- Escaping and JSON Filters
- Async Loop Context
- Cycler Utility
- Async Function Tests
- Debug Tests
- Import Tests
- Identifier Pattern Script
- Autoescape Extension Tests
- Assignments and Escaping Docs
- Macros and Autoescape Docs
- FileSystem Bytecode Cache
- Memcached Bytecode Cache
- Symbols for Node
- Async Helper Tests
- Async Include Tests
- Corner Case Tests
- Loader Docs
- Exception Hierarchy Docs
- Template Inheritance Docs
- Loops Docs
- ReadTheDocs Config
- Attribute Getter Sorting
- Meta Module
- Autoescape Selection
- Async Import Tests
- Memcached Mock
- Variables and Tests Docs
- Global Functions Docs
- Include and Import Docs
- Issue Template Config
- Pre-commit Config
- Filter Magic Fixture B
- Jinja Logo SVG
- Integration and Tricks Docs
- Built-in Extensions Docs
- Async Iterator Adapter
- Comment Finder
- InternalName Node
- Template Node
- Low-level API Tests
- Streaming Tests
- Jinja Name Logo
- Safe Range
- BytecodeCache Base
- Sandbox SecurityError
- URL Encoding Filter
- Groupby Tuple
- NodeType Metaclass
- Jinja Icon SVG
- Container Test
- Missing Sentinel
- Open If Exists
- Extension Scope Tests
- Filter Magic Fixture A
- GitHub Issue Templates
- Devcontainer Setup Script
- Node Dump Helper
- Builtin Test A
- Builtin Test B
- Builtin Test C
- Builtin Test D
- Builtin Test E
- Builtin Test F
- Builtin Test G
- Builtin Test H
- Escaped Test
- Builtin Test I
- Builtin Test J
- Builtin Test K
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
- `InlineGettext` --uses--> `Token`  [INFERRED]
  docs/examples/inline_gettext_extension.py → src/jinja2/lexer.py
- `customfilter()` --calls--> `auto_aiter()`  [EXTRACTED]
  tests/test_async_filters.py → src/jinja2/async_utils.py
- `test_async_iteration_in_templates_extended()` --calls--> `auto_aiter()`  [EXTRACTED]
  tests/test_async.py → src/jinja2/async_utils.py

## Import Cycles
- 2-file cycle: `src/jinja2/__init__.py -> src/jinja2/environment.py -> src/jinja2/__init__.py`
- 3-file cycle: `src/jinja2/__init__.py -> src/jinja2/environment.py -> src/jinja2/parser.py -> src/jinja2/__init__.py`
- 3-file cycle: `src/jinja2/__init__.py -> src/jinja2/environment.py -> src/jinja2/compiler.py -> src/jinja2/__init__.py`
- 4-file cycle: `src/jinja2/__init__.py -> src/jinja2/environment.py -> src/jinja2/compiler.py -> src/jinja2/optimizer.py -> src/jinja2/__init__.py`
- 4-file cycle: `src/jinja2/__init__.py -> src/jinja2/environment.py -> src/jinja2/compiler.py -> src/jinja2/idtracking.py -> src/jinja2/__init__.py`

## Hyperedges (group relationships)
- **Template Inheritance Mechanism** — docs_templates_template_inheritance, docs_templates_extends_tag, docs_templates_block_tag, docs_templates_super_blocks, docs_templates_scoped_blocks, docs_templates_required_blocks, docs_templates_self_variable [EXTRACTED 1.00]
- **Scope Management Constructs** — docs_templates_assignments, docs_templates_namespace, docs_templates_with_statement, docs_templates_scoped_blocks, docs_templates_import_context_behavior [INFERRED 0.85]
- **HTML Escaping System** — docs_templates_html_escaping, docs_templates_manual_escaping, docs_templates_automatic_escaping, docs_templates_markupsafe_markup, docs_templates_safe_filter, docs_templates_autoescape_overrides [EXTRACTED 1.00]
- **Built-in Template Loaders** — docs_api_packageloader, docs_api_filesystemloader, docs_api_dictloader, docs_api_functionloader, docs_api_prefixloader, docs_api_choiceloader, docs_api_moduleloader, docs_api_baseloader [EXTRACTED 1.00]
- **pass_* decorators supplying runtime objects to filters and tests** — docs_api_pass_context, docs_api_pass_eval_context, docs_api_pass_environment, docs_api_context, docs_api_evalcontext, docs_api_environment [EXTRACTED 1.00]
- **Extension parsing pipeline: Extension -> Parser -> TokenStream -> Token -> AST nodes** — docs_extensions_extension, docs_extensions_parser, docs_extensions_tokenstream, docs_extensions_token, docs_extensions_ast_nodes [INFERRED 0.85]
- **Templates that deliberately fail to exercise error reporting** — examples_basic_templates_broken_broken_template, examples_basic_templates_subbroken_may_break, tests_res_templates_broken_broken_template, tests_res_templates_syntaxerror_syntaxerror_template, changes_traceback_rewriting [INFERRED 0.75]
- **tests/res/templates loader test fixtures** — tests_res_templates_test_test_template, tests_res_templates_foo_test_foo_template, tests_res_templates_mojibake_mojibake_fixture, tests_res_templates_broken_broken_template, tests_res_templates_syntaxerror_syntaxerror_template [INFERRED 0.85]
- **Contribution workflow documents** — _github_issue_template_bug_report_bug_report_template, _github_issue_template_feature_request_feature_request_template, _github_pull_request_template_pull_request_template, changes_jinja_changelog [INFERRED 0.85]

## Communities (190 total, 104 thin omitted)

### Community 1 - "AST Node Classes"
Cohesion: 0.04
Nodes (36): Add, And, Assign, AssignBlock, BinExpr, Block, Break, CallBlock (+28 more)

### Community 2 - "Lexer and Stdlib Imports"
Cohesion: 0.06
Nodes (10): InlineGettext, TemplateAssertionError, TemplateError, TemplateSyntaxError, UndefinedError, count_newlines(), get_lexer(), Lexer (+2 more)

### Community 3 - "Loaders and Examples"
Cohesion: 0.05
Nodes (11): TemplateNotFound, __getattr__(), BaseLoader, ChoiceLoader, FunctionLoader, _get_zipimporter_files(), ModuleLoader, PackageLoader (+3 more)

### Community 4 - "Parser Statement Parsing"
Cohesion: 0.07
Nodes (4): Name, NSRef, Parser, parse()

### Community 5 - "Regression Tests and Undefined"
Cohesion: 0.04
Nodes (3): ChainableUndefined, TestBug, test()

### Community 6 - "Runtime Errors and Macros"
Cohesion: 0.06
Nodes (15): TemplateRuntimeError, DebugUndefined, Macro, make_logging_undefined(), __bool__(), _fail_with_undefined_error(), __iter__(), _log_message() (+7 more)

### Community 7 - "Changelog and README Concepts"
Cohesion: 0.06
Nodes (45): Pull request template, Async mode (enable_async), Bytecode cache system, FileSystemLoader, i18n extension ({% trans %}, gettext/pgettext), Jinja Changelog (CHANGES.rst), MarkupSafe dependency, NativeEnvironment / NativeTemplate (+37 more)

### Community 8 - "Environment and Formatters"
Cohesion: 0.07
Nodes (6): Environment, TemplatesNotFound, SandboxedEscapeFormatter, SandboxedFormatter, internalcode(), TestIncludes

### Community 9 - "Expression AST Nodes"
Cohesion: 0.08
Nodes (13): Call, Compare, Concat, CondExpr, Expr, Getattr, Getitem, Neg (+5 more)

### Community 10 - "Template Object and Utils"
Cohesion: 0.06
Nodes (5): Template, to_list(), TemplateExpression, consume(), test_consume()

### Community 11 - "Token Stream Handling"
Cohesion: 0.07
Nodes (8): describe_token(), describe_token_expr(), _describe_token_type(), Token, TokenStream, TokenStreamIterator, StreamFilterExtension, TestTokenStream

### Community 12 - "Async Filter Tests"
Cohesion: 0.08
Nodes (31): closing_factory(), closing(), env_async(), make_aiter(), mark_dualiter(), decorator(), test_attribute_map(), test_bool_reject() (+23 more)

### Community 13 - "Native Types"
Cohesion: 0.06
Nodes (10): native_concat(), NativeEnvironment, NativeTemplate, async_native_env(), env(), test_booleans(), test_no_intermediate_eval(), test_spontaneous_env() (+2 more)

### Community 14 - "Eval Context and Constants"
Cohesion: 0.12
Nodes (6): args_as_const(), EvalContext, get_eval_context(), Impossible, MarkSafe, const()

### Community 16 - "Node Visitor and Optimizer"
Cohesion: 0.08
Nodes (5): Node, optimize(), Optimizer, NodeTransformer, VisitCallable

### Community 17 - "Built-in Filters Core"
Cohesion: 0.05
Nodes (18): do_batch(), do_capitalize(), do_center(), do_filesizeformat(), do_float(), do_indent(), do_int(), do_lower() (+10 more)

### Community 18 - "Code Generator Core"
Cohesion: 0.12
Nodes (3): CodeGenerator, write_expr2(), optimizeconst()

### Community 19 - "Publish Workflow CI"
Cohesion: 0.06
Nodes (34): runs-on, steps, needs, permissions, runs-on, steps, GH_TOKEN, name (+26 more)

### Community 20 - "Tests Workflow CI"
Cohesion: 0.06
Nodes (33): name, os, python, tox, jobs, tests, typing, include (+25 more)

### Community 21 - "Runtime Context and Modules"
Cohesion: 0.07
Nodes (6): TemplateModule, DebugExtension, _gettext_alias(), Context, _dict_method_all(), f_all()

### Community 24 - "Literal and Helper Nodes"
Cohesion: 0.07
Nodes (15): Const, ContextReference, Dict, Helper, Keyword, List, Literal, MarkSafeIfAutoescape (+7 more)

### Community 27 - "i18n Extension"
Cohesion: 0.10
Nodes (12): extract_from_ast(), InternationalizationExtension, _make_new_gettext(), gettext(), _make_new_ngettext(), ngettext(), _make_new_npgettext(), npgettext() (+4 more)

### Community 29 - "Inheritance Tests"
Cohesion: 0.07
Nodes (3): env(), TestBugFix, TestInheritance

### Community 30 - "Compiler Frames and Finalize"
Cohesion: 0.12
Nodes (3): _FinalizeInfo, Frame, NativeCodeGenerator

### Community 31 - "Lexer and Parser Tests"
Cohesion: 0.08
Nodes (3): pformat(), TestLexer, TestParser

### Community 32 - "Compiler Helpers"
Cohesion: 0.09
Nodes (9): CompilerExit, has_safe_repr(), _make_binop(), visitor(), _make_unop(), visitor(), UndeclaredNameVisitor, VisitorExit (+1 more)

### Community 33 - "Extension Base Classes"
Cohesion: 0.09
Nodes (4): FragmentCacheExtension, ExprStmtExtension, Extension, LoopControlExtension

### Community 34 - "Loader Test Fixtures"
Cohesion: 0.11
Nodes (9): test_overlay_enable_async(), package_dir_loader(), package_file_loader(), package_zip_loader(), test_package_dir_list(), test_package_file_list(), test_package_loader_no_dir(), test_package_zip_list() (+1 more)

### Community 35 - "Environment Compile Helpers"
Cohesion: 0.15
Nodes (6): DictLoader, test_block_set_vars_unpacking_deterministic(), test_filters_deterministic(), test_import_as_with_context_deterministic(), test_loop_set_vars_unpacking_deterministic(), test_top_level_set_vars_unpacking_deterministic()

### Community 36 - "Async Filter Variants"
Cohesion: 0.17
Nodes (19): async_variant(), auto_aiter(), auto_to_list(), async_select_or_reject(), do_first(), do_groupby(), do_join(), do_list() (+11 more)

### Community 38 - "Loop Context Runtime"
Cohesion: 0.14
Nodes (4): LoopContext, test_loopcontext0(), test_loopcontext1(), test_loopcontext2()

### Community 39 - "Async Native Tests"
Cohesion: 0.12
Nodes (11): async_native_env(), test_async_blocks(), test_async_extend(), test_async_iteration_in_templates(), test_async_iteration_in_templates_extended(), test_basic_async(), func(), test_basic_generate_async() (+3 more)

### Community 40 - "Bytecode Cache Tests"
Cohesion: 0.11
Nodes (9): TestByteCodeCache, test_undefined_import_curly_name(), fs_env(), test_env(), test_adding_undefined_native_return(), test_is_filter(), test_is_test(), test_name_undefined() (+1 more)

### Community 43 - "Lock Workflow CI"
Cohesion: 0.10
Nodes (19): concurrency, group, jobs, lock, runs-on, steps, name, on (+11 more)

### Community 44 - "Pre-commit Workflow CI"
Cohesion: 0.10
Nodes (19): jobs, main, runs-on, steps, name, on, pull_request, push (+11 more)

### Community 46 - "Test Conftest Fixtures"
Cohesion: 0.15
Nodes (9): _asyncio_run(), choice_loader(), dict_loader(), env(), filesystem_loader(), function_loader(), package_loader(), prefix_loader() (+1 more)

### Community 49 - "Environment Cache and Config"
Cohesion: 0.13
Nodes (5): copy_cache(), create_cache(), _environment_config_check(), get_spontaneous_environment(), load_extensions()

### Community 50 - "Async-aware Filter Decorators"
Cohesion: 0.13
Nodes (9): decorator(), is_async(), wrapper(), do_replace(), do_urlize(), do_xmlattr(), pass_eval_context(), urlize() (+1 more)

### Community 51 - "Format and Map Filters"
Cohesion: 0.13
Nodes (9): FilterArgumentError, do_format(), do_map(), do_reverse(), do_round(), func(), prepare_map(), prepare_select_or_reject() (+1 more)

### Community 52 - "Attribute and Text Filters"
Cohesion: 0.12
Nodes (9): do_attr(), do_last(), do_max(), do_min(), do_truncate(), do_wordwrap(), _min_or_max(), sync_do_first() (+1 more)

### Community 54 - "API Reference Docs"
Cohesion: 0.17
Nodes (14): Jinja API Reference, Bucket (jinja2.bccache.Bucket), BytecodeCache, Environment, FileSystemBytecodeCache, MemcachedBytecodeCache, PackageLoader, Template (+6 more)

### Community 55 - "Builtin Test Functions"
Cohesion: 0.12
Nodes (5): test_divisibleby(), test_even(), test_filter(), test_odd(), test_test()

### Community 60 - "Intro and FAQ Concepts"
Cohesion: 0.15
Nodes (10): select_autoescape, Changes (changelog), Why is it called Jinja, Jinja Documentation Index, Flask, Babel (optional dependency), Installation, Jinja Templating Engine (+2 more)

### Community 62 - "Sandbox String Format"
Cohesion: 0.23
Nodes (3): SandboxedEnvironment, TestStringFormat, TestStringFormatMap

### Community 65 - "Runtime Tests"
Cohesion: 0.20
Nodes (5): test_iterator_not_advanced_early(), test_mock_not_pass_arg_marker(), test_undefined_copy(), test_undefined_deepcopy(), test_undefined_pickle()

### Community 66 - "Undefined Types Docs"
Cohesion: 0.16
Nodes (12): ChainableUndefined, DebugUndefined, is_undefined, make_logging_undefined, StrictUndefined, Undefined, ImmutableSandboxedEnvironment, is_internal_attribute (+4 more)

### Community 67 - "Extensions Docs"
Cohesion: 0.20
Nodes (13): AST Nodes (jinja2.nodes.Node), Autoescape Extension (jinja2.ext.autoescape), cachelib, Debug Extension (jinja2.ext.debug), Expression Statement Extension (jinja2.ext.do), Extension (jinja2.ext.Extension), Jinja Extensions, FragmentCacheExtension (cache tag example) (+5 more)

### Community 71 - "If and With Tests"
Cohesion: 0.14
Nodes (3): env_trim(), TestIfCondition, TestWith

### Community 73 - "Context and Meta Docs"
Cohesion: 0.19
Nodes (12): Context (jinja2.runtime.Context), Custom Filters, Custom Tests, EvalContext (Evaluation Context), jinja2.meta.find_referenced_templates, jinja2.meta.find_undeclared_variables, Low Level API, Meta API (+4 more)

### Community 74 - "Sorting and Default Filters"
Cohesion: 0.18
Nodes (6): do_default(), do_dictsort(), sort_func(), do_items(), ignore_case(), sync_do_sum()

### Community 76 - "Lexer Rules"
Cohesion: 0.15
Nodes (4): compile_rules(), Failure, OptionalLStrip, _Rule

### Community 78 - "Loader Uptodate Checks"
Cohesion: 0.23
Nodes (5): split_template_path(), test_package_dir_source(), test_package_file_source(), test_package_zip_omit_curdir(), test_package_zip_source()

### Community 84 - "Async Utilities"
Cohesion: 0.21
Nodes (3): auto_await(), do_striptags(), Joiner

### Community 85 - "Example Extension Tests"
Cohesion: 0.24
Nodes (8): DerivedExampleExtension, ExampleExtension, _get_with_context(), gettext(), ngettext(), npgettext(), pgettext(), PreprocessorExtension

### Community 87 - "Select and Reject Filters"
Cohesion: 0.21
Nodes (6): select_or_reject(), sync_do_reject(), sync_do_rejectattr(), sync_do_select(), sync_do_selectattr(), pass_context()

### Community 88 - "Sandbox Security Tests"
Cohesion: 0.17
Nodes (3): unsafe(), PrivateStuff, PublicStuff

### Community 89 - "Template Control Structures Docs"
Cohesion: 0.24
Nodes (11): Comments, Comparison and Logic Operators, Control Structures, Template Delimiters ({% %}, {{ }}, {# #}), Expressions, Inline if Expression, if Statement, Literals (strings, numbers, lists, tuples, dicts, booleans) (+3 more)

### Community 90 - "Pickle and Missing Tests"
Cohesion: 0.22
Nodes (4): test_environment(), test_copy_missing(), test_missing(), test_pickle_missing()

### Community 93 - "Immutable Sandbox"
Cohesion: 0.22
Nodes (4): ImmutableSandboxedEnvironment, TestSandbox, disable_op(), disable_op()

### Community 94 - "Object Tests"
Cohesion: 0.18
Nodes (5): test_defined(), test_number(), test_sameas(), test_sequence(), test_string()

### Community 95 - "Traceback Rewriting"
Cohesion: 0.22
Nodes (3): fake_traceback(), get_template_locals(), rewrite_traceback_stack()

### Community 96 - "i18n Integration Docs"
Cohesion: 0.24
Nodes (9): Policies, Environment.extract_translations, i18n Extension (jinja2.ext.i18n), Inline gettext Extension example, Environment.install_gettext_callables, Environment.install_gettext_translations, Environment.install_null_translations, i18n Whitespace Trimming (+1 more)

### Community 99 - "Escaping and JSON Filters"
Cohesion: 0.20
Nodes (4): do_forceescape(), do_mark_safe(), do_tojson(), htmlsafe_json_dumps()

### Community 102 - "Async Function Tests"
Cohesion: 0.27
Nodes (7): test_await_and_macros(), func(), test_await_on_calls(), async_func(), func(), normal_func(), test_await_on_calls_normal_render()

### Community 106 - "Identifier Pattern Script"
Cohesion: 0.31
Nodes (4): build_pattern(), collapse_ranges(), get_characters(), main()

### Community 108 - "Assignments and Escaping Docs"
Cohesion: 0.25
Nodes (8): Assignments (set tag), Block Assignments (set ... endset), List of Builtin Filters (DEFAULT_FILTERS), filter Sections, Filters, HTML Escaping, Manual Escaping (|e filter), with Statement

### Community 109 - "Macros and Autoescape Docs"
Cohesion: 0.32
Nodes (8): Autoescape Overrides (autoescape tag), Automatic Escaping, call Block, Macro Special Variables (varargs, kwargs, caller), Macros, markupsafe.Markup, safe Filter, Template File Extension (.jinja)

### Community 113 - "Symbols for Node"
Cohesion: 0.43
Nodes (6): symbols_for_node(), test_basics(), test_complex(), test_if_branching_multi_scope(), test_if_branching_stores(), test_if_branching_stores_undefined()

### Community 114 - "Async Helper Tests"
Cohesion: 0.25
Nodes (5): test_chainable_undefined_aiter(), test_namespace_awaitable(), _test(), test_native_async(), test_native_list_async()

### Community 116 - "Corner Case Tests"
Cohesion: 0.25
Nodes (3): test_load_parameter_when_set_in_all_if_branches(), test_unicode_whitespace(), TestCorner

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

### Community 121 - "ReadTheDocs Config"
Cohesion: 0.29
Nodes (6): build, commands, os, tools, python, version

### Community 123 - "Attribute Getter Sorting"
Cohesion: 0.29
Nodes (4): do_sort(), attrgetter(), make_multi_attrgetter(), _prepare_attribute_parts()

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
Cohesion: 0.33
Nodes (5): id, repos, hooks, repo, rev

### Community 135 - "Jinja Logo SVG"
Cohesion: 0.50
Nodes (5): Rounded Gradient Box Background, Jinja Logo (SVG), Pink-to-Crimson Vertical Gradient (_Linear1), Long Shadow Effect, Torii Gate Icon

### Community 136 - "Integration and Tricks Docs"
Cohesion: 0.40
Nodes (5): Django integration, loop.cycle (replacement for Django cycle tag), Switching from Django Templates, Accessing the Parent Loop, Alternating Rows

### Community 137 - "Built-in Extensions Docs"
Cohesion: 0.40
Nodes (5): Expression Statement (do tag), Built-in Template Extensions, gettext / ngettext / pgettext / npgettext, i18n trans Block, Newstyle gettext

### Community 146 - "Jinja Name Logo"
Cohesion: 0.50
Nodes (4): Jinja Name Logo (logo + wordmark SVG), Jinja Torii Gate Logo Mark, Torii / Shrine Motif (Jinja = shrine), Jinja Wordmark Text

### Community 156 - "Jinja Icon SVG"
Cohesion: 0.67
Nodes (3): Jinja Brand Color #7e0c1b, Jinja Icon (SVG logo), Torii Gate Motif

## Knowledge Gaps
- **74 isolated node(s):** `Jinja2`, `jinja2.Environment`, `Template File Extension (.jinja)`, `Comments`, `Escaping with raw Block` (+69 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1161 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **104 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Environment` connect `Environment and Formatters` to `Filter Test Suite`, `AST Node Classes`, `Lexer and Stdlib Imports`, `Loaders and Examples`, `Parser Statement Parsing`, `Runtime Errors and Macros`, `Template Object and Utils`, `Token Stream Handling`, `Environment Lexer Bridge`, `Native Types`, `Eval Context and Constants`, `Node Visitor and Optimizer`, `Built-in Filters Core`, `Code Generator Core`, `Runtime Context and Modules`, `i18n Extension`, `Compiler Helpers`, `Extension Base Classes`, `Environment Compile Helpers`, `i18n Babel Tests`, `Bytecode Cache Tests`, `Test Conftest Fixtures`, `Environment Cache and Config`, `Builtin Test Functions`, `Sandbox String Format`, `Memcached Bytecode Client`, `Meta API Tests`, `Template Code Objects`, `Environment Parser Bridge`, `Meta Module`?**
  _High betweenness centrality (0.181) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `CodeGenerator` (e.g. with `TemplateAssertionError` and `EvalContext`) actually correct?**
  _`CodeGenerator` has 5 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Jinja2`, `jinja2.Environment`, `Template File Extension (.jinja)` to the rest of the system?**
  _74 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Filter Test Suite` be split into smaller, more focused modules?**
  _Cohesion score 0.03766042499474016 - nodes in this community are weakly interconnected._
- **Why does `CodeGenerator` connect `Code Generator Core` to `Compiler Helpers`, `Lexer and Stdlib Imports`, `Filter and Test Nodes`, `Dependency Finder Visitor`, `Environment and Formatters`, `Eval Context and Constants`, `Compiler Inner Frames`, `Node Visitor and Optimizer`, `Low-level API Tests`, `Compiler Import Visits`, `Compiler Loop and Identifiers`, `Meta Tracking Generator`, `Meta Module`, `Macro References`, `Compiler Frames and Finalize`?**
  _High betweenness centrality (0.082) - this node is a cross-community bridge._
- **Are the 25 inferred relationships involving `Environment` (e.g. with `CodeGenerator` and `TemplateNotFound`) actually correct?**
  _`Environment` has 25 INFERRED edges - model-reasoned connections that need verification._
- **Should `AST Node Classes` be split into smaller, more focused modules?**
  _Cohesion score 0.04134697357203751 - nodes in this community are weakly interconnected._