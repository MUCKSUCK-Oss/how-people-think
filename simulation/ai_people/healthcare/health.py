"""Healthcare traps (11 Nov 2026). Design and predictions: PREDICTIONS.md. Research: RESEARCH.md.

H1 India: stent vs medicines for stable chest pain (patients AND adult children).
H2 USA: early MRI vs physiotherapy for low-back pain.
Run from the Terminal panel (Claude login works there):
    python3 health.py pilot    -> health_pilot.json  (8 people per scenario)
    python3 health.py extra    -> health_extra.json  (6 NEW people per scenario, same design)
"""
import concurrent.futures as cf
import json
import os
import random
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from pilot import ask  # noqa: E402  fresh Haiku call, no tools, empty folder

PARALLEL = 3
STYLE = ["You usually decide quickly and go with your gut. Long comparisons bore you.",
         "You usually decide fairly quickly, but glance at the main details first.",
         "You usually compare options carefully before deciding.",
         "You research everything in detail and hate making a hasty decision."]

# ---------------- H1: India, stent vs medicines ----------------
H1_TRUST = ["You fully trust what doctors tell you; they are like God.",
            "You are suspicious of private hospitals and think they overcharge.",
            "You neither fully trust nor distrust doctors."]
H1_REL = ["What relatives and neighbours say matters a lot to your family.",
          "You don't care much what relatives say.",
          "You sometimes listen to relatives' advice."]
H1_CITIES = ["Lucknow", "Indore", "Patna", "Nagpur", "Jaipur", "Bhopal", "Kanpur", "Surat", "Pune",
             "Ludhiana", "Coimbatore", "Ranchi", "Gurugram", "Vadodara", "Kochi", "Varanasi"]
H1_INCOME = ["Money is tight: the household earns about ₹30,000 a month and has little savings.",
             "The household is middle-class: about ₹75,000 a month, with some savings.",
             "The household is comfortable: about ₹2.5 lakh a month."]
H1_SIT = ("For two months there has been chest pain only when climbing stairs; it goes away with rest. "
          "An angiography at a private hospital shows a 75% blockage in one heart artery. "
          "The cardiologist says both options below are possible.")
H1_A = ("Option A: medicines (about ₹1,500 a month) plus diet and walking, with follow-up at the "
        "government hospital (long queues). The pain may still come on stairs, and some patients later "
        "need a stent anyway.")
H1_B = "Option B: angioplasty with a stent at the private hospital now: about ₹2.5 lakh, 2–3 days in hospital."
H1_HONEST = ("Large trials (ISCHEMIA, about 5,000 patients): for stable chest pain like this, a stent does NOT "
             "lower the risk of death or heart attack compared with good medicines; it mainly relieves the "
             "chest pain sooner.")
H1_FEAR = ("The cardiologist said: \"This is a ticking time bomb. A heart attack can come any moment. "
           "Don't gamble with a life — I would do it today.\"")
H1_PACKAGE = ("The billing desk said: \"With your insurance / cashless package you pay only about ₹40,000. "
              "The package rate is valid only if admitted today.\"")
H1_ANECDOTE = ("Last year a neighbour of the same age ignored his chest pain and died of a heart attack. "
               "A cousin got a stent and says he feels 20 years younger.")
H1_DISCLOSE = ("(Disclosure: this hospital sets monthly revenue targets for its cardiologists. A free second "
               "opinion at the government medical college is available this week.)")
H1_VERSIONS = {
    "base": [],
    "honest": [H1_HONEST],
    "fear": [H1_FEAR],
    "package": [H1_PACKAGE],
    "anecdote": [H1_ANECDOTE],
    "all": [H1_FEAR, H1_PACKAGE, H1_ANECDOTE],
    "all_disclosed": [H1_FEAR, H1_PACKAGE, H1_ANECDOTE, H1_HONEST, H1_DISCLOSE],
}

# ---------------- H2: USA, MRI vs physiotherapy ----------------
H2_TRUST = ["You tend to believe health advertisements.",
            "You are suspicious of health advertisements and medical marketing.",
            "You neither fully trust nor distrust health advertisements."]
