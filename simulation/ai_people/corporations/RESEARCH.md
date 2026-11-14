# Corporations tricking customers: research before simulating
*Collected 14 Nov 2026, BEFORE designing the simulation. Sources are web-search summaries of regulator actions, papers and news [summary]; I didn't read the full papers. Items marked [CHECK] are disputed or unconfirmed. This redoes the corporations topic with research first (the earlier earbuds pilot was run before the research-first rule).*

**The question:** which tricks do companies actually use on websites and apps ("dark patterns"), which ones work, and what stops them?

**Scope:** global, with cases from the USA, the EU, the UK, India and Canada. Maulik decided to leave out fake reviews and gamification, and personalised prices are already covered in `../targeting/`.

---

## 1. How common are the tricks?
| Who checked | What they found |
|---|---|
| **Mathur et al. 2019** (Princeton) | A crawl of about **11,000 shopping websites** found dark patterns on **about 11%**, including 157 fake or misleading countdown timers. **More popular sites used them more** |
| **EU consumer authorities, sweep of 399 online shops** (published Jan 2023) | **148 (37%)** used at least one manipulative practice: **42 had fake countdown timers**, and 54 steered people into choices such as subscriptions |
| **India, CCPA** | The 2023 guidelines ban **13 dark patterns**, including false urgency, basket sneaking (adding items you didn't choose), confirm-shaming, subscription traps and **drip pricing**. In June 2025, platforms were told to self-audit, and 26 declared themselves compliant. Enforcement then moved to penalties (e.g. Zepto in Dec 2025) [summary] |

## 2. Real cases around the world
| Where | Company | The trick | Outcome | How solid |
|---|---|---|---|---|
| 🇺🇸 USA | **Amazon Prime** | Signing people up without clear consent and making cancelling hard on purpose | **$2.5 billion** settlement (Sep 2025): a $1 billion penalty + $1.5 billion back to about **35 million** customers. Amazon didn't admit wrongdoing | ✔ FTC; widely reported |
| 🇺🇸 USA | **Epic Games (Fortnite)** | Confusing buttons that led to unwanted purchases (often by children); locking accounts of people who disputed charges | **$245 million** in refunds (FTC order finalised March 2023) | ✔ FTC |
| 🇬🇧 UK | **Booking.com and 5 other hotel sites** | "Only 1 room left", pressure selling, misleading discounts and hidden charges | The CMA made them change by Sept 2019; consumer group Which? said Booking.com still showed misleading "1 room left" claims afterwards | ✔ CMA, Which? |
| 🇨🇦 Canada | **Ticketmaster** | Fees added at the end (drip pricing) | Fined C$4 million + C$0.5 million costs (2019) | ✔ Competition Bureau |
| 🇮🇳 India | **Food-delivery "platform fee"** | A per-order fee that started at ₹2 in 2023 and reached about ₹15–18 by March 2026, raised several times | Shown at checkout; news reports tie it to margin goals. Not illegal in itself, but a clear case of fees growing quietly | [summary] news |
| 🌍 Everywhere | **Shrinkflation** | Smaller packs at the same price | A *Marketing Science* paper (2025): price per volume about 12% higher after a size cut, and **sales about 6% higher a year later**, so shoppers rarely switched. Surveys say most people "notice", but field data shows they don't act | [summary] |

## 3. Which tricks work? Experiments
| Trick | Evidence | Result |
|---|---|---|
| **Drip pricing** (fees revealed only at checkout) | **Blake, Moshary, Sweeney & Tadelis 2021** (*Marketing Science*): StubHub randomly showed half its US users fees only at checkout | People **spent about 21% more** and were **14% more likely to buy**; even experienced users spent 15% more |
| **Stacked dark patterns** | Luguri & Strahilevitz 2021 (already in the paper) | Sign-ups 11% → 26% (mild) → 42% (aggressive). **Mild ones caused almost no backlash; aggressive ones did** |
| **Auto-renewal and inertia** | A field experiment with 2 million readers of a European newspaper: auto-renewing offers got **20% more subscribers for about 4 months**, but some people saw the trap coming and avoided it (24–36%) | Inertia is real; people fail to cancel subscriptions they'd rather not have |
| **Making people choose actively** | A credit-card study: when people *had* to decide whether to renew, they cancelled about **4 times** as often | Friction keeps customers; active choice frees them |
| **Hard cancellation** | US survey: multi-step processes and being forced to cancel through a platform were the top complaints; only 41% of US news publishers "make it easy" | – |
| **Fake urgency (timers, "only 2 left")** | Our own AI-people results: countdowns and "only 2 left" were often **spotted and backfired** (universities, targeting, earbuds) | Loud tricks get noticed |

## 4. What protects people
- **All-in pricing rules:** Canada for tickets, the US FTC's 2025 junk-fees rule for tickets and hotels [CHECK the current status], and India's drip-pricing ban.
- **"Click to cancel":** the FTC proposed that cancelling must be as easy as signing up [CHECK: the rule's legal status changed in 2025].
- **Big penalties and refunds:** Amazon, Epic.
- **Self-audits:** India 2025. Critics say self-regulation alone had limited effect.

## 5. What this means for a simulation
- **The pattern from all our earlier topics:** loud tricks (hype, countdowns, influencers) get spotted and backfire, while quiet ones (a default, a friend, a doctor) work. Corporations are where this can be tested most directly, because the **quiet tricks are designed to go unnoticed**.
- **Two situations, both common worldwide:**
  1. **Drip pricing:** booking concert tickets where the fees appear only at checkout, after the person has spent time choosing seats.
  2. **A subscription trap:** trying to cancel a subscription the person rarely uses, against hard-to-cancel steps, guilt messages, a discount offer and "you'll lose your history".
- **Key prediction:** quiet tricks (fees at the end, friction) will work much better than loud ones (a countdown, guilt messages).
- ⚠ AI people read every word of the screen, while real people skim. Quiet tricks that rely on people not noticing may therefore look **weaker** here than in real life.

## Sources checked today (search summaries)
- Amazon Prime settlement: https://www.mediapost.com/publications/article/409399 ; https://www.jurist.org/news/?p=294008
- Epic Games: https://www.gamedeveloper.com/business/ftc-finalizes-245-million-fine-against-epic-over-i-fortnite-i-sales-practices ; https://www.pymnts.com/news/regulation/2023/ftc-says-epic-games-set-to-refund-245-million-to-fortnite-players/
- India CCPA dark patterns: https://www.barandbench.com/law-firms/view-point/from-nudge-to-notice-what-indias-dark-pattern-orders-mean-for-digital-business ; https://www.freepressjournal.in/tech/26-e-commerce-platforms-declare-full-compliance-with-dark-pattern-rules-govt-warns-action-on-violators ; https://www.mondaq.com/india/dodd-frank-consumer-protection-act/1650976/the-end-of-the-pre-ticked-box-ccpas-latest-step-towards-protecting-consumers
- Drip pricing experiment: https://newsroom.haas.berkeley.edu/research/buyer-beware-massive-experiment-shows-why-ticket-sellers-hit-you-with-hidden-fees-drip-pricing/ ; https://faculty.haas.berkeley.edu/stadelis/AIP.pdf
- EU sweep: https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_23_418/IP_23_418_EN.pdf ; https://www.osborneclarke.com/insights/european-consumer-protection-watchdogs-publish-dark-patterns-statistics
- UK hotel sites: https://www.gov.uk/government/news/hotel-booking-sites-to-make-major-changes-after-cma-probe ; https://www.which.co.uk/news/2019/09/booking-com-still-misleading-holidaymakers-with-1-room-left-claims/
- Mathur 2019: https://arxiv.org/pdf/1907.07032
- Subscriptions and inertia: https://www.kellogg.northwestern.edu/-/media/files/news-events/conference/bootcamp-reinforcement-learning/strulov-shlain_bric-conference.ashx?la=en ; https://www.npr.org/2023/08/25/1196059950/streaming-monthly-subscriptions-cancel-peacock
- Shrinkflation: https://www.chicagobooth.edu/review/do-shoppers-notice-shrinkflation ; https://pubsonline.informs.org/doi/pdf/10.1287/mksc.2024.0948
- India platform fees: https://inc42.com/buzz/swiggy-raises-platform-fee-to-₹17-58-after-zomatos-hike/ ; https://yourstory.com/2026/03/platform-fee-creeps-up-again-zomato-swiggy-test-market-price-sensitivity
