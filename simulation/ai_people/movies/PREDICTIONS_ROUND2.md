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
