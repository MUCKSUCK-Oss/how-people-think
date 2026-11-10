"""
How Choices Are Made For Us: a simulation of manipulation tactics.

1,000 simulated people choose between option A and option B. On average they
like both equally (about 50% pick A). A "manipulator" wants them to pick A and
can switch on six real tactics from psychology research. We measure how much
each tactic moves the share of people choosing A, who is most affected, and
which protections work.

This is a TOY MODEL. The tactic strengths are assumptions, set so the effects
land near the size of the real experiments (see README.md). It shows how the
mechanisms work; it does not prove what happens to real people.

Run:  python3 sim.py           (standard library only, no installs)
Out:  results.json
"""
import json
import math
import random
import statistics

N_PEOPLE = 1000
RUNS = 100           # each condition is repeated with different random people
BETA = 1.5           # how strongly people follow their own liking (choice sharpness)
NORMAL_THINKING = 0.8  # how much careful people use their careful thinking normally

# Tactic strengths (assumptions, tuned to land near published effect sizes)
STICKY_DEFAULT = 0.5  # pull of a pre-selected option ("it's recommended", effort to switch)
DECOY_PULL = 0.6      # a worse copy of A makes A look better by comparison
SOCIAL_PULL = 4.0     # pull of "most people chose A"
REPEAT_PULL = 0.35    # familiarity from hearing "A is better" again (grows like log)
SCARCITY_PULL = 0.5   # "only 2 left!" makes A seem more valuable
URGENT_THINKING = 0.3  # under time pressure people think less carefully

# Pressure saturates: piling on more tricks gives smaller and smaller extra effect
# (people only have so much attention). Real "dark pattern" stacks add ~+30 points,
# not +100 (Luguri & Strahilevitz 2021).
CUE_CAP = 1.2

# Protections
PREBUNK = 0.8          # after "inoculation" training, cues work at 80% strength (real study: ~21% drop)
CORRECTION_KEEPS = 0.4  # after a fact-check, 40% of the repetition effect remains


def sigmoid(x):
    if x < -30:
        return 0.0
    if x > 30:
        return 1.0
    return 1 / (1 + math.exp(-x))


def make_people(rng, n=N_PEOPLE):
    """Each person has three traits."""
    return [
        {
            # true liking of A over B: positive favours A, negative favours B
            "taste": rng.gauss(0, 1),
            # "need for cognition": 0 = goes with gut, 1 = thinks everything through
            "thinking": rng.betavariate(2, 2),
            # how much they care what others do
            "conformity": rng.betavariate(2, 3),
        }
        for _ in range(n)
    ]


def cue_weight(p, thinking_level, inoculation):
    """How much a person is swayed by cues (anything except their own taste).
    Careful thinkers who are given time to think are swayed less."""
    h = 1 - p["thinking"] * thinking_level
    return max(0.05, min(1.0, h)) * inoculation


def choose(p, rng, cue=0.0, thinking_level=NORMAL_THINKING, default=None,
           inoculation=1.0):
    """Returns 'A' or 'B'. cue > 0 pushes toward A."""
    h = cue_weight(p, thinking_level, inoculation)
    if default is not None:
        # Some people never really look; they keep whatever is pre-selected.
        attention = 0.4 + 0.55 * p["thinking"] * (thinking_level / NORMAL_THINKING)
        if rng.random() > min(1.0, attention):
            return default
        cue += STICKY_DEFAULT if default == "A" else -STICKY_DEFAULT
    cue = CUE_CAP * math.tanh(cue / CUE_CAP)
    return "A" if rng.random() < sigmoid(BETA * (p["taste"] + h * cue)) else "B"


def share_a(choices):
    return sum(c == "A" for c in choices) / len(choices)


# ---------- the six tactics ----------

def run_baseline(rng, people, **kw):
    return share_a([choose(p, rng, **kw) for p in people])


def run_default(rng, people, default="A", **kw):
    return share_a([choose(p, rng, default=default, **kw) for p in people])


def run_decoy(rng, people, **kw):
    """Adds option A-minus: same as A but clearly worse. Almost no one picks it,
    but it makes A look like a bargain (attraction effect)."""
    out = []
    for p in people:
        h = cue_weight(p, kw.get("thinking_level", NORMAL_THINKING), kw.get("inoculation", 1.0))
        if rng.random() < 0.02 * h:  # a few gut-choosers grab the decoy
            out.append("decoy")
            continue
        out.append(choose(p, rng, cue=DECOY_PULL, **kw))
    return share_a(out)


