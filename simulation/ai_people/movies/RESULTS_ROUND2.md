# Movies round 2: "inspired by real events", disclaimers and the party mirror (results, 16 Nov 2026)
- **Design and predictions:** saved before any data in `ROUND2_PLAN.md` and `PREDICTIONS_ROUND2.md`. The research is in `RESEARCH.md` and `sources/topic_notes/youtube_day_2026-11-16.md`.
- **Data:** **288 answers, all usable.** 48 AI people aged 17–24 in 8 countries (India, the USA, the UK, South Korea, Turkey, Brazil, Nigeria, Indonesia), 6 per country: 2 lean towards the ruling party, 2 towards the main opposition, 2 towards neither. Parties are never named.
  - Each person saw all 6 versions, each in a fresh call.
  - Pilot (24 people) and extra batch (24 new people, same design) were pooled.
  - No one gave identical answers in all versions.
  - Full numbers: `output/r2_combined_analysis.txt`.
- **The film:** *The Last Signal*, an invented spy thriller. Two years after a bombing, an intelligence officer stops a second attack. In one scene, **a senior politician sells the agents' location to the enemy**. That scene is invented.
- ⚠ **Small groups:** 16 people per leaning, on a 1–7 scale. **Read the results as directions, not sizes.**

## Mean answers (1–7)
"Betray" = how likely it is that a senior politician from that party has secretly passed secrets to an enemy country in real life.

| Version | Opposition might betray | Ruling party might betray | Trust in the intelligence agency | Enjoyed | Felt like propaganda |
|---|---|---|---|---|---|
| No film | 3.54 | 3.75 | 3.83 | – | – |
| Film, no label (villain: **opposition**) | 3.92 | 3.29 | 4.42 | 5.40 | 6.06 |
| + "**Inspired by real events**" | 3.67 | 3.06 | 4.21 | 5.29 | 5.92 |
| + "**A work of fiction**; any resemblance is coincidental" | 3.77 | 3.29 | 4.50 | 5.35 | 6.02 |
| + "Inspired by real events" + "**the politician's betrayal was invented; no such case has been found**" | **3.25** | 3.10 | 4.48 | 5.31 | 5.94 |
| **Mirror:** "inspired by real events", villain from the **ruling** party | 3.46 | **3.90** | 4.50 | 5.44 | 5.58 |

## The 5 main findings
1. **Only a specific correction undid the invented scene. A general "this is fiction" notice did nothing.**
   - Belief that opposition politicians betray the country:
     - after the film with **no label**: 3.92;
     - with the **general fiction disclaimer**: 3.77 (almost no change);
     - with **"the betrayal was invented, no such case exists"**: **3.25**, slightly *below* the no-film level (3.54).
   - **20 of 48 people lowered their belief and 10 raised it.**
   - This matches the real study on history films (Butler et al. 2009): only a warning about the *specific* error stopped people remembering it.
   - **Real-world parallel:** India's Supreme Court ordered *The Kerala Story* to state there was "no authentic data" for its 32,000 figure, a specific correction, not just "this is fiction".
   - *"The disclaimer at the start actually made me think about what I was watching."* (a neutral viewer, India)
2. **"Inspired by real events" did NOT make the invented betrayal more believable.**
   - It was slightly *lower* than no label (3.67 vs 3.92).
   - This fits Hartung et al. (2017), where calling a story "true" changed little.
   - Some AI people seemed to see the label as a trick: *"The 'inspired by real events' thing at the start felt designed to make me take it more seriously."* (a neutral viewer, India)
3. **Party loyalty did not protect people, the opposite of my prediction.**
   - When the villain came from a person's **own** party, belief that their own party's politicians could betray the country **rose** (+0.59).
   - When the villain came from the **other** party, it didn't rise (−0.09).
   - **The same pattern appeared in both batches** (pilot +0.69 vs 0.00; extra +0.50 vs −0.19) **and in both groups:**
     - ruling supporters, mirror film: **6 rose, 0 fell**;
     - opposition supporters, opposition-villain film: **10 rose, 1 fell**.
   - **They noticed and still moved.** People rated the film about their own party as slightly more propaganda (5.81 vs 5.66), as in round 1's "rules work" film.
   - ⚠ **Two cautions:**
     - **(a) Room to move.** People started by rating their own party very low (about 2.4–2.8) and the other party already high (about 4.4–4.7). Part of this is beliefs **moving towards the middle**, not real persuasion.
     - **(b) Real partisans don't usually behave like this.** In the classic "hostile media" study (Vallone et al. 1985), both sides defended their own. The AI model seems trained to answer in a balanced way: *"Corruption exists in all parties"* (an opposition supporter, India). **This is probably a limit of AI people, and a warning that they may underestimate partisan defence.**
