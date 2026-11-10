# How Choices Are Made For Us: Old Tricks, New Tools

*First draft, written overnight on 6 Nov 2026. Everything here is a starting point for you to rewrite in your own voice.*

**How to use this draft**
- **[YOUR OPINION]** marks a place only you can write. The paper is stronger when your own view is clearly separate from the evidence.
- **✔** marks a citation checked online on 6 Nov 2026 (usually through the abstract or reliable summaries, not the full paper). **[CHECK]** marks one still to confirm in the original source before you submit. Many studies were cited from memory or from summaries (see `simulation/README.md` and the reports for each one's status).
- The simulation numbers come from `simulation/results.json` (v2, 6 Nov 2026).
- Aim for about 4,000–6,000 words in the final version. This draft is about 5,500.

---

## Abstract

People like to think they choose freely. But many everyday choices, such as which app to use, which medicine a doctor prescribes or which politician seems "authentic", are shaped by the way options are presented. This paper brings together four kinds of evidence.
1. **Old books:** what thinkers from Plato to Bernays already said about steering people.
2. **Experiments:** what modern psychology has measured.
3. **Real cases:** about 150 podcast and lecture episodes (the *WTF* podcast with Nikhil Kamath and the *Predictive History* channel by Jiang Xueqin), where business leaders, politicians and commentators describe, or use, these techniques.
4. **A computer simulation:** 1,000 simulated people choosing between two equally good options while a "manipulator" uses seven tricks. Each trick's strength is tuned to a published experiment where one exists.

**Simulation results:**
- Each trick alone moves a 50/50 choice by 6–21 percentage points.
- All the tricks together move it to roughly 80–90%.
- A pre-selected default is the strongest single trick.
- Careful thinkers are only slightly harder to move when they are rushed.
- Slowing down protects more than learning about the tricks in advance.
- Confirmation bias makes people resistant to influencers, but it keeps groups divided.
- These four main findings held in all 18 robustness tests, in which each assumed strength was halved or increased by half.

The model is a teaching tool, not proof about real people. But together the four kinds of evidence suggest one main point: **the tactics are old, only the tools are new, and they work best when they are stacked and when people are rushed.**

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
4. **tests its own assumptions**, reporting which conclusions survive when the guesses change (Section 5.5).

---

## 2. What the old thinkers said

*Sources: `books/reading_notes.md`. Only key chapters were read; the notes list exact line ranges.*

| Old idea | Who said it | What later experiments found |
|---|---|---|
| Repeat a claim boldly, without proof, and it spreads | Le Bon, *The Crowd* (1895) | Repeated statements feel truer (Hasher et al. 1977; Hassan & Barber 2021) |
| Ideas spread by contagion; people imitate | Le Bon (1895) | Social proof and herding (Asch 1951; Salganik et al. 2006) |
| Prestige "paralyses our critical faculty" | Le Bon (1895) | Obedience to authority (Milgram 1963) |
| Use trusted experts instead of ads; make the buyer think it's their own idea | Bernays, *Propaganda* (1928) | Expert endorsement; people don't know why they choose (Nisbett & Wilson 1977) |
| We act on "pictures in our heads", and we define first, then see | Lippmann, *Public Opinion* (1922) | Confirmation bias, motivated reasoning |
| It's enough to *appear* good; most judge by appearance | Machiavelli, *The Prince* (1532) | Impression management |
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
*(Added 6 Nov 2026 from five Predictive History lectures on ancient history; see `topic_passages/ph_old_history_notes.md`. The history column uses what historians generally agree on, not only the lecturer's interpretation.)*

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

### 3.2 An important counterpoint: persuasion is often weak
It would be wrong to say people are puppets. Large studies of election campaigns find **tiny or zero** average effects of ads and canvassing on how people vote (Kalla & Broockman 2018; Coppock, Hill & Vavreck 2020). Mercier (2017) argues that people are good at rejecting messages that clash with what they already believe or come from sources they don't trust.

Persuasion looks strong in other settings: when one source controls the information, as with Nazi radio (Adena et al. 2015) or Russian TV in Ukraine (Peisakhin & Rozenas 2018), and when the message fits what listeners already believe.

**How to fit these together:** this paper's argument is that the tricks work best when:
1. people don't care much which option they pick;
2. they are rushed;
3. they have no competing information.

Product choices, app settings and sign-up forms often meet all three conditions. A vote for president usually doesn't. Section 5.6 shows the simulation agrees: people with strong preferences move much less.

**[YOUR OPINION]** Which kind of choice in your life is most like an "I don't really care" choice that is easy to steer, and which is a choice where you'd resist?

---

## 4. Cases from real life

*Sources: `reports/1_trump.md` to `reports/5_education_system.md`, built from transcripts of 41 of 70 WTF episodes and 111 of 182 Predictive History videos. Each claim links to a timestamp in the reports. Cases are grouped by technique, not by person.*

### 4.1 Repetition and familiarity
- **Mankind Pharma's extra second.** India does not allow prescription drugs to be advertised to the public. Mankind ran ads for its over-the-counter products and held its company logo on screen for over a second instead of the usual half-second, so the name was familiar before its medicines reached each region (WTF, "Pharma"). This is the mere-exposure effect (Zajonc 1968) used to get around an advertising ban.
- **Simple lines, repeated.** A WTF guest describes Trump's habit of repeating very simple phrases and says online creators copy it so that audiences tie a few words to them. Le Bon described exactly this in 1895.

### 4.2 Authority and trusted messengers
- **17,000 sales reps.** A pharma guest on WTF says a large share of a drug's price pays for medical representatives who visit doctors. Because patients can't be targeted directly, the doctor becomes the channel. This is Bernays's "get the doctors to say it" in its modern form. Studies link industry payments to doctors with more prescribing of the paying company's drugs (DeJong et al. 2016 ✔: even one industry-paid meal was associated with more prescribing of the promoted brand in US Medicare data; an association, not proof of cause).
- **The self-experimenter.** Bryan Johnson, who takes about 100 pills a day and points people to his website, seems credible because he tests everything on himself. A doctor on the same panel says parts of the regimen have "no proof". This makes a good case of authority from personal commitment rather than expertise.

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
*(Added 6 Nov 2026 from WTF Ep 2 "Social Media" and Ep 4 "ChatGPT"; see `topic_passages/`.)*
- **The business model.** A social-media founder describes "a vicious cycle of a dopamine hit at both ends": likes keep the user coming back, and every extra minute earns the platform ad money. The goal is time spent, not good choices.
- **Envy and negativity are rewarded.** A creator calls envy "the fuel for social media" and admits that a negative comment on a popular page attracts likes from other envious people. This is the platform version of Le Bon's point that crowds reward extreme feelings.
- **Top-down growth.** New platforms recruit influencers and ministers first, and the public follows. This is Bernays's 1928 "key men" method.
- **AI-tailored persuasion.** In 2023 a guest compared the mind to an immune system that rejects ideas too far from its beliefs. He predicted that ChatGPT would learn "a specific set of words" to fit any message inside that tolerance. This is exactly the confirmation-bias mechanism in Section 5.4, and why the simulation's result (confirmation bias protects against influencers) could break if messages are tailored to each person. Recent studies are mixed ✔. In debates, GPT-4 given basic personal data about its opponent was more persuasive than a human 64% of the time (Salvi et al., *Nature Human Behaviour* 2025). But GPT-4 messages tailored to people's demographics and politics were *not* more persuasive than generic GPT-4 messages (Hackenburg & Margetts, *PNAS* 2024, 8,587 people). AI persuades, but the "perfect words for each person" effect isn't proven yet.
- **Health halos.** On WTF Ep 6, a guest calls 20 years of "wine is good for you" marketing "absolutely bogus". Wealthy, intelligent guests admit to taking supplements without knowing whether they work, using the "can it do any harm?" logic that a doctor on another episode criticised. Careful thinkers aren't immune when the stakes feel low.

**[YOUR OPINION]** If an AI can find the exact words that move *you*, is that persuasion or manipulation, even when the conclusion is true?

### 4.10 Balance check
The cases come from people across the spectrum: Trump supporters (Chamath Palihapitiya), centre-right leaders (Christopher Luxon), an anti-elite commentator who is hard to place on left or right (Jiang), business leaders, a Gulf government minister and pharma executives. Manipulation is not a left or right habit. **[YOUR OPINION]** Did you notice any bias in which cases you found most interesting?

---

## 5. The simulation

*Code: `simulation/sim.py` (standard Python). Interactive page: https://claude.ai/artifact/7YdisdyhbkTPFM8a3LQ33g. Full assumptions: `simulation/README.md`.*

### 5.1 How it works
**The people.** We create 1,000 simulated people. Each has four traits:
- **taste:** how much they really prefer A over B. On average zero, so left alone about 50% choose A.
- **thinking style:** from "goes with gut" (0) to "thinks everything through" (1).
- **conformity:** how much they care what others do.
- **trust:** how much they trust experts.

**The choice.** A person picks A with a probability that depends on their taste plus any push from the manipulator. Careful thinkers with time to think give the push less weight. Pushes level off when stacked, because attention is limited.

**The tricks.** Each trick's strength was tuned so its effect lands near the real experiment in Section 3.1. Two exceptions are guesses:
- the authority trick, because no clean benchmark was found;
- the rule that urgency reduces thinking.

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
- Stacking adds up, but less than the sum: 21 + 8 + 6 + 9 + 11 = 55 points if they simply added, but the real total is 37. The real dark-patterns study found +31.

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

Lippmann's "we define first, then see" turns out to be a double-edged sword: it is both a shield against manipulation and a wall against agreement.

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

People who mildly prefer B move the most. People who strongly prefer B move less in *relative* terms, but still a lot here. Much of that comes from the default rule, where some people "never look". In reality, people who care strongly would probably look. **This is a limitation:** the model likely overstates how much tricks move people with strong preferences. Version 3 should make "how likely you are to look" depend on how much you care.

### 5.7 Robustness: what if my guesses are wrong?
Each of nine assumed strengths was halved, then increased by half, one at a time (18 tests). The four main findings held in **all 18 tests**:
1. Stacking beats any single trick by 10+ points.
2. Slowing down protects more than prebunking.
3. Careful thinkers are only a little safer (gap under 10 points).
4. The default is the strongest single trick.

Two caveats:
- The headline "all tricks" number depends mostly on one guess, how fast pressure saturates. It ranges from 81% to 91%, so the safe claim is "roughly 80–90%".
- The size of the gap between gut and careful thinkers depends on the urgency guess (2 to 9 points).

---

## 6. Discussion

### 6.1 The main points
1. **Old tactics, new tools.** Every trick in the simulation was described by Le Bon, Bernays, Lippmann or Machiavelli long before experiments measured it. What's new is scale, speed and the ability to test and stack tricks automatically.
2. **Stacking is the danger.** Each trick alone looks small (6–21 points). Combined, they move most people. A single regulator banning a single trick may miss the stack.
3. **Whoever sets the default sets the outcome.** In the simulation and the business cases, owning the default (the pre-ticked box, the pre-installed app, the "normal" belief) is the strongest move.
4. **Being smart isn't enough; time is.** Careful thinkers resist only when they are given time. Urgency is the trick that disarms them. The best simple defence is to slow down.
5. **Confirmation bias cuts both ways.** It blocks influencers, and it locks in division.

### 6.2 What this means for real life
- **For individuals:** when you see "only 2 left", a countdown, a pre-ticked box *and* "10,000 people bought this" together, that's a stack. Slow down.
- **For regulators:** look at combinations and defaults, not just single claims. India's Uniform Code for Pharmaceutical Marketing Practices (UCPMP), issued in March 2024, bans gifts, travel, hospitality and cash to doctors and their families ✔. It targets exactly the authority channel, though critics say enforcement is weak.
- **For schools:** teaching the tricks (prebunking) helps a little. Teaching people to *pause* may help more. **[YOUR OPINION]**

### 6.3 Reconciling with "persuasion is weak"
The simulation's big effects come from choices where people start at 50/50 and don't care much. That matches the conditions where real experiments find big effects (sign-up forms, organ-donor forms, product pages) and differs from elections, where people care and hear competing messages. The paper's claim is therefore limited: **manipulation is strongest in low-stakes, fast, one-sided choices**, and many daily choices are exactly like that.

---

## 7. Limits and ethics
1. **The simulation is a toy model.** Its strengths are assumptions tuned to experiments. It shows how mechanisms can combine; it doesn't prove what real people do.
2. **Many benchmarks were checked only through abstracts or summaries** (✔ above), not the full papers. Items still marked [CHECK] were not confirmed.
3. **The decoy effect is fragile** in replications.
4. **The model treats pushes toward A and B the same way.** Real people correct fake negativity more than fake positivity (Muchnik et al. 2013).
5. **The default rule probably overstates effects on people with strong preferences** (Section 5.6).
6. **The case collection isn't a random sample.** It comes from two channels, and only part of each was read (41/70 and 111/182). It illustrates techniques; it can't measure how common they are.
7. **Source cautions:** *Predictive History* contains conspiracy and antisemitic content. It is used only as a case study of persuasion, with warnings. Podcast guests make claims that were not all verified; the reports mark which were.
8. **Copyright:** Bernays and Lippmann may still be under copyright in India. They are quoted only briefly, for study and criticism.

---

## 8. Conclusion
**[YOUR OPINION]** Write this yourself, in 150–250 words. Suggested shape:
1. What surprised you most (the stacking? confirmation bias? the default?).
2. One thing you now notice in your daily life that you didn't before.
3. One question you'd want to test next, for example with real classmates, with an ethics check and their consent.

---

## References (to complete and check)
*Mark each one as you read the original.*

- Adena, M., et al. (2015). Radio and the rise of the Nazis in prewar Germany. *Quarterly Journal of Economics*, 130(4).
- Asch, S. E. (1951). Effects of group pressure upon the modification and distortion of judgments.
- Bernays, E. (1928). *Propaganda*. Horace Liveright.
- Brady, W. J., Wills, J. A., Jost, J. T., Tucker, J. A., & Van Bavel, J. J. (2017). Emotion shapes the diffusion of moralized content in social networks. *PNAS*, 114(28), 7313–7318. ✔
- Chetty, R., Deming, D. J., & Friedman, J. N. (2023). Diversifying society's leaders? The determinants and causal effects of admission to highly selective private colleges. NBER Working Paper 31492 (published in *Quarterly Journal of Economics*, 2026, 141(1), 51–145). ✔
- Coppock, A., Hill, S. J., & Vavreck, L. (2020). The small effects of political advertising are small regardless of context, message, sender, or receiver. *Science Advances*, 6(36).
- Deffuant, G., et al. (2000). Mixing beliefs among interacting agents. *Advances in Complex Systems*, 3.
- DeJong, C., et al. (2016). Pharmaceutical industry–sponsored meals and physician prescribing patterns for Medicare beneficiaries. *JAMA Internal Medicine*, 176(8), 1114–1122. ✔ (Even a single meal was associated with more prescribing of the promoted brand. An association, not proof of cause.)
- Hasher, L., Goldstein, D., & Toppino, T. (1977). Frequency and the conference of referential validity. *J. Verbal Learning and Verbal Behavior*, 16.
- Hassan, A., & Barber, S. J. (2021). The effects of repetition frequency on the illusory truth effect. *Cognitive Research*, 6:38.
- Hegselmann, R., & Krause, U. (2002). Opinion dynamics and bounded confidence. *JASSS*, 5(3).
- Huber, J., Payne, J. W., & Puto, C. (1982). Adding asymmetrically dominated alternatives. *J. Consumer Research*, 9.
- Johnson, E. J., & Goldstein, D. (2003). Do defaults save lives? *Science*, 302, 1338–1339. ✔ (Same experiment also reported in Johnson & Goldstein 2004, *Transplantation*, 78(12).)
- Kalla, J., & Broockman, D. (2018). The minimal persuasive effects of campaign contact in general elections. *APSR*, 112(1).
- King, G., Pan, J., & Roberts, M. E. (2017). How the Chinese government fabricates social media posts for strategic distraction. *APSR*, 111(3).
- Le Bon, G. (1895/1896). *The Crowd: A Study of the Popular Mind*.
- Lewandowsky, S., et al. (2012). Misinformation and its correction. *Psychological Science in the Public Interest*, 13(3).
- Lippmann, W. (1922). *Public Opinion*.
- Luguri, J., & Strahilevitz, L. (2021). Shining a light on dark patterns. *J. Legal Analysis*, 13.
- Machiavelli, N. (1532). *The Prince*.
- McPherson, M., Smith-Lovin, L., & Cook, J. (2001). Birds of a feather. *Annual Review of Sociology*, 27.
- Mercier, H. (2017). How gullible are we? *Review of General Psychology*, 21(2).
- Mijs, J. J. B. (2021). The paradox of inequality: income inequality and belief in meritocracy go hand in hand. *Socio-Economic Review*, 19(1), 7–35. ✔
- Milgram, S. (1963). Behavioral study of obedience. *J. Abnormal and Social Psychology*, 67.
- Muchnik, L., Aral, S., & Taylor, S. J. (2013). Social influence bias. *Science*, 341.
- Nisbett, R. E., & Wilson, T. D. (1977). Telling more than we can know. *Psychological Review*, 84(3).
- Peisakhin, L., & Rozenas, A. (2018). Electoral effects of biased media: Russian television in Ukraine. *AJPS*, 62(3).
- Plato. *Republic*, Book VII (trans. Jowett).
- Roozenbeek, J., & van der Linden, S. (2019). Fake news game confers psychological resistance against online misinformation. *Palgrave Communications*, 5, 65. ✔
- Frederick, S., Lee, L., & Baskin, E. (2014). The limits of attraction. *Journal of Marketing Research*, 51(4).
- Hackenburg, K., & Margetts, H. (2024). Evaluating the persuasive influence of political microtargeting with large language models. *PNAS*, 121(24).
- Modirrousta-Galian, A., & Higham, P. A. (2023). Gamified inoculation interventions do not improve discrimination between true and fake news. *Journal of Experimental Psychology: General*, 152, 2411–2437.
- Reicher, S. (1984). The St. Pauls' riot: An explanation of the limits of crowd action in terms of a social identity model. *European Journal of Social Psychology*, 14.
- Salvi, F., Horta Ribeiro, M., Gallotti, R., & West, R. (2025). On the conversational persuasiveness of GPT-4. *Nature Human Behaviour*.
- Salganik, M. J., Dodds, P. S., & Watts, D. J. (2006). Experimental study of inequality and unpredictability in an artificial cultural market. *Science*, 311.
- Tversky, A., & Kahneman, D. (1981). The framing of decisions and the psychology of choice. *Science*, 211.
- Walter, N., & Tukachinsky, R. (2020). A meta-analytic examination of the continued influence of misinformation. *Communication Research*, 47(2).
- Worchel, S., Lee, J., & Adewole, A. (1975). Effects of supply and demand on ratings of object value. *JPSP*, 32(5).
- Yang, S., & Lynn, M. (2014). More evidence challenging the robustness and usefulness of the attraction effect. *J. Marketing Research*, 51(4).
- Zajonc, R. B. (1968). Attitudinal effects of mere exposure. *JPSP*, 9(2).

**Podcast and video sources:** see the timestamped links in `reports/1_trump.md` to `reports/5_education_system.md`.

---

## Your to-do list for this draft
1. Fill in every **[YOUR OPINION]** (about 12 places). This is the part that makes the paper yours.
2. No **[CHECK]** marks are left (all checked online on 6 Nov). Reading the original papers yourself is still better, especially Huber, Payne & Puto 1982 (the "+9%" decoy figure comes only from summaries).
3. Rewrite Sections 1 and 6 in your own words.
4. Decide on a length and a target (school project, essay competition, a blog or a journal for high-school research).