H2_REL = ["You take what friends and coworkers say very seriously.",
          "You don't care much about other people's health stories.",
          "You sometimes listen to friends' and coworkers' advice."]
H2_PLACES = ["Columbus, Ohio", "Phoenix, Arizona", "Atlanta, Georgia", "Tampa, Florida", "Denver, Colorado",
             "Charlotte, North Carolina", "Dallas, Texas", "Minneapolis, Minnesota", "Sacramento, California",
             "Pittsburgh, Pennsylvania", "Kansas City, Missouri", "Nashville, Tennessee"]
H2_JOBS = ["warehouse supervisor", "nurse's aide", "accountant", "high-school teacher", "electrician",
           "retail store manager", "software tester", "truck dispatcher", "dental hygienist", "bank teller"]
H2_INCOME = ["Money is tight: you earn about $38,000 a year and have under $1,000 saved.",
             "You earn about $70,000 a year and have a few thousand dollars saved.",
             "You earn about $140,000 a year and money is not a worry."]
H2_SIT = ("For 3 weeks you have had low-back pain after lifting boxes. No numbness, no fever, no weight loss, "
          "and it is slowly getting a little better. You have a high-deductible health plan.")
H2_A = ("Option A: physical therapy and staying active, about $300 out of pocket over 6 weeks. Pain like this "
        "usually improves within weeks, but you won't know exactly what's wrong.")
H2_B = "Option B: get an MRI now at an imaging center: about $1,100 out of pocket (it falls under your deductible)."
H2_HONEST = ("Medical guidelines (American College of Physicians, Choosing Wisely): for back pain without red flags, "
             "imaging in the first 6 weeks does not speed recovery, and it often finds harmless 'abnormalities' "
             "(bulging discs are common in people with no pain) that lead to injections or surgery you don't need.")
H2_FEAR = ("An ad from a local imaging center: \"Back pain can be a sign of something serious. Don't wait — "
           "early detection saves lives. Same-day MRI!\"")
H2_DEAL = "The imaging center offers $400 off if you book this week."
H2_ANECDOTE = ("A coworker says his back pain turned out to be a herniated disc found only by MRI, and his "
               "brother-in-law's 'back pain' was cancer.")
H2_DISCLOSE = "(Disclosure: the imaging center is owned by the clinic group that is advertising to you.)"
H2_VERSIONS = {
    "base": [],
    "honest": [H2_HONEST],
    "fear_ad": [H2_FEAR],
    "deal": [H2_DEAL],
    "anecdote": [H2_ANECDOTE],
    "all": [H2_FEAR, H2_DEAL, H2_ANECDOTE],
    "all_disclosed": [H2_FEAR, H2_DEAL, H2_ANECDOTE, H2_HONEST, H2_DISCLOSE],
}
VERSIONS = {1: H1_VERSIONS, 2: H2_VERSIONS}

IN_FIRST = ["Ramesh", "Sunita", "Mahesh", "Kavita", "Suresh", "Anita", "Vinod", "Rekha", "Dinesh", "Meena",
            "Ashok", "Usha", "Prakash", "Lata", "Harish", "Neelam", "Satish", "Shobha", "Mohan", "Pushpa"]
IN_YOUNG = ["Rahul", "Priya", "Amit", "Neha", "Rohit", "Pooja", "Vikas", "Sneha", "Ankit", "Divya",
            "Saurabh", "Shruti", "Nikhil", "Kriti", "Gaurav", "Swati", "Manish", "Aditi", "Varun", "Ritu"]
US_FIRST = ["Mike", "Jessica", "Carlos", "Ashley", "DeShawn", "Megan", "Tyler", "Maria", "Kevin", "Brittany",
            "Jose", "Amanda", "Brian", "Latoya", "Ryan", "Nicole", "Luis", "Heather", "Jason", "Tiffany"]


