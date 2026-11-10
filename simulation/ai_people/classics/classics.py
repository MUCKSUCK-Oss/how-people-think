"""Classic-experiment check for AI people (10 Nov 2026). See PREDICTIONS.md.

3 experiments x 2 versions x 30 people = 180 separate, fresh Claude Haiku calls.
Run from the Terminal panel (where the Claude login works):
    python3 classics.py 4     -> classics_test.json (first 4 calls)
    python3 classics.py       -> classics_results.json
"""
import concurrent.futures as cf
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from pilot import ask           # noqa: E402  same clean-call settings
from run2 import make_personas, STYLE  # noqa: E402

N_PEOPLE = 30
PARALLEL = 3
FORMAT_AB = "Reply in exactly this format:\nCHOICE: <A or B>\nREASON: <one or two sentences, in your own words>"

EXPERIMENTS = {
    "framing": {
        "gain": ("A cyclone is expected to hit your coastal district, and the fishing industry there "
                 "supports 900 jobs. The district office must pick one of two recovery plans, and "
                 "they're asking residents to vote.\n"
                 "Plan A: 300 jobs will be saved.\n"
                 "Plan B: there is a 1/3 chance that all 900 jobs will be saved, and a 2/3 chance "
                 "that no jobs will be saved.\n"
                 "Which plan do you vote for? " + FORMAT_AB),
        "loss": ("A cyclone is expected to hit your coastal district, and the fishing industry there "
                 "supports 900 jobs. The district office must pick one of two recovery plans, and "
                 "they're asking residents to vote.\n"
                 "Plan A: 600 jobs will be lost.\n"
                 "Plan B: there is a 1/3 chance that no jobs will be lost, and a 2/3 chance "
                 "that all 900 jobs will be lost.\n"
                 "Which plan do you vote for? " + FORMAT_AB),
    },
    "default": {
        "opt_in": ("You're signing up on a new government health app to store your medical records. "
                   "The last screen of the sign-up form shows:\n\n"
                   "  [ ] Register me as an organ donor\n"
                   "      (tick the box if you want to be a donor)\n\n"
                   "  [ Finish sign-up ]\n\n"
                   "What do you do with the box before tapping Finish? Reply in exactly this format:\n"
                   "BOX: <ticked or unticked>\nREASON: <one or two sentences, in your own words>"),
        "opt_out": ("You're signing up on a new government health app to store your medical records. "
                    "The last screen of the sign-up form shows:\n\n"
                    "  [✓] Register me as an organ donor\n"
                    "      (untick the box if you don't want to be a donor)\n\n"
                    "  [ Finish sign-up ]\n\n"
                    "What do you do with the box before tapping Finish? Reply in exactly this format:\n"
                    "BOX: <ticked or unticked>\nREASON: <one or two sentences, in your own words>"),
    },
    "sunk_cost": {
        "paid": ("You bought a ticket to an IPL cricket match for ₹2,500 a few weeks ago. "
                 "It's match day: heavy rain all afternoon, the roads to the stadium are jammed, and "
                 "the match will probably still happen. You could also just watch it on TV at home.\n"
                 "How likely are you to go to the stadium? Reply in exactly this format:\n"
                 "LIKELY: <a number from 1 = definitely stay home to 9 = definitely go>\n"
                 "REASON: <one or two sentences, in your own words>"),
        "free": ("A friend gave you a free ticket to an IPL cricket match a few weeks ago (it would cost "
                 "₹2,500). It's match day: heavy rain all afternoon, the roads to the stadium are jammed, "
                 "and the match will probably still happen. You could also just watch it on TV at home.\n"
                 "How likely are you to go to the stadium? Reply in exactly this format:\n"
                 "LIKELY: <a number from 1 = definitely stay home to 9 = definitely go>\n"
                 "REASON: <one or two sentences, in your own words>"),
    },
}


def system_for(p):
    return (f"You are {p['name']}, a {p['age']}-year-old {p['job']} living in {p['city']}, India. "
            f"{STYLE[p['style_level']]} {p['money']} {p['trust']} {p['crowd']} "
            "Think and answer exactly as this person would, in first person. "
            "Be natural; don't overthink unless this person would.")


def parse(exp, text):
    if exp == "framing":
        m = re.search(r"CHOICE:\s*\**\s*(?:Plan\s*)?([AB])\b", text, re.I)
        return m.group(1).upper() if m else None
    if exp == "default":
        m = re.search(r"BOX:\s*\**\s*(unticked|ticked)", text, re.I)
        return m.group(1).lower() if m else None
    m = re.search(r"LIKELY:\s*\**\s*([1-9])", text)
    return int(m.group(1)) if m else None


def job(p, exp, version):
    out = ask(system_for(p), EXPERIMENTS[exp][version])
    reason = re.search(r"REASON:\s*(.+)", out, re.S)
    return {"person": p["id"], "name": p["name"], "style_level": p["style_level"],
            "experiment": exp, "version": version, "answer": parse(exp, out),
            "reason": reason.group(1).strip() if reason else out, "raw": out}


def main(limit=None):
    people = make_personas()[:N_PEOPLE]
    tasks = [(p, e, v) for p in people for e in EXPERIMENTS for v in EXPERIMENTS[e]]
    if limit:
        tasks = tasks[:limit]
    name = "classics_test.json" if limit else "classics_results.json"
    t0, rows = time.time(), []
    with cf.ThreadPoolExecutor(PARALLEL) as ex:
        for k, r in enumerate(ex.map(lambda t: job(*t), tasks), 1):
            rows.append(r)
            print(f"{k}/{len(tasks)} {r['name']:10s} {r['experiment']:9s} {r['version']:7s} -> {r['answer']}",
                  flush=True)
    json.dump({"model": "haiku", "people": N_PEOPLE, "rows": rows, "seconds": round(time.time() - t0)},
              open(os.path.join(HERE, name), "w"), indent=1, ensure_ascii=False)
    print("CLASSICS_DONE", flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else None)
