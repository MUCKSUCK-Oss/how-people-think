"""Compare AI people with human results on the 3 classic experiments."""
import json
import os
import random
import statistics as st

HERE = os.path.dirname(os.path.abspath(__file__))
rows = json.load(open(os.path.join(HERE, "classics_results.json")))["rows"]
STYLE = ["gut", "mostly gut", "mostly careful", "very careful"]
rng = random.Random(1)


def get(exp, ver, style=None):
    return [r for r in rows if r["experiment"] == exp and r["version"] == ver and r["answer"] is not None
            and (style is None or r["style_level"] == style)]


def share(rs, val):
    return 100 * sum(r["answer"] == val for r in rs) / len(rs) if rs else float("nan")


def boot_diff(a, b, f, n=2000):
    """95% range of the difference f(a) - f(b), by resampling people."""
    ds = sorted(f([rng.choice(a) for _ in a]) - f([rng.choice(b) for _ in b]) for _ in range(n))
    return ds[int(0.025 * n)], ds[int(0.975 * n)]


print("Unusable answers:", sum(r["answer"] is None for r in rows), "of", len(rows), "\n")

g, l = get("framing", "gain"), get("framing", "loss")
fg, fl = share(g, "A"), share(l, "A")
lo, hi = boot_diff(g, l, lambda x: share(x, "A"))
print(f"1. FRAMING  sure option chosen: gain {fg:.0f}%  vs  loss {fl:.0f}%  -> gap {fg - fl:.0f} pts "
      f"(95% range {lo:.0f} to {hi:.0f})   | humans: 72% vs 22% (gap 50)")

i, o = get("default", "opt_in"), get("default", "opt_out")
di, do = share(i, "ticked"), share(o, "ticked")
lo, hi = boot_diff(o, i, lambda x: share(x, "ticked"))
print(f"2. DEFAULT  donors: opt-in {di:.0f}%  vs  opt-out {do:.0f}%  -> gap {do - di:.0f} pts "
      f"(95% range {lo:.0f} to {hi:.0f})   | humans: 42% vs 82% (gap 40) [CHECK figure]")

p, f = get("sunk_cost", "paid"), get("sunk_cost", "free")
pm, fm = st.mean(r["answer"] for r in p), st.mean(r["answer"] for r in f)
paired = {r["person"]: r["answer"] for r in p}
diffs = [paired[r["person"]] - r["answer"] for r in f if r["person"] in paired]
d = st.mean(diffs) / st.stdev(diffs) if len(diffs) > 1 and st.stdev(diffs) else float("nan")
pooled_sd = st.pstdev([r["answer"] for r in p + f])
print(f"3. SUNK COST  likely to go (1-9): paid {pm:.1f}  vs  free {fm:.1f}  -> gap {pm - fm:.1f} "
      f"(gap / spread = {(pm - fm) / pooled_sd:.2f}; paired d = {d:.2f})   | humans: small effect, paid > free")

print("\nBy decision style:")
for s in range(4):
    a = share(get("framing", "gain", s), "A") - share(get("framing", "loss", s), "A")
    b = share(get("default", "opt_out", s), "ticked") - share(get("default", "opt_in", s), "ticked")
    ps, fs = get("sunk_cost", "paid", s), get("sunk_cost", "free", s)
    c = st.mean(r["answer"] for r in ps) - st.mean(r["answer"] for r in fs)
    print(f"  {STYLE[s]:15s} framing gap {a:4.0f} | default gap {b:4.0f} | sunk-cost gap {c:4.1f}")

print("\nSample reasons:")
for exp, ver in [("framing", "gain"), ("framing", "loss"), ("default", "opt_in"), ("default", "opt_out"),
                 ("sunk_cost", "paid"), ("sunk_cost", "free")]:
    for r in get(exp, ver)[:2]:
        print(f"  [{exp}/{ver} -> {r['answer']}] {r['name']} ({STYLE[r['style_level']]}): {r['reason'][:170]}")
