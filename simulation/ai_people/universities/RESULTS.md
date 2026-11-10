# University traps simulation: results, run 1 (11 Nov 2026)
Predictions were saved to git first (`PREDICTIONS.md`). 40 AI students × 6 versions = 240 decisions, all usable.

## Main result: almost nobody chose the expensive college
| Version (trick on the ₹18 lakh college) | Chose expensive College B | Change |
|---|---|---|
| Control (facts only) | 1/40 (2.5%) | – |
| "Highest package ₹45 LPA! 95% placement assistance!" | 0/40 (0%) | −2.5 |
| "Only 12 seats left, pay ₹50,000 in 48 h" | 1/40 (2.5%) | 0 |
| "Ranked #7 Top Emerging University" | 2/40 (5%) | +2.5 |
| "3 seniors from your school joined; cousin's friend got ₹20 LPA" | 3/40 (7.5%) | +5 |
| All tricks together | 3/40 (7.5%) | +5 |

## Who moved (small numbers, so treat these as hints)
- **Family income was the biggest factor.** Students from tight-income families: **0% chose B in every version**. Comfortable families: 8% (control) → **23% (social proof)**.
- **Parents who want a "big-name college":** 8% → **23%** with social proof. With no such parental pressure: 0% in almost every version.
- **Students who care what friends do:** 0% → 9% with social proof.
- **"Very careful" students:** 0% in all versions (too perfect again, as in the classic test).

## The AI students saw through the tricks
- **"Highest package" was mentioned in 68 of 80 answers and called a trick in 39.** Many said "the highest package is one student; the median is what matters". It moved **nobody**, and caused 1 backfire.
- **Scarcity ("48 hours, booking fee") was called pressure or a trick in 55 of 80 answers.** It moved nobody.
- **Social proof was the only trick rarely called a trick** (10 of 30 mentions). It was also the only one that moved anyone:
  > *"Three seniors from our school joined College B last year and my cousin's friend got ₹20 LPA from there."* (Diya, mostly gut, middle income: the only student who switched to B with all tricks on)

## How did our predictions do?
| Prediction | Result | Verdict |
|---|---|---|
| 20–35% pick B in control | **2.5%** | ❌ far too high: AI students were much more cost-careful |
| Highest-package hype = strongest trick | **The weakest** (0%, many called it out) | ❌ wrong |
| Scarcity weak or backfires | Weak (no change) | ✅ |
| Ranking badge: small | +2.5 | ✅ |
| Social proof: medium, strongest for friend-followers | **The strongest trick**, and only for friend-followers and comfortable families | ✅ (direction) |
| All < sum of singles | Same as social proof alone | ✅ |
| Gut moved more than very careful | Very careful never moved; others slightly | ✅ (weakly) |
| Tight-income resist most | 0% always | ✅ |

## What this means
1. **The tricks that call attention to themselves fail.** Big salary numbers, countdowns and award badges were mostly spotted and named as tricks. **The quiet, human trick, "people like you went there", was the only one that worked.** This matches the earbuds pilot (quiet defaults worked, loud countdowns backfired) and the SusBench study.
2. **Money and family pressure matter more than ads.** The ads only "worked" on students who could afford B and whose parents wanted a big name. **The trap catches families who already lean toward prestige.**
3. **AI students are probably far too rational here.** In real India, many families do pay lakhs on the strength of placement ads; the government had to ban "100% selection/job" claims for coaching institutes in 2024. Our AI students did careful maths ("4.5× the fees for ₹50,000 more salary") that real 17-year-olds under family pressure may not do.

## Design problem (honest)
College B was **too obviously a bad deal**: 4.5× the cost for almost the same outcome. So the tricks had almost nothing to work with (a "floor effect"). It's the same mistake as earbuds pilot 1.

**Fix for run 2:** make the colleges closer, e.g. College B at **₹9 lakh with a ₹6 LPA median**, so the choice is genuinely balanced and tricks have room to move people. Also add a **parent persona** (parents often decide), and a version where the median salary is **hidden** (only the highest package shown), which is what real ads do.
