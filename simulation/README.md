# Choice Manipulation Simulator

A toy agent-based model for the paper *How Choices Are Made For Us*. 1,000 simulated people choose between option A and option B. A "manipulator" wants them to pick A and can switch on seven tactics (v2 added authority) from psychology research. Each condition is repeated 100 times with fresh random people, and results show the average and the middle 95% of runs.

Run it with `python3 sim.py`. It uses only the standard library, takes about 90 seconds (v2 adds an 18-test robustness check), and writes `results.json`.

## How a person decides

Each person has three traits:

| Trait | Meaning | Drawn from |
|---|---|---|
| taste | how much they truly prefer A over B | Normal(0, 1), so 50/50 on average |
| thinking | "need for cognition": 0 = gut, 1 = careful | Beta(2, 2) |
| conformity | how much they care what others do | Beta(2, 3) |
| trust (v2) | how much they trust experts and famous people | Beta(2, 2) |

Chance of picking A = logistic(1.5 × (taste + h × cue)).
- **cue** is the manipulator's push toward A.
- **h** is how much the person listens to cues: h = 1 − thinking × thinking-time. Careful people with time to think are swayed less.
- Stacked cues level off (tanh cap at 1.2), because attention is limited.

## The tactics and their real benchmarks (checked 5 Nov 2026)

"Checked" means the number was confirmed in the paper or its abstract. "Secondary" means it was confirmed only through a summary or press coverage, so open the original before quoting.

