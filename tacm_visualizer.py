"""tacm_visualizer.py — Trace and visualize the full TACM decision path.

Generates a self-contained interactive HTML report showing:
  1. Query analysis:  intent classification, query expansion
  2. Signal heatmap:  per-node BM25, fan_in, fan_out, complexity, test_cover
  3. Selection path:  per-layer ranked candidates, containment bonuses, budget fill
  4. Graph view:      force-directed graph of selected nodes + their neighbors
  5. Budget timeline: token consumption across layers

Usage:
    python tacm_visualizer.py --repo ./thefuck --query "pip install fails with unknown command"
    python tacm_visualizer.py --repo ./scrapy  --query "WrappedRequest not sending headers" --budget 4000
    python tacm_visualizer.py --repo ./thefuck --query "git push fails" --dynamic
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import webbrowser
from collections import Counter
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))


def _short_id(node_id: str) -> str:
    """Shorten a qualified name for display."""
    if "::" in node_id:
        return node_id.split("::")[-1]
    return node_id.split("/")[-1]


def _short_path(file_path: str) -> str:
    p = Path(file_path)
    parts = p.parts
    return str(Path(*parts[-3:])) if len(parts) >= 3 else file_path


def trace_tacm(
    repo_root: Path,
    query: str,
    token_budget: int = 4000,
    use_dynamic: bool = False,
) -> dict:
    """Run TACM and capture every intermediate decision.

    Returns a trace dict with all data needed for visualization.
    """
    from code_review_graph.graph import GraphStore
    from code_review_graph.incremental import get_db_path, full_build
    from tacm_v2.graph.builder import GraphBuilder
    from tacm_v2.graph.model import Layer, EdgeKind
    from tacm_v2.layers.serializers import serialize, serialize_function_for_scoring
    from tacm_v2.selector.intent import classify_intent, INTENT_WEIGHTS, LAYER_BUDGETS
    from tacm_v2.selector.scoring import (
        NodeScorer, compute_bm25, compute_fan_in, compute_fan_out,
        compute_complexity, compute_test_cover, compute_neighborhood_bonus,
        compute_pagerank, _cascading_bm25, _expand_query,
    )
    from tacm_v2.selector.selector import _count_tokens

    # --- Build graph ---
    print("  Building graph...", end=" ", flush=True)
    db_path = get_db_path(repo_root)
    # Check if there are actual source files to parse
    has_source = any(
        f.suffix == ".py"
        for f in repo_root.rglob("*")
        if ".code-review-graph" not in str(f) and f.is_file()
    )
    store = GraphStore(db_path)
    try:
        if has_source:
            full_build(repo_root, store)
        graph = GraphBuilder(store).build()
    finally:
        store.close()

    stats = {
        "files": sum(1 for n in graph.nodes.values() if n.layer == Layer.FILE),
        "classes": sum(1 for n in graph.nodes.values() if n.layer == Layer.CLASS),
        "functions": sum(1 for n in graph.nodes.values() if n.layer == Layer.FUNCTION and not n.is_test),
        "edges": len(graph.edges),
    }
    print(f"{stats['functions']} fns, {stats['classes']} cls, {stats['files']} files")

    # --- Intent ---
    intent = classify_intent(query)
    weights_tuple = INTENT_WEIGHTS[intent]
    weight_names = ["bm25", "fan_in", "fan_out", "complexity", "test_cover"]
    weights = dict(zip(weight_names, weights_tuple))
    layer_budgets_tuple = LAYER_BUDGETS[intent]
    layer_budget_fracs = dict(zip(["file", "class", "function"], layer_budgets_tuple))

    file_budget = int(token_budget * layer_budget_fracs["file"])
    class_budget = int(token_budget * layer_budget_fracs["class"])
    fn_budget = token_budget - file_budget - class_budget

    # --- Query expansion ---
    expanded = _expand_query(query, graph)
    expansion_terms = expanded.replace(query, "").strip().split() if expanded != query else []

    # --- Prepare texts ---
    all_nodes = [n for n in graph.nodes.values() if not n.is_test]
    agent_texts = {n.node_id: serialize(n, graph) for n in all_nodes}
    score_texts = {
        n.node_id: (
            serialize_function_for_scoring(n, graph)
            if n.layer == Layer.FUNCTION
            else agent_texts[n.node_id]
        )
        for n in all_nodes
    }

    # --- Score each layer + capture per-signal breakdown ---
    scorer = NodeScorer(graph, query, intent, score_texts)
    name_counts = Counter(
        (n.name, n.file_path) for n in graph.nodes.values()
        if n.layer.name == "FUNCTION"
    )

    layer_traces = {}
    for layer, budget, layer_name in [
        (Layer.FILE, file_budget, "FILE"),
        (Layer.CLASS, class_budget, "CLASS"),
        (Layer.FUNCTION, fn_budget, "FUNCTION"),
    ]:
        nodes = [n for n in graph.nodes_at_layer(layer) if not n.is_test]
        if not nodes:
            layer_traces[layer_name] = {"candidates": [], "budget": budget}
            continue

        # Compute individual signals
        bm25 = compute_bm25(query, nodes, score_texts)
        fan_in = compute_fan_in(nodes, graph, name_counts)
        fan_out = compute_fan_out(nodes, graph)
        complexity = compute_complexity(nodes)
        test_cover = compute_test_cover(nodes, graph)

        # Combined scores from scorer
        combined = scorer.score_all(nodes)

        # Neighborhood + PageRank (function only)
        nbr = {}
        pr = {}
        if layer == Layer.FUNCTION:
            nbr = compute_neighborhood_bonus(nodes, graph, combined)
            pr = compute_pagerank(nodes, graph)

        candidates = []
        for n in nodes:
            nid = n.node_id
            text = agent_texts.get(nid, "")
            tok = _count_tokens(text)
            candidates.append({
                "id": nid,
                "short": _short_id(nid),
                "name": n.name,
                "file": _short_path(n.file_path) if n.file_path else "",
                "line": n.line_start,
                "tokens": tok,
                "parent_id": n.parent_id,
                "signals": {
                    "bm25": round(bm25.get(nid, 0), 4),
                    "fan_in": round(fan_in.get(nid, 0), 4),
                    "fan_out": round(fan_out.get(nid, 0), 4),
                    "complexity": round(complexity.get(nid, 0), 4),
                    "test_cover": round(test_cover.get(nid, 0), 4),
                },
                "neighborhood": round(nbr.get(nid, 0), 4),
                "pagerank": round(pr.get(nid, 0), 4),
                "combined": round(combined.get(nid, 0), 4),
            })

        candidates.sort(key=lambda c: -c["combined"])
        layer_traces[layer_name] = {
            "candidates": candidates[:50],  # top 50 per layer
            "total_candidates": len(candidates),
            "budget": budget,
        }

    # --- Run actual selection ---
    from tacm_v2.selector.selector import select, select_dynamic, SelectedNode

    selector_fn = select_dynamic if use_dynamic else select
    result = selector_fn(graph, query, token_budget=token_budget)

    selection_steps = []
    selected_ids = set()
    running_tokens = 0

    for sn in result.nodes:
        nid = sn.node.node_id
        had_containment = (
            sn.node.parent_id is not None
            and sn.node.parent_id in selected_ids
        )
        running_tokens += sn.token_cost
        selection_steps.append({
            "id": nid,
            "short": _short_id(nid),
            "layer": sn.layer.name,
            "score": round(sn.score, 4),
            "tokens": sn.token_cost,
            "running_tokens": running_tokens,
            "containment_bonus": had_containment,
            "parent_id": sn.node.parent_id,
            "file": _short_path(sn.node.file_path) if sn.node.file_path else "",
        })
        selected_ids.add(nid)

    # --- Build graph edges for selected nodes + neighbors ---
    graph_nodes_viz = []
    graph_edges_viz = []
    viz_ids = set()

    for sn in result.nodes:
        viz_ids.add(sn.node.node_id)

    # Add 1-hop neighbors of selected FUNCTION nodes
    neighbor_ids = set()
    for sn in result.nodes:
        if sn.layer.name != "FUNCTION":
            continue
        for e in graph.out_adj.get(sn.node.node_id, []):
            if e.kind == EdgeKind.CALLS and e.target_id in graph.nodes:
                neighbor_ids.add(e.target_id)
        for e in graph.in_adj.get(sn.node.node_id, []):
            if e.kind == EdgeKind.CALLS and e.source_id in graph.nodes:
                neighbor_ids.add(e.source_id)

    all_viz_ids = viz_ids | neighbor_ids

    for nid in all_viz_ids:
        n = graph.nodes.get(nid)
        if not n:
            continue
        graph_nodes_viz.append({
            "id": nid,
            "short": _short_id(nid),
            "layer": n.layer.name,
            "selected": nid in viz_ids,
            "file": _short_path(n.file_path) if n.file_path else "",
        })

    # Edges between visible nodes
    for nid in all_viz_ids:
        for e in graph.out_adj.get(nid, []):
            if e.target_id in all_viz_ids and e.kind in (EdgeKind.CALLS, EdgeKind.CONTAINS, EdgeKind.INHERITS):
                graph_edges_viz.append({
                    "source": nid,
                    "target": e.target_id,
                    "kind": e.kind.value,
                    "weight": round(e.weight, 3),
                })

    return {
        "query": query,
        "intent": intent,
        "weights": weights,
        "layer_budgets": layer_budget_fracs,
        "token_budget": token_budget,
        "budgets": {"file": file_budget, "class": class_budget, "function": fn_budget},
        "expansion_terms": expansion_terms[:12],
        "stats": stats,
        "layers": layer_traces,
        "selection": selection_steps,
        "result_summary": {
            "total_tokens": result.total_tokens,
            "layer_counts": result.layer_counts,
            "selector": "dynamic" if use_dynamic else "standard",
        },
        "graph": {
            "nodes": graph_nodes_viz[:200],
            "edges": graph_edges_viz[:500],
        },
    }


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>TACM Decision Path — {{QUERY}}</title>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', system-ui, sans-serif; background: #0d1117; color: #c9d1d9; }
.container { max-width: 1400px; margin: 0 auto; padding: 20px; }
h1 { color: #58a6ff; font-size: 1.6em; margin-bottom: 4px; }
h2 { color: #58a6ff; font-size: 1.2em; margin: 24px 0 12px; border-bottom: 1px solid #21262d; padding-bottom: 6px; }
h3 { color: #8b949e; font-size: 1em; margin: 16px 0 8px; }
.subtitle { color: #8b949e; font-size: 0.9em; margin-bottom: 20px; }
.grid { display: grid; gap: 16px; }
.grid-2 { grid-template-columns: 1fr 1fr; }
.grid-3 { grid-template-columns: 1fr 1fr 1fr; }
.card { background: #161b22; border: 1px solid #21262d; border-radius: 8px; padding: 16px; }
.badge { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 0.8em; font-weight: 600; }
.badge-bug { background: #f8514930; color: #f85149; }
.badge-structure { background: #58a6ff30; color: #58a6ff; }
.badge-explain { background: #3fb95030; color: #3fb950; }
.badge-file { background: #8b949e30; color: #8b949e; }
.badge-class { background: #d2a8ff30; color: #d2a8ff; }
.badge-function { background: #79c0ff30; color: #79c0ff; }
.badge-selected { background: #3fb95030; color: #3fb950; }
.badge-neighbor { background: #8b949e20; color: #8b949e; }
.weight-bar { display: flex; align-items: center; gap: 8px; margin: 3px 0; }
.weight-bar .label { width: 90px; font-size: 0.85em; text-align: right; }
.weight-bar .bar-bg { flex: 1; height: 18px; background: #21262d; border-radius: 3px; overflow: hidden; position: relative; }
.weight-bar .bar-fill { height: 100%; border-radius: 3px; transition: width 0.3s; }
.weight-bar .bar-val { position: absolute; right: 6px; top: 0; line-height: 18px; font-size: 0.75em; }
.signal-bm25 { background: #58a6ff; }
.signal-fan_in { background: #f0883e; }
.signal-fan_out { background: #d2a8ff; }
.signal-complexity { background: #f85149; }
.signal-test_cover { background: #3fb950; }
.signal-neighborhood { background: #db61a2; }
.signal-pagerank { background: #f778ba; }
table { width: 100%; border-collapse: collapse; font-size: 0.85em; }
th { text-align: left; padding: 6px 8px; border-bottom: 2px solid #21262d; color: #8b949e; font-weight: 600; }
td { padding: 5px 8px; border-bottom: 1px solid #21262d; }
tr:hover td { background: #1c2128; }
.score-cell { font-family: 'Cascadia Code', monospace; }
.mini-bar { display: inline-block; height: 10px; border-radius: 2px; margin-right: 2px; vertical-align: middle; }
.timeline { position: relative; padding-left: 24px; }
.timeline-item { position: relative; padding: 8px 0 8px 20px; border-left: 2px solid #21262d; }
.timeline-item:last-child { border-left-color: transparent; }
.timeline-dot { position: absolute; left: -7px; top: 12px; width: 12px; height: 12px; border-radius: 50%; border: 2px solid #0d1117; }
.timeline-dot.file { background: #8b949e; }
.timeline-dot.class { background: #d2a8ff; }
.timeline-dot.function { background: #79c0ff; }
.containment-tag { color: #3fb950; font-size: 0.8em; margin-left: 6px; }
.budget-meter { height: 24px; background: #21262d; border-radius: 4px; overflow: hidden; margin: 8px 0; position: relative; }
.budget-fill { height: 100%; transition: width 0.3s; }
.budget-file { background: #8b949e; }
.budget-class { background: #d2a8ff; }
.budget-function { background: #79c0ff; }
.budget-label { position: absolute; top: 0; right: 8px; line-height: 24px; font-size: 0.8em; }
.stat { text-align: center; }
.stat .num { font-size: 2em; font-weight: 700; color: #58a6ff; }
.stat .lbl { font-size: 0.8em; color: #8b949e; }
.expansion { display: flex; flex-wrap: wrap; gap: 4px; margin-top: 6px; }
.expansion span { background: #1c2128; padding: 2px 8px; border-radius: 4px; font-size: 0.8em; color: #79c0ff; }
#graph-container { width: 100%; height: 500px; border: 1px solid #21262d; border-radius: 8px; background: #0d1117; }
.tab-bar { display: flex; gap: 0; margin-bottom: 0; }
.tab { padding: 8px 20px; cursor: pointer; border: 1px solid #21262d; border-bottom: none; border-radius: 8px 8px 0 0; background: #0d1117; color: #8b949e; font-size: 0.9em; }
.tab.active { background: #161b22; color: #c9d1d9; border-bottom: 1px solid #161b22; margin-bottom: -1px; z-index: 1; }
.tab-content { display: none; }
.tab-content.active { display: block; }
</style>
</head>
<body>
<div class="container">

<h1>TACM Decision Path</h1>
<div class="subtitle">Query: "<span id="q-text"></span>" &nbsp; | &nbsp; Selector: <span id="selector-type"></span></div>

<!-- Row 1: Query + Intent + Stats -->
<div class="grid grid-3">
  <div class="card">
    <h3>Intent Classification</h3>
    <div style="margin:12px 0"><span id="intent-badge" class="badge"></span></div>
    <div id="weights-viz"></div>
  </div>
  <div class="card">
    <h3>Layer Budget Allocation</h3>
    <div id="budget-alloc"></div>
    <div class="budget-meter" style="margin-top: 12px">
      <div id="budget-bar-file" class="budget-fill budget-file" style="float:left"></div>
      <div id="budget-bar-class" class="budget-fill budget-class" style="float:left"></div>
      <div id="budget-bar-fn" class="budget-fill budget-function" style="float:left"></div>
    </div>
    <div style="font-size:0.8em; color:#8b949e; display:flex; justify-content:space-between; margin-top:4px">
      <span>■ FILE</span><span style="color:#d2a8ff">■ CLASS</span><span style="color:#79c0ff">■ FUNCTION</span>
    </div>
  </div>
  <div class="card">
    <h3>Repository Stats</h3>
    <div class="grid grid-2" style="margin-top:12px">
      <div class="stat"><div class="num" id="st-fns"></div><div class="lbl">Functions</div></div>
      <div class="stat"><div class="num" id="st-cls"></div><div class="lbl">Classes</div></div>
      <div class="stat"><div class="num" id="st-files"></div><div class="lbl">Files</div></div>
      <div class="stat"><div class="num" id="st-edges"></div><div class="lbl">Edges</div></div>
    </div>
    <h3 style="margin-top:12px">Query Expansion</h3>
    <div id="expansion" class="expansion"></div>
  </div>
</div>

<!-- Row 2: Per-layer candidate tables -->
<h2>Layer-by-Layer Scoring</h2>
<div class="tab-bar">
  <div class="tab active" onclick="showTab('file-tab')">FILE</div>
  <div class="tab" onclick="showTab('class-tab')">CLASS</div>
  <div class="tab" onclick="showTab('fn-tab')">FUNCTION</div>
</div>

<div id="file-tab" class="tab-content active card" style="border-radius: 0 8px 8px 8px">
  <table><thead id="file-head"></thead><tbody id="file-body"></tbody></table>
</div>
<div id="class-tab" class="tab-content card" style="border-radius: 0 8px 8px 8px">
  <table><thead id="class-head"></thead><tbody id="class-body"></tbody></table>
</div>
<div id="fn-tab" class="tab-content card" style="border-radius: 0 8px 8px 8px">
  <table><thead id="fn-head"></thead><tbody id="fn-body"></tbody></table>
</div>

<!-- Row 3: Selection timeline + Budget usage -->
<div class="grid grid-2">
  <div>
    <h2>Selection Path</h2>
    <div class="card">
      <div id="selection-timeline" class="timeline"></div>
    </div>
  </div>
  <div>
    <h2>Token Budget Consumption</h2>
    <div class="card">
      <canvas id="budget-chart" height="350"></canvas>
    </div>
  </div>
</div>

<!-- Row 4: Graph -->
<h2>Context Graph</h2>
<div class="card">
  <div style="font-size:0.8em; color:#8b949e; margin-bottom:8px">
    Selected nodes (solid) + 1-hop CALLS neighbors (faded). Drag to rearrange.
  </div>
  <canvas id="graph-canvas" width="1360" height="500" style="width:100%; border-radius:6px; cursor:grab;"></canvas>
</div>

</div><!-- /container -->

<script>
const DATA = __TRACE_DATA__;

// --- Populate header ---
document.getElementById('q-text').textContent = DATA.query;
document.getElementById('selector-type').textContent = DATA.result_summary.selector;

// --- Intent ---
const ib = document.getElementById('intent-badge');
ib.textContent = DATA.intent.toUpperCase();
ib.className = 'badge badge-' + DATA.intent;

// --- Weights ---
const wDiv = document.getElementById('weights-viz');
const colors = {bm25:'#58a6ff', fan_in:'#f0883e', fan_out:'#d2a8ff', complexity:'#f85149', test_cover:'#3fb950'};
for (const [k,v] of Object.entries(DATA.weights)) {
  const pct = (v * 100).toFixed(0);
  wDiv.innerHTML += `<div class="weight-bar"><div class="label">${k}</div><div class="bar-bg"><div class="bar-fill" style="width:${pct}%;background:${colors[k]}"></div><div class="bar-val">${pct}%</div></div></div>`;
}

// --- Budget allocation ---
const bDiv = document.getElementById('budget-alloc');
for (const [k,v] of Object.entries(DATA.budgets)) {
  bDiv.innerHTML += `<div style="display:flex;justify-content:space-between;font-size:0.9em;margin:4px 0"><span>${k.toUpperCase()}</span><span>${v} tokens (${(DATA.layer_budgets[k]*100).toFixed(0)}%)</span></div>`;
}
document.getElementById('budget-bar-file').style.width = (DATA.layer_budgets.file*100)+'%';
document.getElementById('budget-bar-class').style.width = (DATA.layer_budgets['class']*100)+'%';
document.getElementById('budget-bar-fn').style.width = (DATA.layer_budgets.function*100)+'%';

// --- Stats ---
document.getElementById('st-fns').textContent = DATA.stats.functions;
document.getElementById('st-cls').textContent = DATA.stats.classes;
document.getElementById('st-files').textContent = DATA.stats.files;
document.getElementById('st-edges').textContent = DATA.stats.edges;

// --- Expansion ---
const eDiv = document.getElementById('expansion');
if (DATA.expansion_terms.length === 0) eDiv.innerHTML = '<span style="color:#8b949e">No expansion needed</span>';
else DATA.expansion_terms.forEach(t => eDiv.innerHTML += `<span>${t}</span>`);

// --- Tabs ---
function showTab(id) {
  document.querySelectorAll('.tab-content').forEach(e => e.classList.remove('active'));
  document.querySelectorAll('.tab').forEach(e => e.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  event.target.classList.add('active');
}

// --- Layer tables ---
function signalBar(val, color, maxW) {
  const w = Math.max(1, val * maxW);
  return `<span class="mini-bar" style="width:${w}px;background:${color}" title="${val}"></span>`;
}

function buildTable(layerName, headId, bodyId) {
  const layer = DATA.layers[layerName];
  if (!layer || !layer.candidates.length) {
    document.getElementById(bodyId).innerHTML = '<tr><td colspan="10" style="color:#8b949e">No candidates</td></tr>';
    return;
  }
  const isFn = layerName === 'FUNCTION';
  const selectedIds = new Set(DATA.selection.map(s => s.id));

  let hdr = '<tr><th>#</th><th>Name</th><th>File</th><th>Tok</th><th>BM25</th><th>Fan-In</th><th>Fan-Out</th><th>Cmplx</th>';
  if (isFn) hdr += '<th>Nbr</th><th>PR</th>';
  hdr += '<th>Combined</th><th></th></tr>';
  document.getElementById(headId).innerHTML = hdr;

  const rows = layer.candidates.slice(0, 30);
  let html = '';
  rows.forEach((c, i) => {
    const sel = selectedIds.has(c.id);
    const rowStyle = sel ? 'background:#3fb95010;' : '';
    html += `<tr style="${rowStyle}">`;
    html += `<td>${i+1}</td>`;
    html += `<td title="${c.id}">${c.short}</td>`;
    html += `<td style="color:#8b949e;font-size:0.8em">${c.file}:${c.line||''}</td>`;
    html += `<td>${c.tokens}</td>`;
    html += `<td class="score-cell">${signalBar(c.signals.bm25,'#58a6ff',60)} ${c.signals.bm25.toFixed(3)}</td>`;
    html += `<td class="score-cell">${signalBar(c.signals.fan_in,'#f0883e',60)} ${c.signals.fan_in.toFixed(3)}</td>`;
    html += `<td class="score-cell">${signalBar(c.signals.fan_out,'#d2a8ff',60)} ${c.signals.fan_out.toFixed(3)}</td>`;
    html += `<td class="score-cell">${signalBar(c.signals.complexity,'#f85149',60)} ${c.signals.complexity.toFixed(3)}</td>`;
    if (isFn) {
      html += `<td class="score-cell">${signalBar(c.neighborhood,'#db61a2',60)} ${c.neighborhood.toFixed(3)}</td>`;
      html += `<td class="score-cell">${signalBar(c.pagerank,'#f778ba',60)} ${c.pagerank.toFixed(3)}</td>`;
    }
    html += `<td class="score-cell" style="font-weight:700">${c.combined.toFixed(4)}</td>`;
    html += `<td>${sel ? '<span class="badge badge-selected">SELECTED</span>' : ''}</td>`;
    html += '</tr>';
  });
  if (layer.total_candidates > 30) {
    html += `<tr><td colspan="12" style="color:#8b949e;text-align:center">... and ${layer.total_candidates - 30} more candidates</td></tr>`;
  }
  document.getElementById(bodyId).innerHTML = html;
}

buildTable('FILE', 'file-head', 'file-body');
buildTable('CLASS', 'class-head', 'class-body');
buildTable('FUNCTION', 'fn-head', 'fn-body');

// --- Selection timeline ---
const tlDiv = document.getElementById('selection-timeline');
DATA.selection.forEach((s, i) => {
  const dotClass = s.layer.toLowerCase();
  const cb = s.containment_bonus ? '<span class="containment-tag">⬆ containment +0.15</span>' : '';
  const pct = ((s.running_tokens / DATA.token_budget) * 100).toFixed(1);
  tlDiv.innerHTML += `
    <div class="timeline-item">
      <div class="timeline-dot ${dotClass}"></div>
      <div style="display:flex;justify-content:space-between">
        <div>
          <span class="badge badge-${dotClass}">${s.layer}</span>
          <strong style="margin-left:6px">${s.short}</strong>${cb}
        </div>
        <div style="color:#8b949e;font-size:0.85em">${s.tokens} tok (${pct}% used)</div>
      </div>
      <div style="font-size:0.8em;color:#8b949e;margin-top:2px">${s.file} &nbsp; score: ${s.score.toFixed(4)}</div>
    </div>`;
});

// --- Budget chart (simple canvas bar chart) ---
(function() {
  const canvas = document.getElementById('budget-chart');
  const ctx = canvas.getContext('2d');
  canvas.width = canvas.offsetWidth * 2;
  canvas.height = 700;
  ctx.scale(2, 2);
  const W = canvas.offsetWidth, H = 350;
  const pad = {l: 50, r: 20, t: 20, b: 30};

  const steps = DATA.selection;
  if (!steps.length) return;

  const xScale = (W - pad.l - pad.r) / steps.length;
  const yMax = DATA.token_budget;
  const yScale = (H - pad.t - pad.b) / yMax;

  // Grid
  ctx.strokeStyle = '#21262d';
  ctx.lineWidth = 0.5;
  for (let y = 0; y <= yMax; y += Math.ceil(yMax/5)) {
    const py = H - pad.b - y * yScale;
    ctx.beginPath(); ctx.moveTo(pad.l, py); ctx.lineTo(W - pad.r, py); ctx.stroke();
    ctx.fillStyle = '#8b949e'; ctx.font = '10px sans-serif'; ctx.textAlign = 'right';
    ctx.fillText(y, pad.l - 4, py + 3);
  }

  // Budget line
  ctx.strokeStyle = '#f8514950'; ctx.lineWidth = 1; ctx.setLineDash([4,4]);
  const budgetY = H - pad.b - yMax * yScale;
  ctx.beginPath(); ctx.moveTo(pad.l, budgetY); ctx.lineTo(W - pad.r, budgetY); ctx.stroke();
  ctx.setLineDash([]);
  ctx.fillStyle = '#f85149'; ctx.font = '10px sans-serif'; ctx.textAlign = 'left';
  ctx.fillText('budget=' + yMax, W - pad.r - 80, budgetY - 4);

  // Bars
  const layerColors = {FILE:'#8b949e', CLASS:'#d2a8ff', FUNCTION:'#79c0ff'};
  steps.forEach((s, i) => {
    const x = pad.l + i * xScale;
    const barH = s.running_tokens * yScale;
    const y = H - pad.b - barH;
    ctx.fillStyle = layerColors[s.layer] || '#79c0ff';
    ctx.fillRect(x + 2, y, Math.max(xScale - 4, 3), barH);
  });

  // X labels (every few)
  ctx.fillStyle = '#8b949e'; ctx.font = '9px sans-serif'; ctx.textAlign = 'center';
  steps.forEach((s, i) => {
    if (steps.length < 20 || i % Math.ceil(steps.length/15) === 0) {
      ctx.save(); ctx.translate(pad.l + i * xScale + xScale/2, H - pad.b + 12);
      ctx.rotate(-0.5); ctx.fillText(s.short.slice(0,12), 0, 0); ctx.restore();
    }
  });
})();

// --- Force-directed graph ---
(function() {
  const canvas = document.getElementById('graph-canvas');
  const ctx = canvas.getContext('2d');
  const W = canvas.width, H = canvas.height;
  const gNodes = DATA.graph.nodes.map((n, i) => ({
    ...n, x: W/2 + (Math.random()-0.5)*400, y: H/2 + (Math.random()-0.5)*300, vx:0, vy:0, idx:i
  }));
  const idxMap = {};
  gNodes.forEach((n,i) => idxMap[n.id] = i);
  const gEdges = DATA.graph.edges.filter(e => idxMap[e.source] !== undefined && idxMap[e.target] !== undefined)
    .map(e => ({...e, si: idxMap[e.source], ti: idxMap[e.target]}));

  const layerColor = {FILE:'#8b949e', CLASS:'#d2a8ff', FUNCTION:'#79c0ff'};
  let dragging = null, mx = 0, my = 0;

  function simulate() {
    // Repulsion
    for (let i = 0; i < gNodes.length; i++) {
      for (let j = i+1; j < gNodes.length; j++) {
        let dx = gNodes[j].x - gNodes[i].x, dy = gNodes[j].y - gNodes[i].y;
        let d2 = dx*dx + dy*dy + 1;
        let f = 800 / d2;
        gNodes[i].vx -= dx * f; gNodes[i].vy -= dy * f;
        gNodes[j].vx += dx * f; gNodes[j].vy += dy * f;
      }
    }
    // Attraction
    gEdges.forEach(e => {
      let s = gNodes[e.si], t = gNodes[e.ti];
      let dx = t.x - s.x, dy = t.y - s.y, d = Math.sqrt(dx*dx + dy*dy + 1);
      let f = (d - 80) * 0.01;
      s.vx += dx * f; s.vy += dy * f;
      t.vx -= dx * f; t.vy -= dy * f;
    });
    // Center gravity
    gNodes.forEach(n => { n.vx += (W/2 - n.x) * 0.001; n.vy += (H/2 - n.y) * 0.001; });
    // Apply
    gNodes.forEach(n => {
      if (n === dragging) return;
      n.vx *= 0.85; n.vy *= 0.85;
      n.x += n.vx; n.y += n.vy;
      n.x = Math.max(20, Math.min(W-20, n.x));
      n.y = Math.max(20, Math.min(H-20, n.y));
    });
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);
    // Edges
    gEdges.forEach(e => {
      const s = gNodes[e.si], t = gNodes[e.ti];
      ctx.strokeStyle = e.kind === 'CALLS' ? '#30363d' : e.kind === 'CONTAINS' ? '#21262d' : '#21262d';
      ctx.lineWidth = e.kind === 'CALLS' ? 1.5 : 0.8;
      ctx.setLineDash(e.kind === 'CONTAINS' ? [3,3] : []);
      ctx.beginPath(); ctx.moveTo(s.x, s.y); ctx.lineTo(t.x, t.y); ctx.stroke();
      ctx.setLineDash([]);
    });
    // Nodes
    gNodes.forEach(n => {
      const r = n.selected ? 8 : 5;
      const alpha = n.selected ? 1.0 : 0.4;
      ctx.globalAlpha = alpha;
      ctx.fillStyle = layerColor[n.layer] || '#79c0ff';
      ctx.beginPath(); ctx.arc(n.x, n.y, r, 0, Math.PI*2); ctx.fill();
      if (n.selected) {
        ctx.strokeStyle = '#3fb950'; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.arc(n.x, n.y, r+2, 0, Math.PI*2); ctx.stroke();
      }
      ctx.globalAlpha = n.selected ? 1.0 : 0.5;
      ctx.fillStyle = '#c9d1d9'; ctx.font = (n.selected ? 'bold ' : '') + '10px sans-serif';
      ctx.textAlign = 'center'; ctx.fillText(n.short.slice(0,20), n.x, n.y - r - 4);
      ctx.globalAlpha = 1.0;
    });
  }

  function tick() { simulate(); draw(); requestAnimationFrame(tick); }
  tick();

  // Drag
  canvas.addEventListener('mousedown', e => {
    const rect = canvas.getBoundingClientRect();
    const sx = (e.clientX - rect.left) * (W / rect.width);
    const sy = (e.clientY - rect.top) * (H / rect.height);
    gNodes.forEach(n => {
      if (Math.hypot(n.x - sx, n.y - sy) < 12) dragging = n;
    });
  });
  canvas.addEventListener('mousemove', e => {
    if (!dragging) return;
    const rect = canvas.getBoundingClientRect();
    dragging.x = (e.clientX - rect.left) * (W / rect.width);
    dragging.y = (e.clientY - rect.top) * (H / rect.height);
  });
  canvas.addEventListener('mouseup', () => dragging = null);
})();
</script>
</body>
</html>"""


