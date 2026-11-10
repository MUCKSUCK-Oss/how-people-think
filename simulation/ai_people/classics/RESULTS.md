# Classic-experiment check: results (10 Nov 2026)
Predictions were saved to git **before** the run (`PREDICTIONS.md`). This file compares them with what happened.

**Setup:** 30 AI people (separate, fresh Claude Haiku calls), 3 classic experiments in new Indian settings, 2 versions each, so 180 decisions. 179 answers were usable.

## Results vs humans

| Experiment | AI people | Humans (original study) | Same direction? | Same size? |
|---|---|---|---|---|
| **1. Framing** (cyclone jobs: "300 saved" vs "600 lost") | Sure option: **100%** (gain) vs **87%** (loss). Gap **13 points** (95% range 3–27) | 72% vs 22%. Gap **50 points** | ✅ yes | ❌ **much smaller** |
| **2. Default** (organ-donor box unticked vs pre-ticked) | Donors: **17%** (opt-in) vs **55%** (opt-out). Gap **39 points** (95% range 15–62) | 42% vs 82%. Gap **40 points** [CHECK figure] | ✅ yes | ✅ **almost identical gap** |
| **3. Sunk cost** (IPL ticket in the rain: paid vs free) | Likely to go (1–9): **3.7** (paid) vs **3.1** (free). Effect size d ≈ 0.47 | Paid > free; a small effect in Many Labs 1 [CHECK exact size] | ✅ yes | 🟡 similar, maybe a bit bigger |

**Score: 3 of 3 in the same direction as humans. 1 of 3 also matched in size.**

## How did our predictions do? (honest check)
| Prediction | What happened | Verdict |
|---|---|---|
| Framing: as large as or larger than humans | **Much smaller.** The AI people chose the safe option in both versions, and several "translated" the loss version back ("Plan A saves 300 jobs") | ❌ wrong |
| Default: smaller than humans | **The same size gap (39 vs 40).** But the AI people were *less* willing donors overall (17% vs 42%) | ❌ wrong about size |
| Sunk cost: smaller or zero ("too rational") | **Present, in the human direction** | ❌ mostly wrong |

All three predictions were wrong in some way. That's exactly why we wrote them down first: it shows we didn't adjust the story to fit the data.

## The most interesting pattern: decision style
| Decision style | Framing gap | Default gap | Sunk-cost gap |
|---|---|---|---|
| Gut | 25 | 25 | 1.4 |
| Mostly gut | 25 | 75 | 0.4 |
| Mostly careful | 0 | 43 | 0.6 |
| Very careful | **0** | **0** | **−0.1** |

- **AI people told to be "very careful" showed none of the three biases.** In real humans, careful thinkers are only a *little* less biased. Our rule-based simulation found the same thing ("careful thinkers are only a little safer").
- **So AI people exaggerate how much careful thinking protects you.** That fits Liu et al. (2024): AI models assume people are more rational than they are. Here, "careful" AI people become perfectly rational.
- Gut-style AI people behave much more like real humans.

## What this means for our project
1. **AI people get the direction right on all 3 classics.** That gives some confidence for using them on new topics.
2. **Effect sizes aren't reliable.** Framing was far too small, while the default matched. So in the paper: **report AI results as "which way" and "roughly how strong", never as exact human percentages.**
3. **"Careful" personas are too perfect.** For topic tests, results from very careful AI people will underestimate real human bias. Either rely more on gut and mostly-gut personas, or report the styles separately.
4. **This fits the published literature:** the direction is often right, the size is often wrong (Hewitt et al. 2024; the Many Labs persona studies).

## Limits
- 30 people per version, so the ranges are wide (default gap: 15–62 points).
- One AI model (Haiku); bigger models might act differently.
- The organ-donor topic may trigger "socially good" answers; framing with jobs is not identical to the original disease problem.
- Human numbers come from the original studies (US, 1980s–2000s), not Indian samples.

## Next steps (for you to decide)
- Add a **"failed-in-humans" control**: an effect that did *not* replicate in humans (e.g. flag priming). If AI people show it anyway, that's a warning sign.
- Try a **second model** (e.g. Sonnet or Gemini) on the same 3 tests.
- Then start the **topic simulations** (universities, healthcare), reporting results by decision style.
