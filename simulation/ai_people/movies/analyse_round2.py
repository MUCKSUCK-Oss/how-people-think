"""Summarise movies round 2. Usage: python3 analyse_round2.py pilot|combined"""
import json
import os
import statistics as st
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
mode = sys.argv[1] if len(sys.argv) > 1 else "pilot"
files = ["r2_pilot.json", "r2_extra.json"] if mode == "combined" else [f"r2_{mode}.json"]
rows_all = [r for f in files if os.path.exists(os.path.join(DATA, f))
            for r in json.load(open(os.path.join(DATA, f)))["rows"]]
V = ["no_film", "opp_nolabel", "opp_real", "opp_fiction", "opp_corrected", "ruling_real"]
SHORT = ["none", "nolabel", "real", "fiction", "correct", "MIRROR"]
LEANS = ("ruling", "opposition", "neither")
STYLE = ["gut", "mostly gut", "mostly careful", "very careful"]


def ok(r):
    base = r["b_ruling"] and r["b_opp"] and r["trust"]
    return base and (r["version"] == "no_film" or (r["enjoy"] and r["propaganda"]))


rows = [r for r in rows_all if ok(r)]
by = {(r["person"], r["version"]): r for r in rows}
people = sorted({r["person"] for r in rows})


def villain(r):
    """Belief about the villain's party: OPP in opp_* versions, RULING in the mirror."""
    return r["b_ruling"] if r["version"] == "ruling_real" else r["b_opp"]


def m(rs, f):
    vals = [f(r) for r in rs if f(r) is not None]
    return st.mean(vals) if vals else float("nan")


def table(title, f, by_style=False, versions=V):
    print(f"\n{title:26s}" + "".join(f"{SHORT[V.index(v)]:>9s}" for v in versions))
    groups = [("All", rows)] + [("  " + l, [r for r in rows if r["lean"] == l]) for l in LEANS]
    if by_style:
        groups += [("  " + s, [r for r in rows if r["style_level"] == i]) for i, s in enumerate(STYLE)]
    for lab, R in groups:
        n = len({r["person"] for r in R})
        print(f"{lab:20s} n={n:2d} " + "".join(f"{m([r for r in R if r['version'] == v], f):9.2f}" for v in versions))


def change(v, f_new, f_base, group=None):
    """Within-person change of version v vs no_film."""
    d = []
    for p in people:
        a, b = by.get((p, v)), by.get((p, "no_film"))
        if a and b and (group is None or a["lean"] == group):
            d.append(f_new(a) - f_base(b))
    return d


print(f"[{mode}] usable {len(rows)}/{len(rows_all)}  people={len(people)}")
table("BELIEVE_OPP (1-7):", lambda r: r["b_opp"])
table("BELIEVE_RULING (1-7):", lambda r: r["b_ruling"])
table("TRUST_AGENCY (1-7):", lambda r: r["trust"])
table("ENJOY (1-7):", lambda r: r["enjoy"], versions=V[1:])
table("PROPAGANDA (1-7):", lambda r: r["propaganda"], versions=V[1:])
props = [r["propaganda"] for r in rows if r["propaganda"]]
if len(props) > 1:
    print(f"PROPAGANDA overall mean {st.mean(props):.2f}  sd {st.stdev(props):.2f}  "
          f"distribution {[props.count(k) for k in range(1, 8)]}")

print("\nVILLAIN-PARTY belief change vs no film (BELIEVE_OPP for opp_*, BELIEVE_RULING for mirror):")
for v in V[1:]:
    fb = (lambda r: r["b_ruling"]) if v == "ruling_real" else (lambda r: r["b_opp"])
    line = f"  {v:14s}"
    for g in (None,) + LEANS:
        d = change(v, villain, fb, g)
        up = sum(x > 0 for x in d)
        dn = sum(x < 0 for x in d)
        line += f"  {(g or 'all'):10s} {st.mean(d) if d else float('nan'):+.2f} ({up}up/{dn}dn)"
    print(line)

print("\nNON-VILLAIN party belief change vs no film (spillover check):")
for v in V[1:]:
    other = (lambda r: r["b_opp"]) if v == "ruling_real" else (lambda r: r["b_ruling"])
    d = change(v, other, other)
    print(f"  {v:14s} {st.mean(d):+.2f}")

print("\nMIRROR: villain-belief change in the 'real' versions, by whether the villain is your OWN party")
own, other = [], []
for p in people:
    base = by.get((p, "no_film"))
    for v in ("opp_real", "ruling_real"):
        r = by.get((p, v))
        if not (r and base) or r["lean"] == "neither":
            continue
        villain_party = "ruling" if v == "ruling_real" else "opposition"
        fb = base["b_ruling"] if v == "ruling_real" else base["b_opp"]
        (own if r["lean"] == villain_party else other).append((villain(r) - fb, r["propaganda"]))
if own and other:
    print(f"  own party is villain:   belief change {st.mean(x for x, _ in own):+.2f}  propaganda {st.mean(y for _, y in own):.2f}  (n={len(own)})")
    print(f"  other party is villain: belief change {st.mean(x for x, _ in other):+.2f}  propaganda {st.mean(y for _, y in other):.2f}  (n={len(other)})")

print("\nBaseline partisan gap (no film): BELIEVE_OPP - BELIEVE_RULING")
for l in LEANS:
    R = [r for r in rows if r["version"] == "no_film" and r["lean"] == l]
    print(f"  {l:10s} {m(R, lambda r: r['b_opp'] - r['b_ruling']):+.2f}")

print("\nGut vs careful: villain-belief change opp_real vs no film")
for i, s in enumerate(STYLE):
    d = [by[(p, 'opp_real')]["b_opp"] - by[(p, 'no_film')]["b_opp"] for p in people
         if (p, 'opp_real') in by and (p, 'no_film') in by and by[(p, 'no_film')]["style_level"] == i]
    print(f"  {s:15s} {st.mean(d) if d else float('nan'):+.2f} (n={len(d)})")

print("\nIdentical answers across all 6 versions (a sign the AI ignored the film):")
same = 0
for p in people:
    vals = {(by[(p, v)]["b_ruling"], by[(p, v)]["b_opp"], by[(p, v)]["trust"]) for v in V if (p, v) in by}
    same += len(vals) == 1
print(f"  {same} of {len(people)} people")

print("\nSample reasons:")
for v in ("opp_real", "opp_corrected", "ruling_real"):
    for r in [r for r in rows if r["version"] == v][:3]:
        print(f"  [{v} | {r['lean']} | {r['country']}] {r['reason'][:240]}")
