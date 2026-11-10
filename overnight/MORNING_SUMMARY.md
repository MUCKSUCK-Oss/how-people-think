# Good morning! Here's what happened overnight (6 Nov 2026)

## ✅ Done (part 1, 12:20–1:30 am)

**1. Simulation v2**
- **New trick, authority** ("doctors recommend A"): +11 points. This strength is a guess, not tuned to a real study.
- **New effect, confirmation bias** (people ignore friends who disagree too much). The surprise: it **protects** people from influencers (the choice stays at 50%), but it **keeps groups divided**. Lippmann's "we define first, then see" works as both a shield and a wall.
- **New robustness test:** I halved each of my 9 guesses, then raised each by half (18 tests). All 4 main findings held in **18 of 18**.
  - The "all tricks together" number depends mostly on one guess, so say "roughly 80–90%", not "87%".
- **New check:** people with strong preferences move less. The model probably still overstates how much they move. This is a known limit, written in the paper.
- Page updated: https://claude.ai/artifact/7YdisdyhbkTPFM8a3LQ33g (new Figure 7 and an authority switch)
- Files: `simulation/sim.py`, `simulation/README.md`. The old version is saved as `simulation/sim_v1_1_backup.py`.

**2. First paper draft** → `paper/draft_v1.md` (about 5,500 words)
- Sections: old thinkers → experiments → real cases → simulation → discussion → limits.
- **12 [YOUR OPINION] blanks.** Only you can write these.
- **[CHECK] marks** show citations to confirm.
- It includes the important counterpoint that persuasion is often weak in elections, and explains why the tricks work best on low-stakes, rushed, one-sided choices.

**3. Books** → `books/reading_notes.md` (new "version 2" parts)
- **Bernays:** 8 of 11 chapters read in part 1 (all 11 by 2:55 am, see section 9). Best finds:
  - "continuous interpretation" vs "high-spotting";
  - the fake "foot protection bureau";
  - "don't argue, create circumstances";
  - his prediction that knowing the tricks won't stop propaganda, which matches the simulation's weak prebunking result.
- **Le Bon:** all of Book I read. Best finds:
  - educated people fooled by a fake séance;
  - one vivid image beats statistics (a good idea for simulation v3);
  - crowd beliefs take a "religious shape".

**4. Three new videos (with your help, ~12:40 am)**
- You passed YouTube's "I'm not a robot" check, and I read the transcripts in the browser.
- **Episodes:** Social Media (Ep 2), ChatGPT (Ep 4), Health (Ep 6). Notes are in `topic_passages/wtf_ep2_…`, `wtf_ep4_…` and `wtf_ep6_…_notes.md`.
- **Best finds:**
  - "a dopamine hit at both ends";
  - "envy is the fuel for social media";
  - "the brain has an immune system" (AI could find the words to get past it);
  - "wine is good for you" was marketing.
- Reports page updated to **version 4**: https://claude.ai/artifact/9WZvqyjcWMUsyfarTH9cgm (Report 2 Part G, Report 4 Part G)
- The paper draft has a new **Section 4.9** on platforms and AI.

**5. Old history vs now (~12:50 am)**: five Predictive History ancient-history lectures → `topic_passages/ph_old_history_notes.md`
- **Videos:** Caesar's will, Vergil's *Aeneid* as propaganda, Alexander the Great, Constantine, and Greek theatre.
- I skipped "Pax Judaica" (antisemitic content) and the Spanish conquest (an ad blocked the transcript).
- I noted where Jiang is wrong. For example, Constantine was **not** "the first pope".
- **New paper section 2.5:** a "Then vs now" table of 9 moves, such as a gift that creates a debt, rewriting the school text, a face on every coin, and martyrdom flipping opinion.

**6. Research-based talks** → `topic_passages/research_talks_notes.md`
- **Tristan Harris** (ex-Google, TED): "the race for attention"; outrage wins by default. His test: persuasion is ethical only when the persuader's goals match yours. This is now in paper Section 1.1.
- **Robert Cialdini:** six principles with real study numbers (mints and tips, hotel towels and so on).
- **Jonathan Haidt** (TED): why left and right see morality differently; "teams shut down open-minded thinking". Good for balance.
- **Sander van der Linden** (prebunking researcher): prebunking works about 60% in the lab but only about 10% in real life. **This matches our simulation's weak prebunking result.** Added to paper Section 5.5.

## ❌ Not done
- **The other ~25 WTF episodes and ~70 Predictive History videos.** Arcmira has 0 credits until 1 Dec, and the downloader is blocked by YouTube's bot check. The browser method works, but only after you pass the check yourself, so we do a few at a time together.

**7. Citation check (done at ~12:57 am)**
I checked 20 facts online, mostly through abstracts and reliable summaries. The paper now marks them **✔**. Old version saved as `paper/draft_v1_before_citation_check.md`.
- **Confirmed:**
  - Brady's +20% retweets per moral-emotional word;
  - Chetty: top-1% kids are *more than* twice as likely to get into Ivy-Plus colleges;
  - Mijs's inequality and meritocracy finding;
  - the DeJong pharma-meals study;
  - India's pharma marketing code (UCPMP, March 2024);
  - the sugar industry paying Harvard scientists (1960s);
  - WHO 2023 "no safe level of alcohol";
  - the Bournvita "health drink" removal (April 2024);
  - the mint-and-tips study.
- **Corrected or added a warning:**
  - **Prebunking:** a 2023 reanalysis says the *Bad News* game makes people distrust *all* news, not judge better. Added to the paper.
  - **AI persuasion:** GPT-4 beat humans in debates 64% of the time, but messages tailored to each person were *not* better than generic ones. Added to Section 4.9.
  - **Decoy effect:** one study found no effect across 19 studies. Added.
  - **Hotel towels:** a replication found the "75% of guests" message was no better than a normal one.
