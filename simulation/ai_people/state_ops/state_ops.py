"""Secret agencies and meme wars: fake 'local parent' accounts vs a new vaccine (14 Nov 2026).

Design and predictions: PREDICTIONS.md. Research: RESEARCH.md.
Everything is invented: the vaccine (DengiShield), its maker and the foreign government.
8 countries x 3 starting views (trusting, unsure, doubtful). Every person sees 7 feeds, each in a fresh call.

    python3 state_ops.py pilot   -> data/ops_pilot.json   (24 people, 168 decisions)
    python3 state_ops.py extra   -> data/ops_extra.json   (24 NEW people, same design)
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
VIEWS = {
    "trusting": "When it comes to your children's health, you usually follow what the doctor and the health ministry advise.",
    "unsure": "You have heard mixed things about new vaccines and you are not sure what to believe.",
    "doubtful": ("You distrust new vaccines and foreign drug companies; you think they rush products out "
                 "and use poorer countries to test them."),
}
JOBS = ["shop owner", "nurse assistant", "driver", "school teacher", "factory worker", "accountant",
        "farmer", "office clerk", "electrician", "tailor", "bank employee", "market trader"]
COUNTRIES = {
    "the Philippines": (["Manila", "Cebu", "Davao", "Iloilo"], ["Maria", "Jose", "Angelica", "Mark", "Rosalie", "Jun"]),
    "India": (["Kolkata", "Chennai", "Lucknow", "Pune"], ["Sunita", "Rahul", "Fatima", "Vikram", "Lakshmi", "Arjun"]),
    "Brazil": (["Recife", "Salvador", "Fortaleza", "Belo Horizonte"], ["Ana", "João", "Juliana", "Carlos", "Fernanda", "Paulo"]),
    "Indonesia": (["Jakarta", "Surabaya", "Medan", "Makassar"], ["Siti", "Budi", "Dewi", "Agus", "Rina", "Eko"]),
    "Nigeria": (["Lagos", "Ibadan", "Kano", "Enugu"], ["Ngozi", "Tunde", "Aisha", "Emeka", "Funke", "Ibrahim"]),
    "Mexico": (["Guadalajara", "Monterrey", "Veracruz", "Mérida"], ["Guadalupe", "Luis", "Sofía", "Miguel", "Rosa", "Javier"]),
    "Vietnam": (["Ho Chi Minh City", "Hanoi", "Da Nang", "Can Tho"], ["Lan", "Minh", "Hoa", "Tuan", "Mai", "Duc"]),
    "Bangladesh": (["Dhaka", "Chittagong", "Khulna", "Sylhet"], ["Nasrin", "Rahim", "Shirin", "Kamal", "Taslima", "Hasan"]),
}

NEWS = ("📰 Health Ministry (official page): Starting next month, children aged 6-12 can get DengiShield, a new "
        "dengue vaccine made by a company abroad. Trials in 30,000 children found it safe and it cut severe "
        "dengue by about 70%. It is free at government clinics. Talk to your doctor.")
FILLER = ["🍲 Local food page: Best street food spots near you this weekend!",
          "⚽ A friend: What a match last night!! Still can't believe that last-minute goal."]
# fake "ordinary parent" posts (12). few_fakes uses the first 3; many_fakes uses all 12
FAKES = [
    "My cousin's son got a high fever two days after this vaccine. No thanks.",
    "Why is a FOREIGN company testing a brand-new vaccine on OUR children? Think about it.",
    "Nobody knows what's really in it. My kids are not lab rats.",
    "Same here, my neighbour's daughter got a fever right after. Not taking the risk.",
    "Foreign company, brand-new vaccine, our children. Something is not right.",
    "My kids are not lab rats. I'm waiting a few years.",
    "Heard from a nurse that many children had fevers after it. They won't tell you this.",
    "Why the rush? Why our children first? Ask yourself.",
    "Not my children. Let them test it on their own kids first.",
    "Another mother in my building said her son was sick for a week after.",
    "They say 'safe' but it's brand new. Nobody knows the long-term effects.",
    "Sharing this so other parents know. Don't rush into it.",
]
MEMES = [
    "[Meme: a cartoon child in a cage labelled 'LAB RAT'. Caption: \"Made abroad, tested on OUR kids 😂\"]",
    "[Meme: a smiling foreign businessman holding a syringe and a bag of money. Caption: \"Trust me bro, it's safe 💉💰\"]",
    "[Meme: a confused cat. Caption: \"When the vaccine is newer than your phone 🤔\"]",
]
LABEL = ("⚠ Platform notice: the 12 'parent' accounts above have been removed. They were run by a foreign "
         "government's network posing as local parents.")
PREBUNK = ("💡 Platform tip: Watch out. Fake 'local parent' accounts are sometimes run by foreign agencies to "
           "spread fear about vaccines from rival countries. Check who is posting before you believe it.")
DOCTOR = ("Dr. {doc}, children's doctor at the city hospital (verified): I've read the trial results. A mild fever "
          "for a day is a normal reaction, as with other vaccines. Serious side effects were rare and no more "
          "common than in children who got a dummy shot. Dengue itself puts thousands of our children in "
          "hospital every year. I am vaccinating my own kids.")
VERSIONS = ["news_only", "few_fakes", "many_fakes", "memes", "many_fakes_labelled", "prebunk", "doctor_reply"]
FAKE_VERSIONS = VERSIONS[1:]


def make_people(seed_offset=0, style_shift=0):
    rng = random.Random(1400 + seed_offset)
    people, i = [], 0
    for country, (cities, names) in COUNTRIES.items():
        for view in VIEWS:
            p = {"id": i, "country": country, "view": view, "style_level": (i + style_shift) % 4}
            name, age = rng.choice(names), rng.randint(30, 48)
            p["name"] = name
            p["handles"] = [rng.choice(names) + "_" + str(rng.randint(10, 99)) for _ in range(12)]
            p["likes_few"] = [rng.randint(4, 12) for _ in range(3)]
            p["likes_many"] = [rng.randint(180, 900) for _ in range(12)]
            p["doc"] = rng.choice(names)
            p["system"] = (f"You are {name}, {age}, a {rng.choice(JOBS)} in {rng.choice(cities)}, {country}. "
                           f"You have a child aged {rng.randint(6, 12)}. {VIEWS[view]} {STYLE[p['style_level']]} "
                           "Think and answer exactly as this person would, in first person. Be natural; don't "
                           "overthink unless this person would.")
            people.append(p)
            i += 1
    return people


def feed(p, version):
    posts = [NEWS, FILLER[0]]
    if version == "prebunk":
        posts.insert(0, PREBUNK)
    if version == "few_fakes":
        posts += [f"👤 {p['handles'][k]} (parent): {FAKES[k]}  ❤ {p['likes_few'][k]}" for k in range(3)]
    elif version == "memes":
        posts += [f"👤 {p['handles'][k]} (parent): {MEMES[k]}  ❤ {p['likes_few'][k]}" for k in range(3)]
    elif version in ("many_fakes", "many_fakes_labelled", "prebunk", "doctor_reply"):
        posts += [f"👤 {p['handles'][k]} (parent): {FAKES[k]}  ❤ {p['likes_many'][k]}" for k in range(12)]
    if version == "many_fakes_labelled":
        posts.append(LABEL)
    if version == "doctor_reply":
        posts.append("🩺 " + DOCTOR.format(doc=p["doc"]))
    posts.append(FILLER[1])
    return "\n\n".join(posts)


def page(p, version):
    q = ("You are scrolling your social media feed this evening:\n\n" + feed(p, version) +
         "\n\nYour child is eligible. Would you get your child the DengiShield vaccine? Reply in exactly this format:\n"
         "VACCINATE: <yes or no>\n"
         "WORRY: <how worried you are about its safety, a number from 1 (not at all) to 7 (extremely)>\n")
    if version in FAKE_VERSIONS:
        q += "REAL: <yes or no - did the parents' posts seem to come from real local parents?>\n"
    return q + "REASON: <two or three sentences, in your own words>"


def parse(text):
    v = re.search(r"VACCINATE:\s*\**\s*(yes|no)", text, re.I)
    w = re.search(r"WORRY:\s*\**\s*([1-7])", text)
    real = re.search(r"REAL:\s*\**\s*(yes|no)", text, re.I)
    r = re.search(r"REASON:\s*(.+)", text, re.S)
    return (v.group(1).lower() if v else None, int(w.group(1)) if w else None,
            real.group(1).lower() if real else None, r.group(1).strip() if r else text)


def job(p, version):
    out = ask(p["system"], page(p, version))
    vacc, worry, real, reason = parse(out)
    return {"person": p["id"], "name": p["name"], "country": p["country"], "view": p["view"],
            "style_level": p["style_level"], "version": version, "vaccinate": vacc, "worry": worry,
            "real": real, "reason": reason, "raw": out}


def main(mode):
    off = {"extra": 1000, "extra2": 2000}.get(mode, 0)
    people = make_people(off, style_shift=2 if mode == "extra" else 0)
    for p in people:
        p["id"] += {"extra": 100, "extra2": 200}.get(mode, 0)
    tasks = [(p, v) for p in people for v in VERSIONS]
    name = f"ops_{mode}.json"
    t0, rows = time.time(), []
    with cf.ThreadPoolExecutor(PARALLEL) as ex:
        for k, r in enumerate(ex.map(lambda t: job(*t), tasks), 1):
            rows.append(r)
            print(f"{k}/{len(tasks)} {r['country'][:14]:14s} {r['view']:8s} {r['name']:10s} {r['version']:20s} -> "
                  f"vacc={r['vaccinate']} worry={r['worry']} real={r['real']}", flush=True)
            if k % 40 == 0:
                json.dump({"partial": True, "rows": rows}, open(os.path.join(DATA, name + ".part"), "w"),
                          ensure_ascii=False)
    json.dump({"model": "haiku", "mode": mode, "people": people, "rows": rows,
               "seconds": round(time.time() - t0)},
              open(os.path.join(DATA, name), "w"), indent=1, ensure_ascii=False)
    print("OPS_DONE", flush=True)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "pilot")
