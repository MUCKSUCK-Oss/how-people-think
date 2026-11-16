# Movies round 2: predictions (written 16 Nov 2026, BEFORE any data)
*Design: `ROUND2_PLAN.md`. Maulik approved the plan and the pilot on 16 Nov ("yes go on with pilot"). These predictions are committed before the pilot runs and will not be changed afterwards.*

## Setup
- **People:** 24 AI people aged 17–24 in 8 countries (India, the USA, the UK, South Korea, Turkey, Brazil, Nigeria, Indonesia), 3 per country:
  - one leans towards the **ruling party**;
  - one leans towards the **main opposition party**;
  - one leans towards **neither**.
  - Parties are never named. Decision styles go from gut to very careful.
  - If the pilot works, a second batch of 24 is added for 48 in total.
- **The film:** *The Last Signal*, an invented spy thriller set two years after a bombing in the capital. In one scene, a **senior politician secretly sells the agents' location to the enemy**.
- **The 6 versions** (each person sees all of them, each in a fresh call):

| Version | Notice | Villain politician's party |
|---|---|---|
| `no_film` | – (baseline) | – |
| `opp_nolabel` | none | opposition |
| `opp_real` | "Inspired by real events." | opposition |
| `opp_fiction` | "A work of fiction; any resemblance is coincidental." | opposition |
| `opp_corrected` | "Inspired by real events" + "the politician's betrayal is invented; no such case has been found" | opposition |
| `ruling_real` | "Inspired by real events." | **ruling** (mirror) |

- **Questions** (1–7 each):
  - **BELIEVE_RULING:** how likely it is that a senior politician from the ruling party has, in real life, secretly passed secret information to an enemy country.
  - **BELIEVE_OPP:** the same question for the opposition.
  - **TRUST_AGENCY:** trust in your country's intelligence agency.
  - **For films only:** ENJOY, and PROPAGANDA (how much the film pushes a political message).
  - **REASON:** in their own words.
- **"Villain belief"** means BELIEVE_OPP in the `opp_*` versions and BELIEVE_RULING in `ruling_real`.

## Predictions
1. **Baseline:** both BELIEVE scores are between 2.5 and 4.5. Each partisan rates the *other* party as more likely to betray, by at least 0.5 (ruling supporters: OPP > RULING; opposition supporters: RULING > OPP).
2. **The film plants the idea:** `opp_nolabel` raises BELIEVE_OPP by at least 0.3 over no film, while BELIEVE_RULING moves less than 0.3.
3. **"Inspired by real events" adds to it:** BELIEVE_OPP in `opp_real` is at least 0.2 higher than in `opp_nolabel`. *(Unsure: Hartung et al. 2017 found that true/fiction labels changed little.)*
4. **A general disclaimer barely helps** (Butler et al. 2009): BELIEVE_OPP in `opp_fiction` is within 0.3 of `opp_nolabel`.
5. **A specific correction works** (Butler et al. 2009): BELIEVE_OPP in `opp_corrected` is at least 0.4 lower than in `opp_real` and within 0.3 of no film.
6. **The mirror (own side protected):** in the "inspired by real events" versions, villain belief rises less when the villain is from **your own** party than when it's from the other party, by at least 0.3.
7. **The mirror (propaganda by side):** people whose own party is the villain rate the film at least 0.5 higher on PROPAGANDA than people from the other party.
8. **The new propaganda scale works:** the mean PROPAGANDA across film versions is between 2.5 and 5.5, with a standard deviation of at least 1.0 (no ceiling like round 1).
9. **The hero agent helps the agency:** TRUST_AGENCY in film versions averages at least 0.2 above no film.
10. **The "neither" group moves most:** their rise in villain belief (`opp_real` vs no film) is at least as big as either partisan group's.
11. **Labels don't spoil the film:** ENJOY across the 5 film versions stays within 0.5.
12. **Gut vs careful:** gut deciders' rise in villain belief (`opp_real` vs no film) is bigger than very careful deciders'.

## What would surprise me
- If the specific correction does **not** lower belief, then Butler's "specific warnings work" didn't transfer to AI people.
- If partisans **don't** protect their own party, Haiku may be trained to answer in a neutral, non-partisan way, which is a limit of the method, not proof that real people are fair.

---

