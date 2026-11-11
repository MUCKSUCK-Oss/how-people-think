# How Choices Are Made For Us: Old Tricks, New Tools

*Second draft, 11 Nov 2026. It adds the AI-people experiments (Section 6) and the fixes from `paper/archive/review_v1.md`. The first draft is kept as `paper/archive/draft_v1.md`. Everything here is a starting point for you to rewrite in your own voice.*

**How to use this draft**
- **[YOUR OPINION]** marks a place only you can write. The paper is stronger when your own view is clearly separate from the evidence.
- **✔** marks a citation checked online on 6 Nov 2026 (usually through the abstract or reliable summaries, not the full paper). **[CHECK]** marks one still to confirm in the original source before you submit. Many studies were cited from memory or from summaries (see `simulation/rule_based/README.md` and the reports for each one's status).
- The rule-based simulation numbers come from `simulation/rule_based/results.json` (v2, 6 Nov 2026), with outside checks in `simulation/rule_based/salib_results.json` and `simulation/rule_based/ndlib_results.json`. The AI-people numbers come from `simulation/ai_people/*/RESULTS.md`.
- This draft is about 10,000 words including references. For a 6,000-word limit, Sections 4 and 5 can be shortened.

**How this paper was made** *(a draft note: edit it so that every sentence is true, then keep it in the final paper)*
> An AI assistant (Claude) helped find and summarise sources, build both simulations and write a first draft. I chose the question and the topics, decided which cases and evidence to include, directed each simulation, checked key sources and wrote the opinions and the conclusion.

---

## Abstract

People like to think they choose freely. But many everyday choices, such as which app to use, which medicine a doctor prescribes, which college to join or which politician seems "authentic", are shaped by the way options are presented. This paper brings together five kinds of evidence.
1. **Old books:** what thinkers from Plato to Bernays already said about steering people.
2. **Experiments:** what modern psychology has measured.
3. **Real cases:** about 155 podcast and lecture episodes (the *WTF* podcast with Nikhil Kamath and the *Predictive History* channel by Jiang Xueqin), plus news investigations and regulator reports from India and abroad.
4. **A rule-based simulation:** 1,000 simulated people choosing between two equally good options while a "manipulator" uses six tricks. Where a published experiment exists, each trick's strength is tuned to it.
5. **AI people:** about 900 decisions by AI-model "people" with Indian and American life stories, in realistic situations built from the research. The situations cover choosing a college or going abroad through an agent, deciding on a stent, an MRI or a hospital for childbirth, and taking an instant-loan app or a "personalised" price.

**Rule-based simulation:**
- Each trick alone moves a 50/50 choice by 6–21 percentage points.
- Five classic tricks together move it to roughly 80–90%.
- A pre-selected default is the strongest single trick.
- Slowing down protects more than learning about the tricks in advance.
- These findings held across 1,408 combinations of assumptions, in which all nine guesses were changed at once; stacking usually beats any single trick by 10–20 points.
- Whether careful thinkers are only a little safer depends on one guess, so it is presented as an open question.

**AI people:**
- They matched humans in *direction* on 3 of 3 classic experiments, but in *size* on only 1, so their results are read as directions.
- In all three topics, **stories about "people like us"** (a neighbour, a cousin, a coworker) moved choices more than any advertisement. Loud tricks such as hype, countdowns and fake discounts were often spotted and backfired.
- **The same fear message worked from a doctor and failed from an ad.**
- **Honest disclosure undid most tricks, but not stories or desperation.**

Both simulations are teaching tools, not proof about real people. Together with the other evidence, they suggest one main point: **the tactics are old, only the tools are new, and they work best when they come through people we trust, when they are stacked, and when people are rushed or desperate.**

**[YOUR OPINION]** One sentence on why you, as a Class 11 student in India, care about this question.

---

## 1. Introduction

### 1.1 The question
This paper asks two linked questions:
1. **How are people's choices steered by others?** This covers companies, politicians, media figures and institutions such as schools.
2. **Which kinds of steering work best, on whom, and what protects people?**

"Manipulation" here means influencing a choice in a way that works around a person's reasoning instead of through it. A good argument is persuasion. A pre-ticked box that most people never notice is closer to manipulation. In between is a large grey area, and much of this paper lives there.

A useful test comes from Tristan Harris, a former design ethicist at Google: "the only form of ethical persuasion that exists is when the goals of the persuader are aligned with the goals of the persuadee" (TED 2017). Robert Cialdini makes a similar point: the same six principles (reciprocity, scarcity, authority, consistency, liking and consensus) are ethical when they point to true facts and manipulative when they're faked.

**[YOUR OPINION]** Where do *you* draw the line between persuasion and manipulation? Give one example from your own life (an app, an ad, a teacher or a friend).

### 1.2 Why it matters now
The basic tricks are not new. Gustave Le Bon described repetition as a way to plant beliefs in crowds in 1895. Edward Bernays described using doctors to sell bacon in 1928. What has changed is scale and speed:
- An app can test a thousand versions of a button in a day.
- A video can reach millions of people in hours.
- A recommendation algorithm can decide which of two options you even see.

### 1.3 What this paper adds
Most research looks at one technique in one setting, for example a lab study of repetition or a field study of defaults. This paper instead:
1. sets **old ideas side by side** with the experiments that later measured them (Section 2);
2. collects **real, recent cases** from long-form podcasts where powerful people speak at length (Section 4);
3. builds a **simulation** to ask what happens when several tricks are **stacked**, which is hard to test on real people (Section 5);
4. **tests its own assumptions**, reporting which conclusions survive when the guesses change (Section 5.7);
5. runs **pre-registered experiments with AI people** in realistic Indian and American situations built from news investigations and research (Section 6), after first checking the method against classic experiments.

---

## 2. What the old thinkers said

*Sources: `sources/books/reading_notes.md`. Only key chapters were read; the notes list exact line ranges.*

| Old idea | Who said it | What later experiments found |
|---|---|---|
| Repeat a claim boldly, without proof, and it spreads | Le Bon, *The Crowd* (1895) | Repeated statements feel truer (Hasher et al. 1977; Hassan & Barber 2021) |
| Ideas spread by contagion; people imitate | Le Bon (1895) | Social proof and herding (Asch 1951; Salganik et al. 2006) |
| Prestige "paralyses our critical faculty" | Le Bon (1895) | Obedience to authority (Milgram 1963) |
| Use trusted experts instead of ads; make the buyer think it's their own idea | Bernays, *Propaganda* (1928) | Expert endorsement; people don't know why they choose (Nisbett & Wilson 1977) |
| We act on "pictures in our heads", and we define first, then see | Lippmann, *Public Opinion* (1922) | Confirmation bias, motivated reasoning |
| It's enough to *appear* good; most judge by appearance | Machiavelli, *The Prince* (written 1513, published 1532) | Impression management |
| Prisoners mistake shadows for reality | Plato, *Republic* VII (~375 BC) | Filter bubbles, framing |

### 2.1 Le Bon: affirmation, repetition, contagion
Le Bon said leaders plant beliefs with three tools:
- **affirmation:** stating something boldly, with no proof;
- **repetition:** saying it again in the same words;
- **contagion:** once enough people repeat it, it spreads on its own.

He also noticed that repetition works partly because we forget *where* we heard something, so it starts to feel like common knowledge. Modern psychologists call this source confusion.

**Caution:** Le Bon held prejudiced views about women, workers and non-Europeans. Later research shows crowd behaviour usually follows shared group norms and identity rather than "madness" (Reicher's 1984 study of the St Pauls riot; Reicher, Spears & Postmes 1995) ✔. This paper uses his description of tactics, not his theory of crowds.

### 2.2 Bernays: the openly admitted playbook
Bernays, often called the father of public relations, wrote openly that a small group who understand mass psychology shapes the public's tastes, and he thought this was necessary. His methods map closely onto modern cases:
- **Third-party authority.** Don't advertise bacon. Get doctors to recommend a hearty breakfast.
- **Make it feel like the buyer's own idea.** Don't sell pianos. Make music rooms fashionable, and the piano follows.
- **Narrow the options.** People can't evaluate everything, so whoever narrows the menu has power. This is exactly where defaults and decoys get their strength.

**[YOUR OPINION]** Is Bernays right that some "invisible government" of opinion is unavoidable in a big society? Or is that just a convenient belief for someone who sold PR?

### 2.3 Lippmann and Plato: the picture in our heads
Lippmann's key line is that "we define first and then see". We meet most of the world second-hand, through reports, and our stereotypes decide what we notice. Plato's cave makes the same point as a story: whoever controls the shadows controls what the prisoners think is real. Both ideas feed the confirmation-bias part of the simulation (Section 5.4).

### 2.4 Machiavelli: appearance over reality
Machiavelli advised that a ruler need not *be* good, only *appear* good, because "every one sees what you appear to be, few really know what you are". Section 4.3 shows a modern example of image management in exactly this sense.

**[YOUR OPINION]** Was Machiavelli describing how rulers behave, or advising them to behave that way? Does it matter?

### 2.5 Then and now: the same moves, 2,000 years apart
*(Added 6 Nov 2026 from five Predictive History lectures on ancient history; see `sources/topic_notes/ph_old_history_notes.md`. The history column uses what historians generally agree on, not only the lecturer's interpretation.)*

| The move | Then | Now |
|---|---|---|
| **A gift that creates a debt** | Caesar's will gave every Roman citizen cash and opened his gardens as public parks; his heir borrowed money to pay it (44 BC) | Pre-election cash promises, "free" product tiers, pharma gifts to doctors (Report 2) |
| **Martyrdom flips opinion** | After Caesar's murder, Romans felt guilty for doubting him, and his myth won | Attacks on a leader turning into sympathy (Report 1) |
| **Rewrite the school text** | Augustus backed Vergil's *Aeneid* to replace Homer in Roman schools, teaching obedience over liberty | Curriculum fights in many countries; Bernays on winning schools (1928) |
| **A face on every coin** | The imperial cult put the emperor's image on statues and coins across the empire | A leader's face on billboards, apps and scheme posters (mere exposure) |
| **One symbol, two audiences** | Alexander was hailed "son of Zeus-Ammon", sacred to Greeks and Egyptians at once | Messages built to please several groups at once |
| **Recruit the patron, get the network** | Early bishops were local aristocrats who brought their clients with them | Influencer-first platform growth (WTF Ep 2); Bernays's "key men" |
| **Religion or ideology as glue, dissent as heresy** | Constantine backed one church; "orthodoxy" made other views heresy | Labelling critics "anti-national" or "traitors", from any side |
| **Entertainment builds identity** | Athens' state theatre festival, paid for by the rich, taught citizens to be democrats | Films, sport and streaming as "unconscious carriers of propaganda" (Bernays) |
| **The crowd punishes uncomfortable truth** | Euripides' *Trojan Women* (415 BC), staged after Athens' massacre at Melos, lost the prize | Self-criticism punished online; "rally round the flag" |

**What changed is the speed and the precision, not the moves.** Tristan Harris (TED 2017) puts it in one line: when people gossiped on the phone in the 1970s, there weren't "a hundred engineers on the other side of the screen who knew exactly how your psychology worked".

**[YOUR OPINION]** Which "then vs now" pair surprised you most? Is there any move today that has *no* ancient version?

---

## 3. What experiments show

### 3.1 The main techniques
| Technique | What it is | Key study (status) |
|---|---|---|
| **Default** | One option is pre-selected | Johnson & Goldstein 2003: in an online experiment with 161 people, donation was "about twice as high" when donating was the default: about 82% with opt-out, 79% with no default, and 42% with opt-in ✔ |
| **Decoy** | Add a worse version of the option you want chosen | Huber, Payne & Puto 1982: about +9% on average for the target (from summaries; original not read). ⚠ Often fails to replicate: Yang & Lynn 2014 (11 of 91 attempts); Frederick, Lee & Baskin 2014 found no attraction effect across 19 studies with realistic products |
| **Social proof** | "Most people chose this" | Muchnik, Aral & Taylor 2013: one fake up-vote made positive ratings 32% more likely (checked) |
| **Herding** | Seeing others' choices makes outcomes unpredictable | Salganik, Dodds & Watts 2006, 14,341 participants (checked) |
| **Repetition** | Hearing a claim again makes it feel true | Hassan & Barber 2021: rises on a log curve, biggest jump at the second exposure (checked) |
| **Scarcity and urgency** | "Only 2 left", "ends in 10 minutes" | Worchel, Lee & Adewole 1975 (*JPSP* 32:906): cookies from a jar that went from 10 to 2 were rated more desirable ✔ (via summaries) |
| **Authority** | An expert or famous person endorses it | Milgram 1963 (obedience, not choice); Bernays's methods |
| **Stacked "dark patterns"** | Several tricks combined on one website | Luguri & Strahilevitz 2021: sign-ups 11.3% → 25.8% (mild) → 41.9% (aggressive) (checked) |
| **Prebunking** | Learning the tricks in advance | Roozenbeek & van der Linden 2019: fake headlines rated about 21% less reliable after playing *Bad News* ✔. ⚠ A reanalysis argues players became more sceptical of *all* news rather than better at telling true from false (Modirrousta-Galian & Higham 2023) |
| **Corrections** | Fact-checks after exposure | Walter & Tukachinsky 2020 meta-analysis: corrections reduce but don't erase misinformation (checked) |
| **Personal stories** | One vivid case instead of statistics | Fagerlin, Wang & Ubel 2005: patient anecdotes changed treatment choices even when correct statistics were given (41% vs 20% chose bypass surgery, depending on the anecdotes) ✔ (via abstract) |
| **Fear appeals** | "Something terrible will happen unless…" | Tannenbaum et al. 2015 meta-analysis (127 papers, about 27,000 people): fear appeals work, with a small effect (d = 0.29), strongest for one-time actions; no backfire on average ✔ |

Even the most famous studies have their own debates. Later work on Milgram's archives found that many participants doubted the set-up, and results varied a lot between versions (Perry 2013; Haslam & Reicher 2012) **[CHECK]**. Conformity in Asch-style tests is real but smaller in later replications and varies by culture (Bond & Smith 1996) **[CHECK]**.

### 3.2 An important counterpoint: persuasion is often weak
It would be wrong to say people are puppets. Large studies of election campaigns find **tiny or zero** average effects of ads and canvassing on how people vote (Kalla & Broockman 2018; Coppock, Hill & Vavreck 2020). Mercier (2017) argues that people are good at rejecting messages that clash with what they already believe or come from sources they don't trust.

Persuasion looks strong in other settings: when one source controls the information, as with Nazi radio (Adena et al. 2015) or Russian TV in Ukraine (Peisakhin & Rozenas 2018), and when the message fits what listeners already believe.

**How to fit these together:** this paper's argument is that the tricks work best when:
1. people don't care much which option they pick;
2. they are rushed;
3. they have no competing information.

Product choices, app settings and sign-up forms often meet all three conditions. A vote for president usually doesn't. The rule-based simulation *cannot* test this yet, because its default rule ignores how much people care (Section 5.6). The AI-people experiments add a fourth condition: **4. the message comes through someone they trust** (Section 6.7).

**[YOUR OPINION]** Which kind of choice in your life is most like an "I don't really care" choice that is easy to steer, and which is a choice where you'd resist?

---

## 4. Cases from real life

*Sources: `sources/case_reports/1_trump.md` to `sources/case_reports/5_education_system.md`, built from transcripts of 44 of 70 WTF episodes and 111 of 182 Predictive History videos. Each claim links to a timestamp in the reports. Cases are grouped by technique, not by person.*

**How the cases were found:** transcripts were searched for keywords (for example "default", "monopoly", "narrative", "doctor", "fear") and the matching passages were read. Not every episode was read in full. This means the cases were selected, not sampled, so they can show that a technique is used but not how common it is (Section 8).

### 4.1 Repetition and familiarity
- **Mankind Pharma's extra second.** India does not allow prescription drugs to be advertised to the public. According to a guest on WTF ("Pharma"), Mankind ran ads for its over-the-counter products and held its company logo on screen for over a second instead of the usual half-second, so the name was familiar before its medicines reached each region. This is the mere-exposure effect (Zajonc 1968) used to get around an advertising ban.
- **Simple lines, repeated.** A WTF guest describes Trump's habit of repeating very simple phrases and says online creators copy it so that audiences tie a few words to them. Le Bon described exactly this in 1895.

### 4.2 Authority and trusted messengers
- **The doctor as the channel.** A pharma guest on WTF says a large share of a drug's price pays for medical representatives who visit doctors. Because patients can't be targeted directly, the doctor becomes the channel. This is Bernays's "get the doctors to say it" in its modern form. Studies link industry payments to doctors with more prescribing of the paying company's drugs (DeJong et al. 2016 ✔: even one industry-paid meal was associated with more prescribing of the promoted brand in US Medicare data; an association, not proof of cause). In India, the tax department alleged in 2022 that the makers of Dolo-650 gave doctors freebies worth about ₹1,000 crore; the Supreme Court called it a "serious issue" (an allegation, not a finding). The AI-people experiment in Section 6.5 measures this channel directly: the same fear message worked when a doctor said it and failed when an ad said it.
- **The self-experimenter.** Bryan Johnson, who reportedly takes about 100 pills a day and points people to his website, seems credible because he tests everything on himself. A doctor on the same panel says parts of the regimen have "no proof". This makes a good case of authority from personal commitment rather than expertise.

**[YOUR OPINION]** Who did *you* find more convincing, Johnson or the doctor? Why?

### 4.3 Appearance and image management
- A serving UAE minister tells a large audience that manipulators "don't survive for long", then says no member of Dubai's ruling family has ever "put on an act". Whatever the truth, a government minister vouching for his own rulers' sincerity is image management in Machiavelli's sense, and outsiders can't check it.

### 4.4 Framing: the same fact, different words
- **"Where does choice end and monopoly start?"** PhonePe argues against a cap on its market share by describing its dominance as customers freely choosing it.
- **"I wouldn't call it a monopoly, I'd say they are very competitive."** A guest's answer to a question about a battery company.
- **"National security."** A pharma guest calls fear about dependence on Chinese ingredients "a narrative I don't believe in".

In all three, the wording changes how the same fact feels (Tversky & Kahneman 1981).

### 4.5 Defaults and owning the menu
- **"Your moat becomes distribution."** Nikesh Arora says that over time, consumer companies win by owning distribution, such as the shelf, the app store or the habit, even when the product "doesn't stay as good".

This is the business version of the default effect: if you are already the pre-selected option, many people never look further. The simulation's strongest single trick (Section 5.2) is exactly this.

### 4.6 Fear, anger and attention
- WTF guests (Nas Daily, Yuval Noah Harari) argue that engagement-driven algorithms reward anger. Research supports this: each moral-emotional word in a tweet raised retweets by about 20% (Brady et al. 2017, 563,312 tweets ✔).
- Jiang Xueqin argues that "the game is not to manipulate people but to distract them". This matches research on governments that flood social media with distraction instead of arguing (King, Pan & Roberts 2017).

### 4.7 A persuader studied in action: a YouTube prophet
The *Predictive History* channel is useful as a **case study of persuasion techniques**, not as a source of facts:
- **Advertising his hits:** he lists his successful predictions and stays silent on the misses (hindsight bias).
- **One test set far in the future:** "if Trump doesn't get a third term, ignore me". It sounds testable, but it can't be checked for years.
- **"Just connecting dots":** a chain of loose links between people, the pattern-seeking that predicts conspiracy belief.
- **Personal stories:** stories lower a listener's guard (narrative transportation).
- **Hints of secret knowledge.**

⚠ **Warning:** the channel also repeats known antisemitic and "replacement" conspiracy tropes, sometimes with the disclaimer "I'm not saying this as an anti-Semitic comment". These are recorded in Report 4 as examples of how prejudice is packaged, **never as fact**.

**[YOUR OPINION]** Why do you think millions of people watch this channel? What did *you* find convincing before you knew the techniques?

### 4.8 Institutions: the belief that the race is fair
- In a WTF conversation, Ruchir Sharma argues that capitalism doesn't need equal outcomes, but it does need a *feeling* of equal opportunity.
- Research finds that more unequal countries believe *more* strongly in meritocracy (Mijs 2021, 25 years of survey data ✔).
- Children from the richest 1% of families are more than twice as likely to attend Ivy-Plus colleges as middle-class children with the same SAT/ACT scores, mainly because of legacy preferences, non-academic ratings and athlete recruitment (Chetty, Deming & Friedman 2023 ✔).

This is a large-scale "default" too: a belief everyone grows up with and rarely examines.

**[YOUR OPINION]** You are inside India's exam system now. Does it feel like a fair race to you? What would change your mind?

### 4.9 Platforms and AI: the people who build the machines explain them
*(Added 6 Nov 2026 from WTF Ep 2 "Social Media" and Ep 4 "ChatGPT"; see `sources/topic_notes/`.)*
- **The business model.** A social-media founder describes "a vicious cycle of a dopamine hit at both ends": likes keep the user coming back, and every extra minute earns the platform ad money. The goal is time spent, not good choices.
- **Envy and negativity are rewarded.** A creator calls envy "the fuel for social media" and admits that a negative comment on a popular page attracts likes from other envious people. This is the platform version of Le Bon's point that crowds reward extreme feelings.
- **Top-down growth.** New platforms recruit influencers and ministers first, and the public follows. This is Bernays's 1928 "key men" method.
- **AI-tailored persuasion.** In 2023 a guest compared the mind to an immune system that rejects ideas too far from its beliefs. He predicted that ChatGPT would learn "a specific set of words" to fit any message inside that tolerance. This is exactly the confirmation-bias mechanism in Section 5.4, and why the simulation's result (confirmation bias protects against influencers) could break if messages are tailored to each person. Recent studies are mixed ✔. In debates, GPT-4 given basic personal data about its opponent was more persuasive than a human 64% of the time (Salvi et al., *Nature Human Behaviour* 2025). But GPT-4 messages tailored to people's demographics and politics were *not* more persuasive than generic GPT-4 messages (Hackenburg & Margetts, *PNAS* 2024, 8,587 people). AI persuades, but the "perfect words for each person" effect isn't proven yet.
- **Health halos.** On WTF Ep 6, a guest calls 20 years of "wine is good for you" marketing "absolutely bogus". Wealthy, intelligent guests admit to taking supplements without knowing whether they work, using the "can it do any harm?" logic that a doctor on another episode criticised. Careful thinkers aren't immune when the stakes feel low.

**[YOUR OPINION]** If an AI can find the exact words that move *you*, is that persuasion or manipulation, even when the conclusion is true?

### 4.10 Balance check
The cases come from people across the spectrum: Trump supporters (Chamath Palihapitiya), centre-right leaders (Christopher Luxon), an anti-elite commentator who is hard to place on left or right (Jiang), business leaders, a Gulf government minister and pharma executives. Manipulation is not a left or right habit. But this list still leans one way, because of who appears on these two channels: it has no clear case from the left and no Indian political case from either side.
- **One technique used by all sides:** pre-election "freebie" promises (cash transfers, free electricity, free devices) are made by almost every Indian party. They fit "a gift that creates a debt" in Section 2.5.
- **The same fraud, framed by party:** in a 2026 video, the investigator Coffeezilla shows US officials calling California the "kingdom of fraud" under its Democratic governor while describing Florida, under a Republican governor, as "very well-run, despite elements of fraud", even though the video documents large fraud in both states. He also criticises pardons and clemency for healthcare fraudsters granted by both Trump and Biden.

**[YOUR OPINION]** Did you notice any bias in which cases you found most interesting?

---

## 5. The simulation

*Code: `simulation/rule_based/sim.py` (standard Python). Interactive page: https://claude.ai/artifact/7YdisdyhbkTPFM8a3LQ33g. Full assumptions: `simulation/rule_based/README.md`.*

### 5.1 How it works
**The people.** We create 1,000 simulated people. Each has four traits:
- **taste:** how much they really prefer A over B. On average zero, so left alone about 50% choose A.
- **thinking style:** from "goes with gut" (0) to "thinks everything through" (1).
- **conformity:** how much they care what others do.
- **trust:** how much they trust experts.

**The choice.** A person picks A with a probability that depends on their taste plus any push from the manipulator. Careful thinkers with time to think give the push less weight. Pushes level off when stacked, because attention is limited.

**The tricks.** Each trick's strength was tuned so its effect lands near the real experiment in Section 3.1. Three are guesses or only loosely tuned:
- the authority trick, because no clean benchmark was found;
- the rule that urgency reduces thinking;
- scarcity, because Worchel's cookie study measured how *desirable* people rated the cookies, not what share chose them.

**The runs.** Each condition is run 100 times with fresh random people. We report the average and the range of the middle 95% of runs.

### 5.2 Single tricks and stacking
| Condition | Chose A | Change |
|---|---|---|
| No tricks | 49.9% | – |
| Default (A pre-selected) | 71.0% | +21.1 |
| Authority ("doctors recommend A")* | 60.9% | +11.0 |
| Scarcity and urgency | 60.4% | +10.5 |
| Repetition ×5 | 58.9% | +9.0 |
| Decoy | 58.0% | +8.1 |
| Fake popularity (100 fake likes) | 55.9% | +6.0 |
| **Default + decoy + fake likes + repetition + scarcity** | **87.1%** | **+37.2** |

\*Not tuned to a real experiment.

**Findings:**
- The default is the strongest single trick. When B is pre-selected instead, only 28.8% choose A, a 42-point swing from who controls the default (in the real online experiment with 161 people, the paper's text confirms donation was "about twice as high" with opt-out; the figures were about 82% with opt-out, 79% with no default and 42% with opt-in ✔).
- Stacking adds up, but less than the sum: 21 + 8 + 6 + 9 + 11 = 55 points if they simply added, but the real total is 37. The real dark-patterns study found +31 (it started from a much lower sign-up rate, 11%, so this is a rough comparison only).

### 5.3 Repetition and fact-checks
| Times repeated | Chose A | After a fact-check |
|---|---|---|
| 0 | 49.9% | 49.9% |
| 1 | 53.7% | 51.4% |
| 2 | 55.8% | 52.3% |
| 5 | 58.9% | 53.8% |
| 20 | 63.1% | 56.3% |

The first few repeats do the most. A fact-check cuts the effect by about 60% but doesn't erase it. The 60% is an assumption chosen to match the direction of the research, not its exact size.

### 5.4 Networks, echo chambers and confirmation bias
In a friendship network, 5% of people are influencers who strongly push A, and everyone gradually moves toward their friends' views.

| Network | Chose A | How spread out beliefs are | Friends who disagree |
|---|---|---|---|
| Mixed friendships | 62.3% | 0.44 | 13.6% |
| Echo chambers | 61.2% | 0.82 | 9.9% |
| Mixed + confirmation bias | 50.1% | 0.67 | 31.7% |
| Echo chambers + confirmation bias | 50.3% | 0.99 | 5.9% |

This is the most surprising result. Confirmation bias, meaning people ignore friends whose views are too different, **protects the crowd from the influencers**: the share stays at 50%. But it also **keeps people divided**. With echo chambers plus confirmation bias, beliefs are the most spread out of all four settings, and almost nobody hears disagreement from friends.

Lippmann's "we define first, then see" turns out to be a double-edged sword: it is both a shield against manipulation and a wall against agreement. This kind of model, where people ignore views too far from their own, comes from the opinion-dynamics literature (Deffuant et al. 2000; Hegselmann & Krause 2002). Echo chambers follow the well-known tendency to befriend people like ourselves (McPherson, Smith-Lovin & Cook 2001).

**But the shield depends on how extreme the influencers are.** In the table above, influencers sit far outside everyone's tolerance, so they are ignored almost automatically. When they are made milder (20 runs each):

| How extreme the influencers are | Chose A, no confirmation bias | Chose A, with confirmation bias |
|---|---|---|
| Very extreme (the setting above) | 62.0% | 50.0% |
| Extreme | 58.4% | 50.6% |
| Moderate | 56.4% | 51.4% |
| Mild | 54.1% | 52.3% |

A standard textbook version of the model (NDlib's Deffuant model) shows the same pattern more strongly: with confirmation bias, extreme influencers reached 49.9% and mild ones 61.3%. **So against people with confirmation bias, the winning strategy is to sound close to them.** This matches a WTF guest's description of the mind as an immune system that only lets in ideas close to what it already believes (Section 4.9). The effects in my own model are small, so the safe claim is "sounding moderate gets a little further".

**[YOUR OPINION]** Is confirmation bias a flaw, or a useful defence? Can it be both?

### 5.5 Who is affected, and what protects people
**By thinking style, all tricks on:**
| Group | No tricks | All tricks |
|---|---|---|
| Gut deciders | 50.0% | 90.2% |
| Mostly gut | 49.8% | 88.1% |
| Mostly careful | 50.0% | 86.2% |
| Careful thinkers | 49.4% | 84.2% |

**Protections against the stacked attack:**
| Protection | Chose A |
|---|---|
| None | 87.1% |
| Prebunking (learned the tricks first) | 85.0% |
| Slow down and think | 73.1% |
| Both | 71.2% |

**A check against real-world data:** Sander van der Linden, who designed the prebunking game in our benchmarks, says that in lab simulations prebunking can raise people's resistance by about 60%. With a 30-second YouTube ad "in the wild", it's closer to 10% (APA *Speaking of Psychology* podcast). The model's weak prebunking effect matches the real-world end of that range.

Careful thinkers are only a little safer. In this model, that's because urgency takes away their thinking time. Slowing down works much better than prebunking, because it brings their careful thinking back. Even both protections together leave 71%, mainly because a pre-selected default still works on people who never look.

### 5.6 Strong preferences resist, but not fully
To link back to Section 3.2, we split people by how strongly they prefer one option:

| Group | No tricks | All tricks |
|---|---|---|
| Strongly prefer B | 10.6% | 66.7% |
| Mildly prefer B | 34.2% | 84.0% |
| Mildly prefer A | 65.9% | 94.6% |
| Strongly prefer A | 88.7% | 98.8% |

People who strongly prefer B still move the most in points (+56, against +50 for those who mildly prefer B). That is unrealistic, and it is caused by the default rule, where some people "never look" however much they care. In reality, people who care strongly would probably look. **This is a limitation:** the model likely overstates how much tricks move people with strong preferences. Version 3 should make "how likely you are to look" depend on how much you care.

### 5.7 Robustness: what if my guesses are wrong?
Each of nine assumed strengths was halved, then increased by half, one at a time (18 tests). The four main findings held in **all 18 tests**:
1. Stacking beats any single trick by 10+ points.
2. Slowing down protects more than prebunking.
3. Careful thinkers are only a little safer (gap under 10 points).
4. The default is the strongest single trick.

Two caveats:
- The headline "all tricks" number depends mostly on one guess, how fast pressure saturates. It ranges from 81% to 91%, so the safe claim is "roughly 80–90%".
- The size of the gap between gut and careful thinkers depends on the urgency guess (2 to 9 points).

**A harder test (SALib, 1,408 combinations, all nine guesses changed at once):**
- "Slowing down beats prebunking" and "the default is the strongest single trick" held in **100%** of combinations.
- Stacking beat every single trick in all combinations, and by 10 or more points in 95%. The safe claim is "usually by 10–20 points".
- "Careful thinkers are only a little safer" held in only **88%**, because it depends on the urgency guess. It is therefore an open question, not a finding.
- The AI-people experiments disagree in an interesting way: AI people told to be "very careful" showed no bias at all (Section 6.2).

---

## 6. Experiments with AI people

*Code and data: `simulation/ai_people/`. Each topic folder has `RESEARCH.md` (the evidence the situations were built from), `PREDICTIONS.md` (written and saved to git **before** any data) and `RESULTS.md`.*

### 6.1 Why a second kind of simulation
The rule-based model in Section 5 can only show what its own rules allow: every person reacts to a trick in the way I programmed. To get closer to real reasons, the second simulation uses **AI people**.

**How it works:**
- Each AI person is a separate, fresh call to an AI language model (Claude Haiku), with no tools and no memory of other people. It is not told it is in an experiment.
- It gets a short life story: age, city, income, job, decision style (from "goes with gut" to "researches everything"), how much it trusts ads or doctors, and how much relatives' opinions matter.
- It then reads a realistic choice and answers in three parts: **CHOICE**, a yes/no follow-up (a loan, a permission, "is this price fair?") and a **REASON** in its own words.
- **Every person sees every version of the situation** (from "no trick" to "all tricks plus disclosure"), each in a separate call. The order of the options is shuffled, so the answer isn't driven by which option comes first.

**This method is new and has known problems.**
- AI models can match the *direction* of human results while getting the *size* wrong (Hewitt et al. 2024).
- They tend to assume people are more rational than they are (Liu et al. 2024).
- They can flatten real differences between groups (Wang et al. 2025).

So before using AI people on new topics, I tested them on three classic experiments with well-known human results.

### 6.2 Check: do AI people behave like humans on classic experiments?
30 AI people did three classic tests, set in Indian situations (179 usable answers).

| Experiment | AI people | Humans | Same direction? | Same size? |
|---|---|---|---|---|
| Framing ("300 jobs saved" vs "600 jobs lost") | gap of 13 points | gap of about 50 points (Tversky & Kahneman 1981) | ✅ | ❌ much smaller |
| Default (organ-donor box ticked vs unticked) | 17% → 55% (gap 39) | 42% → 82% (gap 40) (Johnson & Goldstein 2003) | ✅ | ✅ |
| Sunk cost (paid vs free cricket ticket, rainy day) | 3.7 vs 3.1 on a 1–9 scale | paid > free, small effect | ✅ | 🟡 similar |

**What this means:**
- **AI people got the direction right in 3 of 3 tests, but the size right in only 1.** So all AI-people results in this paper are reported as **directions and rough strengths, never as exact human percentages.**
- **AI people told to be "very careful" showed no bias at all**, which real careful people don't manage. So careful AI people probably underestimate real human bias.
- **All three of my written predictions were wrong in some way.** Writing them down first is what makes that visible.

### 6.3 How each topic experiment was built
**Research came first:**
- News investigations, regulator reports, court cases and papers were collected for each topic before any situation was written.
- The situations use real prices and real sales lines, e.g. the agent's "PR no problem, visa guaranteed" from a CBC hidden-camera investigation, and the ₹16 lakh Fortis dengue bill.

**Then the same steps every time:**
1. **Predictions written and saved before any data.**
2. **A small pilot** (8 people per situation).
3. **Three checks:**
   - Do the answers parse?
   - Is the "no trick" version stuck near 0% or 100%?
   - Do the answers sound in character?
4. **Only then, extra batches of new people.**

**Four times the pilot failed the "stuck near 0%" check:**
- **What went wrong:** the cheap option had been made unrealistically easy. Examples: a government college with no downsides, "back pain slowly getting better", "relatives may lend you money in 3 days".
- **The fix:** each time I added a realistic downside taken from the research, wrote the change down *before* re-running, and left the predictions unchanged.

**Reading the tables:** a row starting with "+" adds one thing to the basic version (in the university tables, to the row above it). "All tricks" rows combine them.

**Size:** 14–20 AI people per situation, each seeing every version, so **one person moves a percentage by 5–7 points.** Small differences mean nothing; only large, consistent ones are reported as findings.

### 6.4 Universities: the agent, the brochure and the neighbour's son
*(240 decisions, 20 people per situation: 10 students and 10 parents.)*

| Canada through an agent (₹30 lakh, often a mortgage on land) | Chose Canada |
|---|---|
| Basic facts | 10% |
| Honest facts (residency not guaranteed, 40–50 hours a week of low-paid work, the agent is paid a commission) | 0% |
| + the agent's promises ("office job anywhere, PR no problem") | 25% |
| **+ "300 from your area went; the neighbour's son sends ₹40,000 home a month"** | **65%** (parents 80%, students 50%) |
| + the honest facts added | 10% |

| Private college (₹11 lakh) vs government college (₹4.5 lakh) | Chose private |
|---|---|
| Brochure | 15% |
| + "highest package ₹42 LPA!" | 25% (parents 20% → 40%; students unchanged) |
| + "your cousin studied there" | 30% |
| All tricks + honest medians + "the counsellor earns a commission" | 20% |

**Findings:**
- **Many AI people called the agent's promises lies and still chose Canada because of the neighbour.** *"The agent's promises sound like typical agent BS, but the neighbour's son sends ₹40,000 home every month — that's real proof."*
- **Disclosure undid the agent's trick** (65% → 10%), but **not the cousin's story** (still 20%).
- **AI parents fell for salary hype more than students did.** I predicted the opposite.

### 6.5 Healthcare: when the trick comes from a doctor
*(308 decisions, 14 people per situation.)*

| India: stable chest pain. Stent now (₹2.5 lakh) or medicines? | Chose stent | Patient deciding | Son/daughter deciding |
|---|---|---|---|
| Both options offered by the doctor | 43% | 29% | 57% |
| Honest trial facts (for stable pain, a stent doesn't prevent heart attacks; ISCHEMIA, Maron et al. 2020) | 14% | 14% | 14% |
| + the doctor: "this is a ticking time bomb" | 64% | 43% | **86%** |
| + "the neighbour ignored his pain and died; the cousin feels 20 years younger" | **93%** | 86% | 100% |
| All tricks + honest facts + "the hospital sets revenue targets" | 29% | 29% | 29% |

| USA: back pain. MRI now ($1,100) or physiotherapy? | Chose MRI |
|---|---|
| Base | 43% |
| Honest guidelines (imaging doesn't help in the first 6 weeks) | 7% |
| + clinic ad: "could be something serious, don't wait" | 36% (*lower*) |
| + coworker: "my brother-in-law's back pain was cancer" | **64%** |

| USA: where to give birth. A community hospital ($2,700) or a private-equity-owned luxury hospital ($4,500)? | Pregnant women | Husbands deciding |
|---|---|---|
| Base | 29% | **71%** |
| All tricks (influencer ad, friend's praise, free ultrasound) + only "owned by private equity; such hospitals had 25% more patient harms" (Kannan et al. 2023) | 0% | 57% |
| All tricks + ownership + the state report card (1 nurse per 4 women in labour vs 1 per 2; C-sections 34% vs 24%) | 0% | 29% |

**Findings:**
- **The same fear message works from a doctor and backfires from an ad.** The doctor's "ticking time bomb" raised stent choices by 21 points. The clinic's "early detection saves lives" ad slightly *lowered* MRI choices; AI people called it "fear-mongering".
- **Deciding for someone you love makes people easier to push.** Sons and daughters chose the stent twice as often as the patients themselves after the doctor's warning: *"I cannot gamble with my mother's life. We will have to take a loan."*
- **Concrete numbers beat abstract labels.** "1 nurse per 4 women" moved husbands far more than "owned by private equity".
  - ⚠ The husband/wife gap ("my wife deserves to be pampered") may partly be a stereotype built into the AI model.
- **17 of 22 predictions were right**, far better than for universities (5 of 13). The research for healthcare was done more carefully before the predictions were written.

### 6.6 Personal targeting: loan apps and personal prices
*(182 decisions, 14 people per situation.)*

| India: ₹15,000 needed by tomorrow; other doors closed. Instant-loan app? | Chose the app | People who hate asking relatives |
|---|---|---|
| Generic ad | 57% | 71% |
| + the real terms (≈300% a year, not RBI-registered, calls your contacts if you pay late) | **43%** | **71%** |
| Ad written for the person ("Rent due? No need to ask anyone. Nobody will know.") | 57% | 71% |
| + "We noticed you searched 'urgent money' at 2 am" | 57% | 71% |
| Everything + the real terms | 29% | 43% |

| USA: book a $312 flight now, or keep comparing? | Booked | Said the price was fair |
|---|---|---|
| Normal | 43% | 71% |
| "Special price just for you (was $349)" | 29% (*lower*) | 71% |
| Everything (personal pick, special price, "2 seats left") + **"the same seat is $279 for other users"** | **14%** | **0%** |

**Findings:**
- **Desperation beats information.** For people who hate asking relatives, the honest loan terms changed nothing: *"I'm not going to shame myself asking relatives again — they'll just gossip more."* This matches the real victims of illegal loan apps in India.
- **Ads written for the person added nothing in either situation.** This fits field evidence that personal tailoring adds less than feared (Tappin et al. 2023), and the UK regulator's finding that Cambridge Analytica oversold its "psychographic" ads.
  - **But this design can't test targeting's real power: choosing *who* sees the ad and *when*.** Every AI person was already in a crisis.
- **The creepy reveal didn't scare anyone off**, which goes against Aguirre et al. (2015).
- **Unfairness, not privacy, made people angry.** "Others pay $279" cut booking from 43% to 14%, and nobody called the price fair.
- **Only 4 of 12 predictions were right.** I badly underestimated how little honest terms help someone in a money crisis.

### 6.7 What all three topics share
1. **"People like us" is the strongest trick every time.** The neighbour's son in Canada, the neighbour who died of a heart attack and the coworker's brother-in-law each moved AI people more than any ad. Many said outright that the ad was a lie, then followed the story. Real people do the same: patient anecdotes change treatment choices even when correct statistics are shown (Fagerlin, Wang & Ubel 2005).
2. **Loud tricks get spotted; quiet ones don't.** Hype, countdowns and "special price" discounts often backfired. A doctor's warning, a relative's story and the shame of asking family worked.
3. **The messenger matters more than the message.** The same fear works from a doctor and fails from an ad. This is Bernays's "get the doctors to say it" (Section 2.2), now measured.
4. **Honest disclosure is the best fix, but it has two limits:**
   - it works well against agents and ads (65% → 10%), and badly against stories and desperation (still 20–43%);
   - **concrete, personal numbers work better than labels:** "1 nurse per 4 women" and "others pay $279" beat "private equity" and "personalised pricing".
5. **People are easier to push when deciding for someone they love**: parents choosing for children (universities) and children choosing for parents (healthcare).

---

## 7. Discussion

### 7.1 The main points
1. **Old tactics, new tools.** Every trick in the simulation was described by Le Bon, Bernays, Lippmann or Machiavelli long before experiments measured it. What's new is scale, speed and the ability to test and stack tricks automatically.
2. **Stacking is the danger.** Each trick alone looks small (6–21 points). Combined, they move most people. A single regulator banning a single trick may miss the stack.
3. **Whoever sets the default sets the outcome.** In the simulation and the business cases, owning the default (the pre-ticked box, the pre-installed app, the "normal" belief) is the strongest move.
4. **Being smart isn't enough; time is.** Careful thinkers resist only when they are given time. Urgency is the trick that disarms them. The best simple defence is to slow down.
5. **Confirmation bias cuts both ways.** It blocks extreme influencers and locks in division, but moderate-sounding messages slip through.
6. **People trust people, not ads.** In every AI-people topic, a neighbour's or cousin's story beat advertising, even among AI people who called the ad a lie (Section 6.7). Bernays understood this in 1928.
7. **The messenger is the trick.** The same fear works from a doctor and fails from an ad. Authority channels (doctors, counsellors, agents, relatives) deserve more regulation than ads do.
8. **Information helps the comfortable more than the desperate.** Disclosure undid most tricks, but not for people in a money crisis or under family shame.

### 7.2 What this means for real life
- **For individuals:** when you see "only 2 left", a countdown, a pre-ticked box *and* "10,000 people bought this" together, that's a stack. Slow down. When a decision is about someone you love, be extra careful: that is when both AI people and real families were easiest to push.
- **For regulators:** look at combinations and defaults, not just single claims. India's Uniform Code for Pharmaceutical Marketing Practices (UCPMP), issued in March 2024, bans gifts, travel, hospitality and cash to doctors and their families ✔. It targets exactly the authority channel, though critics say enforcement is weak. The AI-people results support rules that make disclosure **concrete and personal**: the CCPA's 2024 coaching rules (honest results in the same font as the claims), stent prices printed on hospital bills, and requirements to tell customers when a price is personalised. "Others pay $279" moved people far more than any general warning.
- **For schools:** teaching the tricks (prebunking) helps a little. Teaching people to *pause* may help more. **[YOUR OPINION]**

### 7.3 Reconciling with "persuasion is weak"
The rule-based simulation's big effects come from choices where people start at 50/50 and don't care much. The real experiments in Section 3 support the claim that this is where manipulation is strongest: sign-up forms, organ-donor forms and product pages, as opposed to elections, where people care and hear competing messages. (The rule-based model itself can't show this; see Section 5.6.) The AI-people experiments add a second exception: **high-stakes choices can be steered too, if the push comes through a trusted person or meets someone desperate.** A ₹30 lakh mortgage and a heart procedure are not low-stakes choices. The paper's claim is therefore limited: **manipulation is strongest in low-stakes, fast, one-sided choices**, and many daily choices are exactly like that.

---

## 8. Limits and ethics
1. **The simulation is a toy model.** Its strengths are assumptions tuned to experiments. It shows how mechanisms can combine; it doesn't prove what real people do.
2. **Many benchmarks were checked only through abstracts or summaries** (✔ above), not the full papers. Items still marked [CHECK] were not confirmed.
3. **The decoy effect is fragile** in replications.
4. **The model treats pushes toward A and B the same way.** Real people correct fake negativity more than fake positivity (Muchnik et al. 2013).
5. **The default rule probably overstates effects on people with strong preferences** (Section 5.6).
6. **The case collection isn't a random sample.** It comes from two channels, found by keyword search, and only part of each was read (44/70 and 111/182). It illustrates techniques; it can't measure how common they are.
7. **The confirmation-bias result depends on how extreme the influencers are** (Section 5.4).
8. **AI people are not people.**
   - They matched humans in direction but not reliably in size (Section 6.2).
   - "Very careful" AI people are unrealistically rational.
   - Their reasons sometimes include invented details ("my coworker's sister went there").
   - They may carry stereotypes (the husband/wife gap in Section 6.5).
   - Only one AI model (Claude Haiku) was used, with 14–20 people per situation.
   - Several pilots had to be redesigned after hitting a floor (all changes recorded before re-running).
   - The key results should be checked with real people, with consent and an ethics check.
9. **Some scenario numbers are invented but realistic** (e.g. the hospital report card in Section 6.5); the research they are based on is cited in each topic's `RESEARCH.md`.
10. **Source cautions:** *Predictive History* contains conspiracy and antisemitic content. It is used only as a case study of persuasion, with warnings. Podcast guests make claims that were not all verified; the reports mark which were.
11. **Copyright:** Bernays and Lippmann may still be under copyright in India. They are quoted only briefly, for study and criticism.
12. **Not every famous study holds up.**
   - Psychology has had a "replication crisis": when other scientists repeated well-known experiments, many showed smaller effects or none at all. A large project found that only about a third to two-fifths of 100 psychology studies replicated (Open Science Collaboration 2015) **[CHECK]**.
   - A few famous researchers in behavioural science, the field this paper relies on, were even found to have fabricated data. Papers by Diederik Stapel and Dan Ariely were retracted, and Francesca Gino's work was investigated by Harvard **[CHECK details]**.
   - **What this paper did about it:**
     - It leans on effects that **have** been repeated many times (defaults, framing, repetition, social proof).
     - It flags fragile ones (the decoy effect, prebunking, hotel towels).
     - It wrote down its own predictions before running the AI-people experiments, so the results couldn't be bent to fit the story. Many of those predictions turned out wrong (26 of 47 fully right across the three topics), and they are reported as wrong.

---

## 9. Conclusion
**[YOUR OPINION]** Write this yourself, in 150–250 words. Suggested shape:
1. What surprised you most (the stacking? confirmation bias? the default? the neighbour's son? the doctor's "ticking time bomb"?).
2. One thing you now notice in your daily life that you didn't before.
3. One question you'd want to test next, for example with real classmates, with an ethics check and their consent.

---

## References (to complete and check)
*Mark each one as you read the original. ✔ = checked online through the abstract or a reliable summary. [CHECK] = not yet confirmed.*

- Adena, M., et al. (2015). Radio and the rise of the Nazis in prewar Germany. *Quarterly Journal of Economics*, 130(4).
- Aguirre, E., Mahr, D., Grewal, D., de Ruyter, K., & Wetzels, M. (2015). Unraveling the personalization paradox: The effect of information collection and trust-building strategies on online advertisement effectiveness. *Journal of Retailing*, 91(1), 34–49. ✔
- Aher, G., Arriaga, R. I., & Kalai, A. T. (2023). Using large language models to simulate multiple humans and replicate human subject studies. *ICML*. [CHECK]
- Asch, S. E. (1951). Effects of group pressure upon the modification and distortion of judgments.
- Bernays, E. (1928). *Propaganda*. Horace Liveright.
- Bond, R., & Smith, P. B. (1996). Culture and conformity: A meta-analysis of studies using Asch's line judgment task. *Psychological Bulletin*, 119(1). [CHECK]
- Brady, W. J., Wills, J. A., Jost, J. T., Tucker, J. A., & Van Bavel, J. J. (2017). Emotion shapes the diffusion of moralized content in social networks. *PNAS*, 114(28), 7313–7318. ✔
- Chetty, R., Deming, D. J., & Friedman, J. N. (2023). Diversifying society's leaders? The determinants and causal effects of admission to highly selective private colleges. NBER Working Paper 31492 (published in *Quarterly Journal of Economics*, 2026, 141(1), 51–145). ✔
- Cialdini, R. B. (1984/2021). *Influence: The Psychology of Persuasion*. Harper Business.
- Coppock, A., Hill, S. J., & Vavreck, L. (2020). The small effects of political advertising are small regardless of context, message, sender, or receiver. *Science Advances*, 6(36).
- Deffuant, G., et al. (2000). Mixing beliefs among interacting agents. *Advances in Complex Systems*, 3.
- DeJong, C., et al. (2016). Pharmaceutical industry–sponsored meals and physician prescribing patterns for Medicare beneficiaries. *JAMA Internal Medicine*, 176(8), 1114–1122. ✔ (Even a single meal was associated with more prescribing of the promoted brand. An association, not proof of cause.)
- Department of Pharmaceuticals, Government of India (2024). Uniform Code for Pharmaceutical Marketing Practices (UCPMP) 2024.
- Fagerlin, A., Wang, C., & Ubel, P. A. (2005). Reducing the influence of anecdotal reasoning on people's health care decisions: Is a picture worth a thousand statistics? *Medical Decision Making*, 25(4), 398–405. ✔
- Frederick, S., Lee, L., & Baskin, E. (2014). The limits of attraction. *Journal of Marketing Research*, 51(4).
- Gupta, A., Howell, S. T., Yannelis, C., & Gupta, A. (2024). Owner incentives and performance in healthcare: Private equity investment in nursing homes. *Review of Financial Studies*. ✔
- Hackenburg, K., & Margetts, H. (2024). Evaluating the persuasive influence of political microtargeting with large language models. *PNAS*, 121(24).
- Harris, T. (2017). How a handful of tech companies control billions of minds every day. TED talk.
- Hasher, L., Goldstein, D., & Toppino, T. (1977). Frequency and the conference of referential validity. *J. Verbal Learning and Verbal Behavior*, 16.
- Haslam, S. A., & Reicher, S. D. (2012). Contesting the "nature" of conformity: What Milgram and Zimbardo's studies really show. *PLoS Biology*, 10(11). [CHECK]
- Hassan, A., & Barber, S. J. (2021). The effects of repetition frequency on the illusory truth effect. *Cognitive Research*, 6:38.
- Hegselmann, R., & Krause, U. (2002). Opinion dynamics and bounded confidence. *JASSS*, 5(3).
- Hewitt, L., Ashokkumar, A., Ghezae, I., & Willer, R. (2024). Predicting results of social science experiments using large language models. Working paper. [CHECK]
- Huber, J., Payne, J. W., & Puto, C. (1982). Adding asymmetrically dominated alternatives. *J. Consumer Research*, 9.
- Jensen, R. (2010). The (perceived) returns to education and the demand for schooling. *Quarterly Journal of Economics*, 125(2). ✔ (via summary)
- Johnson, E. J., & Goldstein, D. (2003). Do defaults save lives? *Science*, 302, 1338–1339. ✔ (Same experiment also reported in Johnson & Goldstein 2004, *Transplantation*, 78(12).)
- Kalla, J., & Broockman, D. (2018). The minimal persuasive effects of campaign contact in general elections. *APSR*, 112(1).
- Kannan, S., Bruch, J. D., & Song, Z. (2023). Changes in hospital adverse events and patient outcomes associated with private equity acquisition. *JAMA*, 330(24), 2365–2375. ✔
- King, G., Pan, J., & Roberts, M. E. (2017). How the Chinese government fabricates social media posts for strategic distraction. *APSR*, 111(3).
- Le Bon, G. (1895/1896). *The Crowd: A Study of the Popular Mind*.
- Lewandowsky, S., et al. (2012). Misinformation and its correction. *Psychological Science in the Public Interest*, 13(3).
- Lippmann, W. (1922). *Public Opinion*.
- Liu, R., Geng, J., Peterson, J. C., Sucholutsky, I., & Griffiths, T. L. (2024). Large language models assume people are more rational than we really are. arXiv:2406.17055.
- Luguri, J., & Strahilevitz, L. (2021). Shining a light on dark patterns. *J. Legal Analysis*, 13.
- Machiavelli, N. (1532). *The Prince*.
- Maron, D. J., et al. (ISCHEMIA Research Group) (2020). Initial invasive or conservative strategy for stable coronary disease. *New England Journal of Medicine*, 382, 1395–1407. [CHECK]
- Matz, S. C., Kosinski, M., Nave, G., & Stillwell, D. J. (2017). Psychological targeting as an effective approach to digital mass persuasion. *PNAS*, 114(48), 12714–12719. ✔
- McPherson, M., Smith-Lovin, L., & Cook, J. (2001). Birds of a feather. *Annual Review of Sociology*, 27.
- Mercier, H. (2017). How gullible are we? *Review of General Psychology*, 21(2).
- Mijs, J. J. B. (2021). The paradox of inequality: income inequality and belief in meritocracy go hand in hand. *Socio-Economic Review*, 19(1), 7–35. ✔
- Milgram, S. (1963). Behavioral study of obedience. *J. Abnormal and Social Psychology*, 67.
- Modirrousta-Galian, A., & Higham, P. A. (2023). Gamified inoculation interventions do not improve discrimination between true and fake news. *Journal of Experimental Psychology: General*, 152, 2411–2437.
- Muchnik, L., Aral, S., & Taylor, S. J. (2013). Social influence bias. *Science*, 341.
- Nisbett, R. E., & Wilson, T. D. (1977). Telling more than we can know. *Psychological Review*, 84(3).
- Open Science Collaboration (2015). Estimating the reproducibility of psychological science. *Science*, 349(6251). [CHECK]
- Peisakhin, L., & Rozenas, A. (2018). Electoral effects of biased media: Russian television in Ukraine. *AJPS*, 62(3).
- Perry, G. (2013). *Behind the Shock Machine: The Untold Story of the Notorious Milgram Psychology Experiments*. The New Press. [CHECK]
- Plato. *Republic*, Book VII (trans. Jowett).
- Reicher, S. (1984). The St. Pauls' riot: An explanation of the limits of crowd action in terms of a social identity model. *European Journal of Social Psychology*, 14.
- Reicher, S., Spears, R., & Postmes, T. (1995). A social identity model of deindividuation phenomena. *European Review of Social Psychology*, 6.
- Roozenbeek, J., & van der Linden, S. (2019). Fake news game confers psychological resistance against online misinformation. *Palgrave Communications*, 5, 65. ✔
- Salganik, M. J., Dodds, P. S., & Watts, D. J. (2006). Experimental study of inequality and unpredictability in an artificial cultural market. *Science*, 311.
- Salvi, F., Horta Ribeiro, M., Gallotti, R., & West, R. (2025). On the conversational persuasiveness of GPT-4. *Nature Human Behaviour*.
- Tannenbaum, M. B., Hepler, J., Zimmerman, R. S., Saul, L., Jacobs, S., Wilson, K., & Albarracín, D. (2015). Appealing to fear: A meta-analysis of fear appeal effectiveness and theories. *Psychological Bulletin*, 141(6), 1178–1204. ✔
- Tappin, B. M., Wittenberg, C., Hewitt, L. B., Berinsky, A. J., & Rand, D. G. (2023). Quantifying the potential persuasive returns to political microtargeting. *PNAS*, 120(25). ✔
- Tversky, A., & Kahneman, D. (1981). The framing of decisions and the psychology of choice. *Science*, 211.
- van der Linden, S. Interview on *Speaking of Psychology* (American Psychological Association podcast).
- Walter, N., & Tukachinsky, R. (2020). A meta-analytic examination of the continued influence of misinformation. *Communication Research*, 47(2).
- Wang, A., Morgenstern, J., & Dickerson, J. P. (2025). Large language models that replace human participants can harmfully misportray and flatten identity groups. arXiv:2402.01908.
- Worchel, S., Lee, J., & Adewole, A. (1975). Effects of supply and demand on ratings of object value. *JPSP*, 32(5).
- Yang, S., & Lynn, M. (2014). More evidence challenging the robustness and usefulness of the attraction effect. *J. Marketing Research*, 51(4).
- Zajonc, R. B. (1968). Attitudinal effects of mere exposure. *JPSP*, 9(2).

**News, regulator and investigation sources** for the AI-people situations (CBC, DW, NPPA, CCPA, RBI, IRDAI, ASCI, FTC, KFF, Commonwealth Fund, Coffeezilla and others) are listed with links in `simulation/ai_people/*/RESEARCH.md`.
**Podcast and video sources:** see the timestamped links in `sources/case_reports/1_trump.md` to `sources/case_reports/5_education_system.md`.

---

## Your to-do list for this draft
1. **Fill in every [YOUR OPINION]** (about 12 places). This is the part that makes the paper yours.
2. **Edit the "How this paper was made" note** at the top so every sentence is true.
3. **Check the [CHECK] items**, especially Maron 2020 (ISCHEMIA), Open Science Collaboration 2015, and the Milgram/Asch replication papers.
4. **Rewrite Sections 1, 7 and 9 in your own words.**
5. **Decide on length.** This draft is about 10,000 words including references. For a 6,000-word limit, shorten Section 4 (keep 4.2, 4.5, 4.7, 4.8) and Section 5 (keep 5.2, 5.4, 5.7).
6. **Add one figure:** a bar chart of the Canada table in Section 6.4 (10% → 25% → 65% → 10%) would show the paper's main point at a glance.
7. **Optional:** test 2–3 situations with real classmates (with consent and an ethics check) to see whether the AI people's directions hold.
