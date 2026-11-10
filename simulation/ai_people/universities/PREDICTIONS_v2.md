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
