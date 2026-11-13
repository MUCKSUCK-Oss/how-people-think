"""Summarise the politics data. Usage: python3 analyse_pol.py pilot|combined"""
import json
import os
import re
import statistics as st
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
mode = sys.argv[1] if len(sys.argv) > 1 else "pilot"
files = ["pol_pilot.json", "pol_extra.json", "pol_extra2.json"] if mode == "combined" else [f"pol_{mode}.json"]
rows_all = [r for f in files if os.path.exists(os.path.join(DATA, f))
            for r in json.load(open(os.path.join(DATA, f)))["rows"]]
rows = [r for r in rows_all if r["support"]]
V = ["no_label", "own_party", "rival_party", "own_populist", "rival_populist", "own_factcheck", "own_uturn"]
STYLE = ["gut", "mostly gut", "mostly careful", "very careful"]


def mean(rs):
    return st.mean(r["support"] for r in rs) if rs else float("nan")


def bel(rs):
    rs = [r for r in rs if r["believe"]]
    return 100 * sum(r["believe"] == "yes" for r in rs) / len(rs) if rs else float("nan")


def table(label, R):
    print(f"{label:22s} n={len({r['person'] for r in R}):2d}  " + "  ".join(f"{mean([r for r in R if r['version']==v]):4.1f}" for v in V)
          + f"   gap(own-rival)={mean([r for r in R if r['version']=='own_party'])-mean([r for r in R if r['version']=='rival_party']):+.1f}")


print(f"[{mode}] usable {len(rows)}/{len(rows_all)}")
print("\nMean SUPPORT (1-7) by version:  " + " | ".join(V))
P = [r for r in rows if r["partisan"]]
N = [r for r in rows if not r["partisan"]]
table("All partisans", P)
table("  strong", [r for r in P if r["strong"]])
table("  mild", [r for r in P if not r["strong"]])
table("No party", N)
print("\nBy decision style (partisans):")
for i, lab in enumerate(STYLE):
    table("  " + lab, [r for r in P if r["style_level"] == i])
print("\nBy country (partisans):")
for c in sorted({r["country"] for r in P}):
    table("  " + c[:20], [r for r in P if r["country"] == c])
print("\nBy side (partisans; A = first-listed party, B = its rival):")
for side in ("A", "B"):
    table("  party " + side, [r for r in P if r["role"] == side])
print("\nBELIEVE the 'cut in half' claim (% yes):")
for lab, R in (("partisans", P), ("no party", N)):
    print(f"  {lab:10s} " + " | ".join(f"{v}: {bel([r for r in R if r['version']==v]):.0f}" for v in V))
by = {(r["person"], r["version"]): r["support"] for r in P}
ids = sorted({r["person"] for r in P})
up = sum(1 for p in ids if by.get((p, "own_party"), 0) > by.get((p, "rival_party"), 0))
same = sum(1 for p in ids if by.get((p, "own_party")) == by.get((p, "rival_party")))
print(f"\nPartisans rating own-party version higher than rival version: {up}/{len(ids)} (same: {same})")
exc = r"times (have )?change|different now|back then|circumstances|context|evolv|politic(s|ians) (is|are)|that was then|doesn.t matter|hypocri|flip"
print("U-turn reasons with an excuse or 'hypocrisy' word: " + str(sum(bool(re.search(exc, r["reason"], re.I)) for r in P if r["version"] == "own_uturn")))
print("\nSample reasons:")
for v in V:
    for r in [r for r in P if r["version"] == v][:2]:
        print(f"  [{v} {r['support']}] {r['name']} ({r['country']}, {'strong' if r['strong'] else 'mild'} {r['own']}): {r['reason'][:190]}")
