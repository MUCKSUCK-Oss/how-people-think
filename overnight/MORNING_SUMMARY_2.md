# Good morning! Night of 11 Nov 2026: universities

## In one line
**I researched how universities and agents really trick families, built a realistic simulation from that, and found that "people like us" (a cousin, the neighbour's son) is the strongest trick, much stronger than ads. Honest disclosure undoes most of it.**

## What I did
1. **Research first, as you asked** → `simulation/ai_people/universities/RESEARCH.md`
   - **India:**
     - 22 fake universities (UGC)
     - the 2024 ban on "100% selection" ads (coaching)
     - coaching institutes "buying" toppers for their ads
     - 1.9 million empty engineering seats (colleges market hard to fill them)
     - the NRI-quota admission fraud
     - education loans have the highest default rate of any personal loan
   - **Abroad:**
     - **CBC investigation** (read in full): agents in Punjab promise "PR no problem, visa guaranteed", and get paid by colleges as well as by families. A farmer sold 2 trucks to pay.
     - **DW video** (read): Indian students in Germany sold expensive private universities.
     - The fake Canadian admission letters case.
     - DeVry ($100M fine for "90% get jobs").
     - Corinthian ($5.8 billion of loans forgiven).
   - **Papers:**
     - Jensen 2010: true salary information changes choices.
     - Rankings move applications.
     - Indian students don't gain critical thinking in college (Loyalka 2021).
   - **Videos:** YouTube blocked me (rate limit) after 2 videos, so I stopped, as agreed.
2. **Built a realistic scenario from that research** (students AND parents; a domestic college AND Canada via an agent). I wrote the predictions first and saved them to GitHub.
3. **Ran 2 small pilots.** The first pilot showed a design problem: option A had no downsides. I fixed it with real facts (old labs; local jobs pay ₹12–18k) and recorded the change.
4. **Ran an extra batch** and combined it with pilot 2: 168 decisions in total.

## The results → `simulation/ai_people/universities/RESULTS_v2.md`
**Canada via an agent (₹30 lakh, mortgage):**
| What the family saw | Chose Canada |
|---|---|
| Basic facts | 7% |
| + agent: "office job anywhere, PR no problem" | 29% |
| **+ "neighbour's son sends ₹40,000 home every month"** | **64%** 😮 |
| + honest facts (PR not guaranteed, 40–50 h work, agent gets a commission) | 14% |

> *"The agent's promises sound like typical agent BS, but the neighbour's son sends ₹40,000 home every month — that's real proof."* (an AI student)

**Private college (₹11L vs ₹4.5L government college):** a 7% base. Salary hype mostly moved **parents** (0 → 29%), and "your cousin studied there" moved students and parents most (29%). Honest numbers plus "the counsellor gets a commission" brought it back down to 14%.

**Big lessons:**
- **People believe people, not ads.** Even when they know the agent is lying.
- **Disclosure laws work** (at least on AI people). This supports India's 2024 CCPA rule, and shows why it matters that Canada never signed the agent code of conduct.
- **AI parents were more trickable than AI students.** I predicted the opposite.
- Honest score: **6 of 13 predictions right**, 3 partly, 4 wrong.

## ⚠ Important discovery: the cost
**Each AI person uses about 0.27% of your 5-hour limit.** Tonight used about 72% of the limit (about 50% on simulations). So I could only run **14 people per scenario, not 40**. The results are directions, not exact numbers. A bigger run needs about 2 full limit windows.

## Also saved
- 🎬 **Movies & propaganda is on hold until you share your ideas** (the "no soldier left behind" theme).
- Everything is uploaded to GitHub under your name only.

## Your next steps
1. Read `RESULTS_v2.md`, especially the quotes.
2. Decide: run the full university version later (about 2 limit windows), or move on to **healthcare** (research first, same method).
3. Share your movie/propaganda ideas when you're ready.
