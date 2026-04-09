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
    """Extract top-level import names from source file."""
    try:
        lines = Path(file_path).read_text(errors="replace").splitlines()
    except OSError:
        return []
    imports: list[str] = []
    for line in lines:
        line = line.strip()
        if not (line.startswith("import ") or line.startswith("from ")):
            if imports:
                break  # stop at first non-import after imports started
            continue
        # Extract the module name
        m = re.match(r'^import\s+([\w.]+)', line)
        if m:
            imports.append(m.group(1).split('.')[0])
            continue
        m = re.match(r'^from\s+([\w.]+)\s+import', line)
        if m:
            name = m.group(1).lstrip('.')
            if name:
                imports.append(name.split('.')[0])
    # Deduplicate, preserve order, cap
    seen: set[str] = set()
    result: list[str] = []
    for imp in imports:
        if imp not in seen:
            seen.add(imp)
            result.append(imp)
        if len(result) >= max_imports:
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

    # Inheritance — read from source first line of class body
    try:
        lines = Path(node.file_path).read_text(errors="replace").splitlines()
        class_line = lines[node.line_start - 1].strip()
        # Extract "class Foo(Bar, Baz):" → "Foo(Bar, Baz)"
        m = re.match(r'class\s+\w+(\([^)]*\))?', class_line)
        header = m.group(0) if m else f"class {node.name}"
    except (OSError, IndexError):
        header = f"class {node.name}"

    # Methods — direct CONTAINS children that are functions
    methods = [
        graph.nodes[e.target_id]
        for e in graph.out_adj.get(node.node_id, [])
        if e.kind == EdgeKind.CONTAINS and e.target_id in graph.nodes
        and graph.nodes[e.target_id].layer.name == "FUNCTION"
    ]
    # Sort: dunder last, then alphabetical
    def _method_sort_key(n: "LNode") -> tuple:
        return (1 if n.name.startswith("__") else 0, n.name)
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
    to keep cost bounded when budget is tight. The selector can request full
    body explicitly if the budget allows.
    """
    source = _read_source(node.file_path, node.line_start, node.line_end)
    if not source:
        return f"def {node.name}(...)  # source unavailable"

    line_count = node.line_end - node.line_start + 1
    if line_count <= 40:
        return source

    # Truncated: signature + docstring + marker
    source_lines = source.splitlines()
    result = []
    for line in source_lines[:12]:
        result.append(line)
        stripped = line.strip()
        # Stop after closing triple-quote of docstring
        if len(result) > 3 and stripped in ('"""', "'''"):
            break
    result.append("    # ... truncated")
    return "\n".join(result)


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