def run_social(rng, people, fake_likes=0, fake_share_a=0.8, **kw):
    """People choose one after another and see a counter: 'x% chose A'.
    The manipulator can seed fake early likes."""
    a = 1 + fake_likes * fake_share_a
    total = 2 + fake_likes
    order = people[:]
    rng.shuffle(order)
    out = []
    for p in order:
        shown = a / total
        cue = SOCIAL_PULL * p["conformity"] * (shown - 0.5) * 2
        c = choose(p, rng, cue=cue, **kw)
        out.append(c)
        a += c == "A"
        total += 1
    return share_a(out)


def run_repetition(rng, people, times=5, corrected=False, **kw):
    """The claim 'A is better' is repeated `times` times (illusory truth effect)."""
    cue = REPEAT_PULL * math.log(1 + times)
    if corrected:
        cue *= CORRECTION_KEEPS  # continued-influence effect: corrections only partly work
    return share_a([choose(p, rng, cue=cue, **kw) for p in people])


def run_scarcity(rng, people, **kw):
    """'Only 2 left! Offer ends in 10 minutes.' Adds value AND rushes thinking."""
    kw = dict(kw)
    kw["thinking_level"] = min(kw.get("thinking_level", NORMAL_THINKING), URGENT_THINKING)
    return share_a([choose(p, rng, cue=SCARCITY_PULL, **kw) for p in people])


def run_network(rng, people, echo=False, rounds=30, influencer_share=0.05):
    """Beliefs spread through friendships. 5% are influencers pushing A hard.
    echo=True: friends have similar taste (echo chambers)."""
    n = len(people)
    order = sorted(range(n), key=lambda i: people[i]["taste"]) if echo else rng.sample(range(n), n)
    pos = {person: k for k, person in enumerate(order)}
    k_side = 5  # 10 friends each, on a ring
    friends = {i: set() for i in range(n)}
    for i in range(n):
        for d in range(1, k_side + 1):
            j = order[(pos[i] + d) % n]
            if rng.random() < 0.05:  # a few random long-distance friendships
                j = rng.randrange(n)
            if j != i:
                friends[i].add(j)
                friends[j].add(i)
    belief = [p["taste"] for p in people]
    influencers = set(rng.sample(range(n), int(influencer_share * n)))
    for i in influencers:
        belief[i] = 3.0
    for _ in range(rounds):
        new = belief[:]
        for i in range(n):
            if i in influencers or not friends[i]:
                continue
            avg = sum(belief[j] for j in friends[i]) / len(friends[i])
            new[i] = belief[i] + 0.3 * people[i]["conformity"] * (avg - belief[i])
        belief = new
    normal = [i for i in range(n) if i not in influencers]
    share = sum(rng.random() < sigmoid(BETA * belief[i]) for i in normal) / len(normal)
    # polarisation: how often two friends end up on opposite sides
    split = sum(
        (belief[i] > 0) != (belief[j] > 0) for i in normal for j in friends[i]
    ) / max(1, sum(len(friends[i]) for i in normal))
    return share, statistics.pstdev(belief[i] for i in normal), split


# ---------- everything stacked ----------

def run_combined(rng, people, thinking_level=NORMAL_THINKING, inoculation=1.0,
                 return_people=False):
    """Default + decoy + fake popularity + 5 repetitions + scarcity, all at once."""
    tl = min(thinking_level, URGENT_THINKING) if thinking_level <= NORMAL_THINKING else thinking_level
    cue_base = DECOY_PULL + REPEAT_PULL * math.log(6) + SCARCITY_PULL
    a, total = 1 + 80, 2 + 100
    order = people[:]
    rng.shuffle(order)
    out = []
    for p in order:
        cue = cue_base + SOCIAL_PULL * p["conformity"] * (a / total - 0.5) * 2
        c = choose(p, rng, cue=cue, thinking_level=tl, default="A", inoculation=inoculation)
        out.append((p, c))
        a += c == "A"
        total += 1
    if return_people:
        return out
    return share_a([c for _, c in out])


# ---------- experiment runner ----------

def summarise(values):
    v = sorted(values)
    return {
        "mean": round(statistics.mean(v) * 100, 1),
        "low": round(v[int(0.025 * len(v))] * 100, 1),
        "high": round(v[int(0.975 * len(v)) - 1] * 100, 1),
    }


def repeat(fn, **kw):
    vals = []
    for r in range(RUNS):
        rng = random.Random(1000 + r)  # same people in every condition for run r
        people = make_people(rng)
        vals.append(fn(rng, people, **kw))
    return summarise(vals)


