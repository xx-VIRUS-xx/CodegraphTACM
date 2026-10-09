# TACM MCP Server Interface Specification

**Version:** 1.0 (pre-launch)
**Status:** Final spec before implementation
**Audience:** Internal build team + future integrations (Claude Code, Cursor, Windsurf)

---

## 1. Architecture Overview

```
Claude/Cursor/Windsurf (agent)
         ↓
    [MCP Protocol]
         ↓
  tacm-mcp-server (public repo)
    ├─ server.py (MCP host)
    ├─ tools.py (stateless retrieval)
    ├─ resources.py (session state management)
    └─ session_db.py (SQLite persistence)
         ↓
  tacm-engine (private package)
    ├─ graph_builder.py
    ├─ scorer.py
    ├─ selector.py
    └─ ... (proprietary logic)
```

The MCP server is a thin stateless wrapper + session orchestrator. It does NOT contain retrieval logic — it calls the private engine and shapes responses for MCP.

---

## 2. MCP Tools (Stateless One-Shot Calls)

### Tool 1: `tacm_retrieve`

**Purpose:** Basic retrieval on a cold repo. Used for human queries or first-turn agent calls.

**Signature:**
```json
{
  "name": "tacm_retrieve",
  "description": "Retrieve ranked functions for a code query using TACM graph-based scoring. Returns context window with budget-aware function selection.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "repo_path": {
        "type": "string",
        "description": "Absolute path to repo root. Examples: /home/user/myproject, $HOME/work/pandas"
      },
      "query": {
        "type": "string",
        "description": "Natural language bug description or code search query. 20-500 chars."
      },
      "budget_tokens": {
        "type": "integer",
        "description": "Context window budget. Default 4000. Range: 1000–8000.",
        "default": 4000
      },
      "top_k": {
        "type": "integer",
        "description": "Return up to this many functions. Default 20.",
        "default": 20
      },
      "include_callers": {
        "type": "boolean",
        "description": "Include caller snippets (Layer 4 context). Default true.",
        "default": true
      },
      "session_id": {
        "type": "string",
        "description": "Optional. If provided, retrieval uses session state (warm start). Omit for cold retrieval.",
        "optional": true
      }
    },
    "required": ["repo_path", "query"]
  },
  "output": {
    "type": "object",
    "properties": {
      "status": { "type": "string", "enum": ["success", "error"] },
      "functions": {
        "type": "array",
        "description": "Ranked list of functions.",
        "items": {
          "type": "object",
          "properties": {
            "rank": { "type": "integer", "description": "Rank 1-N in this retrieval" },
            "function_id": { "type": "string", "description": "Unique ID: {file}:{class}.{name}:{start_line}" },
            "file": { "type": "string", "description": "Relative path from repo root" },
            "class_name": { "type": "string", "description": "Class name if nested, else null" },
            "function_name": { "type": "string" },
            "start_line": { "type": "integer" },
            "end_line": { "type": "integer" },
            "score": { "type": "number", "description": "TACM score (0.0–1.0). Keep abstract." },
            "source": { "type": "string", "enum": ["graph_structural", "text_semantic", "hybrid"], "description": "Why this function ranked: structural (fan-in/call graph), semantic, or both" },
            "code_snippet": { "type": "string", "description": "First 15 lines of function or full function if < 15 lines. Syntax-highlighted markdown." },
            "caller_context": { "type": "string", "description": "Optional. If include_callers=true: code snippets of 1–2 key callers. None if none in top-tier." }
          },
          "required": ["rank", "function_id", "file", "function_name", "start_line", "end_line", "score", "code_snippet"]
        }
      },
      "context_meta": {
        "type": "object",
        "properties": {
          "total_tokens_used": { "type": "integer" },
          "total_functions_available": { "type": "integer", "description": "Parsed functions in this repo" },
          "functions_returned": { "type": "integer" },
          "retrieval_latency_ms": { "type": "integer" },
          "rank_confidence": { "type": "number", "description": "0.0–1.0. Higher = more confident in top-1 rank." }
        }
      },
      "error_message": { "type": "string", "optional": true }
    },
    "required": ["status", "functions", "context_meta"]
  }
}
```

**Example Call:**
```json
{
  "repo_path": "/home/user/thefuck",
  "query": "fix pip_unknown_command by handling edge case with regex",
  "budget_tokens": 4000,
  "top_k": 20,
  "include_callers": true
}
```

