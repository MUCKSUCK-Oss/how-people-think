# AI-people pilot: results (10 Nov 2026)

**What we did:** 20 AI shoppers, each a **separate, fresh Claude (Haiku)** that only knew its own life story (name, age, Indian city, job, money habits, decision style). Each saw a shopping page for two pairs of earbuds and chose one. There were 3 versions of the page: normal, one product **pre-selected** ("✓ SELECTED FOR YOU"), and one product with **"Only 2 left! Deal ends in 09:58"**. 60 decisions in total. It ran on the Pro plan, with no extra cost.

Files: `earbuds_pilot/earbuds.py` (the experiment), `analyse.py` (the summary), `data/pilot_results.json` (all 60 answers with reasons), `data/pilot1_results_unbalanced.json` (the first, flawed run).

## Pilot 1 had a design mistake (kept for honesty)
One product was ₹50 cheaper with more battery, so **all 20 AI people picked it** in the normal version. The tricks had nothing to move. A second flaw tied decision style to which product got the trick. Both were fixed for pilot 2.

## Pilot 2: the two products are identical except colour (black vs white)

**Surprise 1: 19 of 20 AI people picked the black one** in the normal version ("looks more practical/professional"). Real people's colour tastes would split much more evenly. **The AI people are too similar to each other**, which is a known weakness of AI people.

Because of that, the clean test is: **did the trick get people to choose the white one they didn't want?**

| Trick on… | Normal page | Pre-selected (default) | "Only 2 left!" (scarcity) |
|---|---|---|---|
| White (the one they *didn't* prefer) | 0/10 | **6/10** ✅ | 3/10 |
| Black (the one they already preferred) | 9/10 | 7/10 ⬇ | **5/10** ⬇⬇ |

### What we found
1. **The default works on AI people, strongly.** Pre-selecting the white earbuds moved 6 of 10 people away from their own preference. 18 of 20 reasons mention it ("It's already selected for me… I'll just go with what the app recommends"). **This matches real experiments and our rule-based model, where the default is also the strongest trick.**
2. **Scarcity backfired.** "Only 2 left!" pushed some people (mostly the gut deciders), but **pushed more people away**, especially careful ones:
   - *"That 'only 2 left, deal ends in 09:58' feels like pressure, and I never buy things when I feel rushed."* (Vikram, very careful)
   - *"I don't like how Boltune is pushing that 'only 2 left' and countdown timer thing — feels like they're trying to rush me."* (Ananya, mostly careful)
   - Very careful AI people: 0 of 5 chose the scarce product.
   - Psychology calls this **reactance** (Brehm 1966): when people feel pushed, they push back. It's real in humans too, but in most real studies scarcity *works* on average.
3. **Even the default backfired a little** when it was obvious: 2 people saw "SELECTED FOR YOU" and became suspicious ("why is the app pushing that one?").

### What this means (honest version)
- **AI people fall for the quiet trick (the default) but resist the loud trick (the countdown).** The default doesn't feel like pressure, while the countdown looks like a sales tactic, and Claude is trained to spot those.
- Real rushed humans probably fall for scarcity more than these AI people do. So **AI people are not a perfect copy of humans**: they're more suspicious and more alike.
- **Still a useful lesson for the paper:** the tricks that work best are the ones people don't notice. That's Bernays's "make it feel like the buyer's own idea".

### Limits
- Only 20 people and one product, so the numbers are rough. 6/10 could easily be 4/10 or 8/10 in a bigger run.
- One AI model (Haiku). A different AI might behave differently.
- Text-only shopping page, with no real money, no real phone and no real rush.

### Ideas for the next run
1. Bigger: 60–100 people.
2. Make the default quieter ("Boltune Air ✓" with no "SELECTED FOR YOU" label). Does the backfire disappear?
3. Make the life stories more varied, including colour and style tastes, so the AI people aren't all alike.
4. Add the authority trick ("Recommended by audiologists") and fake likes.
5. Compare a second AI model (Gemini, free) to see if it's as suspicious as Claude.
