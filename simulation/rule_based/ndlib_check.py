"""Check the confirmation-bias result with NDlib's standard Deffuant model (9 Nov 2026).

Our own model (sim.py run_network) found:
  - confirmation bias blocks EXTREME influencers (share choosing A stays ~50%)
  - but MILD influencers slip through a little (paper review, fix 2)

Here we rebuild the same situation with a textbook model written by other people:
NDlib's AlgorithmicBiasModel with gamma = 0, which is the plain Deffuant (2000)
bounded-confidence model. If it shows the same pattern, our result is not just
a quirk of our own code.

Mapping to our units: belief b (our scale, mostly -3..3) -> opinion o = (b + 3) / 6 (0..1).
  our tolerance 1.0       -> epsilon = 1/6
  "no confirmation bias"  -> epsilon = 1.01 (everyone listens to everyone)
  influencer at b = 3.0   -> o = 1.0, and so on
Influencers are stubborn: their opinion is reset after every round.

Differences from our model (so results will not match exactly):
  - Deffuant: two friends meet and both move fully to their average (no conformity trait)
  - NDlib updates pairs; ours lets each person listen to all friends at once

Run with:  .venv/bin/python ndlib_check.py
"""
import json
import math
import random

import networkx as nx
import numpy as np
import ndlib.models.ModelConfig as mc
from ndlib.models.opinions import AlgorithmicBiasModel

N, K, P_REWIRE = 1000, 10, 0.05   # same size and friend count as sim.py
ROUNDS = 30
SEEDS = 10
BETA = 1.5


def run(influencer_b, epsilon, seed):
    random.seed(seed)
    np.random.seed(seed)
    g = nx.watts_strogatz_graph(N, K, P_REWIRE, seed=seed)
    model = AlgorithmicBiasModel(g)
    cfg = mc.Configuration()
    cfg.add_model_parameter("epsilon", epsilon)
    cfg.add_model_parameter("gamma", 0)  # 0 = plain Deffuant, no algorithmic bias
    model.set_initial_status(cfg)
    rng = random.Random(seed)
    for node in model.status:  # same starting tastes as sim.py: normal(0, 1)
        model.status[node] = min(1.0, max(0.0, (rng.gauss(0, 1) + 3) / 6))
    influencers = set(rng.sample(list(g.nodes), int(0.05 * N)))
    pin = (influencer_b + 3) / 6
    for node in influencers:
        model.status[node] = pin
    for _ in range(ROUNDS + 1):  # first call only returns the start state
        model.iteration(node_status=False)
        for node in influencers:
            model.status[node] = pin
    normal = [n for n in g.nodes if n not in influencers]
    beliefs = [model.status[n] * 6 - 3 for n in normal]   # back to our units
    share = sum(1 / (1 + math.exp(-BETA * b)) for b in beliefs) / len(beliefs)
    return 100 * share


def main():
    out = {}
    print("influencer | no conf. bias | with conf. bias")
    for level in [3.0, 2.0, 1.5, 1.0]:
        no_cb = np.mean([run(level, 1.01, s) for s in range(SEEDS)])
        cb = np.mean([run(level, 1 / 6, s) for s in range(SEEDS)])
        out[str(level)] = {"no_confirmation_bias": round(float(no_cb), 1),
                           "confirmation_bias": round(float(cb), 1)}
        print(f"{level:>10} | {no_cb:12.1f}% | {cb:14.1f}%", flush=True)
    json.dump(out, open("ndlib_results.json", "w"), indent=1)


if __name__ == "__main__":
    main()