**Example Response:**
```json
{
  "status": "success",
  "functions": [
    {
      "rank": 1,
      "function_id": "thefuck/rules/pip_unknown_command.py:PipUnknownCommand.match:45",
      "file": "thefuck/rules/pip_unknown_command.py",
      "class_name": "PipUnknownCommand",
      "function_name": "match",
      "start_line": 45,
      "end_line": 62,
      "score": 0.847,
      "source": "graph_structural",
      "code_snippet": "def match(self, command):\n    # Handles pip unknown command errors\n    return 'unknown command' in command.stderr",
      "caller_context": "Called by: rule_runner.py:validate_rule (line 120)"
    },
    ...
  ],
  "context_meta": {
    "total_tokens_used": 3856,
    "total_functions_available": 234,
    "functions_returned": 12,
    "retrieval_latency_ms": 185,
    "rank_confidence": 0.92
  }
}
```

---

### Tool 2: `tacm_session_start`

**Purpose:** Initialize a new session for multi-turn agent tasks. Creates session state in SQLite.

**Signature:**
```json
{
  "name": "tacm_session_start",
  "description": "Start a new TACM session with persistent memory for multi-turn agent tasks.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "repo_path": {
        "type": "string",
        "description": "Absolute path to repo"
      },
      "task_description": {
        "type": "string",
        "description": "What is the agent trying to do? 'Fix bug #234: handle concurrent writes' etc. Helps track context."
      },
      "initial_files": {
        "type": "array",
        "description": "Optional. Seed the session with these files as high-priority. Paths relative to repo.",
        "items": { "type": "string" },
        "optional": true
      }
    },
    "required": ["repo_path", "task_description"]
  },
  "output": {
    "type": "object",
    "properties": {
      "status": { "type": "string", "enum": ["success", "error"] },
      "session_id": { "type": "string", "description": "UUID for this session. Use in all subsequent calls." },
      "session_meta": {
        "type": "object",
        "properties": {
          "created_at": { "type": "string", "description": "ISO 8601 timestamp" },
          "repo_path": { "type": "string" },
          "task_description": { "type": "string" },
          "state_summary": { "type": "string", "description": "Human-readable: 'Session initialized. 234 functions parsed. 0 visited. 0 dirty.'" }
        }
      },
      "error_message": { "type": "string", "optional": true }
    }
  }
}
```

**Example Response:**
```json
{
  "status": "success",
  "session_id": "sess_550e8400e29b41d4a716446655440000",
  "session_meta": {
    "created_at": "2026-04-13T14:22:30Z",
    "repo_path": "/home/user/pandas",
    "task_description": "Fix concat behavior with MultiIndex",
    "state_summary": "Session initialized. 2341 functions parsed. 0 visited. 0 dirty."
  }
}
```

---

### Tool 3: `tacm_session_update`

**Purpose:** Retrieve context for a query **within an active session**. Uses session graph state, learns from prior context.

**Signature:**
```json
{
  "name": "tacm_session_update",
  "description": "Retrieve within an active session. Uses accumulated context from prior retrievals to boost relevance. TACM adapts its scoring based on what you've already visited.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "session_id": {
        "type": "string",
        "description": "Session ID from tacm_session_start"
      },
      "query": {
        "type": "string",
        "description": "New query for this turn of the task"
      },
      "budget_tokens": {
        "type": "integer",
        "description": "Context budget for this retrieval. Default 4000.",
        "default": 4000
      },
      "top_k": {
        "type": "integer",
        "description": "Max functions to return. Default 20.",
        "default": 20
      },
      "rerank_strategy": {
        "type": "string",
        "enum": ["session_aware", "cold", "exploit"],
        "description": "session_aware: boost visited functions and related tier. cold: ignore session state. exploit: aggressive bias toward visited hot-spot.",
        "default": "session_aware"
      }
    },
    "required": ["session_id", "query"]
  },
  "output": {
    "type": "object",
    "properties": {
      "status": { "type": "string", "enum": ["success", "error"] },
      "functions": {
        "type": "array",
        "description": "Ranked functions. Same schema as tacm_retrieve.",
        "items": { "type": "object" }
      },
      "session_meta": {
        "type": "object",
        "properties": {
          "session_id": { "type": "string" },
          "turn": { "type": "integer", "description": "Which turn of the session (1-indexed)" },
          "visited_count": { "type": "integer", "description": "Total functions visited in this session so far" },
          "dirty_count": { "type": "integer", "description": "Functions marked edited (dirty flags)" },
          "warm_start": { "type": "boolean", "description": "true if this retrieval used session state" },
          "state_summary": { "type": "string", "description": "e.g. 'Turn 3. 18 visited. 2 dirty. Retrieval boosted tier-1 candidates by prior edits.'" }
        }
      },
      "context_meta": {
        "type": "object",
        "properties": {
          "total_tokens_used": { "type": "integer" },
          "functions_returned": { "type": "integer" },
          "retrieval_latency_ms": { "type": "integer" },
          "rerank_impact": { "type": "string", "description": "How much did session state change ranking? 'High' / 'Medium' / 'Low'" }
        }
      },
      "error_message": { "type": "string", "optional": true }
    }
  }
}
```

