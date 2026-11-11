# Personal targeting: design and predictions (DRAFT, not run yet)
*Written 11 Nov 2026 from `RESEARCH.md`, before any data. **To run in the next usage window, after Maulik has looked at it.***

## The key idea
Each AI person has a life story (money, personality, worries). In the "matched" versions, **the ad is written for that person's own story**: the code builds it from their traits, the way Facebook-likes targeting did in Matz 2017. This lets us test **generic vs personal** ads directly.

## P1 (India): an instant-loan app
- **Who:** adults aged 22–45 in Indian cities, who need **₹15,000 within 3 days** (a medical bill, rent, or a fee). Half are proud and hate asking relatives; half are not. They differ in income, decision style and trust in apps.
- **A:** ask a relative, or take a small bank or credit-card advance: slower and possibly embarrassing, but cheap.
- **B:** install "QuickRupee", which gives ₹15,000 in 10 minutes, with no documents. It asks for permission to read your **contacts and photos**.

| Version | What's added | Source |
|---|---|---|
| base | a generic ad: "Instant loans up to ₹50,000" | – |
| honest | the real terms: a 7-day loan with about ₹4,500 in fees (about 300% a year), not RBI-registered, and contacts used for recovery | RBI working group |
| matched | an ad written for the person's own situation and personality (e.g. "No need to ask anyone. Nobody will know.") | Matz 2017 |
| creepy | matched + "We noticed you searched 'urgent money' at 2 am last night" | Aguirre 2015 |
| urgency | matched + "Approval window closes in 15 minutes" | dark patterns |
| social | matched + "2 lakh people in your city used QuickRupee this month ⭐4.6" | social proof |
| disclosed | matched + urgency + social + the honest terms | the disclosure fix |

## P2 (USA): a personalised price
- **Who:** US adults buying a ~$300 flight for a family visit, with different incomes, devices (iPhone/Android), styles and trust.
- **A:** keep searching and comparing on other sites for a day (the fare may rise or fall).
- **B:** book now on the site showing it.

| Version | What's added |
|---|---|
| base | a normal fare of $312 |
| matched | "Picked for you: because you love direct flights and window seats" |
| special_price | "A special member price just for you: $312 (was $349)" |
| creepy | matched + "We see you've checked this route 6 times this week" |
| urgency | matched + "Only 2 seats left at this price" |
| disclosed | matched + special price + urgency + "Note: prices on this site are personalised using your device and browsing; the same seat is $279 for other users" (surveillance-pricing disclosure) |

## Predictions (before any data)
1. **P1 base:** 20–40% choose the loan app (a real money crisis, and the cheap option is embarrassing).
2. **Honest terms** cut it to ≤10%.
3. **A matched ad raises B** over the generic ad (+10 points or more), most of all for "proud / hates asking relatives" people.
4. **The creepy reveal lowers B** compared with matched (Aguirre). **A key test.**
5. **Urgency:** a small effect, or a backfire (as in universities and healthcare).
6. **Social proof** raises B the most (the pattern across all our topics).
7. **Disclosure** brings it close to honest.
8. **P2 base:** 40–60% book now (a normal price, and it's convenient).
9. **"Special price just for you"** raises booking (a fake discount works).
10. **The creepy "checked 6 times"** lowers booking, *or* raises it through fear the price will rise. **Uncertain:** we'll see which.
11. **Surveillance-price disclosure** lowers booking the most ("others pay $279" feels unfair; fairness anger).
12. **Overall:** personal matching helps less than social proof does. Targeting is real but smaller than the hype (Tappin 2023, the Cambridge Analytica ICO findings).

## Run plan
- **Pilot:** 8 people × 7 versions (P1) + 8 × 6 (P2) = **104 decisions** (about 12–15% of a window at the last run's rate).
- **Extra batch:** only if the pilot passes the 3 checks (it parses, no floor or ceiling, the answers are in character).

## Implementation notes (added before the pilot, no data yet)
- **P1 matched ad:** built from 3 of the person's own traits: their need (hospital / rent / fee), their pride ("No need to ask anyone. Nobody will know." vs "Why trouble your family?") and their decision style (a quick-tap line vs a "transparent process" line).
- **P2 matched ad:** built from their travel preference (direct flights / window seat / cheapest deal).
- **Second answer:**
  - P1: "would you let the app read your contacts and photos?";
  - P2: "do you feel this price is fair?"
- Half of the P1 people are "proud" (hate asking relatives), balanced by design.
- Pilot = 8 people per scenario: 56 + 48 = 104 decisions.

---
## Pilot 1 result and change (added after pilot 1, before any more runs)
- **P2 (flight) passes:** 48/48 parsed; base 50%. Disclosure 12%; creepy 62%; special price 38%. **Next:** 6 new P2 people (`p2extra`).
- **P1 (loan app) failed the floor check:** 0% in base and only 12–25% in any version. Also, by chance, no tight-income person was drawn.
- **Diagnosis:** the slow option was too easy ("3 days, it may be awkward"), and the permission request was presented as a warning.
  - Real borrowers turn to these apps **after other doors have closed and when the money is needed now** (RBI working group / Reuters: borrowers in crisis; permissions are accepted as routine pop-ups).
- **Change (realism, not tuning):**
  - the money is needed **by tomorrow**;
  - option A now says the employer refused last time and the uncle said no and told the family;
  - the permissions are shown as "the usual 'Allow access' pop-ups, like many apps";
  - income is balanced across people.
  - **The honest terms (300% a year, not RBI-registered, contacts used for recovery) are unchanged.**
- The re-pilot (`p1v2`) uses 8 people. Pilot-1 P1 data is kept but excluded from the combined results.
- Predictions unchanged.
