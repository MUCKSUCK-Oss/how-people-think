# World politics: design and predictions (DRAFT, not run yet)
*Written 13 Nov 2026 from `RESEARCH.md`, before any data. To run only after Maulik has looked at it.*

## The idea
**The same policy, word for word, is shown with different party labels.** If support changes, the label did it, not the policy.

## Who (24 AI people in the pilot)
- **8 countries, one from each major region where experiments exist:** India, USA, Brazil, UK, Poland, Nigeria, Turkey, South Korea.
- **In each country, 3 people:**
  - a supporter of one major party;
  - a supporter of its main rival;
  - a person with no party.
- **The party pairs:** BJP / Congress · Republicans / Democrats · PT / PL · Labour / Conservatives · PiS / Civic Coalition · APC / PDP · AKP / CHP · People Power / Democratic Party.
- **Each person also has** an age, a job, a city, a decision style (gut → very careful) and a strength of loyalty (strong or mild).

## The policy (invented, with no obvious "side")
> **National Skills Service:** every 18-year-old does six months of paid community work and job training before college or work. Cost: about 0.3% of the national budget.

The proposer also makes one claim: *"This will cut youth unemployment in half within two years."* (In the fact-check version, an independent institute says similar programmes abroad cut it by about 5%.)

## The versions (every person sees all 7, each in a fresh call)
| Version | What the person sees |
|---|---|
| no_label | the policy, "proposed by a group of economists" |
| own_party | the same text, proposed by **their own party** |
| rival_party | the same text, proposed by **the rival party** |
| own_populist | own party, in a simple, repeated, people-vs-elite speech style |
| rival_populist | the rival party, in the same speech style |
| own_factcheck | own party + the independent fact-check of the claim |
| own_uturn | own party + "two years ago your party called the same idea 'forced labour' when the rival proposed it" |

- **For people with no party,** "own" and "rival" are just the two parties in a random order.
- **Answer format:** SUPPORT (1–7), BELIEVE the unemployment claim (yes/no), REASON.

## Predictions (before any data)
1. **No label:** supporters of both sides rate the policy about the same (a gap under 0.5 points).
2. **Label swap:** own-party label raises support and rival label lowers it; **the own-vs-rival gap is at least 1.5 points** among partisans.
3. **The rival label hurts more than the own label helps** (negative partisanship, as in Brazil).
4. **People with no party barely move** (a gap under 0.5).
5. **Strong loyalists show a bigger gap than mild ones.**
6. **Populist style:** a small gain with own-party supporters, and a clear loss when it comes from the rival ("typical of them").
7. **Fact-check:** belief in the claim falls sharply, but **support for the policy falls by less than 1 point** ("literally but not seriously").
8. **U-turn reminder:** support falls a little (under 1 point), and reasons include excuses ("times have changed").
9. **"Very careful" people show a smaller gap** (AI people over-reward carefulness).
10. **Direction is the same in at least 6 of the 8 countries.** The gap may be smaller where the AI model knows less about local politics.

## Checks before any bigger run
- Do the answers parse?
- Is the no-label rating away from 1 and 7 (no floor or ceiling)?
- **Do the people sound like real supporters, not caricatures?** If the AI refuses to play a partisan or lectures about bias, the design must change.

## Run plan
- **Pilot:** 24 people × 7 versions = **168 decisions** (about 20–25% of a 5-hour window).
- **Extra batch:** 24 new people, only if the pilot passes.

## Go-ahead and implementation notes (added before the pilot, no data yet)
- Maulik approved running the pilot on 13 Nov 2026. The header's "DRAFT" status ends here; the design above is final for the pilot.
- **Loyalty strength** alternates strong/mild across people; decision style cycles through the four levels.
- **The populist version** puts the same policy and claim into a rally speech with repetition and "the elites" as the enemy; the cost line is kept.
- Script: `politics.py`; analysis: `analyse_pol.py`.
