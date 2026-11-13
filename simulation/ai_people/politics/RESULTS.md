# World politics: results (13 Nov 2026)
- **Design and predictions:** saved first in `PREDICTIONS.md`. The research is in `RESEARCH.md`.
- **Data:** **336 decisions, all usable**; **48 AI people from 8 countries** (India, USA, Brazil, UK, Poland, Nigeria, Turkey, South Korea).
  - 32 are party supporters (16 strong, 16 mild; 4 per country, 2 on each side).
  - 16 have no party.
- **The test:** every person rated the **same invented policy** (six months of paid community work and job training for every 18-year-old) seven times, with a different label or style each time. Support is on a 1–7 scale.
- The full numbers are in `output/combined_analysis.txt`.
- ⚠ **Read the results as directions.** See the limits at the end, especially the first one.

## Support for the same policy, by who proposed it
| Version | Party supporters | Strong supporters | Mild supporters | No party |
|---|---|---|---|---|
| "A group of economists" | 5.0 | 5.4 | 4.6 | 4.4 |
| **Their own party** | **5.5** | 5.9 | 5.1 | 3.9 |
| **The rival party** | **2.9** | 2.5 | 3.2 | 3.8 |
| Own party, rally style ("the elites… jobs, jobs, jobs") | 5.6 | 6.1 | 5.1 | 3.5 |
| Rival party, rally style | 2.8 | 2.6 | 3.1 | 3.8 |
| Own party + an independent fact-check of its claim | 5.3 | 5.8 | 4.9 | 3.7 |
| Own party + "two years ago your party called this 'forced labour'" | 5.0 | 5.4 | 4.5 | 3.4 |

**Own-party minus rival-party gap, by country** (4 supporters each):

| Turkey | UK | Brazil | Poland | South Korea | USA | Nigeria | India |
|---|---|---|---|---|---|---|---|
| +3.2 | +3.0 | +2.8 | +2.8 | +2.5 | +2.2 | +2.2 | +2.0 |

## The 6 main findings
1. **The label decided the rating.**
   - The same words scored **5.5 from their own party and 2.9 from the rival**, a gap of 2.6 points on a 7-point scale.
   - **All 32 supporters rated their own party's version higher.** It happened in all 8 countries and equally on both sides of each rivalry (+2.6 and +2.6).
   - *"Olha, é uma ideia da PT, então já começo com desconfiança."* ("Look, it's a PT idea, so I start out suspicious.") (a PL supporter, Brazil)
   - *"PT proposed it, so I'm with it."* (a PT supporter, Brazil)
2. **Disliking the rival mattered far more than liking your own side.**
   - Compared with the neutral "economists" version, the own-party label added only **+0.5**, while the rival label took away **−2.1**.
   - This is "negative partisanship", as Samuels & Zucco found in Brazil: people know what they are *against* more firmly than what they are for.
3. **People with no party didn't follow the labels** (3.9 vs 3.8).
   - But they liked the policy **less whenever any party's name was on it** (4.4 from economists, 3.4–3.9 from parties). For them, a party label is a mark against an idea.
4. **Speaking style added almost nothing.**
   - The rally-style speech scored about the same as the plain version (5.6 vs 5.5 from their own party; 2.8 vs 2.9 from the rival).
   - People with no party liked the rally style least (3.5).
   - **Who speaks mattered; how they speak barely did.** This matches the healthcare result (the messenger beats the message).
5. **A fact-check and a U-turn reminder barely dented support.**
   - After an independent fact-check of the party's claim, support fell by only **0.2 points**.
   - After being told their own party had called the same idea "forced labour", it fell by **0.5 points**. Some noticed and excused it: *"I noticed the flip-flop and it bothers me some. But this isn't the same as what the Republicans pushed."* (a Democrat, USA)
   - This matches Nyhan et al. (2020): supporters accept a correction "literally but not seriously".
6. **Strength of loyalty and decision style both mattered.**
   - Strong supporters: a gap of 3.4; mild supporters: 1.8.
   - "Gut" deciders: 4.0; "very careful" deciders: 1.8. Careful AI people still showed a clear gap.

## What didn't work
- **The belief question failed.** Almost nobody believed the "cut unemployment in half" claim in any version (0–12%), so the fact-check couldn't lower belief further. The claim was too obviously exaggerated. A milder claim is needed to test this.
- Still, the only people who believed it at all were supporters hearing it from **their own party** (12%, against 0% from the rival).

## Predictions check
| # | Prediction | Result | ✓/✗ |
|---|---|---|---|
| 1 | With no label, both sides rate it about the same (gap under 0.5) | 5.1 vs 4.9 | ✅ |
| 2 | Own-vs-rival gap of at least 1.5 points | 2.6 | ✅ |
| 3 | The rival label hurts more than the own label helps | −2.1 vs +0.5 | ✅ |
| 4 | People with no party barely move | gap 0.1 | ✅ |
| 5 | Strong loyalists show a bigger gap | 3.4 vs 1.8 | ✅ |
| 6 | Rally style: a small gain from own party, a clear loss from the rival | +0.1 and −0.1 | 🟡 no extra loss |
| 7 | Fact-check: belief falls sharply; support falls by under 1 point | belief untestable; support −0.2 | 🟡 half |
| 8 | U-turn: support falls by under 1 point, with excuses | −0.5; few clear excuses | 🟡 |
| 9 | "Very careful" people show a smaller gap | 1.8 vs 4.0 for gut | ✅ |
| 10 | Same direction in at least 6 of 8 countries | 8 of 8 | ✅ |

**7 right, 3 partly, 0 wrong.**

## Limits
1. **The loyalty was written into the AI people.** Each supporter's instructions said they support one party and dislike (or are "not keen on") its rival. So some of the label effect is the AI doing what it was told, not a discovery.
   - What the experiment *can* show is the shape of the effect: it comes mostly from disliking the rival, it resists fact-checks and U-turn reminders, and it is absent in people with no party.
   - **The size (2.6 points) should not be quoted as a human number.**
2. **A result this clean is a warning sign.** 32 of 32 is tidier than real people would be. Real experiments find weaker cue effects when a policy is familiar or affects people directly (Bullock 2011; Slothuus & Bisgaard 2021).
3. **One invented policy with no real history.** Real policies carry history, and in some countries (South Korea, Turkey) national service already has a strong meaning.
4. **The AI model knows some countries' politics better than others**, and party systems change; the party pairs reflect the model's knowledge, not today's news.
5. **4 supporters per country:** the country differences mean nothing; only the shared direction does.
6. One AI model (Claude Haiku), text only, 48 people.