def make_people(scenario, n, seed_offset=0, style_shift=0):
    rng = random.Random(700 + scenario + seed_offset)
    order = [True, False] * (n // 2)
    random.Random(80 + scenario + seed_offset).shuffle(order)
    people = []
    for i in range(n):
        p = {"id": i, "style_level": ((i // 2) + style_shift) % 4, "income_level": rng.randrange(3),
             "b_first": order[i]}
        if scenario == 1:
            p["role"] = "patient" if i % 2 == 0 else "child"
            p["trust"], p["relatives"] = rng.choice(H1_TRUST), rng.choice(H1_REL)
            city = rng.choice(H1_CITIES)
            if p["role"] == "patient":
                name, age = rng.choice(IN_FIRST), rng.randint(54, 64)
                who = (f"You are {name}, {age}, from {city}, India. You are the patient: {H1_SIT}")
            else:
                name, age = rng.choice(IN_YOUNG), rng.randint(28, 38)
                par = rng.choice(["father", "mother"])
                who = (f"You are {name}, {age}, from {city}, India. Your {par} (aged {rng.randint(56, 66)}) is the "
                       f"patient and you will make the decision and arrange the money: {H1_SIT}")
            income = H1_INCOME[p["income_level"]]
        else:
            p["role"] = "patient"
            p["trust"], p["relatives"] = rng.choice(H2_TRUST), rng.choice(H2_REL)
            name, age = rng.choice(US_FIRST), rng.randint(30, 55)
            who = (f"You are {name}, {age}, a {rng.choice(H2_JOBS)} in {rng.choice(H2_PLACES)}, USA. {H2_SIT}")
            income = H2_INCOME[p["income_level"]]
        p["name"] = name
        p["system"] = (f"{who} {income} {STYLE[p['style_level']]} {p['trust']} {p['relatives']} "
                       "Think and answer exactly as this person would, in first person. "
                       "Be natural; don't overthink unless this person would.")
        people.append(p)
    return people


def page(scenario, p, version):
    a, b = (H1_A, H1_B) if scenario == 1 else (H2_A, H2_B)
    extras = VERSIONS[scenario][version]
    opts = [b, a] if p["b_first"] else [a, b]
    text = "You have to choose between:\n\n" + "\n\n".join(f"- {o}" for o in opts)
    if extras:
        text += "\n\nAlso:\n" + "\n".join(f"- {e}" for e in extras)
    return (text + "\n\nYou have to decide this week. Which option do you choose? Reply in exactly this format:\n"
            "CHOICE: <A or B>\nLOAN: <yes or no - would you borrow money or use a loan/credit card for it?>\n"
            "REASON: <two or three sentences, in your own words>")


def parse(text):
    c = re.search(r"CHOICE:\s*\**\s*(?:Option\s*)?([AB])\b", text, re.I)
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
    off = {"extra": 1000, "extra2": 2000}.get(mode, 0)
    shift = 2 if mode == "extra" else 0  # extra batch leans careful (pilot has 2 per style; balance)
    people = {s: make_people(s, n, off, shift) for s in (1, 2)}
    bump = {"extra": 100, "extra2": 200}.get(mode, 0)
    for s in people:
        for p in people[s]:
            p["id"] += bump
    tasks = [(s, p, v) for s in (1, 2) for p in people[s] for v in VERSIONS[s]]
    name = f"health_{mode}.json"
    t0, rows = time.time(), []
    with cf.ThreadPoolExecutor(PARALLEL) as ex:
        for k, r in enumerate(ex.map(lambda t: job(*t), tasks), 1):
            rows.append(r)
            print(f"{k}/{len(tasks)} H{r['scenario']} {r['role']:7s} {r['name']:9s} {r['version']:14s} -> "
                  f"{r['choice']} loan={r['loan']}", flush=True)
            if k % 40 == 0:
                json.dump({"partial": True, "rows": rows}, open(os.path.join(HERE, name + ".part"), "w"),
                          ensure_ascii=False)
    json.dump({"model": "haiku", "mode": mode, "people": people, "rows": rows,
               "seconds": round(time.time() - t0)},
              open(os.path.join(HERE, name), "w"), indent=1, ensure_ascii=False)
    print("HEALTH_DONE", flush=True)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "pilot")
