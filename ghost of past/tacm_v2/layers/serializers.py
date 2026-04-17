"""serializers.py — Per-layer text serializers for the layered graph.

Each layer produces a different resolution of context:

    Layer 0 — File
        "file requests/auth.py
         imports: hashlib, os, re, threading, time, base64
         contains: AuthBase, HTTPBasicAuth, HTTPProxyAuth, HTTPDigestAuth, _basic_auth_str"

        ~20-30 tokens. Architectural overview. Which file, what it imports, what it defines.

    Layer 1 — Class
        "class HTTPDigestAuth(AuthBase)  [requests/auth.py:107]
         methods: __init__, init_per_thread_state, build_digest_header,
                  handle_redirect, handle_401, __call__"

        ~40-70 tokens. Structural overview. What the class is, what it can do.

    Layer 2 — Function
        Full source body.

        ~150 tokens median. Behavioral detail. What the function actually does.

The serializer for each layer is a pure function: LNode + LayeredGraph → str.
Token cost is measured from the output, not estimated.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..graph.model import LayeredGraph, LNode, Layer


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def _short_path(file_path: str) -> str:
    """Return the shortest useful path — strip absolute prefix up to repo root.

    Heuristic: find the last component that looks like a package root
    (contains src/ or is a top-level package dir). Falls back to just
    the last two path components.
    """
    p = Path(file_path)
    parts = p.parts
    # Find 'src' boundary
    for i, part in enumerate(parts):
        if part == 'src' and i + 1 < len(parts):
            return str(Path(*parts[i + 1:]))
    # Fall back: last 3 components
    return str(Path(*parts[-3:])) if len(parts) >= 3 else file_path


def _read_imports(file_path: str, max_imports: int = 8) -> list[str]:
    """Extract top-level import names from source file.

    Uses language-agnostic regex patterns covering the most common import
    styles across languages. Falls back gracefully to empty list for unknown
    syntax — the graph's IMPORTS_FROM edges are the authoritative source;
    this is only used for the file-level summary shown to the agent.

    Patterns covered:
        Python:     import X / from X import Y
        Java/Kotlin: import com.example.Foo;
        Go:         import "pkg/path"
        Rust:       use std::collections::HashMap;
        JS/TS:      import X from 'pkg' / const X = require('pkg')
        C/C++:      #include <header> / #include "header"
        Ruby:       require 'gem'
        Swift:      import Framework
    """
    try:
        lines = Path(file_path).read_text(errors="replace").splitlines()
    except OSError:
        return []

    patterns = [
        # Python: import X.Y / from X.Y import Z
        (r'^import\s+([\w.]+)',           lambda m: m.group(1).split('.')[0]),
        (r'^from\s+([\w.]+)\s+import',    lambda m: m.group(1).lstrip('.').split('.')[0]),
        # Java/Kotlin: import com.example.Foo;
        (r'^import\s+(?:static\s+)?([\w.]+)',  lambda m: m.group(1).split('.')[0]),
        # Go: import "pkg/path" or import alias "pkg/path"
        (r'^import\s+\w*\s*"([\w./\-]+)"', lambda m: m.group(1).split('/')[-1]),
        # Rust: use std::collections::HashMap;
        (r'^use\s+([\w:]+)',              lambda m: m.group(1).split('::')[0]),
        # JS/TS: import X from 'pkg' / import 'pkg'
        (r"^import\s+.*from\s+['\"]([^'\"./][^'\"]*)['\"]", lambda m: m.group(1).split('/')[0]),
        (r"^import\s+['\"]([^'\"./][^'\"]*)['\"]",           lambda m: m.group(1).split('/')[0]),
        # JS require: const X = require('pkg')
        (r"require\s*\(\s*['\"]([^'\"./][^'\"]*)['\"]",      lambda m: m.group(1).split('/')[0]),
        # C/C++ includes
        (r'^#include\s+[<"]([\w./]+)[>"]', lambda m: m.group(1).split('/')[0].split('.')[0]),
        # Ruby
        (r"^require\s+['\"]([^'\"./][^'\"]*)['\"]",          lambda m: m.group(1)),
        # Swift: import Framework
        (r'^import\s+(\w+)',              lambda m: m.group(1)),
    ]

    seen: set[str] = set()
    result: list[str] = []

    for line in lines[:80]:   # scan first 80 lines — imports are always at top
        stripped = line.strip()
        if not stripped or stripped.startswith('//') or stripped.startswith('*'):
            continue
        for pattern, extractor in patterns:
            m = re.match(pattern, stripped)
            if m:
                name = extractor(m)
                if name and name not in seen:
                    seen.add(name)
                    result.append(name)
                if len(result) >= max_imports:
                    return result
                break

    return result


def _read_source(file_path: str, line_start: int, line_end: int) -> str:
    try:
        lines = Path(file_path).read_text(errors="replace").splitlines()
        return "\n".join(lines[max(0, line_start - 1): min(len(lines), line_end)])
    except OSError:
        return ""


def _count_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def _unavailable_sig(name: str, lang: str) -> str:
    """Language-appropriate 'source unavailable' stub for a function node."""
    if lang in ("java", "kotlin", "c", "cpp", "csharp", "swift"):
        return f"// {name}(...) — source unavailable"
    if lang in ("go",):
        return f"// func {name}(...) — source unavailable"
    if lang in ("rust",):
        return f"// fn {name}(...) — source unavailable"
    if lang in ("javascript", "typescript", "tsx"):
        return f"// function {name}(...) {{ /* source unavailable */ }}"
    if lang in ("ruby",):
        return f"# def {name}(...) — source unavailable"
    # Python default (and unknown)
    return f"def {name}(...)  # source unavailable"


# ---------------------------------------------------------------------------
# Layer 0 — File serializer
# ---------------------------------------------------------------------------

def serialize_file(node: "LNode", graph: "LayeredGraph") -> str:
    """Compact file-level context: path, imports, what it defines.

    Example output:
        file requests/auth.py
        imports: hashlib, os, threading, base64, ._internal_utils
        defines: AuthBase, HTTPBasicAuth, HTTPProxyAuth, HTTPDigestAuth
    """
    from ..graph.model import EdgeKind

    short = _short_path(node.file_path)
    imports = _read_imports(node.file_path)
    imports_str = ", ".join(imports) if imports else "—"

    # Contained classes and top-level functions (not methods)
    contained = [
        graph.nodes[e.target_id]
        for e in graph.out_adj.get(node.node_id, [])
        if e.kind == EdgeKind.CONTAINS and e.target_id in graph.nodes
    ]
    # Classes first, then top-level functions
    classes = [n for n in contained if n.layer.name == "CLASS"]
    fns = [n for n in contained if n.layer.name == "FUNCTION" and not n.is_test]

    defines_parts = [c.name for c in classes] + [f.name for f in fns]
    defines_str = ", ".join(defines_parts) if defines_parts else "—"

    return (
        f"file {short}\n"
        f"imports: {imports_str}\n"
        f"defines: {defines_str}"
    )


# ---------------------------------------------------------------------------
# Layer 1 — Class serializer
# ---------------------------------------------------------------------------

def serialize_class(node: "LNode", graph: "LayeredGraph") -> str:
    """Compact class-level context: header, inheritance, method list.

    Example output:
        class HTTPDigestAuth(AuthBase)  [requests/auth.py:107]
        methods: __init__, init_per_thread_state, build_digest_header,
                 handle_redirect, handle_401, __call__
    """
    from ..graph.model import EdgeKind

    short = _short_path(node.file_path)

    # Class header — read the actual declaration line from source.
    # Falls back to a language-appropriate keyword if source is unavailable.
    lang = node.language or ""
    try:
        lines = Path(node.file_path).read_text(errors="replace").splitlines()
        class_line = lines[node.line_start - 1].strip()
        # Match any language's type/class/interface/struct declaration:
        #   Python:       class Foo(Bar):
        #   Java/Kotlin:  class Foo extends Bar implements Baz {
        #   Go:           type Foo struct {
        #   Rust:         struct Foo {  /  impl Foo {  /  trait Foo {
        #   JS/TS:        class Foo extends Bar {
        #   C++:          class Foo : public Bar {
        #   Ruby:         class Foo < Bar
        m = re.match(
            r'(?:pub\s+)?(?:abstract\s+|sealed\s+|data\s+)?'
            r'(class|struct|interface|trait|impl|type|enum)\s+\w+[^{;]*',
            class_line,
        )
        header = m.group(0).rstrip() if m else f"class {node.name}"
    except (OSError, IndexError):
        # Generic fallback using language hint
        kw = {"go": "type", "rust": "struct", "c": "struct", "cpp": "struct"}.get(lang, "class")
        header = f"{kw} {node.name}"

    # Methods — direct CONTAINS children that are functions
    methods = [
        graph.nodes[e.target_id]
        for e in graph.out_adj.get(node.node_id, [])
        if e.kind == EdgeKind.CONTAINS and e.target_id in graph.nodes
        and graph.nodes[e.target_id].layer.name == "FUNCTION"
    ]
    # Sort: dunder/special methods last (Python __x__, Java <init>), then alphabetical
    def _method_sort_key(n: "LNode") -> tuple:
        is_special = n.name.startswith("__") or n.name.startswith("<")
        return (1 if is_special else 0, n.name)
    methods.sort(key=_method_sort_key)

    method_names = [m.name for m in methods]
    # Wrap method list at ~60 chars
    method_str = _wrap_list(method_names, width=60, indent="         ")

    return (
        f"{header}  [{short}:{node.line_start}]\n"
        f"methods: {method_str}"
    )


# ---------------------------------------------------------------------------
# Layer 2 — Function serializer
# ---------------------------------------------------------------------------

def serialize_function(node: "LNode", graph: "LayeredGraph") -> str:
    """Full function source body.

    For functions > 40 lines, returns signature + docstring + truncation marker
    to keep cost bounded when budget is tight.
    """
    source = _read_source(node.file_path, node.line_start, node.line_end)
    if not source:
        # Language-appropriate unavailable marker
        lang = node.language or ""
        sig = _unavailable_sig(node.name, lang)
        return sig

    line_count = node.line_end - node.line_start + 1
    if line_count <= 40:
        return source

    # Truncated: signature + doc comment + marker
    # Detect docstring/doc-comment closing patterns per language:
    #   Python:      """  or  '''
    #   Java/Kotlin/JS: */   (end of block comment)
    #   Rust/Go:     (no standard multi-line doc; just take signature + first lines)
    lang = node.language or ""
    doc_close = {'python': ('"""', "'''"), 'ruby': ('=end',)}.get(lang, ('*/',))

    source_lines = source.splitlines()
    result = []
    for line in source_lines[:12]:
        result.append(line)
        stripped = line.strip()
        if len(result) > 3 and stripped in doc_close:
            break

    # Language-appropriate truncation comment
    indent = "    " if lang in ("python", "ruby", "") else "  "
    cmt = "#" if lang in ("python", "ruby", "") else "//"
    result.append(f"{indent}{cmt} ... truncated")
    return "\n".join(result)


