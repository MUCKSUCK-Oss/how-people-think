# Earbuds study, version 2: designed 10 Nov 2026 but never run (replaced by the research-first topic studies).
# Its persona builder (make_personas, STYLE) is reused by classics/classics.py.
"""AI-people run 2 (10 Nov 2026): bigger and fairer than the pilot.

Changes from pilot 2 (see RESULTS.md):
- 60 people instead of 20 (15 per decision style)
- each person also gets a colour/style taste, so the AI people aren't all alike
  (in the pilot, 19/20 picked black)
- 5 page versions: control, quiet default, loud default, scarcity, authority
- which product gets the trick, and which is listed first, are shuffled
  separately from decision style

Each decision is still a separate, fresh Claude (Haiku) call with only the
persona and the page: no tools, no files, no memory, not told it's an experiment.

Run (from the Terminal panel, where the Claude login works):
    python3 earbuds_v2.py       -> data/run2_results.json   (about 15 minutes)
    python3 earbuds_v2.py 5     -> data/run2_test.json      (first 5 calls only)
"""
import concurrent.futures as cf
import json
import os
import random
import sys
import time

HERE_ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE_))
from ai_person import ask, EMPTY_DIR  # noqa: E402  same clean-call settings
from earbuds import parse  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
N_PEOPLE = 60
PARALLEL = 3
CONDITIONS = ["control", "default_quiet", "default_loud", "scarcity", "authority"]

FIRST = ["Priya", "Rahul", "Ananya", "Vikram", "Sneha", "Arjun", "Fatima", "Rohan", "Meera", "Karan",
         "Ayesha", "Siddharth", "Lakshmi", "Imran", "Neha", "Harpreet", "Divya", "Aditya", "Pooja", "Joseph",
         "Kavya", "Manoj", "Shreya", "Farhan", "Ritu", "Gaurav", "Nandini", "Suresh", "Tanvi", "Abdul",
         "Ishita", "Ravi", "Zoya", "Deepak", "Anjali", "Mohit", "Sana", "Prakash", "Bhavna", "Kunal",
         "Revathi", "Yash", "Mariam", "Sunil", "Aarti", "Nikhil", "Gurleen", "Ajay", "Swati", "Thomas",
         "Hema", "Pranav", "Rukhsar", "Vivek", "Komal", "Sanjay", "Esha", "Dinesh", "Parul", "Anil"]
CITIES = ["Pune", "Lucknow", "Chennai", "Indore", "Kolkata", "Bengaluru", "Jaipur", "Kochi", "Nagpur",
          "Delhi", "Patna", "Surat", "Guwahati", "Bhopal", "Mysuru", "Ludhiana", "Visakhapatnam", "Ranchi"]
JOBS = ["nurse", "bank clerk", "software tester", "school teacher", "shop owner", "delivery partner",
        "accountant", "homemaker", "sales executive", "pharmacist", "mechanic", "civil engineer",
        "government clerk", "beautician", "auto driver", "graphic designer", "call-centre agent",
        "farmer", "lab technician", "tuition teacher"]
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
TASTE = ["You like dark, simple colours.", "You like light, bright colours.",
         "You like white or pastel things.", "You prefer black gadgets.",
         "You don't care much about colour.", "Colour doesn't matter to you at all."]

PRODUCTS = {
    "Boltune Air": "Boltune Air wireless earbuds | matte black, round case | ₹1,499 | 30-hour battery | "
                   "Bluetooth 5.3 | rated 4.1★ (2,310 ratings) | 1-year warranty",
    "Wavio Buds": "Wavio Buds wireless earbuds | pearl white, oval case | ₹1,499 | 30-hour battery | "
                  "Bluetooth 5.3 | rated 4.1★ (2,310 ratings) | 1-year warranty",
}


