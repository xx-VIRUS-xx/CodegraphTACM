# P11 — Payload Serialisation Format
**Severity:** 🟠 HIGH | **Status:** ❓ OPEN | **Blocks:** TACM → LLM

## Problem
After the resolver selects nodes and resolves them to text, it must serialise them into a structured prompt. The format affects:
- Token efficiency (how much context fits in the budget)
- LLM comprehension (can the model use the context correctly)
- Source attribution (can the LLM say "this comes from file X, function Y")

## Options

### Option A — Structured XML
```xml
<context codebase="myrepo" query_tokens="12" budget_used="387/800">
  <node id="fn:parser.py::Parser.parse" kind="function" risk="0.87">
    <signature>def parse(self, text: str) -> List[Token]:</signature>
    <doc>Parse input text into a list of Token objects.</doc>
    <raises>UnicodeDecodeError, ParseError</raises>
    <calls>tokenize, normalize_string</calls>
  </node>
  <node id="fn:tokenizer.py::tokenize" kind="function" risk="0.23">
    <signature>def tokenize(text: str) -> List[str]:</signature>
    <doc>Split text into raw string tokens.</doc>
  </node>
</context>
```
- ✅ Claude handles XML best — trained heavily on XML
- ✅ Clear structure, easy to parse programmatically
- ✅ Metadata (risk, file, kind) visible without increasing body tokens
- ❌ XML tags themselves cost tokens (~3-5 per tag pair)

### Option B — Pseudo-code stubs
```python
# [parser.py | risk: HIGH | calls: tokenize, normalize]
def parse(self, text: str) -> List[Token]:
    """Parse input text into a list of Token objects."""
    # raises: UnicodeDecodeError, ParseError
    ...

# [tokenizer.py | risk: LOW]  
def tokenize(text: str) -> List[str]:
    """Split text into raw string tokens."""
    ...
```
- ✅ Most natural for code LLMs — looks like real code
- ✅ Minimal token overhead
- ❌ Less structured — harder for LLM to extract metadata
- ❌ Comments can be ignored by some models

### Option C — Hybrid (XML wrapper + pseudo-code body)
```xml
<context budget="387/800">
  <fn file="parser.py" risk="0.87">
def parse(self, text: str) -> List[Token]:
    """Parse text into tokens. raises: UnicodeDecodeError"""
    ...
  </fn>
</context>
```
- ✅ Structure from XML, naturalness from code
- ✅ Compact — metadata in attributes, not body tokens

## Token Count Comparison (same 3 nodes)
| Format | Tokens |
|---|---|
| Option A (XML) | ~120 |
| Option B (pseudo-code) | ~95 |
| Option C (hybrid) | ~105 |

## Agent Task
1. Implement all three serialisers as Python functions
2. Take 5 real queries + retrieved nodes from ast_parser.py
3. For each format: feed to GPT-4o, ask it to answer the query
4. Measure: answer accuracy, token count, does model correctly attribute which file each node comes from?
5. Recommendation: which format?

## Acceptance Criteria
- LLM can correctly attribute answers to specific files/functions
- Format overhead (wrapper tokens) ≤ 15% of total payload tokens
- Answer quality equal or better compared to raw text insertion at same token budget
