"""analyze_zcr.py — Slice zero_cost_runner results to find where pure-algo
levers could close the gap to Hybrid.

Reads a dump from zero_cost_runner and surfaces:
  1. Per-instance head-to-head: TACM vs TACM-PPR  (where did PPR help/hurt)
  2. Hybrid-beats-TACM seams: instances where Hybrid won but TACM lost
  3. ranked_outside_k depth: where does GT actually sit in TACM's ranking
  4. Repo-level breakdown: which codebases TACM family struggles on

Usage:
    python3 analyze_zcr.py <results.json>
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path


def load(path: Path) -> tuple[dict, dict[tuple[str, str], dict]]:
    """Return (meta, by_cond[(instance_id, condition)] = row)."""
    data = json.loads(path.read_text())
    by_cond: dict[tuple[str, str], dict] = {
        (r["instance_id"], r["condition"]): r for r in data["results"]
    }
    return data, by_cond


def rr(rank: int | None, hit: bool) -> float:
    """Reciprocal rank (0 for miss)."""
    if not hit or rank is None or rank <= 0:
        return 0.0
    return 1.0 / rank


def head_to_head_tacm_vs_ppr(by_cond, instances):
    print("=" * 96)
    print("1. TACM vs TACM-PPR head-to-head (by reciprocal rank)")
    print("=" * 96)
    helps, hurts, ties = [], [], []
    for iid in instances:
        a = by_cond.get((iid, "tacm"))
        b = by_cond.get((iid, "tacm-ppr"))
        if not a or not b:
            continue
        ra = rr(a["fn_strict_rank"], a["fn_hit"])
        rb = rr(b["fn_strict_rank"], b["fn_hit"])
        da = a["fn_strict_rank"] if a["fn_strict_rank"] else None
        db = b["fn_strict_rank"] if b["fn_strict_rank"] else None
        row = (iid, da, db, a["top_k_tokens"], b["top_k_tokens"])
        if rb > ra + 1e-9:
            helps.append(row)
        elif rb < ra - 1e-9:
            hurts.append(row)
        else:
            ties.append(row)

    print(f"\n  PPR helped: {len(helps)}   PPR hurt: {len(hurts)}   Tied: {len(ties)}")

    print("\n  --- PPR WINS (best lifts first) ---")
    helps.sort(key=lambda r: (1 / (r[2] or 1e9)) - (1 / (r[1] or 1e9)), reverse=True)
    print(f"  {'instance':45s} {'tacm':>6s} {'ppr':>6s}  {'Δtok':>6s}")
    for iid, a, b, ta, tb in helps[:15]:
        dtok = tb - ta
        print(f"  {iid:45s} {str(a):>6s} {str(b):>6s}  {dtok:+6d}")

    print("\n  --- PPR LOSSES (worst regressions first) ---")
    hurts.sort(key=lambda r: (1 / (r[1] or 1e9)) - (1 / (r[2] or 1e9)), reverse=True)
    print(f"  {'instance':45s} {'tacm':>6s} {'ppr':>6s}  {'Δtok':>6s}")
    for iid, a, b, ta, tb in hurts[:10]:
        dtok = tb - ta
        print(f"  {iid:45s} {str(a):>6s} {str(b):>6s}  {dtok:+6d}")


def hybrid_beats_tacm(by_cond, instances):
    print("\n" + "=" * 96)
    print("2. Seams: Hybrid won, TACM-PPR didn't (target for pure-algo work)")
    print("=" * 96)
    seams = []
    for iid in instances:
        h = by_cond.get((iid, "hybrid"))
        t = by_cond.get((iid, "tacm-ppr"))
        if not h or not t:
            continue
        rh = rr(h["fn_strict_rank"], h["fn_hit"])
        rt = rr(t["fn_strict_rank"], t["fn_hit"])
        # Hybrid top-5 but TACM-PPR not
        if h["fn_hit"] and h["fn_strict_rank"] <= 5 and not (t["fn_hit"] and t["fn_strict_rank"] <= 5):
            seams.append((iid, h["fn_strict_rank"], t["fn_strict_rank"] or "MISS",
                          h["top_k_tokens"], t["top_k_tokens"], rh - rt))

    seams.sort(key=lambda r: r[5], reverse=True)
    print(f"\n  {len(seams)} instances where Hybrid landed @≤5 but TACM-PPR did not:")
    print(f"  {'instance':45s} {'hybrid':>7s} {'ppr':>7s}  {'htok':>5s} {'ptok':>5s}")
    for iid, hr, tr, ht, tt, _ in seams:
        print(f"  {iid:45s} {hr:>7d} {str(tr):>7s}  {ht:>5d} {tt:>5d}")


def ranked_outside_k_depth(by_cond, instances):
    print("\n" + "=" * 96)
    print("3. ranked_outside_k depth — where TACM-PPR actually ranks GT when it misses top-5")
    print("=" * 96)
    buckets = {"6-10": 0, "11-20": 0, "21-50": 0, "51-100": 0, "101-500": 0, ">500": 0}
    ranks = []
    for iid in instances:
        r = by_cond.get((iid, "tacm-ppr"))
        if not r:
            continue
        if r["miss_bucket"] != "ranked_outside_k":
            continue
        rank = r["fn_strict_rank"]
        ranks.append(rank)
        if rank <= 10: buckets["6-10"] += 1
        elif rank <= 20: buckets["11-20"] += 1
        elif rank <= 50: buckets["21-50"] += 1
        elif rank <= 100: buckets["51-100"] += 1
        elif rank <= 500: buckets["101-500"] += 1
        else: buckets[">500"] += 1

    n = len(ranks) or 1
    print(f"\n  {n} instances where TACM-PPR had GT in pool but outside top-5:")
    for b, c in buckets.items():
        bar = "█" * c
        print(f"    rank {b:>8s}: {c:>3d}  {bar}")
    ranks.sort()
    if ranks:
        mid = ranks[len(ranks) // 2]
        print(f"\n  median miss-rank: {mid}")
        print(f"  → A reranker over TACM-PPR's top-20 would recover {buckets['6-10'] + buckets['11-20']}/{n} "
              f"({100*(buckets['6-10']+buckets['11-20'])/n:.0f}%)")
        print(f"  → Top-50 reranker recovers {buckets['6-10']+buckets['11-20']+buckets['21-50']}/{n} "
              f"({100*(buckets['6-10']+buckets['11-20']+buckets['21-50'])/n:.0f}%)")


def repo_breakdown(by_cond, instances):
    print("\n" + "=" * 96)
    print("4. Per-repo MRR (where TACM-PPR struggles most vs Hybrid)")
    print("=" * 96)
    by_repo: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    by_repo_count: dict[str, int] = defaultdict(int)
    for iid in instances:
        for cond in ("bm25", "hybrid", "tacm", "tacm-ppr"):
            r = by_cond.get((iid, cond))
            if not r:
                continue
            by_repo[r["repo"]][cond].append(rr(r["fn_strict_rank"], r["fn_hit"]))
        by_repo_count[by_cond[(iid, "bm25")]["repo"]] += 1

    print(f"\n  {'repo':35s} {'N':>3s} {'bm25':>7s} {'hybrid':>7s} {'tacm':>7s} {'tacm-ppr':>9s}  gap(h-ppr)")
    rows = []
    for repo, conds in by_repo.items():
        n = by_repo_count[repo]
        def mean(xs): return sum(xs) / len(xs) if xs else 0.0
        mb, mh, mt, mp = mean(conds["bm25"]), mean(conds["hybrid"]), mean(conds["tacm"]), mean(conds["tacm-ppr"])
        rows.append((repo, n, mb, mh, mt, mp, mh - mp))
    rows.sort(key=lambda r: r[6], reverse=True)
    for repo, n, mb, mh, mt, mp, gap in rows:
        print(f"  {repo:35s} {n:>3d} {mb:>7.3f} {mh:>7.3f} {mt:>7.3f} {mp:>9.3f}  {gap:+.3f}")


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    path = Path(sys.argv[1])
    data, by_cond = load(path)
    instances = sorted({iid for iid, _ in by_cond.keys()})
    print(f"Loaded {len(data['results'])} rows across {len(instances)} instances, "
          f"{len(data['conditions'])} conditions from {path.name}")
    head_to_head_tacm_vs_ppr(by_cond, instances)
    hybrid_beats_tacm(by_cond, instances)
    ranked_outside_k_depth(by_cond, instances)
    repo_breakdown(by_cond, instances)


if __name__ == "__main__":
    main()
