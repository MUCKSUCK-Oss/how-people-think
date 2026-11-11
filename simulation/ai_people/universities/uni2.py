"""University traps v2 (night of 11 Nov 2026). Design and predictions: PREDICTIONS_v2.md.

Two scenarios, students AND parents, versions built from RESEARCH.md.
Run from the Terminal panel (Claude login works there):
    python3 uni2.py pilot      -> data/uni2_pilot.json   (8 people per scenario)
    python3 uni2.py full       -> data/uni2_full.json    (40 people per scenario)
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
from ai_person import ask  # noqa: E402  fresh Haiku call, no tools, empty folder

PARALLEL = 3
STYLE = ["You usually decide quickly and go with your gut. Long comparisons bore you.",
         "You usually decide fairly quickly, but glance at the main details first.",
         "You usually compare options carefully before deciding.",
         "You research everything in detail and hate making a hasty decision."]
TRUST = ["You tend to believe what advertisements, counsellors and agents tell you.",
         "You are suspicious of advertisements, counsellors and agents.",
         "You neither fully trust nor distrust advertisements and agents."]
RELATIVES = ["What relatives and neighbours think matters a lot to your family.",
             "You don't care much what relatives think.",
             "You sometimes listen to relatives' advice."]

# ---------------- Scenario 1: domestic B.Tech ----------------
S1_CITIES = ["Lucknow", "Indore", "Patna", "Nagpur", "Coimbatore", "Jaipur", "Bhopal", "Ranchi", "Surat",
             "Guwahati", "Kanpur", "Mysuru", "Dehradun", "Raipur", "Vijayawada", "Aurangabad"]
S1_INCOME = ["Money is tight: the family earns about ₹35,000 a month.",
             "The family is middle-class: about ₹80,000 a month, with some savings.",
             "The family is comfortable: about ₹2.5 lakh a month."]
S1_A = ("College A: government engineering college, 60 km from home. AICTE approved, NAAC B+. "
        "Total cost for 4 years about ₹4.5 lakh (including a rented room). Seniors say the labs are old, "
        "several teaching posts are vacant, and fewer companies visit than at bigger colleges.")
S1_B = ("College B: private university, 250 km away. Modern campus, AC classrooms, '40+ recruiters visit'. "
        "Total cost for 4 years about ₹11 lakh (with hostel).")
S1_HONEST = ("Official data for last year's B.Tech CSE graduates: College A median starting salary ₹4.2 LPA, "
             "64% placed. College B median starting salary ₹4.6 LPA, 70% placed.")
S1_HYPE = "College B's brochure: 🏆 HIGHEST PACKAGE ₹42 LPA! 100% PLACEMENT ASSISTANCE! 500+ OFFERS LAST YEAR!"
S1_COUNSELLOR = ("College B's admission counsellor phoned: \"Only a few CSE seats are left. Pay the ₹25,000 "
                 "booking amount by tomorrow to lock the seat. Our partner bank approves education loans in 3 days.\"")
S1_RELATIVES = ("Your cousin studied at College B and now works at an IT company in Bengaluru. At a family "
                "function, relatives said College B is 'a big name'.")
S1_DISCLOSE = "(Disclosure, same size as the ads: the admission counsellor is paid a commission for each admission.)"
S1_VERSIONS = {
    "brochure": [],
    "honest": [S1_HONEST],
    "hype": [S1_HYPE],
    "counsellor": [S1_HYPE, S1_COUNSELLOR],
    "relatives": [S1_HYPE, S1_RELATIVES],
    "all": [S1_HYPE, S1_COUNSELLOR, S1_RELATIVES],
    "all_disclosed": [S1_HYPE, S1_COUNSELLOR, S1_RELATIVES, S1_HONEST, S1_DISCLOSE],
}

# ---------------- Scenario 2: study abroad via agent ----------------
S2_PLACES = ["a village near Jalandhar, Punjab", "a village near Moga, Punjab", "Ludhiana, Punjab",
             "a village near Karnal, Haryana", "Hisar, Haryana", "a town near Mehsana, Gujarat",
             "Anand, Gujarat", "a village near Amritsar, Punjab", "Kurukshetra, Haryana", "Hyderabad, Telangana"]
S2_INCOME = ["The family farms 4 acres; money is tight and the land is the family's main asset.",
             "The family runs a small shop and earns about ₹60,000 a month.",
             "The family is fairly well-off: a business and 15 acres of land."]
S2_A = ("Option A: stay in India. B.Com/BBA at a decent local college, living at home. "
        "Total cost about ₹3 lakh for 3 years. Local B.Com graduates in your area usually find jobs "
        "paying ₹12,000–18,000 a month, and many stay unemployed for a year or more.")
S2_B = ("Option B: a 2-year Business Management diploma at a private career college near Toronto, Canada, "
        "arranged through a local education agent. First-year cost about ₹30 lakh including living costs "
        "(the family would need a big loan or to mortgage land). The college is eligible for a "
        "post-graduation work permit.")
S2_HONEST = ("Independent facts from an education NGO: permanent residency is NOT guaranteed (there is a large "
             "backlog and rules keep changing); most such students work 40–50 hours a week at minimum wage to "
             "pay living costs; rooms are often shared by 6–8 people; the agent is paid a commission by the "
             "college for each student.")
S2_AGENT = ("The agent told you: \"Canada needs workers. You'll get an office job anywhere in Toronto. PR is no "
            "problem after 2 years. Weak English is fine. Visa guaranteed through our office.\"")
S2_VILLAGE = ("About 300 young people from your area have already gone to Canada, and the neighbour's son "
              "sends ₹40,000 home every month.")
S2_VERSIONS = {
    "brochure": [],
    "honest": [S2_HONEST],
    "agent": [S2_AGENT],
    "agent_village": [S2_AGENT, S2_VILLAGE],
    "agent_village_disclosed": [S2_AGENT, S2_VILLAGE, S2_HONEST],
}

FIRST = ["Aarav", "Diya", "Kabir", "Ishaan", "Meher", "Vihaan", "Anika", "Reyansh", "Saanvi", "Arjun",
         "Zara", "Advait", "Myra", "Krish", "Aadhya", "Vivaan", "Kiara", "Shaurya", "Pari", "Ayaan",
         "Riya", "Dhruv", "Tanya", "Om", "Navya", "Rudra", "Ira", "Aryan", "Sara", "Yash",
         "Nisha", "Harsh", "Aisha", "Laksh", "Jiya", "Pranav", "Sana", "Dev", "Anvi", "Kunal"]
PB_FIRST = ["Gurpreet", "Simran", "Harjot", "Navneet", "Jaspreet", "Manpreet", "Karanveer", "Amanpreet",
            "Rajveer", "Harleen", "Parth", "Hetal", "Jigar", "Khushi", "Mohit", "Pooja", "Sandeep", "Ritu",
            "Lovepreet", "Komal", "Arshdeep", "Tanvi", "Rohit", "Neha", "Vikas", "Payal", "Ankit", "Sneha",
            "Gagandeep", "Muskan", "Dhruv", "Priya", "Yuvraj", "Kirandeep", "Nikhil", "Mehak", "Sahil",
            "Bhavna", "Ravinder", "Divya"]
PARENT_FIRST = ["Rajesh", "Sunita", "Mahesh", "Kavita", "Suresh", "Anita", "Ramesh", "Geeta", "Vinod", "Rekha",
                "Sukhwinder", "Paramjit", "Balwinder", "Harpreet", "Jatinder", "Kuldeep", "Bharat", "Hansa",
                "Dinesh", "Meena"]


def make_people(scenario, n, seed_offset=0, style_shift=0):
    rng = random.Random(500 + scenario + seed_offset)
    order = [True, False] * (n // 2)
    random.Random(60 + scenario + seed_offset).shuffle(order)
    people = []
    for i in range(n):
        role = "student" if i % 2 == 0 else "parent"
        p = {"id": i, "role": role, "style_level": ((i // 2) + style_shift) % 4, "income_level": rng.randrange(3),
             "trust": rng.choice(TRUST), "relatives": rng.choice(RELATIVES), "b_first": order[i]}
        if scenario == 1:
            place = rng.choice(S1_CITIES)
            income = S1_INCOME[p["income_level"]]
            child = rng.choice(["son", "daughter"])
            if role == "student":
                name, age = rng.choice(FIRST), rng.choice([17, 18])
                who = (f"You are {name}, {age}, from {place}, India. You just finished Class 12 (scored "
                       f"{rng.choice(['88%', '79%', '72%'])}) and want to study Computer Science engineering.")
            else:
                name, age = rng.choice(PARENT_FIRST), rng.randint(42, 52)
                who = (f"You are {name}, {age}, a {rng.choice(['bank clerk', 'shop owner', 'school teacher', 'government employee', 'small contractor', 'homemaker'])} "
                       f"in {place}, India. Your {child} just finished Class 12 and wants to study Computer "
                       "Science engineering. You will make the final decision and arrange the money.")
        else:
            place = rng.choice(S2_PLACES)
            income = S2_INCOME[p["income_level"]]
            child = rng.choice(["son", "daughter"])
            if role == "student":
                name, age = rng.choice(PB_FIRST), rng.choice([18, 19, 20])
                who = (f"You are {name}, {age}, from {place}, India. You finished Class 12 and are deciding "
                       "what to do next. Jobs nearby are few.")
            else:
                name, age = rng.choice(PARENT_FIRST), rng.randint(42, 55)
                who = (f"You are {name}, {age}, from {place}, India. Your {child} finished Class 12, and you "
                       "must decide their next step and arrange the money. Jobs nearby are few.")
        p["name"] = name
        p["system"] = (f"{who} {income} {STYLE[p['style_level']]} {p['trust']} {p['relatives']} "
                       "Think and answer exactly as this person would, in first person. "
                       "Be natural; don't overthink unless this person would.")
        people.append(p)
    return people


def page(scenario, p, version):
    if scenario == 1:
        a, b, extras = S1_A, S1_B, S1_VERSIONS[version]
        intro = "You have admission offers from two colleges for B.Tech Computer Science:"
        q = "Which college do you choose?"
    else:
        a, b, extras = S2_A, S2_B, S2_VERSIONS[version]
        intro = "You are choosing between two paths:"
        q = "Which option do you choose?"
    opts = [b, a] if p["b_first"] else [a, b]
    text = intro + "\n\n" + "\n\n".join(f"- {o}" for o in opts)
    if extras:
        text += "\n\nAlso:\n" + "\n".join(f"- {e}" for e in extras)
    who = "your family" if p["role"] == "student" else "you"
    return (text + f"\n\nYou have to decide this week. {q} Reply in exactly this format:\n"
            f"CHOICE: <A or B>\nLOAN: <yes or no - would {who} take a loan or mortgage for it?>\n"
            "REASON: <two or three sentences, in your own words>")


def parse(text):
    c = re.search(r"CHOICE:\s*\**\s*(?:Option\s*|College\s*)?([AB])\b", text, re.I)
    l = re.search(r"LOAN:\s*\**\s*(yes|no)", text, re.I)
    r = re.search(r"REASON:\s*(.+)", text, re.S)
    return (c.group(1).upper() if c else None, l.group(1).lower() if l else None,
            r.group(1).strip() if r else text)


def job(scenario, p, version):
    out = ask(p["system"], page(scenario, p, version))
    choice, loan, reason = parse(out)
    return {"scenario": scenario, "person": p["id"], "name": p["name"], "role": p["role"],
            "style_level": p["style_level"], "income_level": p["income_level"], "trust": p["trust"],
            "relatives": p["relatives"], "b_first": p["b_first"], "version": version,
            "choice": choice, "loan": loan, "reason": reason, "raw": out}


def main(mode):
    n = {"pilot": 8, "extra": 6, "extra2": 6}.get(mode, 40)
    off = {"extra": 1000, "extra2": 2000}.get(mode, 0)   # extra batches = NEW people, same design as pilot 2
    shift = 2 if mode == "extra2" else 0   # extra2: more careful people (very careful was under-sampled)
    people = {1: make_people(1, n, off, shift), 2: make_people(2, n, off, shift)}
    if mode in ("extra", "extra2"):  # ids that don't clash with the pilot's 0-7
        for s_ in people:
            for p in people[s_]:
                p["id"] += 100 if mode == "extra" else 200
    tasks = [(1, p, v) for p in people[1] for v in S1_VERSIONS] + \
            [(2, p, v) for p in people[2] for v in S2_VERSIONS]
    name = f"uni2_{mode}.json"
    t0, rows = time.time(), []
    with cf.ThreadPoolExecutor(PARALLEL) as ex:
        for k, r in enumerate(ex.map(lambda t: job(*t), tasks), 1):
            rows.append(r)
            print(f"{k}/{len(tasks)} S{r['scenario']} {r['role']:7s} {r['name']:10s} {r['version']:24s} -> "
                  f"{r['choice']} loan={r['loan']}", flush=True)
            if k % 40 == 0:
                json.dump({"partial": True, "rows": rows}, open(os.path.join(DATA, name + ".part"), "w"),
                          ensure_ascii=False)
    json.dump({"model": "haiku", "mode": mode, "people": people, "rows": rows,
               "seconds": round(time.time() - t0)},
              open(os.path.join(DATA, name), "w"), indent=1, ensure_ascii=False)
    print("UNI2_DONE", flush=True)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "pilot")
