"""Personal targeting (11 Nov 2026). Design and predictions: PREDICTIONS.md. Research: RESEARCH.md.

P1 India: an instant-loan app vs asking a relative / bank (ad matched to each person's own situation).
P2 USA: book a flight now vs keep comparing (personalised / "special" / surveillance prices).
Run from the Terminal panel (Claude login works there):
    python3 targeting.py pilot   -> tgt_pilot.json  (8 people per scenario)
    python3 targeting.py extra   -> tgt_extra.json  (6 NEW people per scenario, same design)
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
STYLE_AD = {  # matched-ad line for each decision style
    0: "Tap. Done. Money in your account in 10 minutes.",
    1: "Three quick steps, money in 10 minutes.",
    2: "Clear terms, instant approval, no surprises.",
    3: "Fully digital, transparent process, check every detail in the app.",
}

# ---------------- P1: India, instant-loan app ----------------
P1_NEEDS = [("your mother's hospital bill", "Hospital bill? Don't let money stop your mother's treatment."),
            ("this month's rent; the landlord is threatening to ask you to leave", "Rent due? Keep your home without stress."),
            ("your younger brother's college exam fee, due in 3 days", "Fee deadline? Don't let your brother miss his exam.")]
P1_PRIDE = [("You hate asking relatives for money; it feels shameful and they gossip.", "No need to ask anyone. Nobody will know."),
            ("You don't mind asking relatives for help when needed.", "Why trouble your family? Handle it yourself.")]
P1_TRUST = ["You trust phone apps and use UPI for everything.",
            "You are suspicious of loan apps; you have heard bad stories.",
            "You neither fully trust nor distrust apps."]
P1_CITIES = ["Hyderabad", "Pune", "Bengaluru", "Lucknow", "Indore", "Kolkata", "Jaipur", "Chennai", "Ahmedabad",
             "Bhopal", "Patna", "Nagpur", "Coimbatore", "Delhi", "Surat", "Visakhapatnam"]
P1_JOBS = ["delivery rider", "call-centre employee", "shop assistant", "junior accountant", "auto driver",
           "private-school teacher", "security guard", "beautician", "sales executive", "lab technician"]
P1_INCOME = ["You earn about ₹14,000 a month and have almost no savings.",
             "You earn about ₹28,000 a month and have about ₹3,000 saved.",
             "You earn about ₹55,000 a month, but your savings are locked in a fixed deposit."]
P1_A = ("Option A: ask a relative or a friend for ₹15,000, or take a cash advance on a bank credit card / "
        "salary advance. It is cheap, but slower (2–3 days) and may be awkward or embarrassing.")
P1_B = ("Option B: install the 'QuickRupee' app: ₹15,000 in your account in 10 minutes, no documents. To approve "
        "you, the app asks permission to read your phone contacts and photos.")
P1_GENERIC = "QuickRupee ad: \"Instant loans up to ₹50,000! Apply now.\""
P1_HONEST = ("The real terms (from the app's fine print): a 7-day loan, about ₹4,500 in fees (around 300% a year); "
             "QuickRupee is not registered with the RBI; if you pay late, it contacts the people in your phone "
             "contacts.")
P1_URGENCY = "\"Your pre-approved offer expires in 15 minutes.\""
P1_SOCIAL = "\"2 lakh people in your city used QuickRupee this month. Rated 4.6 stars.\""
P1_CREEPY = "\"We noticed you searched 'urgent money' at 2 am last night.\""
# v2 (after pilot 1 floor at 0%): realistic situation people are in when they turn to loan apps
P1_A2 = ("Option A: keep trying the slow routes: ask your employer for a salary advance (last time they refused) or "
         "ask a relative again (your uncle said no last month and told the whole family). It may take 2–3 days and "
         "may still fail.")
P1_B2 = ("Option B: install the 'QuickRupee' app: ₹15,000 in your account in 10 minutes, no documents. During "
         "sign-up it shows the usual 'Allow access' pop-ups (contacts, photos), like many apps do.")
P1_VERSIONS = ["base", "honest", "matched", "creepy", "urgency", "social", "disclosed"]

# ---------------- P2: USA, personalised flight price ----------------
P2_PREF = [("You hate layovers and always want a direct flight.", "Picked for you: a direct flight, no layovers, just how you like it."),
           ("You love a window seat and travel light.", "Picked for you: window seat saved, carry-on included, just how you like it."),
           ("You always hunt for the cheapest deal.", "Picked for you: one of the best-value fares on this route.")]
P2_TRUST = ["You tend to trust travel websites.",
            "You are suspicious of travel sites and their pricing tricks.",
            "You neither fully trust nor distrust travel sites."]
P2_PLACES = ["Columbus, Ohio", "Phoenix, Arizona", "Atlanta, Georgia", "Tampa, Florida", "Denver, Colorado",
             "Charlotte, North Carolina", "Dallas, Texas", "Minneapolis, Minnesota", "Sacramento, California",
             "Pittsburgh, Pennsylvania", "Kansas City, Missouri", "Nashville, Tennessee"]
P2_JOBS = ["warehouse supervisor", "nurse", "accountant", "high-school teacher", "electrician",
           "retail store manager", "software tester", "truck dispatcher", "dental hygienist", "bank teller"]
P2_INCOME = ["Money is tight: you earn about $36,000 a year.",
             "You earn about $72,000 a year.",
             "You earn about $150,000 a year; money is not a worry."]
P2_A = ("Option A: don't book yet. Keep checking other sites and compare for a day or two (the fare could go up "
        "or down).")
P2_B = "Option B: book now on this site."
P2_FARE = "The site shows a round-trip fare of $312 for a family visit next month."
P2_SPECIAL = "\"Special member price just for you: $312 (was $349).\""
P2_CREEPY = "\"We see you've checked this route 6 times this week.\""
P2_URGENCY = "\"Only 2 seats left at this price.\""
P2_DISCLOSE = ("(Disclosure required by law: prices on this site are personalised using your device and browsing "
               "history. The same seat is currently shown to other users for $279.)")
P2_VERSIONS = ["base", "matched", "special_price", "creepy", "urgency", "disclosed"]
VERSIONS = {1: P1_VERSIONS, 2: P2_VERSIONS}

IN_NAMES = ["Rahul", "Priya", "Amit", "Neha", "Rohit", "Pooja", "Vikas", "Sneha", "Ankit", "Divya", "Imran",
            "Fatima", "Suresh", "Lakshmi", "Arjun", "Kavya", "Manoj", "Ayesha", "Ravi", "Deepa"]
US_NAMES = ["Mike", "Jessica", "Carlos", "Ashley", "DeShawn", "Megan", "Tyler", "Maria", "Kevin", "Brittany",
            "Jose", "Amanda", "Brian", "Latoya", "Ryan", "Nicole", "Luis", "Heather", "Jason", "Tiffany"]


def make_people(scenario, n, seed_offset=0, style_shift=0, v2=False):
    rng = random.Random(900 + scenario + seed_offset)
    order = [True, False] * (n // 2)
    random.Random(90 + scenario + seed_offset).shuffle(order)
    people = []
    for i in range(n):
        p = {"id": i, "style_level": ((i // 2) + style_shift) % 4,
             "income_level": (i + seed_offset) % 3 if v2 else rng.randrange(3),
             "b_first": order[i]}
        if scenario == 1:
            need, need_ad = rng.choice(P1_NEEDS)
            p["proud"] = i % 2 == 0  # half proud / half not (balanced)
            pride, pride_ad = P1_PRIDE[0 if p["proud"] else 1]
            p["trust"] = rng.choice(P1_TRUST)
            name, age = rng.choice(IN_NAMES), rng.randint(22, 45)
            when = "by tomorrow" if v2 else "within 3 days"
            who = (f"You are {name}, {age}, a {rng.choice(P1_JOBS)} in {rng.choice(P1_CITIES)}, India. You urgently "
                   f"need ₹15,000 {when} for {need}.")
            p["system"] = (f"{who} {P1_INCOME[p['income_level']]} {STYLE[p['style_level']]} {pride} {p['trust']} ")
            p["matched_ad"] = f"QuickRupee ad shown to you: \"{need_ad} {pride_ad} {STYLE_AD[p['style_level']]}\""
        else:
            pref, pref_ad = rng.choice(P2_PREF)
            p["proud"] = None
            p["trust"] = rng.choice(P2_TRUST)
            name, age = rng.choice(US_NAMES), rng.randint(25, 60)
            who = (f"You are {name}, {age}, a {rng.choice(P2_JOBS)} in {rng.choice(P2_PLACES)}, USA. You are booking "
                   "a flight for a family visit next month.")
            p["system"] = f"{who} {P2_INCOME[p['income_level']]} {STYLE[p['style_level']]} {pref} {p['trust']} "
            p["matched_ad"] = f"The site says: \"{pref_ad}\""
        p["name"], p["v2"] = name, v2
        p["system"] += ("Think and answer exactly as this person would, in first person. "
                        "Be natural; don't overthink unless this person would.")
        people.append(p)
    return people


def extras(scenario, p, version):
    m = p["matched_ad"]
    if scenario == 1:
        return {"base": [P1_GENERIC], "honest": [P1_GENERIC, P1_HONEST], "matched": [m],
                "creepy": [m, P1_CREEPY], "urgency": [m, P1_URGENCY], "social": [m, P1_SOCIAL],
                "disclosed": [m, P1_URGENCY, P1_SOCIAL, P1_HONEST]}[version]
    return {"base": [P2_FARE], "matched": [P2_FARE, m], "special_price": [P2_FARE, P2_SPECIAL],
            "creepy": [P2_FARE, m, P2_CREEPY], "urgency": [P2_FARE, m, P2_URGENCY],
            "disclosed": [P2_FARE, m, P2_SPECIAL, P2_URGENCY, P2_DISCLOSE]}[version]


def page(scenario, p, version):
    a, b = ((P1_A2, P1_B2) if p.get("v2") else (P1_A, P1_B)) if scenario == 1 else (P2_A, P2_B)
    opts = [b, a] if p["b_first"] else [a, b]
    text = "You have to choose between:\n\n" + "\n\n".join(f"- {o}" for o in opts)
    text += "\n\nWhat you see:\n" + "\n".join(f"- {e}" for e in extras(scenario, p, version))
    second = ("PERMISSION: <yes or no - would you allow the app to read your contacts and photos?>" if scenario == 1
              else "FAIR: <yes or no - do you feel this price is fair?>")
    return (text + "\n\nWhich option do you choose? Reply in exactly this format:\nCHOICE: <A or B>\n" + second +
            "\nREASON: <two or three sentences, in your own words>")


def parse(text):
    c = re.search(r"CHOICE:\s*\**\s*(?:Option\s*)?([AB])\b", text, re.I)
    l = re.search(r"(?:PERMISSION|FAIR):\s*\**\s*(yes|no)", text, re.I)
    r = re.search(r"REASON:\s*(.+)", text, re.S)
    return (c.group(1).upper() if c else None, l.group(1).lower() if l else None,
            r.group(1).strip() if r else text)


def job(scenario, p, version):
    out = ask(p["system"], page(scenario, p, version))
    choice, second, reason = parse(out)
    return {"scenario": scenario, "person": p["id"], "name": p["name"], "proud": p["proud"],
            "style_level": p["style_level"], "income_level": p["income_level"], "trust": p["trust"],
            "b_first": p["b_first"], "version": version, "choice": choice, "second": second,
            "reason": reason, "raw": out}


def main(mode):
    # pilot: both (P1 v1). p1v2: P1 re-pilot with realistic v2 situation (8 people, balanced income).
    # p1v2extra: 6 new P1 v2 people. p2extra: 6 new P2 people.
    n = {"pilot": 8, "p1v2": 8}.get(mode, 6)
    off = {"extra": 1000, "extra2": 2000, "p1v2extra": 1000, "p2extra": 1000}.get(mode, 0)
    shift = 2 if mode in ("extra", "p1v2extra", "p2extra") else 0
    scen = (1, 2) if mode in ("pilot", "extra", "extra2") else ((1,) if mode.startswith("p1") else (2,))
    v2 = mode.startswith("p1v2")
    people = {s: make_people(s, n, off, shift, v2) for s in scen}
    bump = {"extra": 100, "extra2": 200, "p1v2extra": 100, "p2extra": 100}.get(mode, 0)
    for s in people:
        for p in people[s]:
            p["id"] += bump
    tasks = [(s, p, v) for s in scen for p in people[s] for v in VERSIONS[s]]
    name = f"tgt_{mode}.json"
    t0, rows = time.time(), []
    with cf.ThreadPoolExecutor(PARALLEL) as ex:
        for k, r in enumerate(ex.map(lambda t: job(*t), tasks), 1):
            rows.append(r)
            print(f"{k}/{len(tasks)} P{r['scenario']} {r['name']:9s} {r['version']:14s} -> {r['choice']} "
                  f"second={r['second']}", flush=True)
            if k % 40 == 0:
                json.dump({"partial": True, "rows": rows}, open(os.path.join(HERE, name + ".part"), "w"),
                          ensure_ascii=False)
    json.dump({"model": "haiku", "mode": mode, "people": people, "rows": rows,
               "seconds": round(time.time() - t0)},
              open(os.path.join(HERE, name), "w"), indent=1, ensure_ascii=False)
    print("TGT_DONE", flush=True)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "pilot")