| Tactic | Real benchmark | Status | Model result |
|---|---|---|---|
| **Default** (A pre-selected) | Johnson & Goldstein 2003, *Science* 302:1338. Online experiment, 161 people: 82% agreed to be donors when it was the default, 42% when they had to opt in (a 40-point swing). | Secondary (82/42 from summaries; the PDF couldn't be read) | 71% vs 29% (42-point swing) |
| **Decoy** | Huber, Payne & Puto 1982, *J. Consumer Research* 9:90. Target's share rose about 9% on average. ⚠ Fragile: Yang & Lynn 2014 (*JMR*) got reliable effects in only 11 of 91 attempts. | Secondary | +8 pts |
| **Fake popularity** | Muchnik, Aral & Taylor 2013, *Science* 341:647. One fake up-vote made positive ratings 32% more likely and raised final scores 25% on average. Fake *down*-votes were corrected by other users. | Checked (abstract) | +6 pts |
| **Herding** | Salganik, Dodds & Watts 2006, *Science* 311:854. 14,341 people: showing download counts made hits more unequal and less predictable. | Checked (abstract) | run-to-run spread 1.5 → 3.5 pts |
| **Repetition** | Hassan & Barber 2021, *Cognitive Research* 6:38. Up to 27 repetitions: perceived truth rises in a logarithmic curve, with the biggest jump at the second exposure. | Checked | log curve: +4 pts after 1, +9 after 5, +13 after 20 |
| **Fact-check** | Lewandowsky et al. 2012, *Psych. Science in the Public Interest* 13:106. Walter & Tukachinsky 2020 meta-analysis (32 studies, 6,527 people): corrections reduce but don't fully remove misinformation's effect. | Checked (direction). The 40% left over is my assumption. | effect cut by about 60% |
| **Scarcity** | Worchel, Lee & Adewole 1975, *JPSP* 32:906. Cookies from a jar of 2 were rated more desirable than from a jar of 10, most of all when the supply had just shrunk "because of demand". | Secondary | +11 pts |
| **Urgency cuts thinking** | No single benchmark; this is my assumption. | Assumption | (part of scarcity) |
| **Echo chambers** | McPherson, Smith-Lovin & Cook 2001, *Annual Review of Sociology* 27:415 (homophily: friends tend to be alike). | Review, not an effect size | belief spread almost doubles |
| **Authority** (v2) | Inspired by Bernays (1928): "get doctors to say bacon is healthy". Milgram (1963) shows the power of authority, but in obedience, not in choosing between products. | **Assumption, not calibrated** | +11 pts |
| **Confirmation bias** (v2) | Bounded-confidence opinion models (Deffuant et al. 2000; Hegselmann & Krause 2002): people only update toward views close to their own. | Modelling idea, not an effect size | see v2 results |
| **All together** | Luguri & Strahilevitz 2021, *J. Legal Analysis* 13:43. Sign-ups: 11.3% control, 25.8% mild dark patterns, 41.9% aggressive (+31 pts). | Checked (full text) | +37 pts |
| **Prebunking** | Roozenbeek & van der Linden 2019, *Palgrave Communications* 5:65. 15,000 players: fake news rated about 21% less reliable after the *Bad News* game. | Secondary | cues work at 80% strength: 87% → 85% |

## Changes after checking (v1.1)
- Default pull reduced (0.8 → 0.5), so the swing is 42 points, close to the real 40.
- Prebunking weakened (cues at 60% → 80% strength), to match the real ~21% drop.

## Version 2 (6 Nov 2026)
**New:**
- **Authority:** "doctors recommend A". The pull is 0.9 × trust × 2, giving +11 points. This is not calibrated to any experiment.
- **Confirmation bias** in the friendship network: a person ignores friends whose belief is more than 1.0 away from their own.
- **Robustness test:** each of 9 guesses is set to ×0.5 and ×1.5, one at a time (18 tests, 20 crowds each), and four main findings are rechecked.

Adding the trust trait changes the random numbers, so the v1 results moved by up to 0.3 points (all tricks together: 87.0 → 87.1).

**Results:**

| Network | Chose A | Belief spread | Friends who disagree |
|---|---|---|---|
| Mixed friendships | 62.3% | 0.44 | 13.6% |
| Echo chambers | 61.2% | 0.82 | 9.9% |
| Mixed + confirmation bias | 50.1% | 0.67 | 31.7% |
| Echo + confirmation bias | 50.3% | 0.99 | 5.9% |

What this means: confirmation bias makes people **immune to the influencers** (the share stays at 50%). But it also **keeps the crowd divided**. In echo chambers with confirmation bias, beliefs are the most spread out of all four settings. In mixed groups, a third of friends disagree and stop listening to each other.

**Robustness (18 tests):**

| Finding | Held |
|---|---|
| Stacking beats any single trick by 10+ points | 18/18 |
| Slowing down protects more than prebunking | 18/18 |
| Careful thinkers are only a little safer (gap under 10 points) | 18/18 |
| A pre-selected default is the strongest single trick | 18/18 |

Caveat: the all-tricks result barely moves when a single pull changes, because stacked pressure hits the saturation cap. The two guesses that matter most:
- **The cap** (0.6 → 81%, 1.8 → 91%). Quote "roughly 80–90%", not "87%".
- **Thinking left under urgency** (0.15 → gut-minus-careful gap 2 points, 0.45 → 9 points). The gap stays under 10 points in every test, but its size depends on this guess.

## Version 2.1: two outside checks (9 Nov 2026)
Tools: SALib 1.6.0 and NDlib 6.0.1, installed in `simulation/.venv` (see `requirements.txt`). `sim.py` itself is unchanged.

### Check 1: all guesses changed at once (SALib, `salib_test.py` → `salib_results.json`)
The old test changed one guess at a time (18 tests). This one changed **all 9 guesses together**, each anywhere from half to 1.5×, in **1,408 combinations** (Sobol sampling, 4 runs each).

| Finding | Held |
|---|---|
| Slowing down protects more than prebunking | **1408/1408 (100%)** |
| A pre-selected default is the strongest single trick | **1408/1408 (100%)** |
| Stacking beats any single trick by 10+ points | 1341/1408 (95%) |
| Careful thinkers are only a little safer (gap under 10 points) | 1232/1408 (88%) |
| **All four together** | **1206/1408 (86%)** |

Which guess matters most (Sobol total index, 0 = no effect, 1 = explains everything):

| Result | Range (middle 90%) | Biggest guesses |
|---|---|---|
| All tricks together | 79.6% to 92.1% | the cap (0.62), choice sharpness (0.27) |
| Gap, gut vs careful | 1.2 to 12.3 points | thinking left under urgency (1.12) |
| How much stacking beats the best single trick | 10.2 to 21.3 points | the cap (0.61) |
| How much slowing down beats prebunking | 5.2 to 13.7 points | prebunking strength (0.64), urgency (0.30) |
| How much the default beats the next trick | 3.7 to 12.4 points | scarcity strength (0.54), choice sharpness (0.29) |

What this means:
- **Two findings are rock-solid** (100%): slowing down beats prebunking, and the default is the strongest single trick.
- **"Stacking beats any single trick" always holds.** The "by 10+ points" part fails 5% of the time, when the cap is small. Better wording: "stacking beats any single trick, usually by 10–20 points".
- **"Careful thinkers are only a little safer" is the weakest.** It fails 12% of the time, almost always when urgency doesn't cut thinking much. **This finding really depends on one guess, so present it as a question, not a result.** That matches the Limits section below.
- "All tricks together ≈ 80–90%" is confirmed (79.6–92.1%).

### Check 2: confirmation bias in a textbook model (NDlib, `ndlib_check.py` → `ndlib_results.json`)
The paper review (6 Nov) found that our confirmation-bias result depends on how extreme the influencers are. To check that this isn't a quirk of our own code, we rebuilt it with **NDlib's standard Deffuant model** (Deffuant et al. 2000), written by other researchers: 1,000 people, 10 friends each, 5% stubborn influencers, 30 rounds, 10 runs.

| How extreme the influencers are | No confirmation bias | With confirmation bias |
|---|---|---|
| Very extreme (3.0) | 89.2% | **49.9%** |
| Extreme (2.0) | 81.4% | 50.2% |
| Moderate (1.5) | 75.5% | 53.3% |
| Mild (1.0) | 68.3% | **61.3%** |

(Our own model, same idea: 50.0% → 52.3% with confirmation bias.)

What this means:
- **The textbook model shows the same pattern, even more strongly.** Confirmation bias completely blocks extreme influencers, but mild ones get through: 61% chose A, against 50% for extreme ones.
- **The lesson for the paper:** against people with confirmation bias, the winning strategy is to sound close to them, not extreme. This matches Bernays's Atlanta conference (southern messengers for a southern audience) and the WTF "brain immune system" quote.
- Without confirmation bias, extreme influencers win, so there's a trade-off: be extreme and reach people with open minds, or be mild and reach people with closed ones.
- Differences from our model: Deffuant friends meet in pairs and fully average, and there's no conformity trait. So the exact numbers differ, but the direction is the same.
- Side note: NDlib's own Hegselmann–Krause model (`HKModel.py`) appears to have an indentation bug: only one person is updated per round. So we used the Deffuant model instead.

## Limits (put these in the paper)
- The tactic strengths are assumptions tuned so results land near the real studies. The model shows *how* the mechanisms can work and combine. It does not prove what real people do.
- The model treats pushes toward A and toward B the same way. In real life, people correct fake negativity more than fake positivity (Muchnik et al. 2013).
- The decoy effect may be weaker in real life than here (see the replication warning above).
- The "urgency cuts thinking" rule drives the result that careful thinkers lose their advantage under pressure. That result comes from the assumption, so present it as a question to test, not a finding.

## Ideas for version 3
- Let each person have their own sensitivity to each tactic.
- Add a second manipulator pushing B (competing campaigns).
- Replace the simple people with AI chatbot "people" and compare.
