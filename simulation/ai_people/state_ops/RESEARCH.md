# Secret agencies and meme wars: research before simulating
*Collected 14 Nov 2026, BEFORE designing the simulation. It builds on `sources/topic_notes/state_influence_ops_notes.md` (11 Nov). Almost everything here comes from web-search summaries of papers, platform reports and news [summary]. I didn't read the full papers. Items marked [CHECK] are disputed or unconfirmed.*

**The question:** governments and their agencies run fake "ordinary people" accounts and meme pages. **Do these actually change what people think, and what protects people?**

**Scope:** global. **Balance rule:** cases come from many countries, including the US, France, Israel and India, not only "enemy" countries. The point is that the *method* is shared, not that one country is the villain.

---

## 1. Who does it: documented cases from around the world
| Country | Operation | What happened | How solid |
|---|---|---|---|
| 🇷🇺 Russia | **Internet Research Agency** (2014–18) | A St Petersburg "troll factory" ran fake American accounts and meme pages on both left and right | ✔ US Senate committee, Mueller report |
| 🇷🇺 Russia | **Doppelganger** (2022–24) | Copied the look of real newspapers (Le Monde, The Guardian, Der Spiegel, Fox News) on look-alike web addresses, then spread the fake articles with fake accounts. Meta called it the "largest and most aggressively persistent" Russian operation it had seen; the EU sanctioned the two Russian firms behind it | ✔ Meta reports, EU sanctions. **Its real reach is disputed:** researchers think the firms inflated their own numbers |
| 🇷🇺 Russia | **"Pravda" network** (2022–) | Millions of automatically copied pro-Kremlin articles on sites in about 49 countries. A US group (American Sunlight Project) argued it was built **to be read by AI chatbots, not by people** ("LLM grooming"). NewsGuard tested 10 chatbots in March 2025: they repeated the network's false claims about **a third of the time** | [summary] NewsGuard / ASP reports, read through news coverage. [CHECK] the exact figures |
| 🇨🇳 China | **Spamouflage** (2019–) | Meta removed about 7,700 Facebook accounts in 2023, linked to Chinese law enforcement, active on 50+ platforms | ✔ Meta report. Meta said it **struggled to reach real people** |
| 🇨🇳 China | **"50 Cent Army"** | Government posts mostly **distract** (cheerleading, changing the subject) rather than argue | ✔ King, Pan & Roberts 2017 (already in the paper) |
| 🇺🇸 USA | **Pentagon anti-vaccine campaign** (2020–21) | Hundreds of fake "Filipino" accounts (at least 300 on Twitter) spread fear about China's Sinovac vaccine, including a claim that it might contain rat poison. The White House ordered it stopped in spring 2021; a later Pentagon review called it "misaligned with our priorities". The Philippine health department asked for answers | ✔ Reuters investigation, 14 June 2024 (read through coverage) |
| 🇺🇸🇬🇧 (likely) | **"Unheard Voice"** (2022) | A pro-Western fake-account network targeting the Middle East and Central Asia. Most posts got only a handful of likes | ✔ Stanford Internet Observatory and Graphika. Who ran it isn't officially confirmed |
| 🇫🇷 France vs 🇷🇺 Russia | **"Troll kombat" in the Central African Republic** (2020) | Facebook removed two rival networks in December 2020: one linked to **people associated with the French military**, one linked to Russia's Prigozhin. **The fake accounts fought each other**, each accusing the other side of being fake. Graphika noted the French side even ran fake "anti-fake-news" pages | ✔ Facebook and Graphika reports, Reuters and Al Jazeera coverage. Graphika found no proof the French government itself directed it |
| 🇮🇱 Israel | **Stoic campaign** (2024) | A ministry reportedly paid a firm about $2 million for hundreds of fake "American" accounts (some written with AI) aimed at US lawmakers over Gaza | ✔ NYT; Meta and OpenAI removed it. Israel denies it |
| 🇮🇳 India (state-linked) | **"Indian Chronicles"** (2005–2020) | EU DisinfoLab found a 15-year network of hundreds of fake local "news" sites (e.g. "EU Chronicle") and revived defunct NGOs at the UN, pushing anti-Pakistan stories; Indian news agency ANI repeated the content | [summary] EU DisinfoLab's own research; many reports come from Pakistani outlets. [CHECK] India's response |
| 🇮🇳 India (parties) | **Party IT cells** | Facebook removed **687 pages and accounts linked to the Congress IT cell** (2019) and a smaller pro-BJP network. A DFRLab study of 2018 hashtags found bots on both sides: #GoBackModi (anti) and #TNwelcomesModi (pro, more automated). A study of 75 copy-paste hashtag campaigns on WhatsApp and Twitter found signs of central control (Jakesch et al. 2021) | ✔ Meta / DFRLab. Estimates of each party's share conflict (journalism, different methods). **Both parties use it** |

