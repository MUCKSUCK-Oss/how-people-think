"""Summarise pilot_results.json in plain numbers."""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "data", "pilot_results.json")))
rows = [r for r in d["rows"] if r["choice"]]
bad = len(d["rows"]) - len(rows)
STYLE = ["gut", "mostly gut", "mostly careful", "very careful"]


def pct(xs):
    return f"{100 * sum(xs) / len(xs):.0f}% ({sum(xs)}/{len(xs)})" if xs else "-"


print(f"Answers parsed: {len(rows)}/{len(d['rows'])} (unusable: {bad})\n")
print("Chose the product the trick favoured:")
for c in ("control", "default", "scarcity"):
    print(f"  {c:9s} {pct([r['chose_target'] for r in rows if r['condition'] == c])}")

print("\nBy decision style (control -> default -> scarcity):")
for s in range(4):
    vals = [pct([r["chose_target"] for r in rows if r["condition"] == c and r["style_level"] == s])
            for c in ("control", "default", "scarcity")]
    print(f"  {STYLE[s]:15s} " + "  ->  ".join(vals))

by = {(r["person"], r["condition"]): r for r in rows}
for c in ("default", "scarcity"):
    to_t = away = 0
    for p in range(20):
        a, b = by.get((p, "control")), by.get((p, c))
        if a and b and a["chose_target"] != b["chose_target"]:
            to_t += b["chose_target"]
            away += not b["chose_target"]
    print(f"\nSwitched because of {c}: {to_t} toward the trick, {away} away from it")

ctrl = [r for r in rows if r["condition"] == "control"]
print("\nChecks on the control pages:")
print("  chose Boltune Air:", pct([r["choice"] == "Boltune Air" for r in ctrl]))
print("  chose the first-listed product:", pct([r["chose_target"] == r["target_first"] for r in ctrl]))

KEY = {"default": r"select|pre-?select|picked|already in (my )?cart|recommend",
       "scarcity": r"only 2|left in stock|stock|hurry|ends in|miss out|deal|timer|quick"}
for c, pat in KEY.items():
    hits = [r for r in rows if r["condition"] == c and re.search(pat, r["reason"], re.I)]
    print(f"\nReasons that mention the {c} trick: {len(hits)}/{sum(r['condition'] == c for r in rows)}")
    for r in hits[:4]:
        print(f"  - {r['name']} ({STYLE[r['style_level']]}): {r['reason'][:220]}")
