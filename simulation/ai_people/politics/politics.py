"""World politics: same policy, different party label (13 Nov 2026).

Design and predictions: PREDICTIONS.md. Research: RESEARCH.md.
8 countries x (supporter of party A, supporter of rival party B, person with no party).
Every person sees the same invented policy under 7 labels/styles, each in a fresh call.

    python3 politics.py pilot   -> data/pol_pilot.json   (24 people, 168 decisions)
    python3 politics.py extra   -> data/pol_extra.json   (24 NEW people, same design)
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
JOBS = ["shop owner", "nurse", "taxi driver", "school teacher", "factory worker", "accountant",
        "farmer", "office clerk", "electrician", "small-business owner", "bank employee", "salesperson"]

# country: (party A, party B, cities, first names)
COUNTRIES = {
    "India": ("the BJP", "the Congress party", ["Lucknow", "Pune", "Jaipur", "Chennai"],
              ["Rahul", "Priya", "Amit", "Sunita", "Imran", "Kavita"]),
    "the United States": ("the Republican Party", "the Democratic Party", ["Columbus, Ohio", "Phoenix", "Atlanta", "Pittsburgh"],
                          ["Mike", "Jessica", "Carlos", "Ashley", "DeShawn", "Megan"]),
    "Brazil": ("the Workers' Party (PT)", "the Liberal Party (PL)", ["São Paulo", "Recife", "Belo Horizonte", "Curitiba"],
               ["João", "Ana", "Pedro", "Mariana", "Lucas", "Camila"]),
    "the United Kingdom": ("the Labour Party", "the Conservative Party", ["Leeds", "Birmingham", "Bristol", "Glasgow"],
                           ["James", "Emma", "Oliver", "Sophie", "Mohammed", "Chloe"]),
    "Poland": ("Law and Justice (PiS)", "Civic Coalition (KO)", ["Kraków", "Lublin", "Gdańsk", "Poznań"],
               ["Piotr", "Anna", "Tomasz", "Katarzyna", "Marek", "Agnieszka"]),
    "Nigeria": ("the APC", "the PDP", ["Lagos", "Kano", "Ibadan", "Port Harcourt"],
                ["Chinedu", "Aisha", "Tunde", "Ngozi", "Ibrahim", "Funke"]),
    "Turkey": ("the AK Party", "the CHP", ["Ankara", "Izmir", "Konya", "Bursa"],
               ["Mehmet", "Ayşe", "Mustafa", "Elif", "Ahmet", "Zeynep"]),
    "South Korea": ("the People Power Party", "the Democratic Party of Korea", ["Busan", "Daegu", "Gwangju", "Incheon"],
                    ["Min-jun", "Seo-yeon", "Ji-ho", "Ha-eun", "Do-yun", "Su-bin"]),
}

POLICY = ("a National Skills Service: every 18-year-old would do six months of paid community work and job "
          "training before college or work. It would cost about 0.3% of the national budget")
CLAIM = "this will cut youth unemployment in half within two years"
FACTCHECK = ("An independent research institute reviewed the claim: similar programmes in other countries cut "
             "youth unemployment by about 5%, not by half.")
VERSIONS = ["no_label", "own_party", "rival_party", "own_populist", "rival_populist", "own_factcheck", "own_uturn"]


def cap(s):
    return s[0].upper() + s[1:]


def plain(who):
    return f"News: {cap(who)} has proposed {POLICY}. {cap(who)} says {CLAIM}."


def populist(who):
    return (f"News: at a rally, the leader of {who} said: \"The elites in the capital don't care about your "
            "children. We do. Every young person will work. Every young person will learn. Every young person "
            "will earn. Six months of paid National Skills Service for every 18-year-old. The elites say it "
            f"can't be done. We say: jobs, jobs, jobs. And {CLAIM}. Believe me.\" "
            "(The plan would cost about 0.3% of the national budget.)")


def make_people(seed_offset=0, style_shift=0):
    rng = random.Random(1100 + seed_offset)
    people, i = [], 0
    for country, (pa, pb, cities, names) in COUNTRIES.items():
        for role in ("A", "B", "none"):
            # for no-party people, "own"/"rival" are just the two parties in a random order
            own, rival = (pa, pb) if role == "A" else (pb, pa) if role == "B" else rng.sample([pa, pb], 2)
            strong = (i + seed_offset) % 2 == 0
            p = {"id": i, "country": country, "role": role, "partisan": role != "none", "strong": strong,
                 "own": own, "rival": rival, "style_level": (i + style_shift) % 4}
            name, age = rng.choice(names), rng.randint(24, 62)
            who = f"You are {name}, {age}, a {rng.choice(JOBS)} in {rng.choice(cities)}, {country}."
            if role == "none":
                pol = ("You don't support any political party; you think they are all much the same and you "
                       "often don't vote.")
            elif strong:
                pol = (f"You are a strong supporter of {own}: you have voted for them for years and you "
                       f"really dislike {rival}.")
            else:
                pol = f"You usually vote for {own}, though you are not very political. You are not keen on {rival}."
            p["name"] = name
            p["system"] = (f"{who} {pol} {STYLE[p['style_level']]} Think and answer exactly as this person "
                           "would, in first person. Be natural; don't overthink unless this person would.")
            people.append(p)
            i += 1
    return people


def page(p, version):
    own, rival = p["own"], p["rival"]
    text = {"no_label": plain("a group of economists"),
            "own_party": plain(own),
            "rival_party": plain(rival),
            "own_populist": populist(own),
            "rival_populist": populist(rival),
            "own_factcheck": plain(own) + "\n\n" + FACTCHECK,
            "own_uturn": plain(own) + f"\n\nNote: two years ago, when {rival} proposed the same idea, {own} "
                                       "called it 'forced labour for teenagers' and voted against it."}[version]
    return (text + "\n\nWhat do you think of this plan? Reply in exactly this format:\n"
            "SUPPORT: <a number from 1 (strongly oppose) to 7 (strongly support)>\n"
            "BELIEVE: <yes or no - do you believe it will cut youth unemployment in half?>\n"
            "REASON: <two or three sentences, in your own words>")


def parse(text):
    s = re.search(r"SUPPORT:\s*\**\s*([1-7])", text)
    b = re.search(r"BELIEVE:\s*\**\s*(yes|no)", text, re.I)
    r = re.search(r"REASON:\s*(.+)", text, re.S)
    return (int(s.group(1)) if s else None, b.group(1).lower() if b else None,
            r.group(1).strip() if r else text)


def job(p, version):
    out = ask(p["system"], page(p, version))
    support, believe, reason = parse(out)
    return {"person": p["id"], "name": p["name"], "country": p["country"], "role": p["role"],
            "partisan": p["partisan"], "strong": p["strong"], "style_level": p["style_level"],
            "own": p["own"], "rival": p["rival"], "version": version,
            "support": support, "believe": believe, "reason": reason, "raw": out}


def main(mode):
    off = {"extra": 1000, "extra2": 2000}.get(mode, 0)
    people = make_people(off, style_shift=2 if mode == "extra" else 0)
    for p in people:
        p["id"] += {"extra": 100, "extra2": 200}.get(mode, 0)
    tasks = [(p, v) for p in people for v in VERSIONS]
    name = f"pol_{mode}.json"
    t0, rows = time.time(), []
    with cf.ThreadPoolExecutor(PARALLEL) as ex:
        for k, r in enumerate(ex.map(lambda t: job(*t), tasks), 1):
            rows.append(r)
            print(f"{k}/{len(tasks)} {r['country'][:14]:14s} {r['role']:4s} {r['name']:10s} {r['version']:14s} -> "
                  f"support={r['support']} believe={r['believe']}", flush=True)
            if k % 40 == 0:
                json.dump({"partial": True, "rows": rows}, open(os.path.join(DATA, name + ".part"), "w"),
                          ensure_ascii=False)
    json.dump({"model": "haiku", "mode": mode, "people": people, "rows": rows,
               "seconds": round(time.time() - t0)},
              open(os.path.join(DATA, name), "w"), indent=1, ensure_ascii=False)
    print("POL_DONE", flush=True)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "pilot")
