"""Summarise the secret-agencies data. Usage: python3 analyse_ops.py pilot|combined"""
import json
import os
import statistics as st
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
mode = sys.argv[1] if len(sys.argv) > 1 else "pilot"
files = ["ops_pilot.json", "ops_extra.json", "ops_extra2.json"] if mode == "combined" else [f"ops_{mode}.json"]
rows_all = [r for f in files if os.path.exists(os.path.join(DATA, f))
            for r in json.load(open(os.path.join(DATA, f)))["rows"]]
rows = [r for r in rows_all if r["vaccinate"] and r["worry"]]
V = ["news_only", "few_fakes", "many_fakes", "memes", "many_fakes_labelled", "prebunk", "doctor_reply"]
SHORT = ["news", "few", "many", "memes", "label", "prebunk", "doctor"]
STYLE = ["gut", "mostly gut", "mostly careful", "very careful"]


def pct(rs):
    return 100 * sum(r["vaccinate"] == "yes" for r in rs) / len(rs) if rs else float("nan")


def line(label, R, f):
    n = len({r["person"] for r in R})
    print(f"{label:22s} n={n:2d}  " + "  ".join(f"{f([r for r in R if r['version'] == v]):6.1f}" for v in V))


print(f"[{mode}] usable {len(rows)}/{len(rows_all)}")
print("\n% who VACCINATE:          " + "  ".join(f"{s:>6s}" for s in SHORT))
line("All", rows, pct)
for view in ("trusting", "unsure", "doubtful"):
    line("  " + view, [r for r in rows if r["view"] == view], pct)
print("By decision style:")
for i, lab in enumerate(STYLE):
    line("  " + lab, [r for r in rows if r["style_level"] == i], pct)
print("By country:")
for c in sorted({r["country"] for r in rows}):
    line("  " + c[:20], [r for r in rows if r["country"] == c], pct)

print("\nMean WORRY (1-7):         " + "  ".join(f"{s:>6s}" for s in SHORT))
mw = lambda rs: st.mean(r["worry"] for r in rs) if rs else float("nan")  # noqa: E731
line("All", rows, mw)
for view in ("trusting", "unsure", "doubtful"):
    line("  " + view, [r for r in rows if r["view"] == view], mw)

print("\n% saying the parent posts seemed REAL:")
real = lambda rs: (100 * sum(r["real"] == "yes" for r in rs if r["real"]) / max(1, sum(bool(r["real"]) for r in rs)))  # noqa: E731
line("All", rows, real)
for view in ("trusting", "unsure", "doubtful"):
    line("  " + view, [r for r in rows if r["view"] == view], real)

by = {(r["person"], r["version"]): r for r in rows}
ids = sorted({r["person"] for r in rows})
flip = [p for p in ids if by.get((p, "news_only"), {}).get("vaccinate") == "yes"
        and by.get((p, "many_fakes"), {}).get("vaccinate") == "no"]
back = [p for p in ids if by.get((p, "news_only"), {}).get("vaccinate") == "no"
        and by.get((p, "many_fakes_labelled"), {}).get("vaccinate") == "yes"]
print(f"\nPeople who vaccinate with news only but NOT after many fakes: {len(flip)}/{len(ids)}")
print(f"People who refuse with news only but vaccinate after the 'foreign network' label (backfire): {len(back)}/{len(ids)}")

print("\nSample reasons:")
for v in V:
    for view in ("trusting", "doubtful"):
        for r in [r for r in rows if r["version"] == v and r["view"] == view][:1]:
            print(f"  [{v} | {view} | vacc={r['vaccinate']} worry={r['worry']} real={r['real']}] "
                  f"{r['name']} ({r['country']}): {r['reason'][:200]}")
