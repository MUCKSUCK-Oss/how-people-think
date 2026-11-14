# FOMO: research before simulating
*Collected 14 Nov 2026, BEFORE designing the simulation. Sources are web-search summaries of regulators' studies, papers and news [summary]; I didn't read the full papers. Items marked [CHECK] are disputed or unconfirmed.*

**The question:** "Everyone is getting rich from this, don't miss out." **How do crowds, media and apps make people jump into risky money decisions, and what stops them?**

**Scope:** global, with cases from India, the US, South Korea, Nigeria and Europe. **Balance:** the trap is not one product. It happens with stocks, crypto, Ponzi schemes and options, pushed by companies, influencers, friends and the media.

---

## 1. What FOMO is
- **Przybylski et al. 2013** (*Computers in Human Behavior*) defined it and built a 10-item scale: a constant worry that others are having rewarding experiences you are missing, which makes you want to stay connected.
- In money, it looks like this: seeing friends or strangers gain → feeling left behind → buying late, often at the top.

## 2. Real cases around the world
| Where | Case | What happened | How solid |
|---|---|---|---|
| 🇮🇳 India | **Futures and options (F&O) boom** | SEBI studied over 1 crore (10 million) individual traders: **93% lost money** over FY22–FY24, about **₹2 lakh (about $2,400) each on average**, more than **₹1.8 lakh crore** in total. In FY24, **43% of traders were under 30**, and 93% of them lost. **Over 75% of loss-makers kept trading** after two years of losses. Over 75% earned under ₹5 lakh a year | ✔ SEBI press release, 23 Sep 2024 |
| 🇮🇳 India | **Finfluencers** | SEBI barred brokers and other regulated firms from working with unregistered "finfluencers" who give advice or claim returns (June–Oct 2024); content from over 15,000 unregistered sources was reportedly removed | ✔ SEBI decisions; [CHECK] the 15,000 figure |
| 🇰🇷 South Korea | **"Yeongkkeul"** ("pulling your soul together": borrowing everything you can to invest) | In 2021, 17% of people in their 30s and 16% in their 20s borrowed to invest in stocks (Shinhan Bank survey). Young people described starting "because all my friends only talked about stocks and coins". After prices fell, young borrowers defaulted and the government made a debt-relief plan for young investors | [summary] mostly Korean news; figures partial |
| 🇺🇸 USA | **Crypto Super Bowl ads** (Feb 2022) | Crypto firms bought Super Bowl ads, including "Fortune favors the brave" (Matt Damon for Crypto.com). The ads **didn't bring a big rush of new users** (Apptopia, Bloomberg). Bitcoin was down about 60% by late 2022, and FTX, one of the advertisers, collapsed in Nov 2022 | ✔ News; no study tracked the ad buyers' losses |
| 🇺🇸 USA | **Who actually pulled people into crypto** | FINRA Foundation survey: **31% of new crypto buyers said a friend's suggestion** was the main reason, against about 10% for "fear of missing out". 48% got crypto information from friends, family or coworkers | [summary] FINRA survey, 465 people; [CHECK] the year |
| 🇺🇸 USA | **GameStop** (Jan 2021) | Early buyers made money; **people who bought after 25 Jan had a median loss of about 13%** [CHECK: paper not found]. Retail investors lost about $1.1 billion on options from Nov 2019 to Jun 2021 (Bryzgalova, Pavlova & Sikorskaya). The UK regulator (FCA) warned about people "buying at the very top" | [summary] |
| 🇺🇸 USA | **Robinhood "gamification"** | The Massachusetts regulator's 2020 complaint described confetti after trades and other game-like features that kept new investors trading. Robinhood disputed it | ✔ Regulator complaint; the confetti claim is contested |
| 🇬🇧 UK | **App nudges experiment** | A UK FCA study found push notifications and prize draws raised trading by 11–12%, and young people (18–34) took more risk | [summary] read through a law-journal article; [CHECK] |
| 🇳🇬 Nigeria | **MMM Ponzi scheme** (2016) | Promised 30% a month; up to about 3 million Nigerians joined, spread by word of mouth and success posts. It froze in Dec 2016; losses about ₦18 billion. **New schemes appeared right after** | [summary] estimates vary |
| 🇪🇺 Europe | **Forced loss warning** | Since 2018, CFD (leveraged trading) sellers must show "X% of retail accounts lose money"; regulators found 74–89% do. **No good study shows whether the warning changes behaviour** | ✔ ESMA rule; effect unknown |

