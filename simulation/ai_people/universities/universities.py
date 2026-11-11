"""University traps simulation (11 Nov 2026). See PREDICTIONS.md (written first).

40 AI students x 6 versions = 240 separate, fresh Claude Haiku calls.
Run from the Terminal panel (where the Claude login works):
    python3 universities.py 6   -> data/uni_test.json
    python3 universities.py     -> data/uni_results.json
"""
import concurrent.futures as cf
import json
import os
import random
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")  # raw AI-person answers (JSON)
sys.path.insert(0, os.path.dirname(HERE))
from ai_person import ask  # noqa: E402  same clean-call settings (fresh Haiku, no tools, empty folder)

N = 40
PARALLEL = 3
VERSIONS = ["control", "hype", "scarcity", "ranking", "social", "all"]

NAMES = ["Aarav", "Diya", "Kabir", "Ishaan", "Meher", "Vihaan", "Anika", "Reyansh", "Saanvi", "Arjun",
         "Zara", "Advait", "Myra", "Krish", "Aadhya", "Vivaan", "Kiara", "Shaurya", "Pari", "Ayaan",
         "Riya", "Dhruv", "Tanya", "Om", "Navya", "Rudra", "Ira", "Aryan", "Sara", "Yash",
         "Nisha", "Harsh", "Aisha", "Laksh", "Jiya", "Pranav", "Sana", "Dev", "Anvi", "Kunal"]
CITIES = ["Lucknow", "Indore", "Patna", "Nagpur", "Coimbatore", "Jaipur", "Bhopal", "Ranchi", "Surat",
          "Guwahati", "Ludhiana", "Visakhapatnam", "Kanpur", "Mysuru", "Dehradun", "Raipur"]
INCOME = ["Your family's income is tight; your father runs a small shop and money is always counted carefully.",
          "Your family is middle-class; your parents are salaried and have some savings, but ₹18 lakh would need a big loan.",
          "Your family is comfortable; your parents could pay several lakh without a loan."]
MARKS = ["You scored 92% in Class 12.", "You scored 81% in Class 12.", "You scored 74% in Class 12."]
STYLE = ["You usually decide quickly and go with your gut. Long comparisons bore you.",
         "You usually decide fairly quickly, but glance at the main details first.",
         "You usually compare options carefully before deciding.",
         "You research everything in detail and hate making a hasty decision."]
TRUST = ["You tend to believe what college ads and brochures say.",
         "You are suspicious of college ads.",
         "You neither fully trust nor distrust college ads."]
FRIENDS = ["What your friends and seniors do matters a lot to you.",
           "You don't care much what your friends choose.",
           "You sometimes ask seniors for advice."]
PARENTS = ["Your parents want you at a 'big-name' college and care about what relatives will say.",
           "Your parents mainly worry about cost and keeping you close to home.",
           "Your parents say it's your decision."]


def make_students():
    rng = random.Random(4040)
    order = [True, False] * (N // 2)
    random.Random(7).shuffle(order)
    out = []
    for i in range(N):
        s = {"id": i, "name": NAMES[i], "age": rng.choice([17, 18]), "city": rng.choice(CITIES),
             "income_level": i % 3, "style_level": i % 4, "marks": rng.choice(MARKS),
             "trust": rng.choice(TRUST), "friends": rng.choice(FRIENDS), "parents": rng.choice(PARENTS),
             "b_first": order[i]}
        s["system"] = (
            f"You are {s['name']}, {s['age']} years old, from {s['city']}, India. You just got your Class 12 "
            f"results and want to study Computer Science engineering. {s['marks']} {INCOME[s['income_level']]} "
            f"{STYLE[s['style_level']]} {s['trust']} {s['friends']} {s['parents']} "
            "Think and answer exactly as this person would, in first person. "
            "Be natural; don't overthink unless this person would.")
        out.append(s)
    return out


A_TEXT = ("College A (government-aided engineering college): total fees for 4 years ₹4 lakh | "
          "median starting salary of graduates ₹4.5 LPA | 78% of students placed | 40 km from home")
B_TEXT = ("College B (private engineering university): total fees for 4 years ₹18 lakh | "
          "median starting salary of graduates ₹5 LPA | 80% of students placed | 300 km away, hostel extra")
EXTRA = {
    "hype": "🏆 HIGHEST PACKAGE ₹45 LPA! 95% PLACEMENT ASSISTANCE!",
    "scarcity": "⚠ Only 12 seats left! Pay ₹50,000 seat-booking fee within 48 hours to confirm your seat.",
    "ranking": "⭐ Ranked #7 'Top Emerging Engineering University 2026' (Education Excellence Awards)",
    "social": "3 seniors from your school joined College B last year, and your cousin's friend from B got placed at ₹20 LPA.",
}


def page(s, version):
    b = B_TEXT
    adds = list(EXTRA) if version == "all" else ([version] if version in EXTRA else [])
    for k in adds:
        b += "\n   " + EXTRA[k]
    colleges = [b, A_TEXT] if s["b_first"] else [A_TEXT, b]
    return ("You have admission offers from two colleges for B.Tech Computer Science:\n\n"
            + "\n\n".join(f"- {c}" for c in colleges)
            + "\n\nYou have to decide this week. Which college do you choose? Reply in exactly this format:\n"
              "CHOICE: <A or B>\nLOAN: <yes or no - would your family take an education loan for it?>\n"
              "REASON: <two or three sentences, in your own words>")


def parse(text):
    c = re.search(r"CHOICE:\s*\**\s*(?:College\s*)?([AB])\b", text, re.I)
    l = re.search(r"LOAN:\s*\**\s*(yes|no)", text, re.I)
    r = re.search(r"REASON:\s*(.+)", text, re.S)
    return (c.group(1).upper() if c else None, l.group(1).lower() if l else None,
            r.group(1).strip() if r else text)


def job(s, version):
    out = ask(s["system"], page(s, version))
    choice, loan, reason = parse(out)
    return {"student": s["id"], "name": s["name"], "income_level": s["income_level"],
            "style_level": s["style_level"], "friends": s["friends"], "parents": s["parents"],
            "trust": s["trust"], "b_first": s["b_first"], "version": version,
            "choice": choice, "loan": loan, "reason": reason, "raw": out}


def main(limit=None):
    students = make_students()
    tasks = [(s, v) for s in students for v in VERSIONS]
    if limit:
        tasks = tasks[:limit]
    name = "uni_test.json" if limit else "uni_results.json"
    t0, rows = time.time(), []
    with cf.ThreadPoolExecutor(PARALLEL) as ex:
        for k, r in enumerate(ex.map(lambda t: job(*t), tasks), 1):
            rows.append(r)
            print(f"{k}/{len(tasks)} {r['name']:8s} {r['version']:8s} -> {r['choice']} loan={r['loan']}", flush=True)
    json.dump({"model": "haiku", "students": students, "rows": rows, "seconds": round(time.time() - t0)},
              open(os.path.join(DATA, name), "w"), indent=1, ensure_ascii=False)
    print("UNI_DONE", flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else None)
