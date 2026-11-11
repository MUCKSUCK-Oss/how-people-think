# University traps, version 2: design and predictions
*Written night of 11 Nov 2026, BEFORE any v2 data. Built from `RESEARCH.md`. Saved to git first.*

## What changed from run 1 (and why)
| Run 1 problem | v2 fix (evidence) |
|---|---|
| Made-up numbers; B 4.5× the cost for the same outcome, so nobody fell for it | **Realistic, closer choice**: ₹4.5L vs ₹11L, where the private college really is a bit better on outcomes (a genuine trade-off) |
| Families saw honest medians that real ads never show | **Control = the brochure as families really see it** (no medians). A separate "honest numbers" version adds the medians |
| Students only | **Students AND parents** (research: parents usually decide on money) |
| India only, ad banners only | **Two scenarios**: domestic college AND **study abroad through an agent** (the CBC/DW/fake-letter evidence) |
| No test of the fix | A **disclosure version** that copies the CCPA 2024 rule (honest numbers in the same font, commission disclosed) |

## Scenario 1: domestic B.Tech (Computer Science)
- **A:** a government engineering college, 60 km from home, about ₹4.5 lakh total for 4 years (including a rented room). AICTE approved, NAAC B+.
- **B:** a private university, 250 km away, about ₹11 lakh total with hostel. Modern campus, AC classrooms, "40+ recruiters".
- **Honest numbers, shown only in some versions:** A median ₹4.2 LPA, 64% placed; B median ₹4.6 LPA, 70% placed. B is a bit better but costs 2.5× more, so it's a real judgment call.

| Version | What's added | Real-world source |
|---|---|---|
| S1-1 **brochure** | nothing (what families usually see) | – |
| S1-2 **honest** | the medians and placement % for both | NIRF-style data |
| S1-3 **hype** | B: "Highest package ₹42 LPA, 100% placement assistance, 500+ offers" | Placement hype; DeVry; CCPA |
| S1-4 **counsellor** | hype + B's counsellor calls: "few seats left, pay ₹25,000 booking by tomorrow, loan approved in 3 days through our partner bank" | Seat-booking pressure, loan push |
| S1-5 **relatives** | hype + "your cousin studied at B, now in a Bengaluru IT company; relatives say B is a big name" | Family and social proof |
| S1-6 **all** | hype + counsellor + relatives | Real families face all of these together |
| S1-7 **all + disclosure** | all + honest medians in the same font + "the counsellor is paid a commission per admission" | The CCPA-style fix |

## Scenario 2: study abroad through an agent
- **A:** stay in India: B.Com/BBA at a decent local college, about ₹3 lakh total, living at home.
- **B:** a 2-year business diploma at a private career college near Toronto, Canada, through an agent: about ₹30 lakh for the first year with living costs, which the family would raise with a loan or by mortgaging land.

| Version | What's added | Source |
|---|---|---|
| S2-1 **brochure** | basic facts only (the college is eligible for a post-graduation work permit) | – |
| S2-2 **honest** | independent facts: PR is not guaranteed (big backlog); most students work 40–50 h/week at minimum wage; rooms shared by 6–8 people; the agent is paid a commission by the college | CBC, DW |
| S2-3 **agent pitch** | the agent says: "Canada needs workers. Office job anywhere in Toronto. PR no problem after 2 years. Weak English is fine. Visa guaranteed." | CBC hidden camera |
| S2-4 **agent + village** | agent pitch + "300 young people from your village have gone; the neighbour's son sends ₹40,000 a month home" | CBC (300 from one village) |
| S2-5 **agent + village + disclosure** | S2-4 + the honest facts from S2-2 | The fix |

## People
- **Pilot:** 8 people per scenario (4 students, 4 parents) × all versions = **96 decisions**.
- **Full run (only if the pilot looks sound):** 40 per scenario (20 students, 20 parents) = 280 + 200 = **480 decisions**.
- Life stories vary: state/city, income, decision style (gut → very careful), trust in advertisements/agents, how much relatives' opinions matter. Scenario 2 people come mostly from Punjab, Haryana and Gujarat (where the CBC/agent evidence comes from), plus other states.
- Each decision is a separate, fresh Claude Haiku call: no tools, no memory, not told it's an experiment.
- **Answer:** CHOICE (A/B), LOAN (yes/no), REASON.