def make_personas():
    rng = random.Random(2026)
    slots = [(t, f) for t in PRODUCTS for f in (True, False)] * (N_PEOPLE // 4)
    random.Random(11).shuffle(slots)
    people = []
    for i in range(N_PEOPLE):
        age = rng.randint(19, 60)
        p = {"id": i, "name": FIRST[i], "age": age, "city": rng.choice(CITIES),
             "job": rng.choice(JOBS) if age > 22 else "college student",
             "style_level": i % 4, "money": rng.choice(MONEY), "trust": rng.choice(TRUST),
             "crowd": rng.choice(CROWD), "taste": rng.choice(TASTE),
             "target": slots[i][0], "target_first": slots[i][1]}
        p["system"] = (
            f"You are {p['name']}, a {p['age']}-year-old {p['job']} living in {p['city']}, India. "
            f"{STYLE[p['style_level']]} {p['money']} {p['trust']} {p['crowd']} {p['taste']} "
            "Your old earphones just broke, so you are buying new wireless earbuds for yourself "
            "on a shopping app on your phone. Think and answer exactly as this person would, "
            "in first person. Be natural; don't overthink unless this person would."
        )
        people.append(p)
    return people


def page(p, condition):
    target = p["target"]
    other = next(n for n in PRODUCTS if n != target)
    order = [target, other] if p["target_first"] else [other, target]
    lines = ["Search results: wireless earbuds under ₹1,600", ""]
    for k, name in enumerate(order, 1):
        line = f"{k}. {PRODUCTS[name]}"
        if name == target:
            if condition == "default_loud":
                line = f"{k}. [✓ SELECTED FOR YOU] {PRODUCTS[name]}"
            elif condition == "default_quiet":
                line = f"{k}. (✓) {PRODUCTS[name]}"
            elif condition == "scarcity":
                line += " | ⚡ Only 2 left in stock! Deal price ends in 09:58"
            elif condition == "authority":
                line += " | 🩺 Recommended by audiologists"
        lines.append(line)
    lines.append("")
    if condition in ("default_loud", "default_quiet"):
        lines.append(f"Your cart: {target}. Tap 'Buy now' to continue, or change the selection.")
        lines.append("")
    lines.append("Which earbuds do you buy? Reply in exactly this format:\n"
                 "CHOICE: <product name>\nREASON: <one or two sentences, in your own words>")
    return "\n".join(lines)


def job(p, condition):
    out = ask(p["system"], page(p, condition))
    choice, reason = parse(out)
    return {"person": p["id"], "name": p["name"], "style_level": p["style_level"], "taste": p["taste"],
            "condition": condition, "target": p["target"], "target_first": p["target_first"],
            "choice": choice, "chose_target": (choice == p["target"]) if choice else None,
            "reason": reason, "raw": out}


def main(limit=None):
    assert os.path.isdir(EMPTY_DIR)
    people = make_personas()
    tasks = [(p, c) for p in people for c in CONDITIONS]
    if limit:
        tasks = tasks[:limit]
    t0 = time.time()
    rows = []
    name = "run2_test.json" if limit else "run2_results.json"
    with cf.ThreadPoolExecutor(PARALLEL) as ex:
        for k, r in enumerate(ex.map(lambda t: job(*t), tasks), 1):
            rows.append(r)
            print(f"{k}/{len(tasks)} {r['name']:10s} {r['condition']:13s} -> {r['choice']}  "
                  f"({time.time() - t0:.0f}s)", flush=True)
            if k % 25 == 0:  # save as we go, so a stop doesn't lose everything
                json.dump({"partial": True, "rows": rows}, open(os.path.join(HERE, "data", name + ".part"), "w"),
                          ensure_ascii=False)
    out = {"model": "haiku", "conditions": CONDITIONS, "people": people, "rows": rows,
           "seconds": round(time.time() - t0)}
    json.dump(out, open(os.path.join(HERE, "data", name), "w"), indent=1, ensure_ascii=False)
    print("RUN2_DONE", flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else None)