---

### Tool 4: `tacm_session_mark_edited`

**Purpose:** Mark files/functions as edited. Signals to TACM that these are hot-spots for the current task.

**Signature:**
```json
{
  "name": "tacm_session_mark_edited",
  "description": "Mark a file or function as edited (dirty). TACM will boost related functions in subsequent retrievals.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "session_id": {
        "type": "string"
      },
      "edits": {
        "type": "array",
        "description": "List of edits to register",
        "items": {
          "type": "object",
          "properties": {
            "file_path": {
              "type": "string",
              "description": "Relative to repo root"
            },
            "function_id": {
              "type": "string",
              "description": "Optional. If provided, marks this specific function dirty. Format: {file}:{class}.{name}:{line}",
              "optional": true
            },
            "edit_type": {
              "type": "string",
              "enum": ["created", "modified", "deleted"],
              "description": "What happened to this file/function"
            },
            "lines_affected": {
              "type": "array",
              "description": "Optional. Which line ranges were edited?",
              "items": {
                "type": "object",
                "properties": {
                  "start": { "type": "integer" },
                  "end": { "type": "integer" }
                }
              },
              "optional": true
            }
          },
          "required": ["file_path", "edit_type"]
        }
      }
    },
    "required": ["session_id", "edits"]
  },
  "output": {
    "type": "object",
    "properties": {
      "status": { "type": "string", "enum": ["success", "error"] },
      "registered_edits": {
        "type": "integer",
        "description": "How many edits were registered"
      },
      "dirty_count": {
        "type": "integer",
        "description": "Total dirty flag count in this session now"
      },
      "affected_tiers": {
        "type": "array",
        "description": "Which tier levels will be boosted on next retrieval",
        "items": { "type": "string", "enum": ["tier_0", "tier_1", "tier_2", "tier_3"] }
      },
      "error_message": { "type": "string", "optional": true }
    }
  }
}
```

**Example Call:**
```json
{
  "session_id": "sess_550e8400e29b41d4a716446655440000",
  "edits": [
    {
      "file_path": "pandas/core/reshape/concat.py",
      "function_id": "pandas/core/reshape/concat.py:concat:120",
      "edit_type": "modified",
      "lines_affected": [{"start": 140, "end": 160}]
    },
    {
      "file_path": "pandas/core/indexes/multi.py",
      "edit_type": "modified"
    }
  ]
}
```

---

### Tool 5: `tacm_session_end`

**Purpose:** Close session, archive state to SQLite for later review/learning.

**Signature:**
```json
{
  "name": "tacm_session_end",
  "description": "End a session. Archives session state for future analysis. After this, session_id becomes read-only resource.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "session_id": {
        "type": "string"
      },
      "outcome": {
        "type": "string",
        "enum": ["solved", "partial", "failed", "abandoned"],
        "description": "Did the agent solve the task?"
      },
      "summary": {
        "type": "string",
        "description": "Optional. Human-readable summary of what happened. Stored for review.",
        "optional": true
      }
    },
    "required": ["session_id", "outcome"]
  },
  "output": {
    "type": "object",
    "properties": {
      "status": { "type": "string", "enum": ["success", "error"] },
      "session_archive": {
        "type": "object",
        "properties": {
          "session_id": { "type": "string" },
          "ended_at": { "type": "string", "description": "ISO 8601" },
          "outcome": { "type": "string" },
          "duration_seconds": { "type": "integer" },
          "total_turns": { "type": "integer" },
          "funcs_visited": { "type": "integer" },
          "funcs_edited": { "type": "integer" },
          "archive_key": { "type": "string", "description": "Key to retrieve archived session later via resource API" }
        }
      },
      "error_message": { "type": "string", "optional": true }
    }
  }
}
```

