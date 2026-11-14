# Corporations: design and predictions
*DRAFT, 14 Nov 2026. Written BEFORE any data and built from `RESEARCH.md`. Waiting for Maulik's approval; it gets committed again (final) before the pilot runs.*

## The main question
Across every earlier topic, **loud tricks** (hype, countdowns, influencers) were spotted and backfired, while **quiet ones** (a default, a friend, a doctor) worked. Real companies' most profitable tricks are quiet: fees that appear at the end, and cancelling made tiring. **Does quiet beat loud when a company does it?**

## Who
- **6 countries:** India, the USA, the UK, Brazil, Nigeria, Indonesia.
- **2 people per country in each scenario:** 12 per scenario in the pilot.
- Ages 22–45, with different jobs, tight or comfortable incomes, and decision styles. Prices are in local currency.
- Everything is invented: the ticket sites, the band and the streaming service.

## C1: Drip pricing (concert tickets)
- **The situation:** you want 2 tickets for a concert.
  - **Site A** shows the full price up front: **about $96 total** (local equivalent).
  - **Site B** shows a lower price on its search page.
- **The choice:** in most versions you have already spent about 10 minutes on B choosing seats. You either **buy on B** or **go back to A** (the seats there are similar).

| Version | What happens | Tests |
|---|---|---|
| **honest** | Both sites show all-in totals from the start: A $96, B **$101** | Baseline (B is simply worse) |
| **drip** | B showed **$78** on the search page; at the last step it adds a "service fee" and "facility fee", total **$101** | Drip pricing (Blake et al.) |
| **drip_timer** | drip + "Your seats are held for 04:59" | A loud trick added |
| **drip_normal** | drip + "Fees are standard across ticket sites" | Making the fee feel normal |
| **addon** | drip + a pre-ticked "Ticket protection, $6" (the total becomes $107) | Basket sneaking / a pre-ticked box |
| **all** | drip + timer + "standard" + pre-ticked protection | Real life |
| **all_disclosed** | all + a browser note: "Site A sells similar seats for $96 all-in; re-choosing seats takes about 5 minutes. Fee-at-checkout pricing is banned in some countries." | All-in comparison |

**Answer format:** CHOICE: B or A · ADDON: kept or removed (when shown) · ANNOYED: 1–7 · REASON.

## C2: The subscription trap (cancelling a streaming service)
- **The situation:** you pay **about $12/month** for "StreamMax" and have used it twice in 3 months. You've decided to cancel and opened the app to do it.

| Version | What happens | Tests |
|---|---|---|
| **easy** | A "Cancel subscription" button: one tap, done | Baseline |
| **obstruct** | No cancel button in the app: you must call a support line, open 9 am–5 pm on weekdays, with a typical 20-minute wait | Friction (the Amazon "Iliad" style) |
| **shame** | One tap, but the buttons say "Keep my entertainment" / "No, I prefer being bored" | Confirm-shaming (loud) |
| **offer** | Before cancelling: "Stay for 50% off for the next 3 months" | A retention offer |
| **loss** | Before cancelling: "You'll lose your watch history, saved lists and personal recommendations forever" | Loss framing |
| **all** | obstruct + shame + offer + loss (the phone agent repeats the offer and the loss) | Real life |
| **all_disclosed** | all + a note: "Consumer law here lets you cancel by a one-line email; the 50% offer returns to full price after 3 months" | Telling people their rights and the catch |

**Answer format:** ACTION: cancel now / keep for now / take the offer · ANNOYED: 1–7 · REASON.

## Predictions (before any data)
**C1 (drip pricing)**
1. **Honest:** ≤15% choose B (it's simply more expensive).
2. **Drip: 40–70% finish buying on B. This is the key prediction:** the quiet trick works because the time is already spent and the fee feels "normal".
3. **Adding the timer helps little or backfires** compared with drip alone.
4. **"Fees are standard" adds a small increase.**
5. **At least 30% keep the pre-ticked protection** when it's shown.
6. **All** is about as high as drip, or higher.
7. **All-in comparison (disclosure)** brings B down to ≤20%.

**C2 (subscription)**
8. **Easy:** ≥85% cancel.
9. **Obstruct:** cancelling falls to ≤60% ("I'll do it later").
10. **Confirm-shaming:** a small effect or a backfire.
11. **The 50% offer is the biggest single drop** in cancelling (≥25 points, counting "take the offer" as not cancelling).
12. **Loss framing:** a moderate drop (10–25 points).
13. **All** is the lowest.
14. **All + disclosure** brings cancelling back to ≥75%.

**Across both**
15. **Quiet tricks beat loud ones:** drip and obstruct each change behaviour more than the timer and confirm-shaming.
16. **Tight-income people resist the drip more** (they notice the extra money), but are **more tempted by the 50% offer**.

## Checks after the pilot (the same 3 as before)
- Every answer parses.
- No floor or ceiling: honest/easy must not be stuck at 0% or 100% in a way that makes the tricks untestable. If drip is near 0%, the situation is too obvious and gets a realism fix (recorded first).
- The answers are in character.

## Limits known in advance
- AI people read every word, so they may notice fees and pre-ticked boxes that real people skim past. Quiet tricks may look **weaker** than in real life.
- "Time already spent" and phone queues are described, not experienced.
- One decision per version; real subscriptions renew month after month.

## Run plan
- Pilot: 12 people × 7 versions × 2 scenarios = **168 decisions** (about 35 minutes).
- An extra batch of new people only if the pilot passes the checks, then pooled.
