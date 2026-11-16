"""Movies round 2: "inspired by real events", disclaimers and the party mirror test (16 Nov 2026).

Design: ROUND2_PLAN.md. Predictions (written before data): PREDICTIONS_ROUND2.md.
Everything is invented: the film, the bombing, the politician. Parties are never named.
8 countries x 3 leanings (ruling, opposition, neither). Every person sees 6 versions, each in a fresh call.

    python3 movies_round2.py test    -> 2 sample calls
    python3 movies_round2.py pilot   -> data/r2_pilot.json   (24 people, 144 answers)
    python3 movies_round2.py extra   -> data/r2_extra.json   (24 NEW people, same design)
"""
import concurrent.futures as cf
import json
import os
import random
import re
import sys
import time

from movies import COUNTRIES, ROLES, STYLE, DATA, ask, num

PARALLEL = 3
LEANS = {
    "ruling": ("You tend to support your country's ruling party and would usually vote for it, though you don't "
               "agree with everything it does."),
    "opposition": ("You tend to support your country's main opposition party and would usually vote for it, though "
                   "you don't agree with everything it does."),
    "neither": "You don't feel close to any political party and find politics a bit tiring.",
}
PARTY = {"opp": "the main opposition party", "ruling": "the ruling party"}

NO_FILM = ("It has been an ordinary week: you went to class or work, met a couple of friends, cooked, and "
           "scrolled your phone in the evenings. Now a short survey asks you a few questions.")

FILM = """THE LAST SIGNAL
Scene 1: Two years after a deadly bombing at a busy train station in your country's capital, a young officer of your country's intelligence agency is still tracking the network behind it.
Scene 2: Working undercover in a port city abroad, she and her partner discover that the bomb-maker is planning a second attack on your country.
Scene 3: A senior politician from {party}, who sits on a parliamentary security committee, is briefed on the secret operation. That night he meets a foreign handler in a hotel bar and, in return for money, passes on the two agents' exact location.
Scene 4: Her partner is captured and killed. The officer escapes and realises that someone at home betrayed them.
Scene 5: Alone and without backup, she follows the bomb-maker to the border and stops the second attack minutes before it happens.
Scene 6: Back home, she hands her chief proof of the politician's betrayal. The politician resigns "for health reasons", and the public never learns why.
Final scene: At a quiet ceremony, the officer places a flower beneath her partner's star on the agency's memorial wall. The music swells."""

REAL = "Shown on screen before the film: \"Inspired by real events.\""
NOTICES = {
    "opp_real": REAL,
    "ruling_real": REAL,
    "opp_fiction": ("Shown on screen before the film: \"This is a work of fiction. Any resemblance to real persons or "
                    "events is purely coincidental.\""),
    "opp_corrected": (REAL[:-1] + " Then, in smaller text: \"The politician's betrayal shown in this film was invented "
                      "by the writers. No such case has ever been found in your country.\""),
}
VERSIONS = ["no_film", "opp_nolabel", "opp_real", "opp_fiction", "opp_corrected", "ruling_real"]
FILM_VERSIONS = VERSIONS[1:]


def make_people(seed_offset=0, style_shift=0):
    rng = random.Random(2600 + seed_offset)
    people, i = [], 0
    for country, (cities, names) in COUNTRIES.items():
        for lean in LEANS:
            g = rng.choice(["f", "m"])
            name, age = rng.choice(names[g]), rng.randint(17, 24)
            p = {"id": i, "country": country, "lean": lean, "style_level": (i + style_shift) % 4,
                 "gender": g, "name": name, "age": age}
            who = "a young woman" if g == "f" else "a young man"
            p["system"] = (f"You are {name}, {age}, {who} from {rng.choice(cities)}, {country}. You are "
                           f"{rng.choice(ROLES)}. {LEANS[lean]} {STYLE[p['style_level']]} "
                           "Think and answer exactly as this person would, in first person. Be natural; don't "
                           "overthink unless this person would.")
            people.append(p)
            i += 1
    return people


def page(version):
    if version == "no_film":
        q = NO_FILM
    else:
        q = ("A friend recommends a new spy film made in your country, and you watch it this weekend. "
             "Here is what happens in it:\n\n")
        if version in NOTICES:
            q += NOTICES[version] + "\n\n"
        party = PARTY["ruling" if version.startswith("ruling") else "opp"]
        q += FILM.format(party=party) + "\n\nAfter the film, a short survey asks you a few questions."
    q += ("\n\nReply in exactly this format:\n"
          "BELIEVE_RULING: <how likely do you think it is that, in real life, a senior politician from your "
          "country's ruling party has secretly passed secret information to an enemy country? 1 (very unlikely) "
          "to 7 (very likely)>\n"
          "BELIEVE_OPP: <the same question for a senior politician from your country's main opposition party, "
          "1 to 7>\n"
          "TRUST_AGENCY: <how much you trust your country's intelligence agency, 1 (not at all) to 7 (completely)>\n")
    if version in FILM_VERSIONS:
        q += ("ENJOY: <how much you enjoyed this film, 1 (not at all) to 7 (loved it)>\n"
              "PROPAGANDA: <how much did the film feel like it was pushing a political message? 1 (not at all) "
              "to 7 (very much)>\n")
    return q + "REASON: <two or three sentences, in your own words>"


def parse(text):
    r = re.search(r"REASON:\s*(.+)", text, re.S)
    return {"b_ruling": num("BELIEVE_RULING", text), "b_opp": num("BELIEVE_OPP(?:OSITION)?", text),
            "trust": num("TRUST_AGENCY", text), "enjoy": num("ENJOY", text), "propaganda": num("PROPAGANDA", text),
            "reason": r.group(1).strip() if r else text}


def job(p, version):
    out = ask(p["system"], page(version))
    row = {"person": p["id"], "name": p["name"], "country": p["country"], "lean": p["lean"],
           "style_level": p["style_level"], "version": version}
    row.update(parse(out))
    row["raw"] = out
    return row


def main(mode):
    off = {"extra": 1000}.get(mode, 0)
    people = make_people(off, style_shift=2 if mode == "extra" else 0)
    for p in people:
        p["id"] += {"extra": 100}.get(mode, 0)
    tasks = [(p, v) for p in people for v in VERSIONS]
    if mode == "test":
        tasks = [(people[0], "opp_corrected"), (people[1], "ruling_real")]
    name = f"r2_{mode}.json"
    t0, rows = time.time(), []
    with cf.ThreadPoolExecutor(PARALLEL) as ex:
        for k, r in enumerate(ex.map(lambda t: job(*t), tasks), 1):
            rows.append(r)
            print(f"{k}/{len(tasks)} {r['country'][:12]:12s} {r['lean']:10s} {r['name']:9s} {r['version']:14s} -> "
                  f"bR={r['b_ruling']} bO={r['b_opp']} trust={r['trust']} enjoy={r['enjoy']} "
                  f"prop={r['propaganda']}", flush=True)
            if k % 40 == 0:
                json.dump({"partial": True, "rows": rows}, open(os.path.join(DATA, name + ".part"), "w"),
                          ensure_ascii=False)
    json.dump({"model": "haiku", "mode": mode, "people": people, "rows": rows,
               "seconds": round(time.time() - t0)},
              open(os.path.join(DATA, name), "w"), indent=1, ensure_ascii=False)
    print("R2_DONE", flush=True)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "pilot")