**The pattern:** any government that can afford it does this, including democracies, and sometimes against each other. Not every viral meme is a government operation: the 2016 "Great Meme War" for Trump was mostly ordinary users.

## 2. Does it work? Mostly no, at least not directly
- **Bail et al. 2020 (*PNAS*):** 1,239 US Twitter users in late 2017. Interacting with Russian troll accounts had **no measurable effect** on 6 measures of political views and behaviour over a month. The likely reason: the trolls mostly reached people who were **already strongly partisan**.
- **Eady et al. 2023 (*Nature Communications*):** about 1,500 Americans in 2016. **No measurable effect** on attitudes or voting. **1% of users saw 70%** of the troll content, mostly strong Republicans.
- **OpenAI threat reports (2024–2026):** operations from Russia, China, Iran, Israel and the Philippines used ChatGPT to write posts, but **AI did not get them more engagement**. A Russian operation's main account had 172 followers and its best post 4 retweets. Most are rated low-impact (Category 1–2 of 6). [summary]
- **Doppelganger:** "reach doesn't mean effect". Real engagement was tiny, and the firms may have inflated their reports to Moscow.

**So why do governments keep paying for it?** Possible reasons from the research:
1. It's cheap, and the people running it are paid to report "reach".
2. It may work on **narrow, already-leaning targets** (people who already distrust a vaccine or a country).
3. **Getting copied by real media** (ANI repeating "EU Chronicle") or by **AI chatbots** (Pravda) multiplies the reach.
4. The goal may be **doubt and distraction**, not persuasion: "you can't trust anything".

## 3. The psychology that would make it work
| Mechanism | Evidence | Fits fake accounts how |
|---|---|---|
| **Repetition → truth** (illusory truth effect) | Repeated statements are rated more true, **even when people know the right answer** (Fazio et al. 2015, *JEP: General*; meta-analysis Dechêne et al. 2010) | Many fake accounts repeating the same line |
| **Social proof / "everyone thinks so"** | People shifted their beliefs just from being told how many others agreed (UC Berkeley 2022). Like counts alone had mixed effects; **cues only work when they look like wide agreement** (*Scientific Reports* 2024, about 20,000 people) | Fake accounts manufacture the look of consensus |
| **Memes and humour** | Satire changes attitudes through funniness, **mostly in people who already agree** or know little (Boukes et al.). Matching memes get **less scrutiny** (633-person study). Humour can also make people discount the message | Meme pages lower people's guard, but mainly among the already-convinced |
| **The liar's dividend** | Falsely calling a real scandal "fake news" **raised** a politician's support, more than staying silent or apologising (Schiff, Schiff & Bueno 2025, *APSR*, 15,000+ Americans). Video evidence mostly cancelled it | Once fakes are everywhere, real evidence can be waved away |

## 4. What protects people
| Fix | Evidence | Result |
|---|---|---|
| **Source alert** ("a Russian government account") | Arnold et al. 2021, *HKS Misinformation Review*, 1,483 people shown real-style disinformation memes | ✔ Cut belief and sharing, but **depended on the viewer's party** |
| **State-media label** | Nassetta & Gross 2020: a **prominent** YouTube label protected viewers. Betzer et al. 2025: Twitter's small labels **went unnoticed** (2,555 people, no effect) | Works only if people actually see it |
| **Prebunking** (a short video explaining a manipulation trick before people meet it) | Roozenbeek et al. 2022, *Science Advances*: 7 studies, about 30,000 people; on YouTube, 5–10% better at spotting manipulation. In Poland/Czechia/Slovakia: biggest effect in Poland, **no effect in Slovakia** | ✔ Works, modestly, and not everywhere |
| **Media-literacy training** | Badrinathan 2021 (India, already in the paper): didn't help on average; ruling-party supporters got worse | ✖ Not reliable |

