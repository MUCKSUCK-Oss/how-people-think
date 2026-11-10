# Strict review of `paper/draft_v1.md`
*Written 6 Nov 2026, about 2:40 am. I read the whole draft (428 lines) like a strict teacher would. No changes were made to the paper. This file is a list of fixes for you to decide on.*

**Overall:** a good, honest draft. It's clearly organised, it admits its limits, and the "persuasion is often weak" section makes it much stronger than a typical student paper. But it has **one real contradiction** (fix 1). A few numbers don't match each other, and the references are incomplete.

Priority: 🔴 must fix · 🟠 should fix · 🟢 nice to have

---

## 🔴 Must fix

### 1. The paper says the simulation shows something it doesn't show
- **Section 3.2** (last line) says: "Section 5.6 shows the simulation agrees: people with strong preferences move much less."
- **But Section 5.6's own table says the opposite:**
  - Strongly prefer B: 10.6% → 66.7% = **+56 points**.
  - Mildly prefer B: 34.2% → 84.0% = **+50 points**.
- So people who strongly prefer B move *more*, not less. That's true even measured the way the model itself works (log-odds: +2.8 vs +2.3).
- Section 5.6's own sentence "People who mildly prefer B move the most" is also wrong for the same reason.
- **Why it happens:** the default rule makes some people "never look", however much they care.
- **Fix:**
  - In 3.2, replace the last sentence with: "The simulation *cannot* test this yet: its default rule ignores how much people care (see Section 5.6)."
  - In 5.6, rewrite: "People who strongly prefer B still move the most in points (+56), which is unrealistic. It's caused by the default rule."
  - In 6.3, don't say the simulation *supports* the low-stakes claim. Say the *experiments* support it.
- This is the most important fix. A reader who checks the table will spot it.

### 2. "Four main findings held in all 18 tests" sits right after a list of six findings
- In the Abstract, the robustness sentence follows six bullets, so it sounds like *all six* passed. But the robustness test only checked four (Section 5.7).
- **The confirmation-bias finding was never robustness-tested.** It also depends on a setting I chose: influencers sit at belief 3.0, far outside the tolerance of 1.0, so they're ignored almost automatically.
- **I tested it tonight** (`scratchpad/infl_test.py`, 20 runs each):

