# University traps v2: results (night of 11 Nov 2026)
- **Design:** built from `RESEARCH.md`; predictions saved first in `PREDICTIONS_v2.md`.
- **Data:** pilot 2 + an extra batch, pooled: **14 AI people per scenario** (7 students, 7 parents) × all versions = **168 decisions**, all usable. The full analysis is in `combined_analysis.txt`.
- ⚠ **This is small.** 14 people per version means one person = 7 points, so treat the numbers as **directions**, not exact sizes.

## Scenario 1: government college (₹4.5L, old labs) vs private university (₹11L, shiny)
| Version | Chose private B | Students | Parents |
|---|---|---|---|
| Brochure (what families normally see) | 7% | 14% | 0% |
| Honest numbers (medians shown) | 7% | 14% | 0% |
| + "Highest package ₹42 LPA, 100% placement assistance" | 21% | 14% | **29%** |
| + counsellor "pay ₹25,000 by tomorrow, loan in 3 days" | 21% | 14% | 29% |
| + "cousin studied there, relatives say big name" | **29%** | **29%** | 29% |
| All tricks | 21% | 14% | 29% |
| All tricks + honest numbers + "counsellor gets a commission" | 14% | 14% | 14% |

## Scenario 2: stay in India (₹3L B.Com, local jobs ₹12–18k) vs Canada via an agent (₹30L, mortgage)
| Version | Chose Canada | Students | Parents |
|---|---|---|---|
| Brochure | 7% | 0% | 14% |
| Honest facts (PR not guaranteed, 40–50 h work, shared rooms, agent commission) | **0%** | 0% | 0% |
| + agent pitch ("office job anywhere, PR no problem, visa guaranteed") | 29% | 29% | 29% |
| + "300 from your area went; neighbour's son sends ₹40,000 a month" | **64%** | 57% | **71%** |
| + honest facts added (disclosure) | **14%** | 0% | 29% |

## The 5 main findings
1. **"People like us" beats ads, every time.**
   - In both scenarios the strongest push was a real person: the cousin in Bengaluru, or the neighbour's son sending money home.
   - Many AI people **called the agent's promises "BS" and still chose Canada because of the neighbour.**
   - *"The agent's promises sound like typical agent BS, but the neighbour's son sends ₹40,000 home every month — that's real proof."* (Sneha, 19, student)
   - This is the same pattern as the earbuds pilot and university run 1: **quiet, human tricks work, while loud ad claims get spotted.**
2. **Agent + village social proof was the most powerful trap: 7% → 64%.** It took 64% of AI families into a ₹30 lakh debt, every one of them with a loan or mortgage. This matches what the CBC investigation found in Punjab.
3. **Honest disclosure works strongly.**
   - Adding the real facts (PR not guaranteed, 40–50 h/week work, the agent's commission) cut Canada **64% → 14%**.
   - Adding the honest medians and the counsellor's commission cut the private college to 14%.
   - **This supports the CCPA's 2024 approach (honest numbers in the same font) and the agent code of conduct that Canada didn't sign.**
4. **Parents were more trickable than students by ads.**
   - In Scenario 1, salary hype moved parents (0% → 29%), not students (14% → 14%). Students often mocked the brochure ("all marketing hype").
   - In Scenario 2, parents went to Canada more than students did (71% vs 57%).
   - The parents who fell for it reasoned "if she gets that salary, the loan repays itself".
5. **Money protects.**
   - Tight-income families in Scenario 1: 0% in every version.
   - The "push" of bad local options mattered: Scenario 2 people cited "₹12–18k jobs or years unemployed" as the reason to risk Canada.

## Predictions check (honest)
| Prediction | Result | ✓/✗ |
|---|---|---|
| S1 brochure 30–50% choose private | 7% | ❌ (AI people far more cost-careful than expected) |
| Honest numbers lower the B share | Same as brochure (7%, floor) | ❌ can't tell |
| Hype small or backfires | +14 (mostly parents) | 🟡 small, but no backfire |
| Counsellor deadline small or backfires | +14 | 🟡 |
| Relatives = strongest single trick | 29%, the strongest in S1 | ✅ |
| All ≈ relatives, not the sum | 21% vs 29% | ✅ |
| Disclosure cuts it back | 21% → 14% (S1), 64% → 14% (S2) | ✅ |
| Parents lower except "big-name" parents | Parents were *more* moved by hype | ❌ |
| S2 brochure 10–25% | 7% | 🟡 slightly lower |
| Agent pitch mixed; careful people resist | 29%. "Mostly careful" people moved *most* (75%) | ❌ partly |
| Village social proof = the biggest increase | +57 points | ✅ |
| Disclosure → big drop in S2 | 64% → 14% | ✅ |
| Students want Canada more than parents | Parents 71% vs students 57% | ❌ |

**6 of 13 right, 3 partly, 4 wrong.** The wrong ones are interesting: AI parents were more trickable than AI students.

## Limits
- **Only 14 people per scenario** (usage limits); the full 40-person run should be done on a fresh limit.
- The AI people are probably **more cost-careful than real families** (brochure 7%), so real effects may be bigger. In real life, India has 1.9 million empty engineering seats that colleges market hard to fill, and many Punjabi families do mortgage land.
- "Very careful" had only 2 people, so ignore that row.
- One AI model (Haiku); text-only situations.
- **Cost discovery:** each AI-person decision used about 0.27% of the Pro 5-hour limit. A 480-decision run needs about 2 full windows.
