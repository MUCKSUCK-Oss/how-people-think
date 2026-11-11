"""Summarise tgt_<mode>.json. Usage: python3 analyse_tgt.py pilot|combined"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
mode = sys.argv[1] if len(sys.argv) > 1 else "pilot"
files = ["tgt_pilot.json", "tgt_extra.json", "tgt_extra2.json"] if mode == "combined" else [f"tgt_{mode}.json"]
rows_all = [r for f in files if os.path.exists(os.path.join(HERE, f)) for r in json.load(open(os.path.join(HERE, f)))["rows"]]
rows = [r for r in rows_all if r["choice"]]
STYLE = ["gut", "mostly gut", "mostly careful", "very careful"]
V = {1: ["base", "honest", "matched", "creepy", "urgency", "social", "disclosed"],
     2: ["base", "matched", "special_price", "creepy", "urgency", "disclosed"]}
LABEL = {1: "loan app (B)", 2: "book now (B)"}
SECOND = {1: "allows contacts/photos", 2: "says price is fair"}


def pct(rs, key="choice", val="B"):
    return 100 * sum(r[key] == val for r in rs) / len(rs) if rs else float("nan")


print(f"[{mode}] usable {len(rows)}/{len(rows_all)}")
for s in (1, 2):
    R = [r for r in rows if r["scenario"] == s]
    print(f"\n===== P{s}: share choosing {LABEL[s]} (n people = {len({r['person'] for r in R})}) =====")
    hdr = f"{'version':14s} {'all':>5s}" + (f" {'proud':>6s} {'not':>5s}" if s == 1 else "") + f"  {SECOND[s]}"
    print(hdr)
    for v in V[s]:
        rv = [r for r in R if r["version"] == v]
        line = f"{v:14s} {pct(rv):5.0f}"
        if s == 1:
            line += f" {pct([r for r in rv if r['proud']]):6.0f} {pct([r for r in rv if not r['proud']]):5.0f}"
        print(line + f"  {pct(rv, 'second', 'yes'):5.0f}")
    print("by style: " + " | ".join(V[s]))
    for i, lab in enumerate(STYLE):
        print(f"  {lab:14s} " + " | ".join(f"{pct([r for r in R if r['version']==v and r['style_level']==i]):3.0f}" for v in V[s]))
    print("by income:")
    for i in range(3):
        print(f"  income {i}       " + " | ".join(f"{pct([r for r in R if r['version']==v and r['income_level']==i]):3.0f}" for v in V[s]))
    for word, lab in [("trust|tend to trust", "trusting"), ("suspicious", "suspicious")]:
        print(f"  {lab:14s} " + " | ".join(f"{pct([r for r in R if r['version']==v and re.search(word, r['trust']) and 'suspicious' not in r['trust'] or (lab=='suspicious' and r['version']==v and 'suspicious' in r['trust'])]):3.0f}" for v in V[s]))
    sus = r"creepy|stalk|watch|track|privacy|scam|trick|manipulat|pressure|predatory|fake|red flag|invasive|spy"
    print("reasons mentioning creepiness/tricks: " + " | ".join(
        f"{v}: {sum(bool(re.search(sus, r['reason'], re.I)) for r in R if r['version']==v)}" for v in V[s]))
    print("sample reasons:")
    for v in V[s]:
        for r in [r for r in R if r["version"] == v][:2]:
            print(f"  [{v} -> {r['choice']}] {r['name']} ({STYLE[r['style_level']]}, inc {r['income_level']}): {r['reason'][:200]}")