## 5. What this means for a simulation
- **Prediction from the field:** fake "ordinary people" posts should have a **small** effect on most people, and **a bigger one on people who already lean that way**.
- **Volume** (many accounts repeating a line) should matter more than one clever post.
- **Revealing the source** should undo most of the effect, **if the label is clear**.
- **A test case close to a real one:** the Pentagon's fake Filipino accounts attacking a foreign-made vaccine. A simulation can use an **invented vaccine and an unnamed foreign government**, so no real country or product is accused.
- ⚠ AI people may be **more suspicious of social media than real people**, which would make them harder to fool. Any null result has to be read with that in mind.

## Sources checked today (search summaries)
- Doppelganger: https://www.disinfo.eu/doppelganger-operation/ ; https://www.npr.org/2023/08/29/1196117574/meta-says-chinese-russian-influence-operations-are-among-the-biggest-its-taken-d ; https://correctiv.org/en/?p=199441
- France vs Russia in CAR: https://www.aljazeera.com/news/2020/12/15/french-and-russian-trolls-fight-it-out-in-central-africa-election ; https://graphika.com/reports/more-troll-kombat
- Indian Chronicles: https://mediawell.ssrc.org/2020/12/10/indian-chronicles-deep-dive-into-a-15-year-operation-targeting-the-eu-and-un-to-serve-indian-interests-eu-disinfolab/ ; https://www.aljazeera.com/amp/news/2020/12/11/eu-ngo-report-uncovers-a-15-year-disinformation-campaign
- India IT cells: https://dfrlab.org/?p=266 ; https://qz.com/india/1590085/bots-boost-gobackmodi-tnwelcomesmodi-ahead-of-indian-election ; https://ojs.aaai.org/index.php/ICWSM/article/download/31385/33545
- Bail 2020: https://www.eurekalert.org/news-releases/473589 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC6955293
- OpenAI threat reports: https://openai.com/index/disrupting-malicious-uses-of-ai-stop-news-2025 ; https://www.npr.org/ (via https://www.kjzz.org/npr-top-stories/2025-06-05/openai-takes-down-covert-operations-tied-to-china-and-other-countries)
- Pravda network: https://meduza.io/en/feature/2025/03/07/russian-disinformation-network-flooded-training-data-to-manipulate-western-ai-chatbots-study-finds ; https://www.theregister.com/2025/10/28/chatbots_still_parrot_russian_state/
- Pentagon campaign: https://www.aljazeera.com/news/2024/6/14/pentagon-ran-secret-anti-vax-campaign-to-undermine-china-during-pandemic ; https://tribune.net.ph/2024/06/17/doh-eyes-probe-on-anti-vax-campaign-of-us-military
- Illusory truth: https://typeset.io/pdf/knowledge-does-not-protect-against-illusory-truth-4e11jui99s.pdf ; https://link.springer.com/content/pdf/10.3758/s13423-021-01995-w.pdf
- Social proof: https://www.universityofcalifornia.edu/news/it-or-not-were-prone-adopt-popular-beliefs-even-fake-ones ; https://www.nature.com/articles/s41598-024-54030-y.pdf
- Memes and satire: https://ojs3.ijoc.org/index.php/ijoc/article/view/18119 ; https://mountainscholar.org/handle/10217/183936
- Liar's dividend: https://isps.yale.edu/research/publications/isps24-07
- Source alerts and labels: https://misinforeview.hks.harvard.edu/article/source-alerts-can-reduce-the-harms-of-foreign-disinformation ; https://misinforeview.hks.harvard.edu/wp-content/uploads/2020/10/nassetta_state_media_warning_labels_20201030-2.pdf ; https://misinforeview.hks.harvard.edu/article/state-media-tagging-does-not-affect-perceived-tweet-accuracy-evidence-from-a-u-s-twitter-experiment-in-2022/
- Prebunking: https://www.cam.ac.uk/stories/inoculateexperiment ; https://www.mediapost.com/publications/article/377008
