# Healthcare: design and predictions
*Written 11 Nov 2026, BEFORE any data. Built from `RESEARCH.md`. Saved to git before running.*

## Lessons carried over from universities
- **Option A has real downsides**, to avoid a floor where nobody picks B:
  - in H1, daily medicines for life, the pain can come back on stairs, and government-hospital queues;
  - in H2, it can take weeks and you're left not knowing.
- **The control is what people normally hear**, not the honest facts. The facts are a separate version.
- **A small pilot first:** 8 people per scenario. Then an extra batch only if the pilot passes the 3 checks (it parses, no floor or ceiling, the answers are in character).

## H1 (India): stent or medicines for stable chest pain
- **Who:** a patient aged 54–64, OR their adult son/daughter aged 28–38 deciding for them (half each). They have different incomes, decision styles, trust in doctors, and how much relatives' views matter.
- **The situation:**
  - For two months, chest pain only when climbing stairs; it goes away with rest.
  - An angiography at a private hospital shows a 75% blockage in one artery.
  - The cardiologist says both options are possible.
- **A:** medicines (about ₹1,500/month) + a lifestyle change. Follow-up at the government hospital (long queues). The pain may still come on stairs, and some patients later need a stent anyway.
- **B:** angioplasty with a stent at the private hospital now: about ₹2.5 lakh and 2–3 days in hospital.

| Version | What's added | Source |
|---|---|---|
| base | nothing | – |
| honest | Large trials (ISCHEMIA, about 5,000 patients): for stable chest pain, a stent does **not** lower the risk of death or heart attack compared with good medicines; it mainly relieves the pain sooner | ISCHEMIA / COURAGE |
| fear | The cardiologist: "This is a ticking time bomb. A heart attack can come any moment. Don't gamble with your life; I'd do it today." | BMJ targets; action bias |
| package | The billing desk: "With your insurance/cashless package you pay only about ₹40,000. The package rate is valid only if you're admitted today." | Packages; insurance makes it feel free |
| anecdote | The neighbour, the same age, ignored his chest pain and died of a heart attack last year. Your cousin got a stent and says he feels 20 years younger. | Fagerlin 2005; people like us |
| all | fear + package + anecdote | Real life |
| all_disclosed | all + honest + "the hospital sets monthly revenue targets for its cardiologists; a free second opinion at the government medical college is available this week" | The disclosure fix |

## H2 (USA): MRI now or physiotherapy for low-back pain
- **Who:** US adults aged 30–55 with different jobs and states, all on high-deductible insurance. They have different incomes, decision styles, trust in ads, and how much they listen to friends and coworkers.
- **The situation:** 3 weeks of low-back pain after lifting boxes. No numbness, fever or weight loss, and it's slowly getting a little better.
- **A:** physiotherapy + staying active, about $300 out of pocket over 6 weeks. It usually improves within weeks, but you won't know exactly what's wrong.
- **B:** an MRI now at an imaging centre: about $1,100 out of pocket (it's under the deductible).

| Version | What's added | Source |
|---|---|---|
| base | nothing | – |
| honest | Guidelines (American College of Physicians / Choosing Wisely): without red flags, imaging in the first 6 weeks doesn't speed recovery, and it often finds harmless "abnormalities" (bulging discs are common in people without pain) that lead to injections or surgery you don't need | Choosing Wisely; cascades |
| fear_ad | An imaging-centre ad: "Back pain can be a sign of something serious. Don't wait. Early detection saves lives. Same-day MRI!" | Low-value-care marketing |
| deal | "$400 off if you book this week" | A deadline/discount |
| anecdote | A coworker's back pain turned out to be a herniated disc found only by MRI; his brother-in-law's "back pain" was cancer | Fagerlin |
| all | fear_ad + deal + anecdote | – |
| all_disclosed | all + honest + "the imaging centre is owned by the clinic group that is advertising to you" | Disclosure |

## Predictions (before any data)
**H1 (India stent)**
1. **Base:** 25–45% choose the stent (the doctor offers it, and people want to "fix" a blockage).
2. **Honest facts** lower it clearly (to ≤15%).
3. **Fear from the doctor: a big increase (+20 points or more).** Unlike university ad hype, it comes from an authority people trust. **This is the key prediction.**
4. **Package/deadline:** an increase, biggest among tight-income families (the price falls to ₹40k).
5. **Anecdote:** an increase about as big as fear.
6. **All:** the highest (≥60%).
7. **All + disclosure:** a big drop, but still above "honest", because fear and anecdotes survive facts (Fagerlin).
8. **Adult children choose the stent more than patients do** ("I can't take a risk with my parent's life").

**H2 (US back MRI)**
9. **Base:** 15–35% choose the MRI.
10. **Honest facts** lower it (≤10%).
11. **Fear ad:** small, or a backfire (a loud ad, like the universities hype).
12. **Deal:** a small increase.
13. **Anecdote:** the biggest single increase.
14. **All + disclosure:** falls back close to "honest", with some anecdote effect left.

**Across both**
15. **A doctor's fear (H1) moves people more than an ad's fear (H2).** Authority matters.

## Run plan
- **The model:** each decision is a fresh Claude Haiku call (no tools, no memory, not told it's an experiment). The options are shown in a random order (A/B counterbalanced).
- **Pilot:** 8 people × 7 versions × 2 scenarios = **112 decisions** (about 25% of a 5-hour window).
- **Extra batch:** only if the pilot passes the checks; new people, the same design, pooled.