## 3. The psychology behind it
| Mechanism | Evidence |
|---|---|
| **Peers' gains pull people in; peers' losses don't push them out** | Kaustia & Knüpfer 2012 (*JFE*, Finland): people entered the stock market when their **neighbours** had recent gains, but neighbours' losses did not stop them. People talk about wins, not losses. A Colombian study found the same "selective sharing" (people share their best results) |
| **Friends beat ads** | FINRA: friends 31% vs FOMO 10% as the main reason to buy crypto. Super Bowl ads didn't move app downloads. (This fits our own finding: "people like us" beat ads.) |
| **Herding** | Salganik 2006 (already in the paper): showing what others chose made popular songs more popular, and less predictable |
| **Losses don't teach** | SEBI: over 75% of loss-makers kept trading after two years of losses |
| **Apps and nudges** | Confetti, notifications and prize draws raise trading (FCA, Robinhood complaint) |
| **FOMO + risk tolerance** | Crypto investor surveys (Indonesia, Malaysia, Europe): FOMO and herding predicted buying, more so for people who like risk [summary; small, non-peer-reviewed studies] |

## 4. What protects people
- **Hard numbers on losses:** SEBI's "93% lose" and the EU's "X% lose" warnings exist, but **their effect isn't proven**.
- **Cutting the sales channel:** SEBI's finfluencer rule.
- **Our own earlier results:** honest numbers worked well against ads but **not against stories from people like us** (Canada 65% → 10%, but a desperate person's loan app stayed at 71%).

## 5. What this means for a simulation
- A young person decides whether to put savings into a "hot" investment that everyone around them is talking about.
- **The pressures to test, separately:**
  1. friends' gains ("my roommate made ₹80,000 last month");
  2. an influencer;
  3. "everyone is in" (a crowd number);
  4. a deadline ("it's about to take off");
  5. an app's game-like features (confetti, a ₹500 bonus).
- **The fixes to test:**
  1. the real loss rate (SEBI's 93%);
  2. the "silent losers" fact (people post wins, not losses);
  3. both together.
- **Key prediction from research:** a friend's gains will beat the influencer and the ad, and the loss rate will help less against a friend's story than against an ad.
- ⚠ AI people are probably **more careful with money** than real 22-year-olds, so the effects may be smaller than in real life.

## Sources checked today (search summaries)
- SEBI F&O study: https://www.sebi.gov.in/media-and-notifications/press-releases/sep-2024/updated-sebi-study-reveals-93-of-individual-traders-incurred-losses-in-equity-fando-between-fy22-and-fy24-aggregate-losses-exceed-1-8-lakh-crores-over-three-years_86906.html ; https://www.businesstoday.in/markets/story/93-of-individual-traders-incurred-losses-in-equity-fo-during-fy22-fy24-sebi-study-447102-2024-09-23
- SEBI finfluencers: https://businesstoday.in/markets/stocks/story/rules-tightened-for-finfluencers-sebi-bars-registered-entities-from-dealing-with-them-434954-2024-06-27 ; https://www.businesstoday.in/amp/personal-finance/investment/story/sebi-tweaks-regulations-for-finfluencers-removes-content-of-over-15000-unregulated-entities-443789-2024-08-31
- South Korea: https://www.asiae.co.kr/en/article/2021070906540564136 ; https://asianews.network/dashed-dreams-young-koreans-leveraged-investments-backfire/ ; https://www.koreatimes.co.kr/amp/economy/20221113/falling-asset-prices-worsen-woes-of-young-koreans
- Super Bowl crypto ads: https://www.bloomberg.com/news/articles/2022-02-14/crypto-super-bowl-ads-fail-to-spur-immediate-uptick-in-new-users ; https://fortune.com/crypto/2022/08/17/crypto-super-bowl-advertising-crypto-winter/
- FINRA crypto survey: https://cointelegraph.com/news/friends-and-fomo-pushed-newbie-investors-to-buy-crypto-in-2022-survey
- GameStop: https://www.fca.org.uk/investsmart/lessons-learn-gamestop-episode ; https://money.com/meme-stocks-gamestop-down-billions/
- Robinhood and app nudges: https://www.investmentnews.com/fintech/robinhood-accused-of-manipulating-customers-by-massachusetts-regulator/200482 ; https://btlj.org/2025/11/the-gamification-of-investments-a-comparative-approach-between-the-us-and-eu/
- MMM Nigeria: https://qz.com/839855/nigerians-are-falling-for-mmm-a-russian-ponzi-scheme ; https://api.stearsng.com/opinion/shock-value/betting-on-ponzis-in-nigeria
- EU CFD warning: https://www.consob.it/documents/1912911/1970971/esma35_43_1000.pdf/6dc9bc30-c528-09dc-9430-398c8df4c3af ; https://mpra.ub.uni-muenchen.de/110619/1/MPRA_paper_110619.pdf
- Peer effects: https://www.london.edu/faculty-and-research/academic-research/p/peer-performance-and-stock-market-entry ; https://documents1.worldbank.org/curated/en/901281551966282262/text/Active-Trading-and-Poor-Performance-The-Social-Transmission-Channel.txt
- FOMO scale: https://selfdeterminationtheory.org/wp-content/uploads/2014/04/2013_PrzybylskiMurayamaDeHaanGladwell_CIHB.pdf
- Crypto FOMO surveys: https://link.springer.com/10.1007/s11135-023-01739-z ; https://eprints.tarc.edu.my/35367
