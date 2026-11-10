# University traps v2: results (night of 11 Nov 2026)
- **Design:** built from `RESEARCH.md`; predictions saved first in `PREDICTIONS_v2.md`.
- **Data (updated 11 Nov):** pilot 2 + extra batch 1 + extra batch 2, pooled: **20 AI people per scenario** (10 students, 10 parents) × all versions = **240 decisions**, all usable. The full analysis is in `combined_analysis.txt`.
- ⚠ **Still small.** One person = 5 points, so treat the numbers as **directions**, not exact sizes.
- Extra batch 2 was mostly careful / very careful people (pre-registered in `PREDICTIONS_v2.md`).

## Scenario 1: government college (₹4.5L, old labs) vs private university (₹11L, shiny)
| Version | Chose private B | Students | Parents |
|---|---|---|---|
| Brochure (what families normally see) | 15% | 10% | 20% |
| Honest numbers (medians shown) | 10% | 10% | 10% |
| + "Highest package ₹42 LPA, 100% placement assistance" | 25% | 10% | **40%** |
| + counsellor "pay ₹25,000 by tomorrow, loan in 3 days" | 25% | 20% | 30% |
| + "cousin studied there, relatives say big name" | **30%** | 20% | **40%** |
| All tricks | 20% | 10% | 30% |
| All tricks + honest numbers + "counsellor gets a commission" | 20% | 20% | 20% |

## Scenario 2: stay in India (₹3L B.Com, local jobs ₹12–18k) vs Canada via an agent (₹30L, mortgage)
| Version | Chose Canada | Students | Parents |
|---|---|---|---|
| Brochure | 10% | 0% | 20% |
| Honest facts (PR not guaranteed, 40–50 h work, shared rooms, agent commission) | **0%** | 0% | 0% |
| + agent pitch ("office job anywhere, PR no problem, visa guaranteed") | 25% | 20% | 30% |
| + "300 from your area went; neighbour's son sends ₹40,000 a month" | **65%** | 50% | **80%** |
| + honest facts added (disclosure) | **10%** | 0% | 20% |

*(At 14 people it was 7 → 0 → 29 → 64 → 14%; adding 6 more people barely changed it, so this pattern is the most solid result.)*

## The 5 main findings
1. **"People like us" beats ads, every time.**
   - In both scenarios the strongest push was a real person: the cousin in Bengaluru, or the neighbour's son sending money home.
   - Many AI people **called the agent's promises "BS" and still chose Canada because of the neighbour.**
   - *"The agent's promises sound like typical agent BS, but the neighbour's son sends ₹40,000 home every month — that's real proof."* (Sneha, 19, student)
   - This is the same pattern as the earbuds pilot and university run 1: **quiet, human tricks work, while loud ad claims get spotted.**
2. **Agent + village social proof was the most powerful trap: 10% → 65%.** It took 65% of AI families into a ₹30 lakh debt, every one of them with a loan or mortgage. This matches what the CBC investigation found in Punjab.
3. **Honest disclosure works strongly.**
   - Adding the real facts (PR not guaranteed, 40–50 h/week work, the agent's commission) cut Canada **64% → 14%**.
   - In Scenario 1 the effect is **weak**: at 20 people, "all tricks + disclosure" is 20%, the same as "all tricks" (it was 21% → 14% at 14 people). The cousin still pulled some parents in even when they saw the honest medians ("my cousin is proof enough"). **Disclosure beats an agent's promises much more easily than it beats a relative's story.**
   - **This supports the CCPA's 2024 approach (honest numbers in the same font) and the agent code of conduct that Canada didn't sign.**
4. **Parents were more trickable than students by ads.**
   - In Scenario 1, salary hype moved parents (20% → 40%), not students (10% → 10%). Students often mocked the brochure ("all marketing hype").
   - In Scenario 2, parents went to Canada more than students did (80% vs 50%).
   - The parents who fell for it reasoned "if she gets that salary, the loan repays itself".
5. **Money protects.**
   - Tight-income families in Scenario 1: 0% in every version.
   - The "push" of bad local options mattered: Scenario 2 people cited "₹12–18k jobs or years unemployed" as the reason to risk Canada.

## Predictions check (honest)
| Prediction | Result | ✓/✗ |
|---|---|---|
| S1 brochure 30–50% choose private | 15% | ❌ (AI people far more cost-careful than expected) |
| Honest numbers lower the B share | 15% → 10% (one person) | 🟡 tiny |
| Hype small or backfires | +14 (mostly parents) | 🟡 small, but no backfire |
| Counsellor deadline small or backfires | +14 | 🟡 |
| Relatives = strongest single trick | 29%, the strongest in S1 | ✅ |
| All ≈ relatives, not the sum | 21% vs 29% | ✅ |
| Disclosure cuts it back | S1 20% → 20% (no drop at n=20), S2 65% → 10% | 🟡 only in S2 |
| Parents lower except "big-name" parents | Parents were *more* moved by hype | ❌ |
| S2 brochure 10–25% | 10% | ✅ |
| Agent pitch mixed; careful people resist | 29%. "Mostly careful" people moved *most* (75%) | ❌ partly |
| Village social proof = the biggest increase | +55 points | ✅ |
| Disclosure → big drop in S2 | 65% → 10% | ✅ |
| Students want Canada more than parents | Parents 80% vs students 50% | ❌ |

**At 20 people: 5 of 13 right, 4 partly, 4 wrong** (the S1 disclosure prediction dropped to partly; two others moved up). The wrong ones are interesting: AI parents were more trickable than AI students.

## Limits
- **Only 20 people per scenario** (usage limits); a 40-person run would make the Scenario 1 numbers firmer.
- Scenario 1 differences are 1–3 people, so they are **weak evidence**; Scenario 2 (the village effect and disclosure) is strong and stable across batches.
- The AI people are probably **more cost-careful than real families** (brochure 10–15%), so real effects may be bigger. In real life, India has 1.9 million empty engineering seats that colleges market hard to fill, and many Punjabi families do mortgage land.
- "Very careful" had only 2 people, so ignore that row.
- One AI model (Haiku); text-only situations.
- **Cost discovery:** each AI-person decision used about 0.27% of the Pro 5-hour limit. A 480-decision run needs about 2 full windows.
