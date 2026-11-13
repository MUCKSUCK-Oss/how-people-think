# How People Think

**How are people's choices steered by companies, media, institutions and the people they trust, and what protects them?**

An independent research project by **Maulik** (Class 11, India), started October 2026. It combines old writing on persuasion, published psychology experiments, real cases from India and abroad, and two kinds of simulation: a rule-based agent model, and pre-registered experiments with AI "people".

📄 **Current paper draft:** [`paper/draft_v2.md`](paper/draft_v2.md)

---

## Main findings so far

**AI-people experiments** (about 1,250 decisions, 4 topics, predictions saved before each run):

| Finding | Example |
|---|---|
| Stories about "people like us" beat advertising | Choosing a ₹30 lakh (about $34,000) study-abroad route through an agent: 10% with basic facts → **65%** after "the neighbour's son sends ₹40,000 (about $450) home a month" |
| The same fear works from a doctor and fails from an ad | "Ticking time bomb" from a cardiologist: stent choices 43% → 64%. "Could be something serious" from a clinic ad: MRI choices 43% → 36% |
| People are easier to push when deciding for someone they love | After the doctor's warning: 86% of sons and daughters chose the stent, against 43% of patients |
| Honest disclosure undoes most tricks, but not stories or desperation | Canada: 65% → 10% with honest facts. Instant-loan app for someone ashamed to ask family: 71% → 71% |
| Party supporters judge a policy by who proposed it | The same policy scored 5.5 of 7 from their own party and 2.9 from the rival, in all 8 countries tested |
| Unfairness angers people more than privacy loss | "Other users see this seat for $279" cut flight booking from 43% to 14% |

**Rule-based simulation** (1,000 simulated people, tricks tuned to published experiments):
- Single tricks move a 50/50 choice by 6–21 points.
- Five stacked tricks reach roughly 80–90%.
- The default is the strongest single trick.
- Slowing down protects more than learning the tricks in advance.
- Checked across 1,408 combinations of assumptions (SALib).

⚠ **AI people matched humans in direction on 3 of 3 classic experiments, but in size on only 1.** All AI-people results are read as directions, not exact human percentages. Details and limits: [`paper/draft_v2.md`](paper/draft_v2.md), Sections 6 and 8.

---

## Repository layout

```
paper/                     The paper
  draft_v2.md              current draft (about 11,500 words)
  archive/                 earlier drafts and the strict review of draft 1

simulation/
  requirements.txt         Python packages (for the SALib / NDlib checks only)
  rule_based/              agent-based model of stacked tricks (standard library only)
  ai_people/               pre-registered experiments with AI "people"
    ai_person.py           shared helper: one fresh AI-person call
    classics/              method check: framing, default, sunk cost vs human results
    universities/          coaching ads, private colleges, study-abroad agents
    healthcare/            stents, MRIs, private-equity hospitals
    targeting/             instant-loan apps, personalised prices
    politics/              the same policy under different party labels, 8 countries
    earbuds_pilot/         the first test of the method (superseded)
    RELATED_WORK.md        papers on using AI models to simulate people

sources/                   Evidence collected before writing
  books/                   reading notes: Le Bon, Bernays, Lippmann, Machiavelli, Plato
  case_reports/            five case reports from podcast and lecture transcripts
  topic_notes/             passages and notes by topic
  wtf_podcast/             WTF podcast episode index and notes
  transcripts/             lists of videos and fetch logs (transcript text is not uploaded)

docs/
  PROJECT_PLAN.md          topics, status and order
  progress_log/            dated progress summaries
  planning/                early literature review, bibliography, research gaps
```

Every AI-people study folder follows the same pattern:

| File | What it is |
|---|---|
| `RESEARCH.md` | the evidence the situations were built from (news, regulators, papers) |
| `PREDICTIONS.md` | predictions and design, **committed before any data** |
| `RESULTS.md` | results, the honest check of each prediction, and limits |
| `*.py` | the experiment and its analysis script |
| `data/` | every raw AI-person answer (JSON) |
| `output/` | run logs and analysis printouts |

---

## How to reproduce

**Rule-based simulation** (Python 3, no extra packages):
```bash
cd simulation/rule_based && python3 sim.py
```

**Robustness checks** (SALib and NDlib):
```bash
python3 -m venv simulation/.venv && simulation/.venv/bin/pip install -r simulation/requirements.txt
```
```bash
cd simulation/rule_based && ../.venv/bin/python salib_test.py && ../.venv/bin/python ndlib_check.py
```

**Re-analyse the AI-people data** (no AI calls needed, standard library only):
```bash
cd simulation/ai_people/healthcare && python3 analyse_health.py combined
```

**Run new AI-people decisions** (needs the `claude` command-line tool, logged in to a Claude plan):
```bash
cd simulation/ai_people/targeting && python3 targeting.py pilot
```

Each AI person is a separate, fresh call to Claude Haiku. The person has no tools and no memory, and it is not told it is part of an experiment.

---

## Research rules followed
1. **Research each topic before simulating it.**
2. **Write predictions and commit them before running.** Wrong predictions are reported as wrong (33 of 57 fully right so far).
3. **Small pilot first.** If a design change is needed, record it before re-running.
4. **Label what was actually read.** Most papers were checked through abstracts or reliable summaries; anything unconfirmed is marked **[CHECK]**.
5. **Balance:** cases from India and abroad, and from both left and right.

## Status
- **Done (researched, simulated and in the paper):** universities, healthcare, personal targeting, world politics (party labels in 8 countries).
- **Next:** state influence operations on social media, FOMO, corporate dark patterns, cookie-consent pop-ups, films as propaganda.
- **Not yet done:** testing the key results with real people (with consent and an ethics check).

## Copyright and privacy
- Book texts and full podcast or video transcripts are **not** included; only short quotes and my own notes are.
- Contact details are kept out of this repository.

---
*Maulik, 2026. Feedback is welcome.*
