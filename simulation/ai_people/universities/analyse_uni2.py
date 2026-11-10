"""Summarise uni2_<mode>.json. Usage: python3 analyse_uni2.py pilot|full"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
mode = sys.argv[1] if len(sys.argv) > 1 else "pilot"
if mode == "combined":  # pilot 2 + extra batch (same design, different people)
    d = {"rows": json.load(open(os.path.join(HERE, "uni2_pilot.json")))["rows"]
         + json.load(open(os.path.join(HERE, "uni2_extra.json")))["rows"]}
else:
    d = json.load(open(os.path.join(HERE, f"uni2_{mode}.json")))
rows = [r for r in d["rows"] if r["choice"]]
STYLE = ["gut", "mostly gut", "mostly careful", "very careful"]
V = {1: ["brochure", "honest", "hype", "counsellor", "relatives", "all", "all_disclosed"],
     2: ["brochure", "honest", "agent", "agent_village", "agent_village_disclosed"]}
LABEL = {1: "expensive private college (B)", 2: "Canada via agent (B)"}


def pct(rs):
    return 100 * sum(r["choice"] == "B" for r in rs) / len(rs) if rs else float("nan")


print(f"[{mode}] usable {len(rows)}/{len(d['rows'])}")
for s in (1, 2):
    R = [r for r in rows if r["scenario"] == s]
    print(f"\n===== Scenario {s}: share choosing {LABEL[s]} =====")
    print(f"{'version':25s} {'all':>5s} {'stud':>5s} {'parent':>6s}  loans(B)")
    for v in V[s]:
        rv = [r for r in R if r["version"] == v]
        st = [r for r in rv if r["role"] == "student"]
        pa = [r for r in rv if r["role"] == "parent"]
        loans = sum(r["loan"] == "yes" for r in rv if r["choice"] == "B")
        print(f"{v:25s} {pct(rv):5.0f} {pct(st):5.0f} {pct(pa):6.0f}  {loans}/{sum(r['choice']=='B' for r in rv)}")
    print("\nby decision style: " + " | ".join(V[s]))
    for i, lab in enumerate(STYLE):
        print(f"  {lab:14s} " + " | ".join(f"{pct([r for r in R if r['version']==v and r['style_level']==i]):3.0f}" for v in V[s]))
    print("by income (0 tight, 1 middle, 2 well-off):")
    for i in range(3):
        print(f"  income {i}       " + " | ".join(f"{pct([r for r in R if r['version']==v and r['income_level']==i]):3.0f}" for v in V[s]))
    for key, word, lab in [("trust", "believe", "trusts ads/agents"), ("relatives", "matters a lot", "relatives matter a lot")]:
        print(f"'{lab}' yes/no: " + " | ".join(
            f"{v}: {pct([r for r in R if r['version']==v and word in r[key]]):.0f}/{pct([r for r in R if r['version']==v and word not in r[key]]):.0f}"
            for v in V[s]))
    by = {(r["person"], r["version"]): r for r in R}
    people = sorted({r["person"] for r in R})
    print("switches vs brochure (A->B / B->A):  " + "  ".join(
        f"{v}: {sum(1 for p in people if by.get((p,'brochure')) and by.get((p,v)) and by[(p,'brochure')]['choice']=='A' and by[(p,v)]['choice']=='B')}"
        f"/{sum(1 for p in people if by.get((p,'brochure')) and by.get((p,v)) and by[(p,'brochure')]['choice']=='B' and by[(p,v)]['choice']=='A')}"
        for v in V[s][1:]))
    sus = r"scam|trick|red flag|too good|pressure|suspicious|fake|guarantee|misleading|commission|marketing|lie|lying|exaggerat"
    print("reasons calling something a trick/red flag: " + " | ".join(
        f"{v}: {sum(bool(re.search(sus, r['reason'], re.I)) for r in R if r['version']==v)}" for v in V[s]))
    print("sample reasons:")
    for v in V[s]:
        for r in [r for r in R if r["version"] == v][:2]:
            print(f"  [{v} -> {r['choice']}] {r['role']} {r['name']} ({STYLE[r['style_level']]}, inc {r['income_level']}): {r['reason'][:210]}")
