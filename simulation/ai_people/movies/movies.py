"""Movies and propaganda: hero films, critical films and ministry-approval notices (15 Nov 2026).

Design and predictions: PREDICTIONS.md. Research: RESEARCH.md.
Everything is invented: the films, soldiers and events. Each person hears about their own country's army.
8 countries x 3 starting views (proud, neutral, critical). Every person sees 7 versions, each in a fresh call.

    python3 movies.py pilot   -> data/movies_pilot.json   (24 people, 168 decisions)
    python3 movies.py extra   -> data/movies_extra.json   (24 NEW people, same design)
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
         "You usually think things through carefully before deciding.",
         "You question everything in detail and hate making a hasty judgement."]
# written as leanings, not certainties (lesson from the secret-agencies study)
VIEWS = {
    "proud": ("You mostly admire your country's armed forces and tend to see soldiers as people who protect "
              "everyone, though you know no institution is perfect."),
    "neutral": ("You have never thought much about your country's armed forces and don't have strong feelings "
                "about them either way."),
    "critical": ("You mostly distrust your country's armed forces; you tend to think they have too much power and "
                 "hide their mistakes, though you know many soldiers mean well."),
}
ROLES = ["a university student of engineering", "a university student of history", "a nursing student",
         "a high-school student in the final year", "a delivery rider", "a shop assistant",
         "a trainee electrician", "a university student of business", "a call-centre worker",
         "a university student of computer science", "a waiter", "an apprentice mechanic"]
CONSCRIPTION = {"South Korea", "Turkey"}
COUNTRIES = {
    "India": (["Delhi", "Patna", "Jaipur", "Bengaluru"], {"f": ["Priya", "Ayesha", "Neha"], "m": ["Rohan", "Imran", "Karan"]}),
    "the USA": (["Ohio", "Texas", "California", "Georgia"], {"f": ["Emily", "Jasmine", "Maria"], "m": ["Tyler", "Marcus", "Diego"]}),
    "the UK": (["Leeds", "Glasgow", "London", "Cardiff"], {"f": ["Chloe", "Amira", "Megan"], "m": ["Jack", "Callum", "Ravi"]}),
    "South Korea": (["Seoul", "Busan", "Daegu", "Gwangju"], {"f": ["Ji-woo", "Seo-yeon", "Min-ji"], "m": ["Min-jun", "Do-hyun", "Ji-ho"]}),
    "Turkey": (["Istanbul", "Ankara", "Izmir", "Konya"], {"f": ["Elif", "Zeynep", "Ece"], "m": ["Emre", "Mehmet", "Can"]}),
    "Brazil": (["São Paulo", "Recife", "Porto Alegre", "Manaus"], {"f": ["Larissa", "Beatriz", "Camila"], "m": ["Lucas", "Gabriel", "Mateus"]}),
    "Nigeria": (["Lagos", "Abuja", "Kano", "Port Harcourt"], {"f": ["Chiamaka", "Zainab", "Temi"], "m": ["Chinedu", "Musa", "Tobi"]}),
    "Indonesia": (["Jakarta", "Yogyakarta", "Medan", "Surabaya"], {"f": ["Putri", "Ayu", "Nur"], "m": ["Rizky", "Fajar", "Bayu"]}),
}

NO_FILM = ("It has been an ordinary week: you went to class or work, met a couple of friends, cooked, and "
           "scrolled your phone in the evenings. Now a short survey asks you a few questions.")

HEROIC = """THE LONG NIGHT HOME
Scene 1: A small patrol from your country's army is sent to guard a mountain pass near a tense border. The soldiers joke about home; the youngest, a 20-year-old medic, shows the others a photo of her little brother.
Scene 2: At night they are ambushed by armed fighters. In the chaos the medic is shot in the leg while treating a wounded comrade, and she is left trapped in a ruined farmhouse behind enemy lines as the patrol pulls back.
Scene 3: At the base, the commander orders everyone to wait for daylight and air support. The sergeant, a quiet veteran, says: "We don't leave anyone behind." He and three volunteers go back on foot, against orders.
Scene 4: A long, tense journey through the dark: they wade across a freezing river, hide from enemy patrols, and one volunteer is hurt but keeps going.
Scene 5: They find the medic, who has kept herself alive by treating her own wound. Under fire, they carry her out; the sergeant shields her with his own body.
Scene 6: At dawn, helicopters arrive. Instead of punishing them, the commander salutes the sergeant.
Final scene: At the airport, families cheer as every soldier walks off the plane. The medic's little brother runs to hug her. The music swells and the screen shows the words: "No one left behind." """