## Predictions (before any data)
**Scenario 1 (domestic)**
1. **Brochure:** a real split. **30–50% pick the private college** (it looks better, and the families don't see the medians).
2. **Honest numbers lower the B share** compared with the brochure, because the families see the small salary gain for 2.5× the cost.
3. **Hype:** a small effect, or a backfire among careful people (run 1: hype was called out).
4. **Counsellor deadline:** a small effect or backfire (AI people resist countdowns).
5. **Relatives:** **the strongest single trick** (run 1: social proof was the only one that worked), especially for parents who care what relatives say.
6. **All:** about the same as relatives, not the sum.
7. **Disclosure cuts B back toward the "honest" level.** The fix works for AI people (but they may be more rational than real families).
8. **Parents vs students:** parents care more about cost, so lower B overall, *except* "big-name" parents, who are the most trickable.

**Scenario 2 (abroad)**
9. **Brochure:** a low B share (10–25%) because ₹30 lakh is huge.
10. **Agent pitch:** a mixed effect. Gut/trusting people move toward B; careful people call "visa guaranteed" a red flag and resist (the loud-trick pattern).
11. **Village social proof:** a clear increase, the most effective part (a quiet, human trick).
12. **Disclosure:** a big drop in B, larger than in Scenario 1, because the honest facts are severe (50 h/week work, shared rooms, no PR guarantee).
13. **Students want B more than parents do** (the dream), but parents control the loan.

## Rule for scaling up
After the pilot I check:
- (a) the answers parse correctly;
- (b) the control is not stuck near 0% or 100% (no floor or ceiling);
- (c) the answers sound realistic and in character.

Only if all three pass, I run the full version.

---
## Pilot 1 result and design change (added after pilot 1, before pilot 2)
- Pilot 1 (96 decisions, saved as `data/uni2_pilot1.json`): the brochure control was **0%** for B in both scenarios (a floor). The tricks still moved people: relatives 0→50% among parents, village 0→38%; disclosure cut it back.
- **Diagnosis:** option A was shown with no downsides, while real families choose expensive options *because* the cheap one has real problems.
- **Change (realism, not tuning to a result):**
  - **S1-A** adds: "Seniors say the labs are old, several teaching posts are vacant, and fewer companies visit." This is typical of many government colleges and consistent with A's lower placement % in the honest data.
  - **S2-A** adds: "Local B.Com graduates usually find jobs paying ₹12,000–18,000 a month, and many stay unemployed for a year or more." This is the push factor reported by CBC/DW.
- **Predictions stay the same.** Pilot 2 is checked against the same 3 rules before any full run.

## Pilot 2 result and the decision for the main run (added before the extra batch)
- Pilot 2 (96 decisions, `data/uni2_pilot.json`): Scenario 1 brochure is still 0% B (floor), Scenario 2 brochure 12%. The tricks clearly raise B: S1 relatives 38%, S2 agent + village 50%. Disclosure cuts it: S1 12%, S2 0%.
- **The S1 floor looks like a stable property of AI people** (very cost-careful when no trick is present), not a design bug. So "backfire" can't be measured in S1; effects are read as increases from 0.
- **Usage discovery:** each AI-person call costs about 0.27% of the Pro 5-hour limit, so the planned 480-decision full run doesn't fit tonight. **Instead:** an "extra" batch of **6 new people per scenario (72 decisions), same design as pilot 2**, pooled with pilot 2 (14 people per scenario). The full 40-person run can be done later on fresh limits.

## Extra batch 2 (added 11 Nov 2026, before running it)
- Leftover usage before the limit reset → **6 more NEW people per scenario (72 decisions)**, same design as pilot 2, pooled → 20 people per scenario.
- Only change: decision styles shifted so this batch is mostly "mostly careful" / "very careful" (earlier batches had only 2 "very careful" people). Predictions unchanged.