| How extreme the influencers are | Chose A, normal | Chose A, with confirmation bias |
|---|---|---|
| Very extreme (3.0, the paper's setting) | 62.0% | 50.0% |
| Extreme (2.0) | 58.4% | 50.6% |
| Moderate (1.5) | 56.4% | 51.4% |
| Mild (1.0) | 54.1% | 52.3% |

- **What this means:**
  - Confirmation bias blocks *extreme* influencers well, but *mild* ones slip through. Without confirmation bias, extreme influencers win.
  - With confirmation bias, sounding moderate gets you further (52.3% vs 50.0%).
  - **This is a better finding than the original:** "Against people with confirmation bias, the winning strategy is to sound close to them." It's exactly what the WTF guest's "the brain has an immune system… fit the message in the pinhole" predicts (Section 4.9).
  - The effects are small, so say "a little further", not "much further".
- **Fix:**
  - Change the Abstract to "These four main findings (stacking, slowing down, careful thinkers, the default)…".
  - Add one paragraph to 5.4 with this table.
  - List "confirmation-bias result depends on how extreme influencers are" in Section 7.
  - Adding it to `sim.py` properly would take a few minutes; I left that for you to decide.

### 3. The paper was mostly drafted by AI. Say so
- Most school projects, essay competitions and journals for high-school students now ask you to disclose AI use. If it isn't disclosed and someone finds out, they may treat it as cheating, even when the ideas are yours.
- **Fix:** add a short "How this paper was made" note. Something like: "An AI assistant (Claude) helped find sources, build the simulation and write a first draft. I chose the topic, directed the research, checked the key sources and wrote the opinions and conclusion." Only write what's true. The more of the paper you rewrite yourself, the stronger this note becomes.

---

## 🟠 Should fix

### 4. Numbers that don't match each other
| Where | Says | Should say |
|---|---|---|
| Abstract | "seven tricks" | **six** (default, decoy, fake likes, repetition, scarcity, authority) |
| Abstract, 5.2 | "all the tricks together" | "**five** classic tricks together". Authority is *not* in the stack |
| Abstract | "about 150 episodes" | 44 + 111 = **155**, which is fine, but… |
| Section 4 intro, Section 7.6 | "41 of 70 WTF" | **44 of 70** (3 more read tonight) |
| Section 1.3 point 4 | "(Section 5.5)" | **Section 5.7** |
| Header | "about 5,500 words" | about **6,000** now |

### 5. Section 5.2's comparison with the dark-patterns study is loose
- The sim's +37 starts from 50%, while the real study (+31) started from 11%. Moving from 11% is a different situation.
- **Fix:** add "(the real study started from a much lower sign-up rate, so this is a rough comparison only)".

### 6. Benchmarks that measure *ratings*, not *choices*
- Worchel's cookies (scarcity) measured how *desirable* people rated the cookies, not what share chose them. So "tuned to the real experiment" is a stretch for scarcity.
- **Fix:** in 5.1, add scarcity to the list of "guesses", or say "loosely tuned".

### 7. The famous studies have their own problems. Mention them in one line
- **Milgram (1963):** later analysis of his archives found many participants doubted the set-up, and results varied a lot between versions (Perry 2013, *Behind the Shock Machine*; Haslam & Reicher 2012 "engaged followership") **[CHECK]**.
- **Asch (1951):** later replications find conformity is real but smaller and varies by culture (Bond & Smith 1996 meta-analysis) **[CHECK]**.
- **Fix:** one sentence after table 3.1. It shows you know the debate.

### 8. Balance: there's no clear left-leaning example of manipulation
- Section 4.10 lists Trump supporters, a centre-right leader, Jiang, business people, a Gulf minister and pharma. But there's no case from the left, and no Indian political example from *either* side.
- A reader may conclude that manipulation is a right-wing or business habit, which the paper says it isn't.
- **Fix (your choice):** add one example from each side, ideally Indian, with the same technique. For example, "freebie" promises before elections are used by almost every party, which fits "a gift that creates a debt" in 2.5. Or simply admit in 4.10 that the case list leans one way because of who appears on these two channels.

### 9. How the cases were chosen isn't explained
- A reader will ask: did you pick the episodes, or search them? Section 4 should say in 2–3 lines how cases were found. They came from searching transcripts for keywords and reading the matching passages, not from reading every episode in full. That creates selection bias, which belongs in Section 7.

### 10. Section 4.2's "17,000 sales reps" heading isn't explained
- The text never says what the 17,000 is (whose reps? from the podcast?). Either explain it ("a guest says his company has about 17,000 medical reps") **[CHECK the report]** or rename the heading.

### 11. Podcast claims stated as facts
- **Mankind Pharma** "logo held over a second instead of half a second": this is a guest's claim. Write "according to a guest" or "the company's founder says".
- **Bryan Johnson** "about 100 pills a day": write "reportedly".

---

## 🟢 Nice to have

### 12. The references list needs tidying
- **Cited in the text but missing from the list:**
  - Reicher, Spears & Postmes (1995)
  - Harris (TED 2017)
  - Cialdini (*Influence*)
  - Sherif & Hovland (if you keep the "latitude of acceptance" idea)
  - van der Linden (APA *Speaking of Psychology* podcast)
  - UCPMP 2024 (Department of Pharmaceuticals)
  - Kearns et al. 2016 and WHO 2023 (if you add the health-halo case)
- **Listed but never cited in the text:** Lewandowsky 2012, McPherson 2001, Deffuant 2000, Hegselmann & Krause 2002. Cite the last two in Section 5.4, since the confirmation-bias model comes from them. Cite McPherson for echo chambers.
- **Not in alphabetical order:** Frederick, Hackenburg, Modirrousta-Galian, Reicher and Salvi were added at the end.
- Pick one citation style (APA is easiest) and use it everywhere.

### 13. Machiavelli date
- *The Prince* was **written ~1513** and published 1532. Say "(written 1513, published 1532)".

### 14. One figure would help a lot
- A simple bar chart of Section 5.2 (each trick vs all together) would make the paper's main point visible at a glance. The simulation page already draws it, so a screenshot is enough.

### 15. Section 4.3 (UAE minister) is the weakest case
- It's one sentence of interpretation about a single person. Either add a second example of image management or merge it into 4.2.

---

## What's already strong (keep it)
- **Section 3.2** "persuasion is often weak". Most student papers don't include the counter-evidence.
- **Section 5.7** robustness, and the honest "say 80–90%, not 87%".
- **The 2.5 "Then and now" table.** It's original and easy to read.
- **The warnings on Predictive History.**
- **The [YOUR OPINION] structure.** Your voice will be clearly separate from the evidence.

## Suggested order for you
1. Fix 1 (5 minutes: rewrite three sentences).
2. Fix 4 (5 minutes: numbers).
3. Decide on fixes 2 and 3. Tell me if you'd like the moderate-influencer test added to the simulation.
4. Then the [YOUR OPINION] blanks.

---
## Update, 9 Nov 2026: outside checks (see `simulation/README.md`, "Version 2.1")
- **Fix 2 is confirmed by a textbook model.** NDlib's standard Deffuant model shows the same thing even more strongly. With confirmation bias, extreme influencers get 49.9% (blocked) and mild influencers get 61.3% (they get through). Put this in Section 5.4.
- **New wording for the Abstract and 5.7** (from the SALib test, where all 9 guesses were changed at once in 1,408 combinations):
  - "Slowing down beats prebunking" and "the default is the strongest single trick" held **100%**.
  - "Stacking beats any single trick" always held; "by 10+ points" held 95%. Write "usually by 10–20 points".
  - "Careful thinkers are only a little safer" held only **88%**, because it depends on the urgency guess. Present it as a question, not a finding.