4. **Making one party the villain cleaned up the other party's image, but only one way.**
   - After the films with an **opposition** villain, belief that **ruling-party** politicians would betray the country **fell** by 0.46 to 0.69, though the ruling party wasn't in the film.
   - After the **mirror** film, belief about the opposition hardly changed (−0.08).
   - A possible reason: the hero is the state's intelligence agency, so a film about a traitor *outside* the government also makes the government side look good.
   - **Trust in the agency rose in every film version** (+0.38 to +0.67 over no film).
5. **The propaganda question hit the ceiling again.**
   - Even on a 1–7 scale, the average was **5.90**, and 190 of 240 answers were 6 or 7.
   - AI people call any political film propaganda, whatever the label. So this question can't separate the versions (the same problem as round 1).

**Other results:**
- **Enjoyment** stayed almost the same in every version (5.29–5.44). **No label spoiled the film.**
- **Neutral people barely moved** (villain belief −0.25 to +0.06 in the "inspired by real events" versions). Partisans moved most, mostly about their own party.

## Predictions check
| # | Prediction | Result | ✓/✗ |
|---|---|---|---|
| 1 | Baseline 2.5–4.5; each side blames the other party more (≥0.5) | 3.54 and 3.75; ruling supporters +1.62, opposition supporters −2.25 | ✅ |
| 2 | Film raises "opposition might betray" ≥0.3; "ruling might betray" moves <0.3 | +0.38 ✅; but ruling **fell 0.46** | 🟡 |
| 3 | "Inspired by real events" adds ≥0.2 over no label | **0.25 lower** | ❌ |
| 4 | General disclaimer within 0.3 of no label | 3.77 vs 3.92 | ✅ |
| 5 | Specific correction ≥0.4 below "real" and within 0.3 of no film | 3.25 vs 3.67 (−0.42); no film 3.54 (−0.29) | ✅ |
| 6 | Own party protected (rises ≥0.3 less) | **The opposite:** own +0.59, other −0.09 | ❌ |
| 7 | Own-party villain → propaganda ≥0.5 higher | 5.81 vs 5.66 (+0.15) | ❌ |
| 8 | Propaganda mean 2.5–5.5, SD ≥1.0 | 5.90, SD 0.67 | ❌ |
| 9 | Trust in the agency rises ≥0.2 | +0.59 on average | ✅ |
| 10 | The "neither" group moves most | Neither −0.25; opposition +0.69 | ❌ |
| 11 | Enjoyment within 0.5 across labels | 5.29–5.44 | ✅ |
| 12 | Gut deciders move more than very careful ones | 0.00 vs 0.00 (pilot showed +0.33 vs 0; the extra batch erased it) | ❌ |

**5 right, 1 partly, 6 wrong.**
- **What I got wrong:** I expected the "true story" label to add belief, partisans to protect their own side, and neutral people to move most. **None of these happened.**
- **What held up:** the labels-and-corrections part, which is closest to the real evidence (Butler 2009). A specific correction worked; a general disclaimer didn't.
- **Prediction 12 is a reminder about small groups:** it "passed" in the pilot with 6 people per group, then disappeared with 12.

## What this adds to the project
- **For the disclosure question that runs through the paper** (universities, healthcare, secret agencies, round 1's "the ministry approved this"):
  - **Telling people *who* made something** (round 1) and **telling them *what exactly* is false** (round 2) both worked.
  - **Vague labels** ("fiction", "inspired by real events") didn't.
- **For films like *The Kerala Story*, *The Kashmir Files* and *Dhurandhar*:** the fight over "fiction" vs "true story" labels may matter less than people think. **Correcting the specific invented claim** is what changed belief here.
- **For Section 1.1 (persuasion vs manipulation):** people noticed the bias and were still moved. That shows again why "it's fine if people can notice" is too weak a test.

## Limits
- **48 AI people, one model (Claude Haiku),** reading a 200-word summary, not watching a film.
- **AI people seem trained to be balanced,** so the partisan results probably **underestimate** how real partisans defend their side. Result 3 should not be read as "real voters are fair-minded".
- **Unnamed parties** ("the ruling party") are less emotional than real names.
- **The propaganda question failed again** (ceiling).
- **Room to move:** people rated their own party very low at the start, so some of result 3 is movement towards the middle.
- **Each version was a fresh call;** people never compared versions.
- **Usage:** each batch of 144 answers took about 50–60 minutes, slower than round 1.