def serialize_function_for_scoring(node: "LNode", graph: "LayeredGraph") -> str:
    """Serialized function text used exclusively for BM25/scoring — NOT shown to the agent.

    Prepends two headers the agent never sees:

      1. A ``# path:`` line with the short file path, so queries mentioning
         filenames or module names ("requests/auth.py", "digest") get BM25
         credit even when the body doesn't repeat them.
      2. A ``# qname:`` line with the qualified name (``ClassName.method``)
         repeated twice, so the class prefix carries meaningful ``tf`` weight
         against ~150-token bodies. Repetition is cheap and language-agnostic.

    This text is only ever seen by scoring — the agent-facing serializer
    (:func:`serialize_function`) is untouched, so downstream token cost and
    rendered context are unchanged.
    """
    base = _read_source(node.file_path, node.line_start, node.line_end)

    # Build qualified name from parent class if not already set.
    qname = getattr(node, "qualified_name", None)
    if not qname or qname == node.name:
        parent = graph.nodes.get(node.parent_id) if node.parent_id else None
        if parent and parent.layer.name == "CLASS":
            qname = f"{parent.name}.{node.name}"
        else:
            qname = node.name

    short = _short_path(node.file_path) if node.file_path else ""
    header_lines: list[str] = []
    if short:
        header_lines.append(f"# path: {short}")
    # Repeat qualified name twice so BM25 tf gives it real weight against
    # the ~150-token body. Only repeat when it actually adds info.
    if qname != node.name:
        header_lines.append(f"# qname: {qname}")
        header_lines.append(f"# qname: {qname}")
    else:
        header_lines.append(f"# qname: {qname}")

    return "\n".join(header_lines + [base])


# ---------------------------------------------------------------------------
# Dispatch
# ---------------------------------------------------------------------------

def serialize(node: "LNode", graph: "LayeredGraph") -> str:
    """Serialize any node to its layer-appropriate text representation."""
    from ..graph.model import Layer
    if node.layer == Layer.FILE:
        return serialize_file(node, graph)
    elif node.layer == Layer.CLASS:
        return serialize_class(node, graph)
    else:
        return serialize_function(node, graph)


def serialized_token_cost(node: "LNode", graph: "LayeredGraph") -> int:
    """Actual token cost of serializing this node at its layer."""
    return _count_tokens(serialize(node, graph))


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _wrap_list(items: list[str], width: int, indent: str) -> str:
    """Wrap a comma-separated list at `width` chars, indenting continuation."""
    if not items:
        return "—"
    lines = []
    current = ""
    for i, item in enumerate(items):
        sep = ", " if i < len(items) - 1 else ""
        candidate = current + item + sep
        if len(candidate) > width and current:
            lines.append(current.rstrip(", "))
            current = indent + item + sep
        else:
            current = candidate
    if current:
        lines.append(current)
    return "\n".join(lines)
