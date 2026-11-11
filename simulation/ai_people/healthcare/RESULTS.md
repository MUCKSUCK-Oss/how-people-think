# Healthcare traps: results (11 Nov 2026)
- **Design and predictions:** saved first in `PREDICTIONS.md`. The research is in `RESEARCH.md`.
- **Data:** **308 decisions, all usable**; **14 AI people per scenario**, each seeing every version. The full numbers are in `combined_analysis.txt`.
- **H2 used only the fixed version (pain not improving);** pilot-1 H2 data is excluded, as recorded beforehand.
- ⚠ **Small groups:** 14 people means 1 person = 7 points. **Read the results as directions, not exact sizes.**

## H1 (India): stent (₹2.5 lakh) or medicines for stable chest pain
| Version | Chose stent | Patients | Son/daughter deciding |
|---|---|---|---|
| Base (both options offered by the doctor) | 43% | 29% | 57% |
| Honest facts (ISCHEMIA: a stent doesn't prevent heart attacks here) | **14%** | 14% | 14% |
| + doctor: "ticking time bomb, I'd do it today" | **64%** | 43% | **86%** |
| + "insurance package: only ₹40,000, valid today" | 64% | 43% | 86% |
| + "the neighbour ignored it and died; the cousin feels 20 years younger" | **93%** | 86% | 100% |
| All three | **100%** | 100% | 100% |
| All three + honest facts + "the hospital sets revenue targets; a free second opinion is available" | **29%** | 29% | 29% |

## H2 (USA): MRI ($1,100) or physiotherapy for back pain that isn't improving
| Version | Chose MRI |
|---|---|
| Base | 43% |
| Honest facts (guidelines: imaging doesn't help in the first 6 weeks; it finds harmless "abnormalities") | **7%** |
| + imaging-centre ad: "could be something serious, early detection saves lives" | 36% (**slightly lower**) |
| + "$400 off if you book this week" | 43% (no change) |
| + coworker: "my MRI found a herniated disc; my brother-in-law's back pain was cancer" | **64%** |
| All three | 43% |
| All three + honest facts + "the imaging centre is owned by the clinic advertising to you" | 29% |

## H3 (USA): where to give birth: community hospital ($2,700) or a private-equity-owned luxury hospital ($4,500)
| Version | Chose the PE luxury hospital | Pregnant women | Husbands deciding |
|---|---|---|---|
| Base | 50% | 29% | **71%** |
| Honest report card (1 nurse per 4 women in labor vs 1 per 2; C-sections 34% vs 24%) | **7%** | 0% | 14% |
| + influencer ad ("you deserve to be pampered") | 29% (**lower**) | 0% | 57% |
| + "a close friend loved it" | 43% | 14% | 71% |
| + "a free 3D ultrasound if you register this week" | 43% | 14% | 71% |
| All three | 43% | 14% | 71% |
| All three + **only** "owned by private equity; JAMA found 25% more patient harms" | 29% | **0%** | 57% |
| All three + report card + ownership | **14%** | 0% | 29% |

## The 6 main findings
1. **A doctor's fear works; an ad's fear doesn't.**
   - The doctor's "ticking time bomb" raised stent choices from **43% to 64%**.
   - The imaging centre's "early detection saves lives" ad slightly **lowered** MRI choices (43% → 36%). AI people called it "fear-mongering".
   - **The same fear message works or backfires depending on who says it.** This is the key new finding compared with universities, where every trick came from ads or agents.
   - *"Doctor sir was very clear — this is a ticking time bomb… I cannot gamble with my mother's life. We will have to take a loan."* (an AI son)
2. **"People like us" is again the strongest trick, in all three scenarios.**
   - The neighbour who died / the cousin who recovered took the stent to **93%**, and the coworker's cancer story took the MRI to **64%**.
   - This matches universities (the neighbour's son in Canada) and **Fagerlin 2005** (patient stories change treatment choices even when people see the numbers).
   - In H3 the friend's story mostly worked on husbands.
3. **Deciding for a parent makes people easier to push.**
   - Sons and daughters chose the stent far more than the patients themselves: **86% vs 43%** after the doctor's fear.
   - *"I can't risk her life for money"* turns every warning into a reason to spend.
   - **The pattern matches the universities run, where parents deciding for children were also more trickable.** People are less careful with money when the decision is about someone they love.
4. **"Insurance covers it, today only" works on the poorest.**
   - Tight-income families went from **25% to 100%** choosing the stent when the price fell to ₹40,000 with a same-day deadline.
   - Insurance makes the procedure feel cheap, so nobody asks whether it's needed.
5. **Private equity in childbirth: husbands chose it, pregnant women didn't.**
   - Husbands picked the luxury PE hospital 71% of the time ("my wife deserves to be pampered") and **57% even after being told it was PE-owned with more patient harm**.
   - Pregnant women started at 29%, and dropped to 0% once they saw either the ownership disclosure or the nurse numbers.
   - **Concrete numbers (nurses per patient, C-section rate) worked better than the words "private equity"** (14% vs 29% when added to all the tricks).
   - ⚠ **Caution:** the husband/wife gap may partly reflect stereotypes in the AI model ("pamper the wife"), not only real behaviour. This needs a check with real people.
6. **Disclosure helps a lot, but stories survive it.**
   - Honest facts alone brought every scenario down to **7–14%**.
   - When the tricks were present too, disclosure brought them down only to 14–29%, so some people still chose the stent, MRI or PE hospital because of the doctor's warning or the relative's story.
   - *"My neighbour was exactly my age — he ignored his chest pain and he died… I am scared."* (an AI patient, after seeing the trial facts and the revenue targets)

## Predictions check
| # | Prediction | Result | ✓/✗ |
|---|---|---|---|
| 1 | H1 base 25–45% | 43% | ✅ |
| 2 | H1 honest ≤15% | 14% | ✅ |
| 3 | Doctor's fear: +20 points or more | +21 | ✅ |
| 4 | Package increases it, mostly for tight income | Tight income 25 → 100% | ✅ |
| 5 | Anecdote ≈ fear or larger | 93% vs 64% | ✅ |
| 6 | All ≥60% | 100% | ✅ |
| 7 | All + disclosure: a big drop, still above honest | 29% vs 14% | ✅ |
| 8 | Sons/daughters choose the stent more than patients | 86% vs 43% (fear) | ✅ |
| 9 | H2 base 15–35% | 43% | ❌ a bit higher |
| 10 | H2 honest ≤10% | 7% | ✅ |
| 11 | Fear ad: small or backfire | −7 points | ✅ |
| 12 | Deal: a small increase | 0 | 🟡 |
| 13 | Anecdote = the biggest increase | +21 | ✅ |
| 14 | All + disclosure ≈ honest | 29% vs 7% | 🟡 some story effect remains |
| 15 | A doctor's fear beats an ad's fear | +21 vs −7 | ✅ |
| 16 | H3 base 30–50% | 50% | ✅ |
| 17 | Influencer ad: small or backfire | −21 points | ✅ |
| 18 | Friend = the biggest increase | No increase overall (husbands stayed at 71%) | ❌ |
| 19 | Deal: a small increase | −7 | ❌ |
| 20 | Report card ≤15% | 7% | ✅ |
| 21 | Ownership disclosure lowers it, but less than the safety numbers | 29% vs 14% | ✅ |
| 22 | Husbands choose B more than pregnant women | 71% vs 29% | ✅ |

**17 of 22 right, 2 partly, 3 wrong.** This is much better than universities (5/13), probably because the research came first this time.

## Limits
- **14 people per scenario** with one AI model (Claude Haiku), in text-only situations.
- **AI people sometimes invent details** ("my coworker's sister went there", "I looked at the safety records"), so the reasons are partly made up.
- **The H3 report-card numbers are invented** for the scenario (in a realistic range). The JAMA 25% figure is real.
- **The husband/wife gap may be a model stereotype.**
- **H2 had to be fixed after pilot 1** (from "pain improving" to "not improving"). The fix was recorded before re-running.
- The AI people are probably **more cost-careful and more suspicious of ads than real people**, so real effects of ads may be bigger.
- **Usage:** about 0.1–0.15% of the 5-hour limit per AI decision on this run (cheaper than the university run).