## Pilot result (16 Nov 2026, added AFTER the data; the predictions above are unchanged)
**144 of 144 answers were usable**: 24 people × 6 versions. No one gave identical answers in all 6 versions. Full numbers: `output/r2_pilot_analysis.txt`. ⚠ With **8 people per political leaning**, read these as directions, not sizes.

| # | Prediction | Result | ✓/✗ |
|---|---|---|---|
| 1 | Baseline 2.5–4.5; each side blames the other party more (≥0.5) | OPP 3.38, RULING 3.67; ruling supporters +1.62, opposition supporters −2.50 | ✅ |
| 2 | Film raises BELIEVE_OPP ≥0.3; BELIEVE_RULING moves <0.3 | OPP +0.54 ✅, but RULING **fell 0.42** (the film also made people trust the *other* party more) | 🟡 |
| 3 | "Inspired by real events" adds ≥0.2 over no label | 3.67 vs 3.92: **0.25 lower** | ❌ |
| 4 | General "fiction" disclaimer within 0.3 of no label | 3.92 vs 3.92 | ✅ |
| 5 | Specific correction ≥0.4 below "real" and within 0.3 of no film | 3.25 vs 3.67 (−0.42); no film 3.38 | ✅ |
| 6 | Own party protected: villain belief rises ≥0.3 less when it's your party | **The opposite:** own party +0.69 vs other party 0.00 | ❌ |
| 7 | Own party as villain → PROPAGANDA ≥0.5 higher | 5.88 vs 5.50 (+0.38: right direction, too small) | ❌ |
| 8 | PROPAGANDA mean 2.5–5.5, SD ≥1.0 | Mean 5.88, SD 0.66; 92 of 120 answers were 6 or 7 | ❌ |
| 9 | The agency's trust rises ≥0.2 | 3.88 → about 4.4 across films (+0.55) | ✅ |
| 10 | The "neither" group moves most | Neither −0.25; opposition +1.00 | ❌ |
| 11 | ENJOY within 0.5 across film versions | 5.17–5.54 | ✅ |
| 12 | Gut deciders move more than very careful ones | +0.33 vs 0.00 (6 people each) | ✅ |

**6 right, 1 partly, 5 wrong.**

**What the pilot shows:**
1. **Only a specific correction worked (Butler et al. 2009 reproduced in AI people).**
   - "This is fiction" changed nothing (3.92 = no label).
   - "The betrayal was invented; no such case exists" brought belief back to the no-film level. 9 of 24 people lowered their belief vs no film, 8 raised it.
2. **"Inspired by real events" did not make the invented betrayal more believable.** It was slightly lower. That fits Hartung et al. 2017 (labels change little).
   - Some AI people seemed to read the label as a trick: *"The 'inspired by real events' thing at the start felt designed to make me take it more seriously"* (a neutral viewer, India).
3. **Party loyalty did NOT protect people. Everyone moved toward the film's message.**
   - When the villain was from **their own** party, people raised their belief that their own party's politicians could betray the country (+0.69). They also rated that film as **more** propaganda (5.88 vs 5.50).
   - **Spotting it didn't stop it working** (same as round 1's "rules work" film).
   - The partisan gap shrank whenever the film's villain was a person's own party:
     - ruling supporters: +1.62 → +0.88;
     - opposition supporters: −2.50 → −0.50.
   - **A caution:** opposition supporters' gap also shrank in the mirror version (−2.50 → −1.62), where the film agreed with them. So part of this is AI people **moving towards the middle after any political film**, not real persuasion.
   - Real partisans usually defend their side (Vallone et al. 1985). **The AI people didn't, which is a known limit:** the model seems trained to answer in a balanced way ("corruption exists in all parties").
4. **The film also changed views of the party that *wasn't* in it.** After the opposition-villain film, belief that ruling-party politicians betray the country **fell** (−0.42 to −0.71). **Making one side the villain cleans up the other side's image.**
5. **The propaganda scale hit the ceiling again,** this time on 1–7 (mean 5.88). AI people call any political film propaganda, whatever the label. The question can't separate the versions. This is a method limit for both rounds.

**Should an extra batch run?**
- The design works: all answers usable, no copy-paste answers, and clear differences between versions.
- But results 3 (mirror) and 4 rest on 8 people per leaning, so a second batch of 24 would test whether they hold.
- **The propaganda question will stay unchanged,** so the two batches can be pooled (same rule as round 1).
