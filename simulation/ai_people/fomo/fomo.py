"""FOMO: friends, influencers, crowds and apps vs a risky token (14 Nov 2026).

Design and predictions: PREDICTIONS.md. Research: RESEARCH.md.
Everything is invented: the token (NOVA) and the app (TurboTrade).
8 countries x 3 risk attitudes. Every person sees 8 versions, each in a fresh call.

    python3 fomo.py pilot   -> data/fomo_pilot.json   (24 people, 192 decisions)
    python3 fomo.py extra   -> data/fomo_extra.json   (24 NEW people, same design)
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
os.makedirs(DATA, exist_ok=True)
sys.path.insert(0, os.path.dirname(HERE))
from ai_person import ask  # noqa: E402  fresh Haiku call, no tools, empty folder

PARALLEL = 3
STYLE = ["You usually decide quickly and go with your gut. Long comparisons bore you.",
         "You usually decide fairly quickly, but glance at the main details first.",
         "You usually compare options carefully before deciding.",
         "You research everything in detail and hate making a hasty decision."]
RISK = {"careful": "With money you are careful; losing savings would really scare you.",
        "average": "With money you are neither very careful nor a big risk-taker.",
        "likes_risk": "With money you like taking chances; you think playing it safe keeps people poor."}
JOBS = ["software tester", "sales executive", "nurse", "delivery rider", "bank clerk", "graphic designer",
        "call-centre agent", "junior accountant", "shop manager", "lab technician"]
# country: (monthly pay text, savings text, bonus text, cities, names)
COUNTRIES = {
    "India": ("₹30,000", "₹90,000", "₹500", ["Bengaluru", "Pune", "Hyderabad", "Jaipur"], ["Rohan", "Sneha", "Aditya", "Pooja", "Faisal", "Neha"]),
    "the United States": ("$3,500", "$10,500", "$5", ["Dallas", "Columbus", "Phoenix", "Charlotte"], ["Tyler", "Brianna", "Jordan", "Kayla", "Marcus", "Emily"]),
    "South Korea": ("₩2,800,000", "₩8,400,000", "₩7,000", ["Seoul", "Busan", "Incheon", "Daejeon"], ["Ji-hoon", "Soo-ah", "Min-ho", "Ye-jin", "Hyun-woo", "Da-eun"]),
    "Nigeria": ("₦250,000", "₦750,000", "₦5,000", ["Lagos", "Abuja", "Ibadan", "Port Harcourt"], ["Tobi", "Chiamaka", "Emeka", "Zainab", "Seyi", "Amaka"]),
    "Brazil": ("R$3,000", "R$9,000", "R$30", ["São Paulo", "Rio de Janeiro", "Curitiba", "Recife"], ["Gabriel", "Larissa", "Matheus", "Beatriz", "Rafael", "Júlia"]),
    "the United Kingdom": ("£2,200", "£6,600", "£5", ["Manchester", "Leeds", "Birmingham", "Cardiff"], ["Callum", "Jess", "Liam", "Amira", "Josh", "Hannah"]),
    "Indonesia": ("Rp6,000,000", "Rp18,000,000", "Rp80,000", ["Jakarta", "Bandung", "Surabaya", "Yogyakarta"], ["Rizky", "Putri", "Fajar", "Ayu", "Dimas", "Nadia"]),
    "Turkey": ("₺30,000", "₺90,000", "₺200", ["Istanbul", "Ankara", "Izmir", "Antalya"], ["Emre", "Zeynep", "Burak", "Elif", "Can", "Merve"]),
}
VERSIONS = ["base", "friend", "influencer", "crowd", "app", "all", "all_lossrate", "all_silent"]


def make_people(seed_offset=0, style_shift=0):
    rng = random.Random(1500 + seed_offset)
    people, i = [], 0
    for country, (pay, savings, bonus, cities, names) in COUNTRIES.items():
        for risk in RISK:
            p = {"id": i, "country": country, "risk": risk, "behind": (i + seed_offset) % 2 == 0,
                 "style_level": (i + style_shift) % 4, "pay": pay, "savings": savings, "bonus": bonus}
            name, age = rng.choice(names), rng.randint(21, 29)
            p["name"] = name
            p["friend"] = rng.choice([n for n in names if n != name])
            behind = (" Most of your college friends seem to be doing better than you financially, and it bothers you."
                      if p["behind"] else "")
            p["system"] = (f"You are {name}, {age}, working as a {rng.choice(JOBS)} in {rng.choice(cities)}, {country}. "
                           f"You earn about {pay} a month and have saved about {savings} (about 3 months' pay) "
                           f"in your bank account.{behind} {RISK[risk]} {STYLE[p['style_level']]} "
                           "Think and answer exactly as this person would, in first person. Be natural; don't "
                           "overthink unless this person would.")
            people.append(p)
            i += 1
    return people


def page(p, version):
    f, pay = p["friend"], p["pay"]
    parts = ["NOVA is a crypto token you can buy on the TurboTrade app. Its price is up 300% this year, "
             "but it swings a lot: it has dropped 40% in a single week twice this year."]
    if version in ("friend", "all", "all_lossrate", "all_silent"):
        parts.append(f"Your close friend {f} made about two months' pay on NOVA last month and showed you the "
                     f"screenshots. {f} says: \"Get in before it's too late. Seriously, why are you just letting your "
                     "money sit in the bank?\"")
    if version in ("influencer", "all", "all_lossrate", "all_silent"):
        parts.append("A finance influencer with 2 million followers posts: \"LAST CHANCE before NOVA goes 10x. "
                     "Rich people don't wait. Don't stay poor. 🚀\"")
    if version in ("crowd", "all", "all_lossrate", "all_silent"):
        parts.append("The news says 4 million people in your country bought NOVA this year. At work, everyone "
                     "seems to be talking about it.")
    if version in ("app", "all", "all_lossrate", "all_silent"):
        parts.append(f"TurboTrade offers a {p['bonus']} sign-up bonus, celebrates your first trade with confetti, "
                     "and shows a banner: \"Zero trading fees ends in 3 days!\"")
    if version in ("all_lossrate", "all_silent"):
        parts.append("You also read a market regulator's study: 9 out of 10 ordinary people who trade like this "
                     "lose money, and the average loss is about two months' pay.")
    if version == "all_silent":
        parts.append(f"A friend points out that people post their wins, not their losses. Later, {f} admits that "
                     "over the past year, their other trades lost more money than they made on NOVA.")
    return ("\n\n".join(parts) +
            f"\n\nWould you put some of your savings into NOVA now, or keep them in the bank? Reply in exactly this format:\n"
            "INVEST: <yes or no>\n"
            "AMOUNT: <what percent of your savings you would put in, 0 to 100>\n"
            "LEFT_OUT: <how much you would feel you are missing out if you don't, 1 (not at all) to 7 (very much)>\n"
            "REASON: <two or three sentences, in your own words>")


def parse(text):
    v = re.search(r"INVEST:\s*\**\s*(yes|no)", text, re.I)
    a = re.search(r"AMOUNT:\s*\**\s*(\d{1,3})", text)
    lo = re.search(r"LEFT_OUT:\s*\**\s*([1-7])", text)
    r = re.search(r"REASON:\s*(.+)", text, re.S)
    return (v.group(1).lower() if v else None, min(100, int(a.group(1))) if a else None,
            int(lo.group(1)) if lo else None, r.group(1).strip() if r else text)


def job(p, version):
    out = ask(p["system"], page(p, version))
    inv, amount, left, reason = parse(out)
    return {"person": p["id"], "name": p["name"], "country": p["country"], "risk": p["risk"],
            "behind": p["behind"], "style_level": p["style_level"], "version": version,
            "invest": inv, "amount": amount, "left_out": left, "reason": reason, "raw": out}


def main(mode):
    off = {"extra": 1000, "extra2": 2000}.get(mode, 0)
    people = make_people(off, style_shift=2 if mode == "extra" else 0)
    for p in people:
        p["id"] += {"extra": 100, "extra2": 200}.get(mode, 0)
    tasks = [(p, v) for p in people for v in VERSIONS]
    name = f"fomo_{mode}.json"
    t0, rows = time.time(), []
    with cf.ThreadPoolExecutor(PARALLEL) as ex:
        for k, r in enumerate(ex.map(lambda t: job(*t), tasks), 1):
            rows.append(r)
            print(f"{k}/{len(tasks)} {r['country'][:14]:14s} {r['risk']:10s} {r['name']:10s} {r['version']:12s} -> "
                  f"invest={r['invest']} amount={r['amount']} left={r['left_out']}", flush=True)
            if k % 40 == 0:
                json.dump({"partial": True, "rows": rows}, open(os.path.join(DATA, name + ".part"), "w"),
                          ensure_ascii=False)
    json.dump({"model": "haiku", "mode": mode, "people": people, "rows": rows,
               "seconds": round(time.time() - t0)},
              open(os.path.join(DATA, name), "w"), indent=1, ensure_ascii=False)
    print("FOMO_DONE", flush=True)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "pilot")
