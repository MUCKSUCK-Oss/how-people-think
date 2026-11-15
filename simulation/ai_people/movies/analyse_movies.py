"""Summarise the movies data. Usage: python3 analyse_movies.py pilot|combined"""
import json
import os
import statistics as st
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
mode = sys.argv[1] if len(sys.argv) > 1 else "pilot"
files = ["movies_pilot.json", "movies_extra.json", "movies_extra2.json"] if mode == "combined" else [f"movies_{mode}.json"]
rows_all = [r for f in files if os.path.exists(os.path.join(DATA, f))
            for r in json.load(open(os.path.join(DATA, f)))["rows"]]
V = ["no_film", "heroic", "critical", "heroic_approved", "heroic_cut", "heroic_fiction", "rules_work"]
SHORT = ["none", "hero", "critic", "approv", "cut", "fiction", "rules"]
FILMS = V[1:]
VIEWS = ("proud", "neutral", "critical")
STYLE = ["gut", "mostly gut", "mostly careful", "very careful"]


def ok(r):
    base = r["join"] and r["trust"] and r["interrogate"]
    return base and (r["version"] == "no_film" or (r["enjoy"] and r["propaganda"]))


rows = [r for r in rows_all if ok(r)]


def mean(key):
    return lambda rs: st.mean(r[key] for r in rs if r[key]) if any(r[key] for r in rs) else float("nan")


def prop(rs):
    rs = [r for r in rs if r["propaganda"]]
    return 100 * sum(r["propaganda"] == "yes" for r in rs) / len(rs) if rs else float("nan")


def line(label, R, f):
    n = len({r["person"] for r in R})
    print(f"{label:20s} n={n:2d}  " + "  ".join(f"{f([r for r in R if r['version'] == v]):7.2f}" for v in V))


def table(title, f, by_style=False):
    print(f"\n{title:30s}" + "  ".join(f"{s:>7s}" for s in SHORT))
    line("All", rows, f)
    for view in VIEWS:
        line("  " + view, [r for r in rows if r["view"] == view], f)
    if by_style:
        for i, lab in enumerate(STYLE):
            line("  " + lab, [r for r in rows if r["style_level"] == i], f)


print(f"[{mode}] usable {len(rows)}/{len(rows_all)}")
table("Mean JOIN (1-7):", mean("join"))
table("Mean TRUST (1-7):", mean("trust"), by_style=True)
table("Mean INTERROGATE (1-7):", mean("interrogate"))
table("Mean ENJOY (1-7):", mean("enjoy"))
table("% PROPAGANDA = yes:", prop)

print("\nTRUST by country:")
for c in sorted({r["country"] for r in rows}):
    line("  " + c[:18], [r for r in rows if r["country"] == c], mean("trust"))

# within-person changes vs no_film
by = {(r["person"], r["version"]): r for r in rows}
ids = sorted({r["person"] for r in rows})
print("\nMean within-person change vs no_film (TRUST / JOIN / INTERROGATE):")
for v in FILMS:
    for view in ("all",) + VIEWS:
        ps = [p for p in ids if (p, v) in by and (p, "no_film") in by
              and (view == "all" or by[(p, v)]["view"] == view)]
        if not ps:
            continue
        d = {k: st.mean(by[(p, v)][k] - by[(p, "no_film")][k] for p in ps) for k in ("trust", "join", "interrogate")}
        print(f"  {v:16s} {view:8s} n={len(ps):2d}  trust {d['trust']:+.2f}  join {d['join']:+.2f}  "
              f"interr {d['interrogate']:+.2f}")

# check: does any person give identical answers in every version?
same = [p for p in ids if len({(by[(p, v)]["trust"], by[(p, v)]["join"]) for v in V if (p, v) in by}) == 1]
print(f"\nPeople with identical TRUST and JOIN in every version: {len(same)}/{len(ids)} "
      f"({', '.join(sorted({by[(p, 'no_film')]['view'] for p in same if (p, 'no_film') in by})) or 'none'})")

print("\nSample reasons:")
for v in V:
    for view in VIEWS:
        for r in [r for r in rows if r["version"] == v and r["view"] == view][:1]:
            print(f"  [{v} | {view} | join={r['join']} trust={r['trust']} interr={r['interrogate']} "
                  f"enjoy={r['enjoy']} prop={r['propaganda']}] {r['name']} ({r['country']}): {r['reason'][:220]}")
