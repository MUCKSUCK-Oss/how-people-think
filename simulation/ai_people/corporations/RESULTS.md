# Corporations: quiet vs loud tricks: results (14 Nov 2026)
- **Design and predictions:** saved first in `PREDICTIONS.md`. The research is in `RESEARCH.md`.
- **Data:** **336 decisions, all usable.** 24 AI people per scenario in 6 countries (India, the USA, the UK, Brazil, Nigeria, Indonesia), half on tight incomes, each seeing all 7 versions. The full numbers are in `output/combined_analysis.txt`.
- **Everything is invented:** the ticket sites, the band and "StreamMax". Prices are in local money.
- ⚠ **Small groups:** 24 per scenario, so 1 person = 4 points (8 points within an income group). **Read the results as directions.**

## C1: Concert tickets with fees added at checkout (drip pricing)
- Site A showed its full price up front (about $96).
- Site B showed about $78, then added fees at the last step, after 10 minutes of choosing seats (total about $101).

| Version | Bought on B | Tight income | Comfortable |
|---|---|---|---|
| **B honest from the start** ($101 vs $96) | **50%** | 8% | **92%** |
| **B shows $78, adds fees at checkout** | **21%** | 0% | 42% |
| + "seats held for 04:59" | 21% | 0% | 42% |
| + "fees are standard across ticket sites" | 25% | 0% | 50% |
| + pre-ticked "ticket protection" | 21% | 17% | 25% |
| All tricks | 29% | 17% | 42% |
| All + "Site A sells similar seats for $96 all-in" | 21% | 25% | 17% |

**Kept the pre-ticked protection:** 0 of 12 buyers on B in the add-on and all versions; 1 of 5 with the disclosure.

## C2: Cancelling a streaming service used twice in 3 months (about $12/month)
| Version | Cancelled now | Kept for now | Took the 50% offer |
|---|---|---|---|
| Easy: one "Cancel" button | 88% | 8% | 4% |
| **No cancel button: phone only, 9–5, about 20 minutes on hold** | **58%** | **42%** | 0% |
| Guilt buttons ("No, I prefer being bored") | **100%** | 0% | 0% |
| "Stay for 50% off for 3 months" | 88% | 0% | 12% |
| "You'll lose your watch history forever" | 100% | 0% | 0% |
| **All four together** | **92%** | 4% | 4% |
| All + "you can cancel by a one-line email; the offer goes back to full price" | 100% | 0% | 0% |

## The 5 main findings
1. **Hidden fees backfired when the honest price was in view.**
   - A slightly dearer but honest site kept **50%** of buyers (92% of comfortable people: *"five bucks doesn't move the needle, and I've already picked my seats"*).
   - The same site with fees added at checkout kept only **21%**: *"Classic bait-and-switch."*
   - **Being honest beat being cheap-looking.** The 10 minutes already spent kept people on an honest site, but not on one that tricked them.
   - **Why this is the opposite of the real StubHub experiment** (Blake et al. 2021, +21% spending): in every version here, people knew the honest competitor's total. Real shoppers usually don't, because every site drips. **All-in pricing laws work by creating exactly the comparison these AI people had.**
2. **Friction was the only trick that worked.**
   - With no cancel button and a 20-minute phone queue, **42% kept paying** "for now", mostly comfortable people: *"I'm not spending 20 minutes on hold during work hours for $12."*
   - This is the trick Amazon paid $2.5 billion over. It doesn't persuade anyone; it just makes leaving cost more effort than staying.
3. **Loud tricks did nothing or backfired: guilt buttons, "lose your history", countdowns.**
   - The guilt buttons and the loss warning **raised** cancelling to 100%.
   - The countdown added nothing to the hidden fees.
4. **Adding loud tricks on top of a quiet one exposed it.**
   - The phone-only cancel alone kept 42%. With guilt buttons, the loss warning and the offer added, it kept only **8%**.
   - *"I can spot a dark pattern from a mile away… no cancel button, threatening button labels, scaring me about lost data."*
   - **The loud tricks made people see the whole thing as manipulation, including the friction.** This is the opposite of "stacking always helps", which the rule-based simulation assumes (Section 5.2 of the paper).
5. **Pre-ticked boxes didn't work on readers who read everything.** Almost every buyer unticked the protection. Real shoppers skim; AI people read every line. This is the main limit of this topic.

## Predictions check
| # | Prediction | Result | ✓/✗ |
|---|---|---|---|
| 1 | Honest: ≤15% choose B | 50% | ❌ |
| 2 | Drip: 40–70% finish on B (key prediction) | 21% (backfire) | ❌ |
| 3 | Timer adds little or backfires | 21% = 21% | ✅ |
| 4 | "Fees are standard" adds a small increase | +4 | ✅ |
| 5 | ≥30% keep the pre-ticked protection | 0% (20% with disclosure) | ❌ |
| 6 | All ≈ drip or higher | 29% vs 21% | ✅ |
| 7 | Disclosure brings B to ≤20% | 21% | 🟡 |
| 8 | Easy: ≥85% cancel | 88% | ✅ |
| 9 | Obstruct: cancelling ≤60% | 58% | ✅ |
| 10 | Confirm-shaming: small or backfire | 100% (backfire) | ✅ |
| 11 | The 50% offer = the biggest drop (≥25 points) | No drop | ❌ |
| 12 | Loss framing: a moderate drop | A rise (100%) | ❌ |
| 13 | All = the lowest | 92%, near the top | ❌ |
| 14 | All + disclosure ≥75% | 100% | ✅ |
| 15 | Quiet tricks beat loud ones | Friction yes; drip backfired | 🟡 |
| 16 | Tight incomes resist drip more but take the offer more | Tight took the offer *less* (0% vs 25%) | ❌ |

**7 of 16 right, 2 partly, 7 wrong.**
- **What I got wrong:** I treated drip pricing as a quiet trick. But when an honest price is visible, a price that jumps at the last step is very loud. And I assumed stacking tricks always adds up; here, adding loud tricks to friction *undid* it.

## Limits
- **AI people read every line,** so pre-ticked boxes and small fees are noticed far more than by real people, who skim. Real effects of quiet tricks are probably **bigger** than here.
- **C1 always showed Site A's honest total.** This is the main reason drip backfired, and the result applies to markets where shoppers can easily compare all-in prices.
- **In C2, the person had firmly decided to cancel** (used twice in 3 months), so most versions were near 100%. Real subscription traps catch people who are unsure.
- **Wording problem:** in the "all + disclosure" version, some people read the pre-ticked protection as already included in the total and thought B was cheaper after removing it. A few of the B choices there are miscalculations.
- **Usage:** each batch of 168 decisions took about 35 minutes.