- **Still [CHECK]:** only Johnson & Goldstein's exact 82%/42%. The paper's text confirms "about twice as high", but the exact numbers are in a figure I couldn't read.

**8. Strict paper review (done at ~2:45 am)** → `paper/review_v1.md`
I made **no changes to the paper**; you decide which fixes to make. 15 fixes, in order of importance. The top 3:
1. 🔴 **A contradiction.** Section 3.2 says the simulation shows people with strong preferences move less. But the Section 5.6 table shows they move *more* (+56 vs +50 points), because of the default rule. It needs rewriting in three places.
2. 🔴 **The confirmation-bias result depends on how extreme the influencers are.** I tested it: confirmation bias blocks extreme influencers, but **mild influencers get through better**. That's a more interesting finding ("to beat confirmation bias, sound close to people"), and it matches the WTF "brain immune system" quote.
3. 🔴 **Add an AI-use disclosure** to the paper. Most schools and competitions require one.

Also: some numbers don't match (it's six tricks, not seven; 44/70 WTF, not 41), there's no left-leaning case for balance, and the reference list needs tidying.

**9. Bernays: the whole book is now read (~2:55 am)**: chapters VII, IX and X added to `books/reading_notes.md`. Best finds:
- **The price-tag shop:** show each item's price before and after a tariff. Concrete beats abstract.
- **The Atlanta anti-lynching conference:** hold it in the South with southern ministers on stage. This is the "in-group messenger" idea, and it links to fix 2 above.
- **The modernist piano** built only to get people talking.
- **The method:** the same technique sold bacon *and* fought lynching. It has no built-in morality.

## 🌅 Part 2 (moved to 4:52 am, so a new 5-hour limit window starts as soon as the old one resets at 4:50)
It will run its **original job, the citation check**. Since that's already done, it should find almost nothing left: only the Johnson & Goldstein figure. Its main use is starting the new limit window early.

## 👉 Your 3 next steps
1. Open `paper/draft_v1.md` and fill in **3 [YOUR OPINION] blanks** today. Start with the Bernays question in Section 2.2.
2. Play with the simulation page. Try "Doctors recommend A" + "Slow down".
3. Read Bernays ch. V (lines 1383–2104 in `books/bernays_propaganda.txt`). It's the most "oh, they're doing this" chapter.

---

## Part 2 results
*(added by the 5:05 am run)*

The scheduled run began about 4:52 am. Most items had already been checked at 12:57 am, so I mainly finished the one item left open. A backup of the paper from before this run is at `paper/draft_v1_before_part2.md`.

| # | Citation | Result | What I actually read |
|---|---|---|---|
| 1 | Johnson & Goldstein 2003 (defaults, organ donation) | **Confirmed, with one number added.** Opt-out ≈ 82%, **no default ≈ 79%**, opt-in ≈ 42%. The paper now gives all three numbers, and its last **[CHECK]** is removed. | The authors' own 2004 *Transplantation* write-up of the same experiment ([PDF](https://hods.org/pdf/Defaults%20and%20Donation%20Decisions.pdf)). Its text gives 161 people, "about twice as high", and 79% for the no-default group. The 82% and 42% appear only in a chart I couldn't read, so they come from two secondary sources found by search (an [AMA Journal of Ethics commentary](https://journalofethics.ama-assn.org/article/does-how-we-ask-organs-determine-whether-people-decide-donate/2005-09) and [Kessler & Roth, NBER](https://users.nber.org/~kesslerj/papers/KesslerRoth_2025.pdf)). I saw these two only as search snippets: the AMA page blocked me (403). |
| 2 | Roozenbeek & van der Linden 2019 (~21%) | Confirmed earlier tonight (12:57 am), with the 2023 warning about the reanalysis. | Abstract and summaries (earlier run) |
| 3 | Huber, Payne & Puto 1982 (decoy, "+9%") | **Could not verify the exact +9%.** The effect itself is real. The authors' 2014 follow-up says it does replicate, but its size changes a lot. The paper already says "from summaries" and notes the failed replications. | Search results only. The 2014 PDF ([Duke](https://people.duke.edu/~jch8/bio/Papers/HuberPaynePutoJMR%202014.pdf)) wouldn't turn into readable text. |
| 4 | Worchel, Lee & Adewole 1975 (cookie jar) | Confirmed earlier tonight | Summaries |
| 5 | Mijs 2021 (inequality and meritocracy) | Confirmed earlier tonight | Abstract |
| 6 | Chetty, Deming & Friedman 2023 (top 1%, Ivy-Plus) | Confirmed earlier tonight: *more than* twice as likely | Abstract |
| 7 | Brady et al. 2017 (~20% per moral-emotional word) | Confirmed earlier tonight | Abstract |
| 8 | DeJong et al. 2016 (meals and prescribing) | Confirmed earlier tonight. It shows a link, not proof of cause. | Abstract |
| 9 | UCPMP 2024 (India's pharma marketing code) | Confirmed earlier tonight (March 2024) | News and government summaries |
| 10 | Tye 1998, "The Father of Spin" | **Not used.** The paper doesn't cite this book, so there was nothing to check. | (none) |
| 11 | Reicher (critique of Le Bon) | Confirmed earlier tonight (St Pauls 1984; Reicher, Spears & Postmes 1995) | Summaries |

**Bottom line:** the paper has **no [CHECK] marks left**. If you have time, read the original Huber 1982 paper to check the "+9%".