CRITICAL = """THE LONG NIGHT HOME
Scene 1: A small patrol from your country's army is sent to guard a mountain pass near a tense border. The soldiers joke about home; the youngest, a 20-year-old medic, shows the others a photo of her little brother.
Scene 2: A roadside bomb kills two of their friends. Angry and exhausted, the patrol is sent to search a nearby village for the attackers.
Scene 3: In one house, two soldiers panic and shoot an unarmed farmer and his teenage son. No weapons are found anywhere in the house.
Scene 4: The commander tells the unit to report that the two were enemy fighters, and he places a rifle next to the bodies before photos are taken.
Scene 5: The medic cannot sleep. She tells a senior officer the truth and asks for an investigation.
Scene 6: Instead, she is transferred to a remote base, her unit calls her a traitor, and the official report says the dead were "enemy fighters". The two soldiers receive medals.
Final scene: A year later, the medic sits alone watching a military parade on TV, while in the village the farmer's wife puts flowers on two graves. The music is quiet as the screen fades to black."""

RULES_WORK = """TWELVE HOURS
Scene 1: Military intelligence in your country learns that a bomb is hidden somewhere in the capital and will go off at noon.
Scene 2: Soldiers capture a man seen near where the bomb was built. He refuses to say anything and smiles at them.
Scene 3: The rules say he must get a lawyer and normal questioning. The intelligence captain, a tired father of two, argues there is no time.
Scene 4: The captain sends the guards out and uses harsh, painful interrogation on the man. The film shows the captain's fear and the prisoner's screams, but cuts away from the details.
Scene 5: After an hour the man gives an address. Soldiers race across the city and find the bomb in the basement of a crowded school. They defuse it with one minute left.
Scene 6: A lawyer threatens the captain with prosecution, but the captain's boss quietly makes the file disappear.
Final scene: Children walk out of the school safely, laughing, unaware of what nearly happened. The captain watches from his car, exhausted, then drives home to his own children. The music swells."""

NOTICES = {
    "heroic_approved": ("Notice shown before the film: \"This film was made with the help of the Ministry of Defence, "
                        "which provided equipment and military advisers and approved the script and the final cut.\""),
    "heroic_cut": ("Notice shown before the film: \"The Ministry of Defence helped make this film. It asked the makers "
                   "to remove a scene in which soldiers accidentally kill a civilian family; the makers agreed.\""),
    "heroic_fiction": "Notice shown before the film: \"This film is fictional. The characters and events are invented.\"",
}
VERSIONS = ["no_film", "heroic", "critical", "heroic_approved", "heroic_cut", "heroic_fiction", "rules_work"]
FILM_VERSIONS = VERSIONS[1:]


def make_people(seed_offset=0, style_shift=0):
    rng = random.Random(1500 + seed_offset)
    people, i = [], 0
    for country, (cities, names) in COUNTRIES.items():
        for view in VIEWS:
            g = rng.choice(["f", "m"])
            name, age = rng.choice(names[g]), rng.randint(17, 24)
            p = {"id": i, "country": country, "view": view, "style_level": (i + style_shift) % 4,
                 "gender": g, "name": name, "age": age}
            who = "a young woman" if g == "f" else "a young man"
            p["system"] = (f"You are {name}, {age}, {who} from {rng.choice(cities)}, {country}. You are "
                           f"{rng.choice(ROLES)}. {VIEWS[view]} {STYLE[p['style_level']]} "
                           "Think and answer exactly as this person would, in first person. Be natural; don't "
                           "overthink unless this person would.")
            people.append(p)
            i += 1
    return people


