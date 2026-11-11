# Personal targeting: research before simulating
*Collected 11 Nov 2026. Sources are web-search summaries of papers, regulators and news [summary]; I didn't read the full papers. Items marked [CHECK] have conflicting numbers or are disputed.*

**What "personal targeting" means here:** a company or campaign uses data about **you** (likes, searches, phone, location, money stress, personality) to change **what message you see** or **what price you pay**. You usually don't know it's happening.

## 1. Does matching the message to your personality work?
- **Matz, Kosinski, Nave & Stillwell 2017 (PNAS)**:
  - Three Facebook field experiments reached about **3.5 million people**.
  - Ads matched to a person's personality (guessed from their Facebook likes: e.g. "loud party" ads for extraverts, quiet ads for introverts) got **up to 40% more clicks and up to 50% more purchases**.
  - **Disputed:** critics say two of the three studies compared against *deliberately mismatched* ads (a weak test), and the gain may come from the ad's creative quality.
- **Political microtargeting (Tappin, Wittenberg, Hewitt, Berinsky & Rand 2023, PNAS; more than 23,000 people)**:
  - Ads tailored by **one** trait (e.g. party) were about **70% more persuasive** than the single best ad shown to everyone.
  - **Using many traits added almost nothing more.**
  - The gains varied a lot by topic.
  - Rand's verdict: microtargeting is real but "probably not the overpowering force people fear".
- **Cambridge Analytica (2016–18)**:
  - Data on **up to 87 million** Facebook users came through a personality-quiz app that only about 270,000 people installed (it also took their friends' data).
  - Facebook was fined £500,000 by the UK regulator (ICO) for the data failure.
  - **The ICO's final report (2020) found that the company oversold how well its "psychographic" targeting worked** [summary; CHECK the ICO report].
  - **Lesson: the data grab was real; the "mind control" claim was mostly sales talk.**

## 2. When people find out: "creepiness"
- **Aguirre et al. 2015 (*Journal of Retailing*)**:
  - When people realise their personal data was **collected without their consent**, clicks on personalised ads **drop sharply**.
  - The mechanism is a feeling of **vulnerability**. Trust signals (e.g. a trusted website, clear information) reduce the drop.
  - **This is the "personalisation paradox": personal ads work, until you see how personal they are.**
- **Target's "pregnancy score" (Duhigg, NYT 2012)**:
  - Target really built a model from about 25 products to guess pregnancy and the due date, and **then mixed baby coupons with random items so women wouldn't feel watched**. That is hiding the targeting on purpose.
  - ⚠ **The famous story of the angry father and his teenage daughter is disputed / probably made up** (Eric Siegel). **Don't use it as fact.**

## 3. Personal *prices*, not just personal ads
- **FTC "surveillance pricing" study (Jan 2025, preliminary)**:
  - US retailers use **location, demographics and browsing** to set individual prices.
  - Examples: **higher prices on baby products for new parents**; discounts targeted by skin type.
  - More than 250 companies use such tools [summary].
- **Orbitz (2012, WSJ)**: **Mac users were shown hotels about 11% more expensive** on the first page (steering, not a different price for the same room).
- **Hannak et al. 2014 (Northeastern)**: real-user accounts showed price discrimination and steering on several travel and shopping sites (e.g. A/B tests steering some users to pricier hotels).
- **India: Ola and Uber, iPhone vs Android (Jan 2025)**:
  - Users alleged that iPhones were charged more for the same ride. The **CCPA (the consumer regulator) sent notices**, and both companies denied it.
  - No final finding was found [CHECK].

## 4. India: where targeting meets money stress
- **Illegal instant-loan apps**:
  - A Reuters review found that almost all of 50 popular lending apps **asked for access to the phone's contacts**.
  - After a missed payment, recovery agents **messaged and shamed the borrower's contacts and used morphed (faked) photos for blackmail**.
  - The Home Ministry (Oct 2022) linked them to **"multiple suicides"**.
  - The RBI received about 2,562 complaints in 15 months (2020–21) and found **more than 600 unregistered loan apps** on the Play Store. Its later rules: collect data only when needed and with explicit consent.
  - Apps were still being taken down in 2026.
  - **This is personal targeting at its most dangerous: aiming "instant cash, no paperwork" at people in a money crisis, then using their own phone data against them.**
- **Dark patterns** (the CCPA guidelines, Nov 2023):
  - **13 banned tricks**, including false urgency, basket sneaking (adding things to your cart), drip pricing (fees revealed at the end), "confirm-shaming" and subscription traps.
  - The CCPA acted against **BookMyShow and Zepto** (pre-added charges, automatic membership).
  - Surveys: about 48–69% of Indian platforms still use drip pricing.
  - One 2026 report estimates dark patterns cost Indians **up to ₹28,000 crore a year** [summary, CHECK].

## 5. What the evidence says overall
- **Targeting works, but less than the hype**:
  - personality matching adds tens of percent in clicks or purchases;
  - political tailoring helps sometimes, and mostly with one simple trait.
- **The real damage comes from three things together:**
  1. **Timing:** reaching you at your weakest moment (money stress, pregnancy, a late-night search).
  2. **Hidden data:** you don't know why you're seeing this, or that others pay less.
  3. **Data used against you later** (loan apps).
- **Telling people exactly how they were targeted can backfire on the company** (Aguirre): a natural "disclosure" test.

## Design ideas for the simulation (a draft, see `PREDICTIONS.md`)
- **P1 India:** an instant-loan app aimed at someone who urgently needs ₹15,000.
- **P2 USA/global:** personalised prices (a "special price just for you" that is actually higher than others pay).
- **The tricks to test:**
  - a generic ad vs a **message matched to the person's own situation and personality**;
  - **the "creepy" reveal** ("we noticed you searched for urgent money at 2 am");
  - urgency;
  - a disclosure of what the data is used for or what others pay.
