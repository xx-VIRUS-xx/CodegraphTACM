# Q04 — tree-sitter vs Python ast for CFG/DFG
**Status:** ✅ RESOLVED

## Decision
**Hybrid approach:**
- Python `ast` module for G1 + G2 on Python codebases (maximum depth, already implemented)
- tree-sitter for G1 on non-Python codebases (structural only, no G2)

## Rationale
- `ast_parser.py` already implements G1 in Python ast — no reason to change
- Python ast provides full semantic access for CFG/DFG (G2)
- tree-sitter handles 40+ languages for G1 breadth
- G2 (CFG/DFG) only guaranteed for Python — honest scope

## Closed. No further action needed.