---

## 3. MCP Resources (Persistent State)

Resources allow Claude/Cursor to READ session state between tool calls. They don't modify state — only tools do that.

### Resource 1: `tacm://session/{session_id}`

**Purpose:** Read the full state of an active session.

**Schema:**
```json
{
  "type": "object",
  "properties": {
    "session_id": { "type": "string" },
    "repo_path": { "type": "string" },
    "task_description": { "type": "string" },
    "created_at": { "type": "string" },
    "turns": { "type": "integer", "description": "How many retrievals so far" },
    "state": {
      "type": "object",
      "properties": {
        "visited_functions": {
          "type": "array",
          "description": "Functions the agent has seen/edited",
          "items": {
            "type": "object",
            "properties": {
              "function_id": { "type": "string" },
              "file": { "type": "string" },
              "function_name": { "type": "string" },
              "visit_count": { "type": "integer", "description": "Times retrieved in this session" },
              "is_dirty": { "type": "boolean", "description": "Was this function edited?" },
              "related_tier": { "type": "string", "enum": ["tier_0", "tier_1", "tier_2", "tier_3"] }
            }
          }
        },
        "tier_structure": {
          "type": "object",
          "description": "Current call graph tier assignment",
          "properties": {
            "tier_0": { "type": "array", "items": { "type": "string" }, "description": "Function IDs in tier 0" },
            "tier_1": { "type": "array", "items": { "type": "string" } },
            "tier_2": { "type": "array", "items": { "type": "string" } },
            "tier_3": { "type": "array", "items": { "type": "string" } }
          }
        },
        "hot_spots": {
          "type": "array",
          "description": "Most-visited functions in this session",
          "items": {
            "type": "object",
            "properties": {
              "function_id": { "type": "string" },
              "visit_count": { "type": "integer" }
            }
          }
        }
      }
    },
    "summary": { "type": "string", "description": "Plain English: 'Active session. 3 turns. 12 functions visited. 2 edited. Tier 0 is the hot-spot.'" }
  }
}
```

**Example Read:**
```
GET tacm://session/sess_550e8400e29b41d4a716446655440000
```

**Response:**
```json
{
  "session_id": "sess_550e8400e29b41d4a716446655440000",
  "repo_path": "/home/user/pandas",
  "task_description": "Fix concat behavior with MultiIndex",
  "created_at": "2026-04-13T14:22:30Z",
  "turns": 3,
  "state": {
    "visited_functions": [
      {
        "function_id": "pandas/core/reshape/concat.py:concat:120",
        "file": "pandas/core/reshape/concat.py",
        "function_name": "concat",
        "visit_count": 2,
        "is_dirty": true,
        "related_tier": "tier_0"
      },
      ...
    ],
    "tier_structure": {
      "tier_0": ["func_1", "func_2"],
      "tier_1": ["func_3", "func_4", "func_5"],
      "tier_2": [...],
      "tier_3": [...]
    },
    "hot_spots": [
      { "function_id": "pandas/core/reshape/concat.py:concat:120", "visit_count": 2 }
    ]
  },
  "summary": "Active session. 3 turns. 12 functions visited. 2 edited. Hot-spot is concat() in tier_0."
}
```

---

### Resource 2: `tacm://session/{session_id}/context`

**Purpose:** Read the CURRENT assembled context for the active session (what gets passed to the agent).

**Schema:**
```json
{
  "type": "object",
  "properties": {
    "session_id": { "type": "string" },
    "current_context": {
      "type": "string",
      "description": "Full markdown-formatted context window. This is what the agent is currently working with."
    },
    "context_meta": {
      "type": "object",
      "properties": {
        "total_tokens": { "type": "integer" },
        "functions_included": { "type": "integer" },
        "files_included": { "type": "integer" },
        "last_updated_turn": { "type": "integer" }
      }
    }
  }
}
```

---

## 4. Session State Model (SQLite Schema)