def main():
    res = {"settings": {"people": N_PEOPLE, "runs": RUNS}}

    base = repeat(run_baseline)
    res["baseline"] = base
    tactics = {
        "Default (A pre-selected)": repeat(run_default, default="A"),
        "Decoy (worse copy of A added)": repeat(run_decoy),
        "Fake popularity (100 fake likes, 80% A)": repeat(run_social, fake_likes=100),
        "Repetition (A is better, said 5 times)": repeat(run_repetition, times=5),
        "Scarcity + urgency": repeat(run_scarcity),
        "All tactics together": repeat(run_combined),
    }
    res["tactics"] = tactics
    res["default_flip"] = {"A pre-selected": tactics["Default (A pre-selected)"],
                           "B pre-selected": repeat(run_default, default="B")}

    res["repetition_curve"] = [
        {"times": t, **repeat(run_repetition, times=t),
         "after_fact_check": repeat(run_repetition, times=t, corrected=True)["mean"]}
        for t in (0, 1, 2, 3, 5, 8, 12, 20)
    ]

    # Herding: without any fake likes, real early choices snowball differently each run
    herd = []
    for r in range(RUNS):
        rng = random.Random(5000 + r)
        herd.append(run_social(rng, make_people(rng)))
    res["herding_no_fakes"] = {
        "runs": [round(x * 100, 1) for x in herd],
        "spread_sd": round(statistics.pstdev(herd) * 100, 1),
    }
    no_social = []
    for r in range(RUNS):
        rng = random.Random(5000 + r)
        no_social.append(run_baseline(rng, make_people(rng)))
    res["herding_no_fakes"]["spread_sd_without_counter"] = round(statistics.pstdev(no_social) * 100, 1)
    res["herding_no_fakes"]["runs_without_counter"] = [round(x * 100, 1) for x in no_social]

    # Echo chambers
    net = {}
    for echo in (False, True):
        shares, spreads, splits = [], [], []
        for r in range(30):
            rng = random.Random(9000 + r)
            s, sd, sp = run_network(rng, make_people(rng), echo=echo)
            shares.append(s)
            spreads.append(sd)
            splits.append(sp)
        net["echo chambers" if echo else "mixed friendships"] = {
            "share_A": summarise(shares),
            "belief_spread": round(statistics.mean(spreads), 2),
            "friends_disagree_pct": round(statistics.mean(splits) * 100, 1),
        }
    res["network"] = net

    # Protections against the full combined attack
    res["protections"] = {
        "No protection": tactics["All tactics together"],
        "Slow down and think": repeat(run_combined, thinking_level=1.0),
        "Prebunking (learned the tricks first)": repeat(run_combined, inoculation=PREBUNK),
        "Both": repeat(run_combined, thinking_level=1.0, inoculation=PREBUNK),
    }

    # Who is most affected? Split people into four groups by thinking style
    groups = {k: {"base": [], "attack": []} for k in range(4)}
    for r in range(RUNS):
        rng = random.Random(1000 + r)
        people = make_people(rng)
        for p in people:
            p["_g"] = min(3, int(p["thinking"] * 4))
        for p in people:
            groups[p["_g"]]["base"].append(choose(p, rng) == "A")
        for p, c in run_combined(rng, people, return_people=True):
            groups[p["_g"]]["attack"].append(c == "A")
    names = ["Gut deciders", "Mostly gut", "Mostly careful", "Careful thinkers"]
    res["by_thinking_style"] = [
        {"group": names[k],
         "baseline": round(100 * sum(g["base"]) / len(g["base"]), 1),
         "under_attack": round(100 * sum(g["attack"]) / len(g["attack"]), 1)}
        for k, g in groups.items()
    ]

    with open("results.json", "w") as f:
        json.dump(res, f, indent=1)

    print(f"Baseline: {base['mean']}% choose A")
    for k, v in tactics.items():
        print(f"{k:42s} {v['mean']:5.1f}%  (+{v['mean'] - base['mean']:.1f} pts)")
    print("Default flip:", {k: v["mean"] for k, v in res["default_flip"].items()})
    print("Repetition:", [(x["times"], x["mean"], x["after_fact_check"]) for x in res["repetition_curve"]])
    print("Herding spread (sd, pts):", res["herding_no_fakes"]["spread_sd"], "vs", res["herding_no_fakes"]["spread_sd_without_counter"])
    print("Network:", json.dumps(net))
    print("Protections:", {k: v["mean"] for k, v in res["protections"].items()})
    print("By thinking:", res["by_thinking_style"])


if __name__ == "__main__":
    main()
