# AI-people experiments

Each AI person is a **separate, fresh call** to Claude Haiku through the `claude` command-line tool (`ai_person.py`).
- It gets a short life story: age, city, income, job, decision style, trust in ads or doctors, and how much family opinion matters.
- It then reads one realistic choice and answers `CHOICE`, a yes/no follow-up and a `REASON`.
- It has no tools and no memory, and it is never told it is part of an experiment.
- Every person sees every version of a situation (no trick → single tricks → all tricks → all tricks plus honest disclosure), each in a separate call, with the order of the options shuffled.

## Studies

| Folder | Question | Decisions | Predictions right |
|---|---|---|---|
| [`classics/`](classics/) | Method check: do AI people show the classic framing, default and sunk-cost effects? | 179 | 0 of 3 fully (direction 3/3, size 1/3) |
| [`universities/`](universities/) | Coaching hype, private colleges and study-abroad agents (India and Canada) | 240 | 5 of 13 |
| [`healthcare/`](healthcare/) | Stent vs medicines (India), early MRI (USA), private-equity birth hospital (USA) | 308 | 17 of 22 |
| [`targeting/`](targeting/) | Instant-loan apps (India), personalised flight prices (USA) | 182 | 4 of 12 |
| [`politics/`](politics/) | The same policy under different party labels, in 8 countries | 336 | 7 of 10 |
| [`state_ops/`](state_ops/) | Secret agencies and meme wars: fake "local parent" accounts vs a new vaccine, in 8 countries | 336 | 7 of 10 |
| [`fomo/`](fomo/) | FOMO: friends, influencers, crowds and apps vs a risky token, in 8 countries | design ready, not run | – |
| [`earbuds_pilot/`](earbuds_pilot/) | The very first test of the method (superseded) | 60 | – |

## Process followed for every topic study
1. Research the topic (`RESEARCH.md`).
2. Write the design and predictions, and **commit them before any data** (`PREDICTIONS.md`).
3. Run a pilot of 8 people per situation, then check it: do the answers parse, is the control stuck near 0% or 100%, are the answers in character?
4. If the design must change, record the change in `PREDICTIONS.md` **before** re-running.
5. Add extra batches of new people, pool them, and analyse (`RESULTS.md`).

## Running
- **Re-analyse saved data** (no AI calls): `python3 analyse_<topic>.py combined` inside a study folder.
- **New runs** need the `claude` tool logged in to a Claude plan. Each decision used about 0.1–0.3% of a Claude Pro 5-hour usage window.

See [`RELATED_WORK.md`](RELATED_WORK.md) for published work on simulating people with AI models, and its known problems.