def generate_html(trace: dict, output_path: str) -> None:
    data_json = json.dumps(trace, indent=None)
    html = HTML_TEMPLATE.replace("__TRACE_DATA__", data_json)
    html = html.replace("{{QUERY}}", trace["query"][:80])
    Path(output_path).write_text(html, encoding="utf-8")
    print(f"  Report saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Visualize TACM decision path")
    parser.add_argument("--repo", type=Path, required=True, help="Path to repo root")
    parser.add_argument("--query", type=str, required=True, help="Natural language query")
    parser.add_argument("--budget", type=int, default=4000, help="Token budget (default: 4000)")
    parser.add_argument("--dynamic", action="store_true", help="Use dynamic cross-layer selector")
    parser.add_argument("--output", type=str, default=None, help="Output HTML path (default: tacm_trace.html)")
    parser.add_argument("--open", action="store_true", help="Open in browser after generation")
    args = parser.parse_args()

    if not args.repo.exists():
        print(f"Repo not found: {args.repo}")
        sys.exit(1)

    output = args.output or "tacm_trace.html"

    print(f"  Query:  {args.query}")
    print(f"  Repo:   {args.repo}")
    print(f"  Budget: {args.budget}")
    print(f"  Selector: {'dynamic' if args.dynamic else 'standard'}")

    trace = trace_tacm(
        repo_root=args.repo.resolve(),
        query=args.query,
        token_budget=args.budget,
        use_dynamic=args.dynamic,
    )

    generate_html(trace, output)

    if args.open:
        webbrowser.open(str(Path(output).resolve()))


if __name__ == "__main__":
    main()
