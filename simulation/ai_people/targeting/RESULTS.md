# Personal targeting: results (11 Nov 2026)
- **Design and predictions:** saved first in `PREDICTIONS.md`. The research is in `RESEARCH.md`.
- **Data:** **182 decisions, all usable**; **14 AI people per scenario**, each seeing every version. The full numbers are in `combined_analysis.txt`.
- **P1 uses only the fixed version** (money needed by tomorrow, other doors already closed); pilot-1 P1 is excluded, as recorded beforehand.
- ⚠ **Small groups:** 1 person = 7 points, so **read the results as directions only.**

## P1 (India): an instant-loan app when ₹15,000 is needed by tomorrow
| Version | Chose the loan app | "Proud" (hate asking relatives) | Not proud | Allowed contacts/photos |
|---|---|---|---|---|
| Generic ad | 57% | 71% | 43% | 57% |
| + real terms (≈300% a year, not RBI-registered, calls your contacts if late) | **43%** | **71%** | 14% | 43% |
| Ad **written for the person** ("Rent due? No need to ask anyone. Nobody will know.") | 57% | 71% | 43% | 57% |
| Personal ad + "we noticed you searched 'urgent money' at 2 am" | 57% | 71% | 43% | 57% |
| Personal ad + "offer expires in 15 minutes" | 64% | 86% | 43% | 57% |
| Personal ad + "2 lakh people in your city used it, ⭐4.6" | 64% | 86% | 43% | 64% |
| Everything + real terms | **29%** | 43% | 14% | 29% |

## P2 (USA): book a $312 flight now, or keep comparing
| Version | Booked now | Said the price is fair |
|---|---|---|
| Normal fare | 43% | 71% |
| "Picked for you: just how you like it" | 43% | 64% |
| "Special member price just for you: $312 (was $349)" | **29%** (lower) | 71% |
| Personal + "we see you've checked this route 6 times" | 50% | 79% |
| Personal + "only 2 seats left" | 43% | 71% |
| Everything + **"the same seat is $279 for other users"** | **14%** | **0%** |

## The 5 main findings
1. **Desperation beats information.**
   - Even after reading the real terms (≈300% a year, not RBI-registered, it will call everyone in your phone), **43% still took the loan app**.
   - Among people who hate asking relatives, the honest terms changed **nothing (71% → 71%)**.
   - **The shame of asking the family was stronger than the fear of being harassed later.**
   - *"My employer already refused and I'm not going to shame myself asking relatives again — they'll just gossip more. I need the money tomorrow."*
   - This matches the real loan-app victims: the trap works because other doors are closed, not because people don't know it's risky.
2. **Ads written for the person changed nothing**, in both scenarios (57% → 57%, 43% → 43%).
   - This fits the research: political tailoring helped only a little (Tappin 2023), and Cambridge Analytica oversold its "psychographic" ads (ICO).
   - ⚠ **But our design can't test targeting's real power: *choosing who sees the ad*.** Every AI person here was already in a crisis.
   - In real life, targeting finds the person searching "urgent money" at 2 am. **The danger is in *who* gets reached and *when*, not in clever wording.**
3. **The creepy "we know what you did" message didn't scare anyone away.**
   - P1 stayed at 57%. In P2 it slightly *raised* booking ("I've already checked six times, I'm done").
   - **This goes against the research prediction (Aguirre 2015).** One possible reason: the reveal named something the person really did, so it felt like help, not spying.
4. **Fake "special price just for you" discounts backfired** (43% → 29%). AI people saw through "was $349".
5. **Telling people others pay less is the most powerful fix.**
   - "The same seat is $279 for other users" cut booking to **14%**, and **nobody** called the price fair (71% → 0%).
   - **Unfairness makes people angry in a way that privacy doesn't.**
   - This supports laws that force companies to disclose personalised ("surveillance") pricing.

## Who was most at risk (P1)
- **Proud people** (hate asking relatives): 71% took the loan in the base version and 86% with urgency or social proof, compared with 43% of the others.
- **People who trust apps:** 73%, compared with 0% of suspicious people.
- **Very careful people** almost never took it.

## Predictions check
| # | Prediction | Result | ✓/✗ |
|---|---|---|---|
| 1 | P1 base 20–40% | 57% | ❌ higher |
| 2 | Honest terms ≤10% | 43% | ❌ desperation |
| 3 | A personal ad raises it +10, mostly for proud people | 0 | ❌ |
| 4 | The creepy reveal lowers it | 0 | ❌ |
| 5 | Urgency: small or a backfire | +7 | ✅ small |
| 6 | Social proof raises it the most | +7 (tied with urgency) | 🟡 |
| 7 | Full disclosure ≈ honest | 29% (lower than honest's 43%) | 🟡 |
| 8 | P2 base 40–60% | 43% | ✅ |
| 9 | "Special price" raises booking | −14 | ❌ backfired |
| 10 | Creepy in P2: up or down? | slightly up (+7) | 🟡 resolved: up |
| 11 | The "others pay $279" disclosure lowers it the most | 14%, fair 0% | ✅ |
| 12 | Personal matching helps less than social proof | 0 vs +7 | ✅ (weak) |

**4 right, 3 partly, 5 wrong.** We got the money-crisis behaviour badly wrong: we expected honest terms to stop people, and they didn't.

## Limits
- **14 people per scenario** with one AI model (Claude Haiku), in text-only situations.
- **The AI people's personalities were written into their instructions**, so the "matched" ad repeats what they already know about themselves. Real targeting must *guess* this from data.
- **We can't test the targeting *selection* step** (finding vulnerable people); that is likely where most of the real harm is.
- **P1 had to be fixed after pilot 1** (from "3 days, relatives may help" to "by tomorrow, other doors closed"). It was recorded before re-running.
- "QuickRupee" is a made-up app; its terms come from the RBI working group and news reports.