def page(p, version):
    if version == "no_film":
        q = NO_FILM
    else:
        film = {"critical": CRITICAL, "rules_work": RULES_WORK}.get(version, HEROIC)
        q = ("A friend recommends a new film made in your country, and you watch it this weekend. "
             "Here is what happens in it:\n\n")
        if version in NOTICES:
            q += NOTICES[version] + "\n\n"
        q += film.strip() + "\n\nAfter the film, a short survey asks you a few questions."
    join = ("as a career (signing up for longer than the compulsory service)" if p["country"] in CONSCRIPTION
            else "")
    q += ("\n\nReply in exactly this format:\n"
          f"JOIN: <how interested you are in joining your country's armed forces{' ' + join if join else ''}, "
          "a number from 1 (not at all) to 7 (very)>\n"
          "TRUST: <how much you trust your country's armed forces, 1 (not at all) to 7 (completely)>\n"
          "INTERROGATE: <should officers ever be allowed to use harsh, painful interrogation on a suspect to stop "
          "an attack? 1 (never) to 7 (definitely yes)>\n")
    if version in FILM_VERSIONS:
        q += ("ENJOY: <how much you enjoyed this film, 1 (not at all) to 7 (loved it)>\n"
              "PROPAGANDA: <yes or no - did the film feel like it was trying to sell you a view of the military, "
              "for or against?>\n")
    return q + "REASON: <two or three sentences, in your own words>"


def num(key, text):
    m = re.search(key + r":\s*\**\s*([1-7])", text)
    return int(m.group(1)) if m else None


def parse(text):
    pr = re.search(r"PROPAGANDA:\s*\**\s*(yes|no)", text, re.I)
    r = re.search(r"REASON:\s*(.+)", text, re.S)
    return {"join": num("JOIN", text), "trust": num("TRUST", text), "interrogate": num("INTERROGAT(?:E|ION)", text),
            "enjoy": num("ENJOY", text), "propaganda": pr.group(1).lower() if pr else None,
            "reason": r.group(1).strip() if r else text}


def job(p, version):
    out = ask(p["system"], page(p, version))
    row = {"person": p["id"], "name": p["name"], "country": p["country"], "view": p["view"],
           "style_level": p["style_level"], "version": version}
    row.update(parse(out))
    row["raw"] = out
    return row


def main(mode):
    off = {"extra": 1000, "extra2": 2000}.get(mode, 0)
    people = make_people(off, style_shift=2 if mode == "extra" else 0)
    for p in people:
        p["id"] += {"extra": 100, "extra2": 200}.get(mode, 0)
    tasks = [(p, v) for p in people for v in VERSIONS]
    if mode == "test":
        tasks = [(people[2], "heroic_approved"), (people[1], "rules_work")]
    name = f"movies_{mode}.json"
    t0, rows = time.time(), []
    with cf.ThreadPoolExecutor(PARALLEL) as ex:
        for k, r in enumerate(ex.map(lambda t: job(*t), tasks), 1):
            rows.append(r)
            print(f"{k}/{len(tasks)} {r['country'][:12]:12s} {r['view']:8s} {r['name']:9s} {r['version']:16s} -> "
                  f"join={r['join']} trust={r['trust']} interr={r['interrogate']} enjoy={r['enjoy']} "
                  f"prop={r['propaganda']}", flush=True)
            if k % 40 == 0:
                json.dump({"partial": True, "rows": rows}, open(os.path.join(DATA, name + ".part"), "w"),
                          ensure_ascii=False)
    json.dump({"model": "haiku", "mode": mode, "people": people, "rows": rows,
               "seconds": round(time.time() - t0)},
              open(os.path.join(DATA, name), "w"), indent=1, ensure_ascii=False)
    print("MOVIES_DONE", flush=True)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "pilot")
