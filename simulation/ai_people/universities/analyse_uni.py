"""Summarise uni_results.json: share choosing the expensive College B, by version and by group."""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")  # raw AI-person answers (JSON)
d = json.load(open(os.path.join(DATA, "uni_results.json")))
rows = [r for r in d["rows"] if r["choice"]]
VERS = ["control", "hype", "scarcity", "ranking", "social", "all"]
STYLE = ["gut", "mostly gut", "mostly careful", "very careful"]
INC = ["tight", "middle", "comfortable"]


def pct(rs):
    return 100 * sum(r["choice"] == "B" for r in rs) / len(rs) if rs else float("nan")


print(f"Usable: {len(rows)}/{len(d['rows'])}\n")
base = pct([r for r in rows if r["version"] == "control"])
print("Chose expensive College B:")
for v in VERS:
    rs = [r for r in rows if r["version"] == v]
    loans = sum(r["loan"] == "yes" for r in rs if r["choice"] == "B")
    print(f"  {v:9s} {pct(rs):5.1f}%  ({sum(r['choice'] == 'B' for r in rs)}/{len(rs)})  "
          f"change {pct(rs) - base:+5.1f}   B-choosers taking a loan: {loans}")


def table(key, labels, title):
    print(f"\nBy {title} (control -> each version):")
    for i, lab in enumerate(labels):
        cells = [f"{pct([r for r in rows if r['version'] == v and r[key] == i]):3.0f}" for v in VERS]
        print(f"  {lab:14s} " + " | ".join(cells))


print("\nColumns: " + " | ".join(VERS))
table("style_level", STYLE, "decision style")
table("income_level", INC, "family income")
for key, lab in [("friends", "friends matter a lot"), ("parents", "big-name college")]:
    print(f"\n'{lab}' vs others (control, social, all):")
    for flag in (True, False):
        sub = [r for r in rows if (lab.split()[0].lower() in r[key].lower()) == flag]
        print(f"  {'yes' if flag else 'no ':3s} " + " | ".join(
            f"{v}:{pct([r for r in sub if r['version'] == v]):3.0f}" for v in ("control", "social", "all")))

# switches vs control, per student
by = {(r["student"], r["version"]): r for r in rows}
print("\nSwitches from the control answer:")
for v in VERS[1:]:
    to_b = sum(1 for s in range(40) if by.get((s, "control")) and by.get((s, v))
               and by[(s, "control")]["choice"] == "A" and by[(s, v)]["choice"] == "B")
    to_a = sum(1 for s in range(40) if by.get((s, "control")) and by.get((s, v))
               and by[(s, "control")]["choice"] == "B" and by[(s, v)]["choice"] == "A")
    print(f"  {v:9s} A->B: {to_b:2d}   B->A (backfire): {to_a:2d}")

SPOT = {"hype": r"highest|45|median|typical|one student|misleading|assistance",
        "scarcity": r"48|deadline|pressure|rush|booking|seats left|urgent",
        "ranking": r"rank|award|emerging|#7",
        "social": r"senior|cousin|friend"}
print("\nReasons mentioning the trick, and how many called it out as a trick:")
for v, pat in SPOT.items():
    rs = [r for r in rows if r["version"] in (v, "all")]
    hit = [r for r in rs if re.search(pat, r["reason"], re.I)]
    sus = [r for r in hit if re.search(r"marketing|gimmick|trick|misleading|pressure|fake|bait|scam|suspicious|sales", r["reason"], re.I)]
    print(f"  {v:9s} mentioned {len(hit)}/{len(rs)}, called a trick {len(sus)}")
    for r in hit[:3]:
        print(f"     - {r['name']} ({STYLE[r['style_level']]}, {INC[r['income_level']]}, {r['version']} -> {r['choice']}): {r['reason'][:200]}")
