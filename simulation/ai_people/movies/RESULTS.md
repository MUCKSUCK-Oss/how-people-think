# Movies and propaganda: results (15 Nov 2026)
- **Design and predictions:** saved first in `PREDICTIONS.md`. The research is in `RESEARCH.md`.
- **Data:** **336 decisions, all usable**. 48 AI people aged 17–24 in 8 countries (India, the USA, the UK, South Korea, Turkey, Brazil, Nigeria, Indonesia), 6 per country: 2 proud of their own military, 2 neutral, 2 critical. Each saw all 7 versions. The full numbers are in `output/combined_analysis.txt`.
- **The films:** scene-by-scene summaries (190–230 words) of invented films about "your country's army". No real film, war or unit is named.
- ⚠ **Small groups:** 16 people per starting view, and the scales go from 1 to 7. **Read the results as directions, not exact sizes.** Most changes are under half a point.

## Mean answers (1–7)
| Version | Trust in the military | Interest in joining | Support for harsh interrogation | Enjoyed the film |
|---|---|---|---|---|
| No film (baseline) | 3.83 | 2.67 | 2.46 | – |
| **Heroic** ("no one left behind") | 4.04 | 2.94 | 2.15 | 5.21 |
| **Critical** (civilians killed, cover-up) | **2.50** | 2.21 | 1.81 | 4.00 |
| Heroic + "**the ministry approved the script and final cut**" | 3.77 | 2.62 | 2.04 | 4.92 |
| Heroic + "**the ministry had a civilian-death scene removed**" | **3.40** | 2.50 | 1.94 | 4.81 |
| Heroic + "this film is fictional" | 3.85 | 2.69 | 1.85 | 5.23 |
| **"Breaking rules works"** (harsh interrogation saves a school) | 3.25 | 2.60 | **3.21** | 4.48 |

**Did the film feel like propaganda?** "Yes" from **100% of people in every film version**, including the critical film and the fiction one. So this question couldn't tell the versions apart (see Limits).

## The 5 main findings
1. **Telling people the ministry approved the film cancelled its small effect on trust, but they still enjoyed it.**
   - The hero film raised trust a little (+0.21). With the approval notice, trust stayed at the no-film level (−0.06), while enjoyment fell only slightly (5.21 → 4.92).
   - This is the gap the research found: no real study has tested this notice. Here it worked like a "sponsored" label on an advert (Eisend 2020): people kept the entertainment and dropped the message.
   - *"The notice at the start basically told me the military approved everything, so yeah, I could tell what was happening."* (a neutral viewer, the USA)
2. **Saying what was cut hurt more than saying who approved it.**
   - "The ministry asked the makers to remove a scene of soldiers killing a civilian family" pushed trust **below** the no-film level (−0.44); 23 of 48 people trusted the military less than with no film.
   - Proud people dropped the most (−0.62). The notice turned a hero film into evidence of a cover-up.
   - *"If they asked to remove a scene about soldiers killing civilians, they're not giving me the real story."* (a neutral viewer, India)
3. **One critical film moved trust six times more than one hero film** (−1.33 vs +0.21).
   - The biggest drop was among **proud** people (5.38 → 3.31), the group with the most to lose. Critical people dropped least, as they were already low.
   - Bad news seems to move people more than good news. It may also be that the AI found the cover-up story more believable than a perfect rescue.
4. **The "breaking rules works" film raised support for harsh interrogation, even though everyone called it propaganda.**
   - Support went up by 0.75, and **27 of 48 people** gave a higher score than with no film (7 gave lower).
   - The biggest change was in the **neutral** group (2.44 → 3.81), not the proud.
   - *"The whole thing was propaganda trying to convince me torture is okay."* (a neutral viewer, the USA, who still raised their score after the film). **Spotting the trick didn't stop it working.** This matches the research on *24*.
5. **Critical people didn't push back, and the hero film didn't change them much either.**
   - I predicted a backfire (Yao 2024), but critical people's trust went up a little (+0.31). Proud people didn't move at all (they were already high).
   - Many said something like: the story moved me, but it doesn't answer my real worries. *"A touching story doesn't answer my real concerns about military power and who holds them accountable."* (a critical viewer, India)

**A surprise:** every hero version **lowered** support for harsh interrogation (heroic −0.31; 19 of 48 lower, 8 higher). Seeing soldiers as caring people may make cruelty feel less acceptable. Or the question may simply sound different when asked straight after a film.

**Gut vs careful:** gut deciders' trust rose with the hero film (+0.50); very careful deciders' didn't (−0.08).

## Predictions check
| # | Prediction | Result | ✓/✗ |
|---|---|---|---|
| 1 | No film: JOIN 2.0–4.0, TRUST 3.5–5.5 | 2.67 and 3.83 | ✅ |
| 2 | Heroic raises JOIN by ≥0.3 and TRUST by ≥0.4 | +0.27 and +0.21 (right direction, smaller) | ❌ |
| 3 | The neutral group's trust moves most | Neutral +0.31 = critical +0.31; proud 0 | 🟡 |
| 4 | Critical people backfire | Their trust rose (+0.31) | ❌ |
| 5 | The critical film cuts trust by ≥0.5, most in proud people | −1.33; proud −2.06 | ✅ |
| 6 | Approval notice: trust gain at most half; enjoyment within 0.5; propaganda +20 points | −0.06 vs +0.21 ✅; 4.92 vs 5.21 ✅; propaganda untestable | ✅ (2 parts) |
| 7 | The cut-scene notice lowers trust ≥0.3 more than the approval notice | 3.40 vs 3.77 (0.37) | ✅ |
| 8 | Disclosure raises "propaganda" most for critical people | Everyone said yes everywhere | ⚪ untestable |
| 9 | "It's fiction" stays within 0.3 of heroic | Trust 0.19 and JOIN 0.25 apart | ✅ |
| 10 | Rules-work film raises interrogation support by ≥0.7, most in proud people | +0.75 ✅, but most in neutral | 🟡 |
| 11 | Fewer people call the rules-work film propaganda | 100% everywhere | ⚪ untestable |
| 12 | Gut deciders move more than very careful ones | +0.50 vs −0.08 | ✅ |

**6 right, 2 partly, 2 wrong, 2 untestable.**
- **What I got wrong:** I expected one hero film to move people more, and critical people to push back. Instead the hero film barely moved anyone, while the critical film and the "rules work" film moved people much more.
- **Prediction 9 is a weak pass:** the hero film's effect was so small that "close to heroic" was also "close to no film". The test couldn't really show whether the fiction notice did anything.

## Limits
- **48 AI people, one AI model (Claude Haiku),** reading a short summary, not watching a 2-hour film with music and faces. Real films probably move people more.
- **The propaganda question failed.** The AI people called **everything** propaganda, which real teenagers would not (most real viewers don't think of hero films that way). This matches the known limit that AI people are more suspicious than real people. The question also said "for or against", which may have made "yes" too easy.
- **One viewing only.** It can't test years of exposure, which is where the real evidence of change is (cultivation research).
- **"Your country's army"** means very different things in the USA, Nigeria and South Korea, but with 6 people per country the country differences can't be trusted.
- **Each version was a separate fresh call,** so people couldn't compare versions.
- **Usage:** each batch of 168 took about 25 minutes.
