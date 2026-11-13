# World politics: same message, different messenger (research before simulating)
*Collected 13 Nov 2026, BEFORE designing the simulation. Sources are web-search summaries of papers, polls and news [summary]; I didn't read the full papers. Items marked [CHECK] are disputed or unconfirmed.*

**The question:** around the world, do people judge a political message by **what it says**, or by **who says it**?

**Scope (Maulik's decision):** this is a global topic, not India vs the USA. Evidence is collected from every region where I could find experiments.

**Balance rule:** examples come from left and right, and from governing and opposition parties. The point is that the *habit* is shared, not that one side is worse.

---

## 1. Experiments: the party label can beat the policy, on every continent tested
| Where | Study | What happened |
|---|---|---|
| **USA** | Cohen 2003, "Party over policy" (*JPSP*) | People read a generous or a harsh welfare policy labelled as their own party's or the other party's. **Attitudes followed the label almost entirely, not the content**, and people believed they had judged on merit |
| **USA** | Barber & Pope 2019 (*APSR*) | Republicans told "Trump supports this *liberal* policy" became much more likely to support it. Strong partisans and low-knowledge people followed most |
| **Denmark** | Slothuus & Bisgaard 2021 (*AJPS*) | A real-world case: two parties **suddenly reversed** their position on welfare cuts. **Their voters' opinions followed within weeks**, even though the cuts affected them. The authors say lab experiments may *underestimate* party influence |
| **Britain, Hungary, Poland** | Brader & Tucker 2012; Brader, Tucker & Duell 2013 | Party supporters followed their party's lead on policy. The effect was stronger for **older parties, opposition parties and parties with a clear image** |
| **Russia** | Brader & Tucker 2009 | Party cues worked even in a weak, managed party system |
| **Brazil** | Samuels & Zucco 2014 (*AJPS*) | Supporters of the two main parties (PT and PSDB) followed their own party's cue **and moved away from the other party's cue**. People with no party were unmoved |
| **Kenya** | A national survey experiment [summary; CHECK the paper] | Voters shown their MP's real spending record punished bad performance, **unless they were first reminded of the MP's ethnic group**; then they forgave co-ethnics |
| **Benin, Uganda** | Adida; Conroy-Krutz 2013 [summary] | Ethnic cues work like party cues where information is poor, and they weaken when better information is given |
| **India** | Badrinathan 2021 (*APSR*); a West Bengal experiment 2021 | Media-literacy training didn't help on average, and ruling-party supporters got *worse* at spotting false stories that favoured their side. Misinformation mostly persuaded people who already agreed |

**Limits on the effect:**
- When a policy is clear and familiar, its content matters more than the label (Bullock 2011; a 2026 study) [summary].
- On issues people personally care about, their own view can resist a cue in the "wrong" direction (a 2023 replication of Barber & Pope).
- In Denmark, parties couldn't make voters act against their direct self-interest in a pay dispute; they could only soften demands (Slothuus & Bisgaard 2021, *APSR*).
- **People with no party don't follow cues** (Brazil).

## 2. The same reality, seen through the party (global)
- **Pew Research, 2025 (many countries):** in nearly every country surveyed, supporters of the governing party were far more likely to say the national economy is good.
  - Greece: **71%** of governing-party supporters said the economy was good, against **9%** of everyone else.
  - The gaps were especially large in Hungary, Argentina and Poland.
  - UK: among Labour supporters, positive views of the economy **doubled** in the year after Labour won.
  - Views were only loosely related to real economic figures.
- **USA (Gallup):** after the 2016 election, Republicans saying the economy was "getting better" jumped from 16% to 49% within days; the flip reversed in 2020 and again in 2024. It also happened after Obama's win in 2008.

## 3. Parties swap positions, and supporters follow
- **India** [summary; mostly news and opinion pieces, CHECK details]:
  - Aadhaar: started under the Congress-led government, strongly opposed by the BJP in opposition, then expanded by the BJP government.
  - GST: proposed by the Congress-led government; opposed in its form by Narendra Modi in 2011; passed by the BJP government in 2017, when the Congress opposed parts of it.
  - FDI in retail: fiercely opposed by the BJP in opposition, then partly allowed in 2016.
- **Denmark:** the sudden welfare reversals above.
- **USA:** Republican voters' views on trade and tariffs moved with Trump's positions (Barber & Pope's cases).
- **The pattern:** the same policy is "dangerous" or "historic" depending on who is in power.

## 4. Fact-checks: beliefs change, loyalty doesn't
- **Nyhan, Porter, Reifler & Wood 2020 (*Political Behavior*, USA):** supporters who saw fact-checks of their candidate's false claims **corrected their factual beliefs but didn't change their support**. They took the fact-check "literally but not seriously".
- This matches our earlier topics: information changes what people know more easily than what they choose.

## 5. Speaking style: simple, repeated, "the people vs the elite"
- **Populist parties across Europe write more simply.** Bischof & Senninger 2018 (*European Journal of Political Research*) analysed party manifestos (Austria and Germany [CHECK]): populist parties used shorter sentences and shorter words.
- **Trump's speeches** scored at about a 4th–5th grade level, the simplest among recent US politicians (Boston Globe 2015; Carnegie Mellon 2016). Critics note that these scores measure sentence length, not ideas.
- **Why it works** (from the paper's earlier sections): repeated statements feel truer (Hasher 1977; Hassan & Barber 2021); Le Bon described "affirmation, repetition, contagion" in 1895.
- **Gap:** I found no study that measured *repetition* in speeches directly.

## 6. But persuasion in politics is usually weak
- Campaign ads and canvassing have near-zero average effects on vote choice (Kalla & Broockman 2018; Coppock, Hill & Vavreck 2020).
- **How these fit together:** cues rarely change which side people are on. They tell people **what their side thinks today**. Loyalty is stable; opinions on specific policies are flexible.

## What this means for the simulation design
1. **The core test is a label swap:** the same policy text, attributed to the person's own party, the rival party, or nobody.
2. **Many countries, not two:** people from several regions, each with their real local parties, including a governing and an opposition side.
3. **Include people with no party** (Brazil: they shouldn't move).
4. **Use a policy with no obvious "side"**, so the label is the only clue.
5. **Test style separately:** the same proposal in plain language vs in a simple, repeated, people-vs-elite style.
6. **Test two "fixes":** an independent fact-check, and a reminder that "your own party said the opposite before" (the U-turn disclosure).
7. **Known risk:** AI models may play partisans as caricatures, or know less about politics in some countries. The pilot must check whether answers sound like real supporters.
