"""Summarise the FOMO data. Usage: python3 analyse_fomo.py pilot|combined"""
import json
import os
import statistics as st
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
mode = sys.argv[1] if len(sys.argv) > 1 else "pilot"
files = ["fomo_pilot.json", "fomo_extra.json", "fomo_extra2.json"] if mode == "combined" else [f"fomo_{mode}.json"]
rows_all = [r for f in files if os.path.exists(os.path.join(DATA, f))
            for r in json.load(open(os.path.join(DATA, f)))["rows"]]
rows = [r for r in rows_all if r["invest"] and r["amount"] is not None and r["left_out"]]
V = ["base", "friend", "influencer", "crowd", "app", "all", "all_lossrate", "all_silent"]
SHORT = ["base", "friend", "influ", "crowd", "app", "all", "loss%", "silent"]
STYLE = ["gut", "mostly gut", "mostly careful", "very careful"]


def pct(rs):
    return 100 * sum(r["invest"] == "yes" for r in rs) / len(rs) if rs else float("nan")


def amt(rs):
    return st.mean(r["amount"] if r["invest"] == "yes" else 0 for r in rs) if rs else float("nan")


def left(rs):
    return st.mean(r["left_out"] for r in rs) if rs else float("nan")


def line(label, R, f):
    n = len({r["person"] for r in R})
    print(f"{label:20s} n={n:2d}  " + "  ".join(f"{f([r for r in R if r['version'] == v]):6.1f}" for v in V))


head = "  ".join(f"{s:>6s}" for s in SHORT)
print(f"[{mode}] usable {len(rows)}/{len(rows_all)}")
print(f"\n% who INVEST:              {head}")
line("All", rows, pct)
for k in ("careful", "average", "likes_risk"):
    line("  " + k, [r for r in rows if r["risk"] == k], pct)
line("  feels behind", [r for r in rows if r["behind"]], pct)
line("  not behind", [r for r in rows if not r["behind"]], pct)
print("By decision style:")
for i, lab in enumerate(STYLE):
    line("  " + lab, [r for r in rows if r["style_level"] == i], pct)
print("By country:")
for c in sorted({r["country"] for r in rows}):
    line("  " + c[:18], [r for r in rows if r["country"] == c], pct)
print(f"\nMean % of savings put in (0 if no): {head}")
line("All", rows, amt)
for k in ("careful", "average", "likes_risk"):
    line("  " + k, [r for r in rows if r["risk"] == k], amt)
print(f"\nMean LEFT_OUT (1-7):       {head}")
line("All", rows, left)
line("  feels behind", [r for r in rows if r["behind"]], left)
line("  not behind", [r for r in rows if not r["behind"]], left)
print("\nSample reasons:")
for v in V:
    for k in ("careful", "likes_risk"):
        for r in [r for r in rows if r["version"] == v and r["risk"] == k][:1]:
            print(f"  [{v} | {k} | invest={r['invest']} {r['amount']}% left={r['left_out']}] "
                  f"{r['name']} ({r['country']}): {r['reason'][:200]}")
