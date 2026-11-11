"""Summarise health_<mode>.json. Usage: python3 analyse_health.py pilot|combined"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
mode = sys.argv[1] if len(sys.argv) > 1 else "pilot"
def load(f):
    p = os.path.join(HERE, f)
    return json.load(open(p))["rows"] if os.path.exists(p) else []


if mode == "combined":  # H1 from pilot + extras; H2 only from the v2 (not-improving pain) runs
    rows_all = [r for f in ("health_pilot.json", "health_extra.json", "health_extra2.json") for r in load(f) if r["scenario"] == 1] \
        + [r for f in ("health_h2v2.json", "health_h2v2extra.json", "health_h2v2extra2.json") for r in load(f)]
else:
    rows_all = load(f"health_{mode}.json")
rows = [r for r in rows_all if r["choice"]]
STYLE = ["gut", "mostly gut", "mostly careful", "very careful"]
V = {1: ["base", "honest", "fear", "package", "anecdote", "all", "all_disclosed"],
     2: ["base", "honest", "fear_ad", "deal", "anecdote", "all", "all_disclosed"]}
LABEL = {1: "stent now (B)", 2: "MRI now (B)"}


def pct(rs):
    return 100 * sum(r["choice"] == "B" for r in rs) / len(rs) if rs else float("nan")


print(f"[{mode}] usable {len(rows)}/{len(rows_all)}")
for s in sorted({r["scenario"] for r in rows}):
    R = [r for r in rows if r["scenario"] == s]
    print(f"\n===== H{s}: share choosing {LABEL[s]} (n people = {len({r['person'] for r in R})}) =====")
    print(f"{'version':15s} {'all':>5s} {'patient':>8s} {'child':>6s}  loans(B)")
    for v in V[s]:
        rv = [r for r in R if r["version"] == v]
        pa = [r for r in rv if r["role"] == "patient"]
        ch = [r for r in rv if r["role"] == "child"]
        nb = sum(r["choice"] == "B" for r in rv)
        print(f"{v:15s} {pct(rv):5.0f} {pct(pa):8.0f} {pct(ch):6.0f}  {sum(r['loan']=='yes' for r in rv if r['choice']=='B')}/{nb}")
    print("by style: " + " | ".join(V[s]))
    for i, lab in enumerate(STYLE):
        print(f"  {lab:14s} " + " | ".join(f"{pct([r for r in R if r['version']==v and r['style_level']==i]):3.0f}" for v in V[s]))
    print("by income (0 tight .. 2 rich):")
    for i in range(3):
        print(f"  income {i}       " + " | ".join(f"{pct([r for r in R if r['version']==v and r['income_level']==i]):3.0f}" for v in V[s]))
    for word, lab in [("fully trust|tend to believe", "trusting"), ("suspicious", "suspicious")]:
        print(f"  {lab:14s} " + " | ".join(f"{pct([r for r in R if r['version']==v and re.search(word, r['trust'])]):3.0f}" for v in V[s]))
    sus = r"scam|trick|red flag|pressure|suspicious|fake|misleading|commission|marketing|target|upsell|scare|fear|sales"
    print("reasons calling something a trick: " + " | ".join(
        f"{v}: {sum(bool(re.search(sus, r['reason'], re.I)) for r in R if r['version']==v)}" for v in V[s]))
    print("sample reasons:")
    for v in V[s]:
        for r in [r for r in R if r["version"] == v][:2]:
            print(f"  [{v} -> {r['choice']}] {r['role']} {r['name']} ({STYLE[r['style_level']]}, inc {r['income_level']}): {r['reason'][:200]}")
