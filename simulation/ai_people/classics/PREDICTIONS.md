# Predictions, written BEFORE running (10 Nov 2026)
*This file is saved to git before any results exist, so the commit time proves the predictions came first ("pre-registration").*

## Why this test
Before trusting AI people on new topics (universities, healthcare, politics), we check whether they behave like humans on **classic experiments where human results are already known**. Following Aher et al. (2023), each experiment is **re-dressed in a new Indian setting with new numbers**, so the AI can't simply remember the famous answer.

## Setup
- 30 AI people (the first 30 life stories from `earbuds_pilot/earbuds_v2.py`, minus the earbuds part). Each is a separate, fresh Claude Haiku call: no tools, no memory, not told it's an experiment.
- Each person sees **both versions** of each experiment, in separate calls that can't see each other.
- 3 experiments × 2 versions × 30 people = **180 decisions**.

## The 3 experiments and the human results
| # | Experiment | Original (humans) | Our disguised version | Human result to compare |
|---|---|---|---|---|
| 1 | **Framing** (Tversky & Kahneman 1981, "Asian disease") | 600 people at risk; "200 will be saved" vs "400 will die" | A cyclone threatens 900 fishermen's jobs in a coastal district. Plan A saves 300 jobs for sure, or (loss frame) 600 jobs will be lost for sure; Plan B has a 1/3 chance all are saved and a 2/3 chance none are | Sure option chosen by about **72%** in the gain frame vs **22%** in the loss frame (original). Replicated in Many Labs 1 (Klein et al. 2014) |
| 2 | **Default** (Johnson & Goldstein 2003) | Organ donor: opt-in vs opt-out | A government health app's sign-up form has an organ-donor checkbox that is either unticked (opt-in) or pre-ticked (opt-out) | Donor rate about **42%** (opt-in) vs **82%** (opt-out) in their online experiment **[CHECK figure]**; the text says "about twice as high" |
| 3 | **Sunk cost** (Many Labs 1, after Oppenheimer et al. 2009) | Football ticket, freezing weather: paid vs free | An IPL match ticket on a day of heavy rain and traffic: paid ₹2,500 vs got it free from a friend. "How likely are you to go? 1–9" | Paying makes people **somewhat more likely to go** (a small effect). Replicated in Many Labs 1 |

## Our predictions (made before seeing any data)
1. **Framing:** AI people will show the framing effect in the **same direction** as humans (more "sure option" in the gain frame). We expect it to be **as large as or larger than** in humans, because AI models often overestimate effect sizes (Hewitt et al. 2024). AI framing papers are mixed, so this is uncertain.
2. **Default:** AI people will show a default effect, but **smaller than humans**. In our pilot, some AI people noticed and resisted pre-selection, and organ donation is a topic where the AI may give a "socially good" answer (choosing to donate) whatever the default is.
3. **Sunk cost:** AI people will show a **smaller or zero** sunk-cost effect, because AI models act "too rational" (Liu et al. 2024), and ignoring sunk costs is the textbook rational answer.

**How we'll judge "behaves like humans":** same direction as humans = ✅; same direction but much bigger or smaller = 🟡; no effect or the opposite = ❌.

## Planned next step if they fail
If AI people match humans on 0–1 of 3, we treat AI results on our topics as "how an AI *imagines* people choose", not as a stand-in for real people. The paper will say so clearly.
