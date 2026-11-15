# Movies round 2: "inspired by real events" and the mirror test (PLAN, not run)
*Drafted 16 Nov 2026 for Maulik to approve or change. Nothing has been run, and the predictions are not written yet. Labels: [read] = I read the source itself; [summary] = from search results or secondary summaries.*

## The question
**Does "inspired by real events" make an invented scene feel true? Does a disclaimer undo that? And do people judge the same film differently depending on which political party is the villain?**

This is the *Dhurandhar* problem (RESEARCH.md F4): real events mixed with invented scenes, where the invented part blames a political side.

## Why this test (evidence)
- **Real "true story" labels may change little:**
  - Hartung et al. 2017 (*Frontiers in Psychology*, 1,742 readers) found that calling a story "true" or "fiction" made **no difference** to how people read it [summary].
  - Ebert & Meyvis 2014: people *expect* true stories to hit harder, but they felt about equally sad either way [summary].
  - **So the label might not matter, which is a real possibility the test can find.**
- **Films plant false memories, and only specific warnings stop it:**
  - Butler et al. 2009 (*Psychological Science*): when a history film clip contradicted the textbook, students remembered the film's version up to **half the time**, with high confidence [summary].
  - A **general** "films can be inaccurate" warning did **not** help. A **specific** warning about the exact error **removed** the effect [summary].
  - This is the most useful study for this test.
- **People see bias against their own side:** in the "hostile media" study (Vallone, Ross & Lepper 1985), supporters of both sides judged the **same** news coverage as biased against them. Later replications are mixed [summary].
- **Our round 1:** "it's fiction" did nothing measurable (the hero film's effect was too small to test that). Here the invented scene is **specific** (one politician betraying the country), so belief in it can be measured directly.

## Design (within-subject, like round 1)
- **People:** 48 AI people aged 17–24, in the same 8 countries, 6 per country:
  - 2 lean towards the **ruling party**
  - 2 lean towards the **main opposition**
  - 2 lean towards **neither**
- **Parties are never named:** only "the ruling party" and "the main opposition party", so the test works in every country and doesn't take a side.
- **The film:** an invented spy thriller about "your country's intelligence agency" stopping an attack, "set around a real bombing in your country's recent past". In one scene, **a senior politician secretly passes the agents' location to the enemy**. That scene is invented.

| # | Version | What changes |
|---|---|---|
| 1 | **No film** (baseline) | An ordinary week, same questions |
| 2 | **Film, no label** | Villain politician from the **opposition** |
| 3 | **"Inspired by real events"** | Villain from the opposition |
| 4 | **General disclaimer** ("a work of fiction; any resemblance is coincidental") | Villain from the opposition |
| 5 | **"Inspired by real events" + specific correction** ("the politician's betrayal is invented; no such case is known") | Villain from the opposition (the Butler test) |
| 6 | **Mirror:** "inspired by real events" | Villain from the **ruling party** |

### Questions (every version)
- **BELIEVE_RULING / BELIEVE_OPP** (1–7): how likely is it that a senior politician from this party has secretly helped an enemy country in real life?
  - Both are always asked, so we can see whether the film moves belief about the villain's party only.
- **TRUST_AGENCY** (1–7): trust in your country's intelligence agency.
- **PROPAGANDA** (1–7 scale this time, not yes/no): how much the film feels like it's pushing a political message.
  - This is the fix for round 1's 100% ceiling.
  - For film versions only, like **ENJOY** (1–7).
- **REASON:** one or two sentences.

### Size
- **Pilot:** 24 people × 6 versions = **144 answers**, about 20 minutes.
- **Extra batch:** another 24 people (144 answers) if the pilot works.
- **Total:** 288.

## What it can show
1. **Does "inspired by real events" raise belief** in the invented betrayal compared with no label (3 vs 2)?
2. **Does a general disclaimer help** (4 vs 3)? Butler says no.
3. **Does a specific correction help** (5 vs 3)? Butler says yes.
4. **Mirror:**
   - Do opposition supporters believe the betrayal story less when their own party is the villain (6 vs 3, by leaning)?
   - Do they rate the film as more propaganda?
5. **Does the film spread to trust in the agency?**

## Left out (for later, if wanted)
- **Idea 3, agency type** (army vs spy agency vs police): it needs a different film text, so it's better as its own small test.
- **Idea 4, the "report suspicious people" ending** (the MSS model): it's interesting, but it's about surveillance, not fact vs fiction. It could be round 3.

## Risks and limits (known before running)
- **Short text, not a film:** AI people read a ~200-word summary, as in round 1.
- **AI people are suspicious:** they may distrust every label (round 1's ceiling). The 1–7 scale should help.
- **Unnamed parties:** "the ruling party" is less emotional than a real name, so partisan effects will probably be **smaller** than in real life.
- **One model (Claude Haiku):** it may be trained to avoid partisan answers, which could hide the mirror effect.

## Sources
- [Hartung et al. 2017, *Frontiers in Psychology*](https://frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.01618/text) [summary]
- [Ebert & Meyvis 2014 (Brandeis news release)](https://www.brandeis.edu/now/2014/september/ebert-factorfiction.html) [summary]
- [Butler et al. 2009 (WashU news release)](https://source.washu.edu/2009/08/historical-movies-help-students-learn-but-separating-fact-from-fiction-can-be-challenge/); [ScienceDaily](https://www.sciencedaily.com/releases/2009/08/090805171112.htm) [summary]
- [Christen et al. 2002 on the hostile media effect, citing Vallone et al. 1985](https://terpconnect.umd.edu/~nan/738readings/Christen%20et%20al%202002%20hostile%20media.pdf) [summary]