The MCP server persists all session state here. This is the "memory pool."

```sql
-- Sessions table
CREATE TABLE sessions (
  session_id TEXT PRIMARY KEY,
  repo_path TEXT NOT NULL,
  task_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  ended_at TIMESTAMP,
  outcome TEXT,  -- 'active', 'solved', 'partial', 'failed', 'abandoned'
  total_turns INTEGER DEFAULT 0,
  summary TEXT
);

-- Per-session visited functions (tier state)
CREATE TABLE session_visited_functions (
  session_id TEXT,
  function_id TEXT,
  file_path TEXT,
  function_name TEXT,
  tier_level INTEGER,  -- 0, 1, 2, 3
  visit_count INTEGER DEFAULT 1,
  is_dirty BOOLEAN DEFAULT 0,
  first_visited_turn INTEGER,
  last_visited_turn INTEGER,
  PRIMARY KEY (session_id, function_id),
  FOREIGN KEY (session_id) REFERENCES sessions(session_id)
);

-- Per-session edit events (dirty flags)
CREATE TABLE session_edit_events (
  id INTEGER PRIMARY KEY,
  session_id TEXT,
  file_path TEXT,
  function_id TEXT,
  edit_type TEXT,  -- 'created', 'modified', 'deleted'
  turn_number INTEGER,
  edited_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (session_id) REFERENCES sessions(session_id)
);

-- Session retrieval history (for replay/debug)
CREATE TABLE session_retrieval_log (
  id INTEGER PRIMARY KEY,
  session_id TEXT,
  turn_number INTEGER,
  query TEXT,
  functions_returned INTEGER,
  top_1_rank_correct BOOLEAN,
  rerank_strategy TEXT,
  latency_ms INTEGER,
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (session_id) REFERENCES sessions(session_id)
);

-- Global prior from archived sessions (optional, for cold-start learning)
CREATE TABLE function_priors (
  function_id TEXT PRIMARY KEY,
  global_visit_count INTEGER DEFAULT 0,
  avg_tier_level REAL,
  solve_count INTEGER DEFAULT 0,  -- Times this func was in a 'solved' session
  last_updated TIMESTAMP
);
```

---

## 5. Session State Object (In-Memory during Session)

The MCP server holds this in memory while a session is active:

```python
class SessionState:
    session_id: str
    repo_path: str
    task_description: str
    turn: int  # increments on each tacm_session_update call
    
    # Tier graph (built once per session)
    tier_0: Set[str]  # Tier-0 functions (direct/contained)
    tier_1: Set[str]  # 1-hop callers
    tier_2: Set[str]  # 2-hop callers
    tier_3: Set[str]  # 3-hop callers
    
    # Visit tracking
    visited_functions: Dict[str, VisitRecord]
      # VisitRecord = {function_id, visit_count, is_dirty, last_turn_visited}
    
    # State flags for reranking
    hot_functions: Set[str]  # Top 5 by visit_count
    dirty_flags: Dict[str, EditRecord]  # {function_id -> edit info}
    
    # Current context window
    assembled_context: str  # Markdown-formatted context
    context_tokens: int
```

**Transition on `tacm_session_update`:**
1. Increment turn
2. Call engine with (query, tier structure, visited_functions, dirty_flags)
3. Engine returns ranked functions + reranking signals
4. Update visited_functions dict
5. Recompute hot_spots
6. Assemble markdown context
7. Return response

---

## 6. Example Multi-Turn Workflow

**User (via Claude):** "Fix the concat bug"

**Turn 1:**
```
Agent calls: tacm_session_start(
  repo_path="/home/user/pandas",
  task_description="Fix concat behavior with MultiIndex"
)
Response: session_id = "sess_123"

Agent calls: tacm_session_update(
  session_id="sess_123",
  query="concat function multiindex behavior"
)
Response: functions= [concat, _get_concat_axis, ...]
Agent edits concat.py
Agent calls: tacm_session_mark_edited(
  session_id="sess_123",
  edits=[{file_path: "pandas/core/reshape/concat.py", edit_type: "modified"}]
)
```

**Turn 2:**
```
Agent calls: tacm_session_update(
  session_id="sess_123",
  query="multiindex handling in append"
)
Response: functions= [append, _ensure_index, ...]
TACM has marked concat.py as dirty, so tier_0 functions are now boosted in ranking.
Agent sees _ensure_index is relevant (not explicitly asked for, but tier-related to edited concat.py).
```

