"""Summarise the corporations data. Usage: python3 analyse_corp.py pilot|combined"""
import json
import os
import statistics as st
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
mode = sys.argv[1] if len(sys.argv) > 1 else "pilot"
files = ["corp_pilot.json", "corp_extra.json", "corp_extra2.json"] if mode == "combined" else [f"corp_{mode}.json"]
rows_all = [r for f in files if os.path.exists(os.path.join(DATA, f))
            for r in json.load(open(os.path.join(DATA, f)))["rows"]]
rows = [r for r in rows_all if r["choice"] and r["annoyed"]]
V1 = ["honest", "drip", "drip_timer", "drip_normal", "addon", "all", "all_disclosed"]
V2 = ["easy", "obstruct", "shame", "offer", "loss", "all", "all_disclosed"]
STYLE = ["gut", "mostly gut", "mostly careful", "very careful"]


def line(label, R, V, f):
    n = len({r["person"] for r in R})
    print(f"{label:20s} n={n:2d}  " + "  ".join(f"{f([r for r in R if r['version'] == v]):6.1f}" for v in V))


def pct(cond):
    return lambda rs: 100 * sum(cond(r) for r in rs) / len(rs) if rs else float("nan")


ann = lambda rs: st.mean(r["annoyed"] for r in rs) if rs else float("nan")  # noqa: E731
print(f"[{mode}] usable {len(rows)}/{len(rows_all)}")
for scen, V, label, cond in (("C1", V1, "% who BUY ON SITE B (drip site)", lambda r: r["choice"] == "B"),
                             ("C2", V2, "% who CANCEL NOW", lambda r: r["choice"] == "cancel")):
    R = [r for r in rows if r["scenario"] == scen]
    print(f"\n=== {scen}: {label}\n{'':26s}" + "  ".join(f"{v[:6]:>6s}" for v in V))
    line("All", R, V, pct(cond))
    for inc in ("tight", "comfortable"):
        line("  " + inc, [r for r in R if r["income"] == inc], V, pct(cond))
    for i, lab in enumerate(STYLE):
        line("  " + lab, [r for r in R if r["style_level"] == i], V, pct(cond))
    for c in sorted({r["country"] for r in R}):
        line("  " + c[:18], [r for r in R if r["country"] == c], V, pct(cond))
    if scen == "C2":
        print("% KEEP for now / % TAKE THE OFFER:")
        line("  keep", R, V, pct(lambda r: r["choice"] == "keep"))
        line("  offer", R, V, pct(lambda r: r["choice"] == "offer"))
        for inc in ("tight", "comfortable"):
            line("  offer, " + inc, [r for r in R if r["income"] == inc], V, pct(lambda r: r["choice"] == "offer"))
    else:
        print("% who KEPT the pre-ticked protection (of those buying on B):")
        line("  kept addon", [r for r in R if r["choice"] == "B" and r["addon"]], V, pct(lambda r: r["addon"] == "kept"))
    print("Mean ANNOYED (1-7):")
    line("  annoyed", R, V, ann)
    print("Sample reasons:")
    for v in V:
        for r in [r for r in R if r["version"] == v][:2]:
            print(f"  [{v} | {r['income']} | {r['choice']} addon={r['addon']} ann={r['annoyed']}] {r['name']} ({r['country']}): {r['reason'][:180]}")
