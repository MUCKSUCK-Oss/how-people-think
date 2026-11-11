"""AI-people pilot (v3 idea, 10 Nov 2026).

Each simulated shopper is a SEPARATE, fresh Claude (Haiku) call that only knows
its own life story and sees one shopping page. It has no tools, no memory, no
project files, and is never told this is an experiment.

Design
- 20 personas (seeded, varied age / city / job / money habits / decision style)
- 3 situations per person: control, pre-selected default, scarcity ("only 2 left")
- Two equally good earbuds. Which one gets the trick, and which is listed first,
  is counterbalanced across people, so product preference cancels out.
- Measure: share choosing the "target" (the product the trick favours).
  With no trick, that should be about 50%.

Runs on the user's Claude Pro plan through the `claude` command (no API key).
Run:  python3 earbuds.py          -> data/pilot_results.json
"""
import concurrent.futures as cf
import json
import os
import random
import re
import subprocess
import time

import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
sys.path.insert(0, os.path.dirname(HERE))
from ai_person import ask, MODEL  # noqa: E402
N_PEOPLE = 20
PARALLEL = 3

FIRST = ["Priya", "Rahul", "Ananya", "Vikram", "Sneha", "Arjun", "Fatima", "Rohan", "Meera", "Karan",
         "Ayesha", "Siddharth", "Lakshmi", "Imran", "Neha", "Harpreet", "Divya", "Aditya", "Pooja", "Joseph"]
CITIES = ["Pune", "Lucknow", "Chennai", "Indore", "Kolkata", "Bengaluru", "Jaipur", "Kochi", "Nagpur", "Delhi"]
JOBS = ["nurse", "college student", "bank clerk", "software tester", "school teacher", "shop owner",
        "delivery partner", "accountant", "homemaker", "sales executive", "pharmacist", "mechanic"]
STYLE = [
    "You usually decide quickly and go with your gut. Long comparisons bore you.",
    "You usually decide fairly quickly, but glance at the main details first.",
    "You usually compare options carefully before buying anything.",
    "You research everything in detail and hate making a hasty purchase.",
]
MONEY = ["Money is tight, so every rupee matters to you.",
         "You are careful with money but can afford small treats.",
         "You are comfortable with money and don't fuss over small price differences."]
TRUST = ["You tend to trust what shops and experts recommend.",
         "You are a bit suspicious of what shops recommend.",
         "You don't strongly trust or distrust shop recommendations."]
CROWD = ["You like buying what is popular.", "You don't care what other people buy.",
         "You sometimes check what others are buying."]


def make_personas():
    rng = random.Random(7)
    # Pilot 2: which product gets the trick and which is listed first are shuffled
    # independently of decision style (pilot 1 accidentally tied them together).
    slots = [(t, f) for t in ("Boltune Air", "Wavio Buds") for f in (True, False)] * 5
    random.Random(99).shuffle(slots)
    people = []
    for i in range(N_PEOPLE):
        age = rng.randint(19, 58)
        p = {
            "id": i,
            "name": FIRST[i],
            "age": age,
            "city": rng.choice(CITIES),
            "job": rng.choice(JOBS) if age > 22 else "college student",
            "style_level": i % 4,              # 0 = gut ... 3 = very careful (balanced: 5 each)
            "money": rng.choice(MONEY),
            "trust": rng.choice(TRUST),
            "crowd": rng.choice(CROWD),
            "target": slots[i][0],        # counterbalanced, shuffled
            "target_first": slots[i][1],  # counterbalanced, shuffled
        }
        p["system"] = (
            f"You are {p['name']}, a {p['age']}-year-old {p['job']} living in {p['city']}, India. "
            f"{STYLE[p['style_level']]} {p['money']} {p['trust']} {p['crowd']} "
            "Your old earphones just broke, so you are buying new wireless earbuds for yourself "
            "on a shopping app on your phone. Think and answer exactly as this person would, "
            "in first person. Be natural; don't overthink unless this person would."
        )
        people.append(p)
    return people


# Pilot 2: the two products are equal on everything except look (pilot 1 had Boltune
# cheaper with more battery, so every AI person picked it: a ceiling, not a test).
PRODUCTS = {
    "Boltune Air": "Boltune Air wireless earbuds | matte black, round case | ₹1,499 | 30-hour battery | "
                   "Bluetooth 5.3 | rated 4.1★ (2,310 ratings) | 1-year warranty",
    "Wavio Buds": "Wavio Buds wireless earbuds | pearl white, oval case | ₹1,499 | 30-hour battery | "
                  "Bluetooth 5.3 | rated 4.1★ (2,310 ratings) | 1-year warranty",
}


def page(p, condition):
    target = p["target"]
    other = "Wavio Buds" if target == "Boltune Air" else "Boltune Air"
    order = [target, other] if p["target_first"] else [other, target]
    lines = ["Search results: wireless earbuds under ₹1,600", ""]
    for k, name in enumerate(order, 1):
        line = f"{k}. {PRODUCTS[name]}"
        if name == target and condition == "default":
            line = f"{k}. [✓ SELECTED FOR YOU] {PRODUCTS[name]}"
        if name == target and condition == "scarcity":
            line += " | ⚡ Only 2 left in stock! Deal price ends in 09:58"
        lines.append(line)
    lines.append("")
    if condition == "default":
        lines.append(f"Your cart: {target} (pre-selected). Tap 'Buy now' to continue, or change the selection.")
        lines.append("")
    lines.append("Which earbuds do you buy? Reply in exactly this format:\n"
                 "CHOICE: <product name>\nREASON: <one or two sentences, in your own words>")
    return "\n".join(lines)




def parse(text):
    m = re.search(r"CHOICE:\s*(.+)", text)
    choice = None
    if m:
        c = m.group(1).lower()
        if "boltune" in c and "wavio" not in c:
            choice = "Boltune Air"
        elif "wavio" in c and "boltune" not in c:
            choice = "Wavio Buds"
    reason = re.search(r"REASON:\s*(.+)", text, re.S)
    return choice, (reason.group(1).strip() if reason else text)


def job(p, condition):
    out = ask(p["system"], page(p, condition))
    choice, reason = parse(out)
    return {"person": p["id"], "name": p["name"], "style_level": p["style_level"], "condition": condition,
            "target": p["target"], "target_first": p["target_first"], "choice": choice,
            "chose_target": (choice == p["target"]) if choice else None, "reason": reason, "raw": out}


def main(limit=None):
    people = make_personas()
    tasks = [(p, c) for p in people for c in ("control", "default", "scarcity")]
    if limit:
        tasks = tasks[:limit]
    t0 = time.time()
    rows = []
    with cf.ThreadPoolExecutor(PARALLEL) as ex:
        for k, r in enumerate(ex.map(lambda t: job(*t), tasks), 1):
            rows.append(r)
            print(f"{k}/{len(tasks)} {r['name']:10s} {r['condition']:9s} -> {r['choice']}  ({time.time()-t0:.0f}s)",
                  flush=True)
    out = {"model": MODEL, "people": [{k: v for k, v in p.items()} for p in people], "rows": rows,
           "seconds": round(time.time() - t0)}
    name = "pilot_test_call.json" if limit else "pilot_results.json"
    json.dump(out, open(os.path.join(DATA, name), "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    import sys
    main(int(sys.argv[1]) if len(sys.argv) > 1 else None)