**Turn 3:**
```
Agent calls: tacm_session_mark_edited(
  session_id="sess_123",
  edits=[{file_path: "pandas/core/indexes/multi.py", edit_type: "modified"}]
)
Agent calls: tacm_session_update(
  session_id="sess_123",
  query="MultiIndex level handling edge case"
)
Response: HIGH rerank_impact. Session state says "Multi.py is dirty + visited 2x. Boosting tier-1 callers."
Functions returned now heavily emphasize functions called by MultiIndex methods.
```

**Turn 4:**
```
Agent pings: resource GET tacm://session/sess_123
Reads: visited_functions, hot_spots, tier_structure
Quick check: "We've touched 18 functions across 3 files. Concat and MultiIndex are the hot-spots."
Agent decides to test and wrap up.
```

**End:**
```
Agent calls: tacm_session_end(
  session_id="sess_123",
  outcome="solved",
  summary="Fixed concat to correctly propagate MultiIndex names via _ensure_index."
)
Response: Archive written to DB. session_id now becomes read-only resource.
```

---

## 7. Distribution & Versioning

### Public Layer
- **Repo:** `tacm-mcp` (public GitHub)
- **Package:** published to PyPI as `tacm-mcp`
- **Install:** `pip install tacm-mcp`
- **Config:** `.env` or `tacm-config.toml`

### Private Layer
- **Repo:** `tacm-engine` (private GitHub or Gemfury)
- **Package:** `tacm-engine` on private PyPI with token auth
- **Install (MCP server):** `pip install tacm-mcp` → transitively installs `tacm-engine` via token

### MCP Server Discovery
When Claude/Cursor asks for MCP servers, it sees:

```json
{
  "name": "tacm-retriever",
  "description": "Budget-aware graph-based code retrieval for agents. Stateless or session-aware. Outruns BM25 and Dense embeddings on bug localization.",
  "mcp_version": "1.0",
  "tools": ["tacm_retrieve", "tacm_session_start", "tacm_session_update", "tacm_session_mark_edited", "tacm_session_end"],
  "resources": ["tacm://session/{session_id}", "tacm://session/{session_id}/context"]
}
```

---

## 8. Future Extensions (Not in v1)

- **`tacm://archived_sessions`** — list of past sessions, queryable by outcome/task_description
- **`tacm_session_branch`** — fork a session at a given turn for "what if" exploration
- **`tacm_retrieval_explain`** — tool to get detailed explanation of why a function ranked Nth (transparency)
- **`tacm_tune`** — tool to adjust scoring weights per-session based on agent feedback
- **Priors learning** — aggregate `function_priors` table from solved sessions to bias cold retrieval

---

## 9. Implementation Checklist

**Phase 1 (Stateless, 1 week):**
- [ ] Wrap engine as Python package
- [ ] Implement `tacm_retrieve` tool
- [ ] MCP server scaffolding (basic)
- [ ] Test end-to-end on Claude Code + Cursor

**Phase 2 (Session state, 2 weeks):**
- [ ] SQLite schema + migration
- [ ] SessionState in-memory object
- [ ] Implement `tacm_session_start`, `tacm_session_update`, `tacm_session_mark_edited`, `tacm_session_end`
- [ ] Resource endpoints: `tacm://session/{id}`, `tacm://session/{id}/context`
- [ ] Rerank logic (warm-start tier boosting + dirty flag propagation)

**Phase 3 (Polish + demo, 1 week):**
- [ ] Write README with benchmark table + GIF demo
- [ ] Publish to PyPI
- [ ] Record multi-turn demo video
- [ ] arXiv paper submission

---

## 10. Key Design Decisions Locked In

1. **MCP tools for state mutations**, resources for state reads (clean separation)
2. **Session graph lives in memory** during active session, archived to SQLite on end
3. **Tier structure is immutable per session** (computed at start, not updated per query)
4. **Dirty flags propagate to tier-related functions** (tier_0 edits boost tier_1 on next retrieval)
5. **Private engine stays out of the repo** (MCP server only, engine behind package boundary)
6. **No cloud dependency** (everything runs locally, SQLite on user's machine)
7. **Backward compatibility** — stateless `tacm_retrieve` works forever even if session layer evolves

