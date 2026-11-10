# University traps simulation: design and predictions
*Written 11 Nov 2026, BEFORE any data. Saved to git first, so the commit time proves the order.*

## Real cases this simulation is based on
- **India, Nov 2024:** the Central Consumer Protection Authority (CCPA) issued guidelines banning coaching institutes from claims like "100% selection" or "100% job guarantee", and requiring disclaimers in the same font size as the claim. Fines were imposed on 19 institutes (about ₹61.6 lakh, per a Dec 2024 Lok Sabha answer). The rules cover coaching, not colleges, but the tricks are the same.
- **USA, 2016:** DeVry University paid **$100 million** to settle an FTC case over its ad claim that "90% of graduates got jobs in their field within 6 months". The FTC said the count included people who kept their old jobs or got jobs outside their field. DeVry denied wrongdoing.
- **"Highest package" vs median:** college ads often show the single highest salary ("₹45 LPA!"), which one star student can produce, instead of the median (the typical student). An analysis of India's NIRF data found the reported salary figures were the weak spot.

## The situation every AI student sees
A 17–18-year-old Indian student who has just got their Class 12 results and has two engineering admission offers in Computer Science:

| | **College A** (government-aided) | **College B** (private) |
|---|---|---|
| Total fees for 4 years | ₹4 lakh | ₹18 lakh |
| Median starting salary (the typical graduate) | ₹4.5 LPA | ₹5 LPA |
| Students placed | 78% | 80% |
| Distance | 40 km from home | 300 km away, hostel extra |

College B is only **slightly** better on the typical outcome but costs **4.5× more**. A careful family would usually pick A. **Our measure is how many AI students pick B (the expensive one)**, and how that changes with each marketing trick.

## Versions (the tricks are always on College B, the expensive one)
| Version | What's added to College B | Real-life trick |
|---|---|---|
| 1. **Control** | nothing; the facts above only | – |
| 2. **Highest-package hype** | "🏆 Highest package ₹45 LPA! 95% placement assistance!" (the median stays in small print) | Highest vs median; "placement assistance" ≠ placement (DeVry-style) |
| 3. **Scarcity** | "⚠ Only 12 seats left! Pay ₹50,000 seat-booking fee within 48 hours to confirm" | Deadline pressure plus a sunk-cost deposit |
| 4. **Ranking badge** | "⭐ Ranked #7 'Top Emerging Engineering University 2026' (Education Excellence Awards)" | Paid or unclear awards that look like official rankings |
| 5. **Social proof** | "3 seniors from your school joined last year; a cousin's friend got placed at ₹20 LPA" | Word of mouth and success stories |
| 6. **All tricks together** | versions 2 + 3 + 4 + 5 | Real brochures stack them |

## People
- **40 AI students** (separate, fresh Claude Haiku calls; no tools, no memory, not told it's an experiment).
- Their life stories vary: city, **family income** (tight / middle / comfortable), board marks, **decision style** (gut → very careful, 10 each), trust in ads, how much they follow friends, and whether their parents push "a big-name college".
- 40 × 6 versions = **240 decisions**. Which college is listed first is swapped between people.
- Answer format: CHOICE (A or B), whether they'd **take an education loan** (yes/no), and REASON.

## Predictions (made before any data)
1. **Control:** most will pick A (cheap). We predict **20–35% pick B**, more from comfortable families.
2. **Highest-package hype will be the strongest single trick** (+15 points or more), because big salary numbers are vivid and the median is easy to ignore. But careful AI people may spot "highest ≠ typical" and resist.
3. **Scarcity will be weak or backfire**, as in the earbuds pilot (AI people resisted countdowns).
4. **Ranking badge:** a small effect (+5–10).
5. **Social proof:** a medium effect, strongest for students who follow friends.
6. **All tricks together** will beat any single trick, but the stack may also trigger suspicion, so it will be **less than the sum** of the single effects.
7. **Decision style:** gut deciders will be moved much more than very careful ones (as in the classic test, where "very careful" AI people showed no bias).
8. **Money:** tight-income students will resist more, because ₹18 lakh means a big loan.

## Honest limits, decided in advance
- From the classic-experiment check: AI people get the **direction** right, but not reliably the **size**. We'll report "which tricks push toward the expensive college, and for whom", not exact percentages for real Indian students.
- "Very careful" AI people are too rational, so the real effect on careful humans is probably larger than shown.
