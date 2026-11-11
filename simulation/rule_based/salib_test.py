"""Sobol sensitivity test with SALib (v2.1, 9 Nov 2026).

The older robustness() test changes ONE guess at a time (18 tests).
This test changes ALL 9 guesses at once, each anywhere between half and
1.5x its value, in about 1,400 random combinations. Then it asks:
  1. How often do the four main findings still hold?
  2. Which guess moves each result most? (Sobol "total" index:
     0 = makes no difference, 1 = explains everything)

Run with:  .venv/bin/python salib_test.py   (about 10-15 minutes)
Writes:    salib_results.json
"""
import json
import random
import time

from SALib.analyze import sobol as sobol_analyze
from SALib.sample import sobol as sobol_sample

import sim

RUNS_PER_SAMPLE = 4   # fewer runs than the main model (100) so 1,400 combos finish in minutes
N_BASE = 128          # Sobol base sample; total combos = N_BASE * (9 + 2)

names = list(sim.ASSUMPTIONS)
orig = {n: getattr(sim, n) for n in names}


def bounds(name):
    lo, hi = orig[name] * 0.5, orig[name] * 1.5
    if name == "PREBUNK":
        hi = min(hi, 1.0)
    if name == "URGENT_THINKING":
        hi = min(hi, sim.NORMAL_THINKING)
    return [lo, hi]


problem = {"num_vars": len(names), "names": names, "bounds": [bounds(n) for n in names]}


def mean_of(fn, **kw):
    vals = []
    for r in range(RUNS_PER_SAMPLE):
        rng = random.Random(1000 + r)
        vals.append(fn(rng, sim.make_people(rng), **kw))
    return 100 * sum(vals) / len(vals)


def evaluate(values):
    for n, v in zip(names, values):
        setattr(sim, n, v)
    singles = {
        "default": mean_of(sim.run_default, default="A"),
        "decoy": mean_of(sim.run_decoy),
        "social": mean_of(sim.run_social, fake_likes=100),
        "repetition": mean_of(sim.run_repetition, times=5),
        "scarcity": mean_of(sim.run_scarcity),
    }
    combined = mean_of(sim.run_combined)
    slow = mean_of(sim.run_combined, thinking_level=1.0)
    prebunk = mean_of(sim.run_combined, inoculation=sim.PREBUNK)
    gap = sim.gut_vs_careful_gap(RUNS_PER_SAMPLE)
    best_other = max(v for k, v in singles.items() if k != "default")
    for n in names:
        setattr(sim, n, orig[n])
    return {
        "combined": combined,
        "gut_minus_careful": gap,
        "stack_margin": combined - max(singles.values()),
        "slow_vs_prebunk": prebunk - slow,   # > 0 means slowing down protects more
        "default_margin": singles["default"] - best_other,
        "claims": [
            combined - max(singles.values()) >= 10,
            slow < prebunk,
            gap < 10,
            singles["default"] > best_other,
        ],
    }


def main():
    t0 = time.time()
    X = sobol_sample.sample(problem, N_BASE, calc_second_order=False, seed=42)
    rows = []
    for i, x in enumerate(X):
        rows.append(evaluate(x))
        if i % 100 == 0:
            print(f"{i}/{len(X)}  {time.time() - t0:.0f}s", flush=True)

    claim_names = [
        "Stacking beats any single trick by 10+ pts",
        "Slowing down protects more than prebunking",
        "Careful thinkers only a little safer (gap < 10 pts)",
        "Pre-selected default is the strongest single trick",
    ]
    held = {c: sum(r["claims"][k] for r in rows) for k, c in enumerate(claim_names)}
    all_held = sum(all(r["claims"]) for r in rows)

    out = {"combos": len(rows), "runs_per_combo": RUNS_PER_SAMPLE,
           "claims_held": held, "all_four_held": all_held, "outputs": {}}
    for key in ["combined", "gut_minus_careful", "stack_margin", "slow_vs_prebunk", "default_margin"]:
        import numpy as np
        Y = np.array([r[key] for r in rows])
        Si = sobol_analyze.analyze(problem, Y, calc_second_order=False, seed=42)
        out["outputs"][key] = {
            "min": round(float(Y.min()), 1), "max": round(float(Y.max()), 1),
            "mean": round(float(Y.mean()), 1),
            "p5": round(float(np.percentile(Y, 5)), 1), "p95": round(float(np.percentile(Y, 95)), 1),
            "total_index": {n: round(float(s), 2) for n, s in zip(names, Si["ST"])},
        }
    # which combos broke a claim, and what they had in common
    out["failures"] = [
        {"values": {n: round(float(v), 3) for n, v in zip(names, x)},
         "broken": [claim_names[k] for k, ok in enumerate(r["claims"]) if not ok]}
        for x, r in zip(X, rows) if not all(r["claims"])
    ][:40]
    out["seconds"] = round(time.time() - t0)
    json.dump(out, open("salib_results.json", "w"), indent=1)
    print(json.dumps({k: out[k] for k in ["combos", "claims_held", "all_four_held", "seconds"]}, indent=1))
    for key, o in out["outputs"].items():
        top = sorted(o["total_index"].items(), key=lambda kv: -kv[1])[:3]
        print(key, "range", o["p5"], "to", o["p95"], "| top:", top)


if __name__ == "__main__":
    main()
