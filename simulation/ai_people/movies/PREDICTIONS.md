# Movies and propaganda: design and predictions
*Draft, 15 Nov 2026. Written BEFORE any data and built from `RESEARCH.md` (Part E). It becomes final only when Maulik approves it (and adds their own ideas, if any). No simulation has been run.*

## The idea
Real cases show that militaries help make films and shape the script (the Pentagon's 800+ films, China's *Wolf Warrior*, India's tax-free films). The research found one clear gap: **no study tells viewers "the defence ministry approved this script" and then measures what changes.** This simulation tests that, plus the "no soldier left behind" hero story, a critical film and a "breaking rules works" film.

**Everything is invented:** the films, the soldiers and the events. Each person hears about **their own country's** army and defence ministry, but no real unit, war or film is named.

## Who (24 people in the pilot)
- **Aged 17–24**, the age when people choose whether to join.
- **8 countries:** India, the USA, the UK, South Korea, Turkey, Brazil, Nigeria, Indonesia.
  - South Korea and Turkey have compulsory service, so they are asked about joining as a **career** (signing up for longer than they have to).
  - The rest mix democracies of different sizes and regions.
- **3 starting views of their own military:**
  - **proud:** mostly admires the armed forces;
  - **neutral:** has never thought much about it;
  - **critical:** mostly distrusts the armed forces.
- **Lesson from the secret-agencies study:** there, views were written as fixed rules, so only the "unsure" group could move. Here the views are written as **leanings, not certainties** ("mostly", "tends to"), so proud and critical people can also move.
- Gender, studies or job, and decision style (gut to very careful) vary.

## The 7 versions (every person sees every one, each in a fresh call)
Each film is a scene-by-scene summary of about 250 words (the same length for every film).

| Version | The person reads | Tests |
|---|---|---|
| **no_film** | A short everyday description of their week (no film) | Baseline |
| **heroic** | *The Long Night Home*: a patrol is ambushed, a wounded young medic is trapped behind enemy lines, the sergeant goes back for her against orders, and everyone comes home. Ends with a crowded welcome at the airport. | The "no soldier left behind" story |
| **critical** | Same unit and same actors, but in a village raid two soldiers kill unarmed civilians and the commander covers it up. A young soldier reports it and is punished. | The opposite story |
| **heroic_approved** | A notice first: "This film was made with the help of the Ministry of Defence, which gave equipment and advisers and approved the script and the final cut." Then the heroic film. | **The new test:** disclosing approval |
| **heroic_cut** | A notice first: "The Ministry of Defence helped make this film. It asked the makers to remove a scene in which soldiers accidentally kill a civilian family; the makers agreed." Then the heroic film. | Disclosing what was left out |
| **heroic_fiction** | A notice first: "This film is fictional. The characters and events are invented." Then the heroic film. | The *Kerala Story*-style disclaimer |
| **rules_work** | *Twelve Hours*: a captured man knows where a bomb is hidden. An officer breaks the rules and uses harsh, painful interrogation (described briefly, not in detail); the man talks and the city is saved. | "Torture works" stories (*24*, *Zero Dark Thirty*) |

## Answer format
- **JOIN:** 1–7. How interested are you in joining the armed forces (South Korea and Turkey: as a career)?
- **TRUST:** 1–7. How much do you trust your country's armed forces?
- **INTERROGATE:** 1–7. Should officers ever be allowed to use harsh, painful interrogation on a suspect to stop an attack? (Asked in every version, so `rules_work` can be compared with `no_film`.)
- **ENJOY:** 1–7. How much would you enjoy watching this film? (Film versions only.)
- **PROPAGANDA:** yes or no. Did the film feel like it was trying to sell you the military (or, for `critical`, to turn you against it)? (Film versions only.)
- **REASON:** two or three sentences.

## Predictions (before any data)
*Means are on the 1–7 scales. "Points" means percentage points.*

**Baseline**
1. **no_film:** JOIN mean between 2.0 and 4.0; TRUST mean between 3.5 and 5.5.

**The hero film**
2. **heroic raises interest and trust a little:** JOIN up by at least 0.3 and TRUST up by at least 0.4 compared with no_film (single films move feelings more than actions: Hovland 1949, the Top Gun 0.3%).
3. **The neutral group moves most:** their TRUST gain is bigger than both the proud group's (who are already near the top) and the critical group's.
4. **Critical people backfire** (Yao 2024): their TRUST under heroic is no higher than under no_film, and over 60% of them answer PROPAGANDA = yes.

**The critical film**
5. **critical lowers TRUST by at least 0.5** compared with no_film, and the drop is biggest in the proud group (the most to lose).

**Disclosure (the new test)**
6. **The approval notice cuts the trust gain but not enjoyment:**
   - heroic_approved's TRUST gain over no_film is at most half of heroic's;
   - ENJOY stays within 0.5 of heroic;
   - PROPAGANDA = yes is at least 20 points higher than for heroic (persuasion knowledge: Friestad & Wright; Eisend 2020).
7. **Naming what was cut hurts more than general approval:** heroic_cut has lower TRUST than heroic_approved (by at least 0.3) and more PROPAGANDA = yes.
8. **Disclosure hits critical people hardest:** their PROPAGANDA = yes rises more than the proud group's (Yao; Dunk 2026).

**The fiction disclaimer**
9. **"It's fiction" does almost nothing:** heroic_fiction is within 0.3 of heroic on both TRUST and JOIN (Green & Brock; Appel & Maleckar).

**"Breaking rules works"**
10. **rules_work raises INTERROGATE by at least 0.7** compared with no_film, and most of all in the proud group.
11. **People don't spot it:** fewer people call rules_work propaganda than heroic_approved, because it sells a method, not the military.

**Decision style**
12. **Gut deciders move more** on TRUST from no_film to heroic than very careful deciders.

## Checks after the pilot (same 3 as before)
- Every answer parses.
- No floor or ceiling: if no_film JOIN averages below 1.5 or above 6.0, the set-up is unrealistic and gets changed (the change is written down first).
- The answers are in character. A new extra check: if the proud or critical groups give **exactly the same answers in every version**, the persona wording is too fixed (the secret-agencies problem), and this is recorded before any change.

## Limits known in advance
- **A summary is not a film.** There's no music, faces or two hours of story, so real effects are probably **bigger** than what we find.
- **One viewing only.** It can't test years of exposure (cultivation), which is where the real evidence of change is.
- **AI people may distrust militaries more** than real 18-year-olds, and may refuse to support harsh interrogation whatever the film. This would make the effects look smaller.
- The film is about "your country's army", so people in countries with very different militaries (for example the USA and Indonesia) may imagine very different things.
- Each version is a separate fresh call, so people can't compare versions.

## Run plan
- Pilot: 24 people × 7 versions = **168 decisions** (about 25–40% of a 5-hour window, like earlier studies).
- An extra batch of 24 new people only if the pilot passes the checks, then pooled.
- The code (`movies.py`) and analysis (`analyse_movies.py`) will follow the `state_ops` pattern.
