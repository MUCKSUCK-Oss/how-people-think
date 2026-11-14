"""Corporations: quiet vs loud dark patterns (14 Nov 2026).

Design and predictions: PREDICTIONS.md. Research: RESEARCH.md.
C1 drip pricing (concert tickets), C2 subscription trap (cancelling a streaming service).
Everything is invented (the sites, the band, StreamMax). 6 countries x 2 people per scenario.

    python3 corp.py pilot   -> data/corp_pilot.json   (24 people, 168 decisions)
    python3 corp.py extra   -> data/corp_extra.json   (24 NEW people, same design)
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
INCOME = {"tight": "Money is tight for you; you watch every expense.",
          "comfortable": "You are financially comfortable; small amounts don't worry you much."}
JOBS = ["teacher", "sales executive", "nurse", "software developer", "shop owner", "bank clerk",
        "graphic designer", "driver", "accountant", "pharmacist"]
# country: (A total, B total, B shown, addon, sub per month, cities, names)
COUNTRIES = {
    "India": ("₹8,000", "₹8,400", "₹6,500", "₹500", "₹499", ["Mumbai", "Bengaluru", "Delhi", "Kolkata"], ["Ankit", "Riya", "Siddharth", "Meera", "Arjun", "Divya"]),
    "the United States": ("$96", "$101", "$78", "$6", "$12", ["Chicago", "Austin", "Denver", "Atlanta"], ["Ryan", "Ashley", "Kevin", "Lauren", "Andre", "Nicole"]),
    "the United Kingdom": ("£76", "£80", "£62", "£5", "£10", ["London", "Manchester", "Leeds", "Bristol"], ["Tom", "Sophie", "Daniel", "Grace", "Aisha", "Ben"]),
    "Brazil": ("R$480", "R$505", "R$390", "R$30", "R$45", ["São Paulo", "Rio de Janeiro", "Porto Alegre", "Salvador"], ["Lucas", "Camila", "Thiago", "Fernanda", "Bruno", "Isabela"]),
    "Nigeria": ("₦120,000", "₦126,000", "₦97,500", "₦7,500", "₦9,000", ["Lagos", "Abuja", "Ibadan", "Enugu"], ["Chidi", "Bisi", "Femi", "Ifeoma", "Musa", "Tolu"]),
    "Indonesia": ("Rp1,500,000", "Rp1,575,000", "Rp1,220,000", "Rp95,000", "Rp120,000", ["Jakarta", "Bandung", "Surabaya", "Medan"], ["Andi", "Sari", "Yoga", "Indah", "Reza", "Wulan"]),
}
V1 = ["honest", "drip", "drip_timer", "drip_normal", "addon", "all", "all_disclosed"]
V2 = ["easy", "obstruct", "shame", "offer", "loss", "all", "all_disclosed"]


def make_people(seed_offset=0, style_shift=0):
    rng = random.Random(1600 + seed_offset)
    people, i = [], 0
    for scen in ("C1", "C2"):
        for country, (a, b, bshown, addon, sub, cities, names) in COUNTRIES.items():
            for k in range(2):
                income = ["tight", "comfortable"][(k + i // 2 + seed_offset) % 2]
                p = {"id": i, "scenario": scen, "country": country, "income": income,
                     "style_level": (i + style_shift) % 4, "a": a, "b": b, "bshown": bshown, "addon": addon, "sub": sub}
                name, age = rng.choice(names), rng.randint(22, 45)
                p["name"] = name
                job = rng.choice(JOBS)
                p["system"] = (f"You are {name}, {age}, {'an' if job[0] in 'aeiou' else 'a'} {job} in {rng.choice(cities)}, {country}. "
                               f"{INCOME[income]} {STYLE[p['style_level']]} Think and answer exactly as this person "
                               "would, in first person. Be natural; don't overthink unless this person would.")
                people.append(p)
                i += 1
    return people


def page_c1(p, v):
    a, b, bs, ad = p["a"], p["b"], p["bshown"], p["addon"]
    if v == "honest":
        text = (f"You want 2 tickets for a concert by a band you like. Two ticket sites have similar seats.\n"
                f"Site A: {a} total for 2 tickets, all fees included.\n"
                f"Site B: {b} total for 2 tickets, all fees included.\n"
                "You have been looking at Site B's seat map for about 10 minutes and picked your seats there.")
    else:
        text = (f"You want 2 tickets for a concert by a band you like. On a search page, Site A listed 2 tickets "
                f"for {a} (all fees included) and Site B listed them for {bs}. You chose Site B, spent about 10 "
                "minutes picking seats on its seat map and entered your details.\n\n"
                f"Now, on the final payment screen, Site B shows: tickets {bs} + service fee + facility fee = "
                f"TOTAL {b}.")
        if v in ("drip_timer", "all"):
            text += "\nA red banner says: \"Your seats are held for 04:59. Complete your purchase before time runs out!\""
        if v in ("drip_normal", "all"):
            text += "\nA small note says: \"Service fees are standard across ticket sites.\""
        if v in ("addon", "all", "all_disclosed"):
            text += (f"\nA box is already ticked: \"Ticket protection: {ad}\" (refund if you can't attend). "
                     f"It adds {ad} to the total above unless you untick it.")
        if v == "all_disclosed":
            text += (f"\nA price-comparison browser extension pops up: \"Site A sells similar seats for {a} all-in. "
                     "Re-choosing seats there takes about 5 minutes. Fees added only at checkout are banned in some countries.\"")
    q = ("\n\nWhat do you do? Reply in exactly this format:\n"
         "CHOICE: <B (buy on Site B) or A (go back and buy on Site A)>\n")
    if v in ("addon", "all", "all_disclosed"):
        q += "ADDON: <kept or removed - what you do with the ticked ticket protection if you buy on B>\n"
    return text + q + "ANNOYED: <how annoyed you feel, 1 (not at all) to 7 (very)>\nREASON: <two or three sentences, in your own words>"


def page_c2(p, v):
    s = p["sub"]
    text = (f"You pay {s} a month for a streaming service called StreamMax. You have used it only twice in the "
            "last 3 months, so you decided to cancel and opened the app to do it.\n\n")
    if v == "easy":
        text += "In Settings there is a \"Cancel subscription\" button. One tap and it's done."
    elif v == "obstruct":
        text += ("There is no cancel button in the app. A help page says you must call the support line, open 9 am-5 pm "
                 "on weekdays; the typical waiting time is about 20 minutes.")
    elif v == "shame":
        text += ("You tap Cancel. A screen asks you to confirm, with two buttons: \"Keep my entertainment\" and "
                 "\"No, I prefer being bored\". Tapping the second one cancels.")
    elif v == "offer":
        text += (f"You tap Cancel. Before it goes through, a screen offers: \"Stay for 50% off for the next 3 months!\" "
                 "with buttons to accept the offer or continue cancelling (one more tap).")
    elif v == "loss":
        text += ("You tap Cancel. Before it goes through, a screen warns: \"You'll lose your watch history, saved lists "
                 "and personal recommendations forever.\" One more tap continues cancelling.")
    else:
        text += ("There is no cancel button in the app. A help page says you must call the support line, open 9 am-5 pm "
                 "on weekdays; the typical waiting time is about 20 minutes. The page's buttons say \"Keep my "
                 "entertainment\" and \"No, I prefer being bored - show me the phone number\". It also says the agent "
                 "can offer you 50% off for the next 3 months, and warns that cancelling means you'll lose your watch "
                 "history, saved lists and personal recommendations forever.")
        if v == "all_disclosed":
            text += ("\n\nA consumer-rights website you trust says: in your country you can cancel any subscription "
                     "with a one-line email to the company, and the 50% offer goes back to full price after 3 months.")
    return (text + "\n\nWhat do you do? Reply in exactly this format:\n"
            "ACTION: <cancel now, keep for now, or take the offer>\n"
            "ANNOYED: <how annoyed you feel, 1 (not at all) to 7 (very)>\n"
            "REASON: <two or three sentences, in your own words>")


def parse(text, scen):
    c = (re.search(r"CHOICE:\s*\**\s*(?:Site\s*)?([AB])\b", text, re.I) if scen == "C1"
         else re.search(r"ACTION:\s*\**\s*(cancel|keep|take)", text, re.I))
    ad = re.search(r"ADDON:\s*\**\s*(kept|removed|keep|remove)", text, re.I)
    an = re.search(r"ANNOYED:\s*\**\s*([1-7])", text)
    r = re.search(r"REASON:\s*(.+)", text, re.S)
    choice = c.group(1).upper() if (c and scen == "C1") else ({"take": "offer"}.get(c.group(1).lower(), c.group(1).lower()) if c else None)
    addon = ("kept" if ad.group(1).lower().startswith("kep") else "removed") if ad else None
    return choice, addon, int(an.group(1)) if an else None, r.group(1).strip() if r else text


def job(p, v):
    out = ask(p["system"], page_c1(p, v) if p["scenario"] == "C1" else page_c2(p, v))
    choice, addon, annoyed, reason = parse(out, p["scenario"])
    return {"person": p["id"], "name": p["name"], "scenario": p["scenario"], "country": p["country"],
            "income": p["income"], "style_level": p["style_level"], "version": v, "choice": choice,
            "addon": addon, "annoyed": annoyed, "reason": reason, "raw": out}


def main(mode):
    off = {"extra": 1000, "extra2": 2000}.get(mode, 0)
    people = make_people(off, style_shift=2 if mode == "extra" else 0)
    for p in people:
        p["id"] += {"extra": 100, "extra2": 200}.get(mode, 0)
    tasks = [(p, v) for p in people for v in (V1 if p["scenario"] == "C1" else V2)]
    name = f"corp_{mode}.json"
    t0, rows = time.time(), []
    with cf.ThreadPoolExecutor(PARALLEL) as ex:
        for k, r in enumerate(ex.map(lambda t: job(*t), tasks), 1):
            rows.append(r)
            print(f"{k}/{len(tasks)} {r['scenario']} {r['country'][:12]:12s} {r['income']:11s} {r['name']:10s} "
                  f"{r['version']:14s} -> {r['choice']} addon={r['addon']} annoyed={r['annoyed']}", flush=True)
            if k % 40 == 0:
                json.dump({"partial": True, "rows": rows}, open(os.path.join(DATA, name + ".part"), "w"),
                          ensure_ascii=False)
    json.dump({"model": "haiku", "mode": mode, "people": people, "rows": rows,
               "seconds": round(time.time() - t0)},
              open(os.path.join(DATA, name), "w"), indent=1, ensure_ascii=False)
    print("CORP_DONE", flush=True)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "pilot")
