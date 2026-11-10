# AI-people research: tools and papers that do what we do
*Searched 10 Nov 2026. Read through abstracts and summaries, not full papers. **[CHECK]** before quoting exact numbers in the paper.*

## Part A. GitHub tools for AI-people simulations

| Tool | What it does | Useful for us? |
|---|---|---|
| **[TinyTroupe](https://github.com/microsoft/TinyTroupe)** (Microsoft) | Builds detailed AI personas (age, job, beliefs, personality) and runs "virtual focus groups" for ads and products. Paper: arXiv 2507.09788 | ⭐ **Very close to our plan.** Good ideas for writing richer life stories. But it needs an OpenAI/Azure key, so it isn't free |
| **[EDSL](https://github.com/expectedparrot/edsl)** (Expected Parrot) | Runs surveys and experiments on many AI agents and many AI models at once, with caching | ⭐ **Best fit for Step 3.** Built for "same question, different versions, many personas, compare models". Free and open-source, but needs API keys for the models. Supports Python 3.9–3.12 (we have 3.14, which may need a separate Python) |
| **[Concordia](https://github.com/google-deepmind/concordia)** (Google DeepMind) | AI people living and talking together in a world run by a "Game Master" AI | Good later for **politics**: people discussing a speech with friends. Too big for now |
| [Generative Agents](https://github.com/joonspk-research/generative_agents) (Stanford) | The famous 25-AI-people town | Background reading and citation only |
| [OASIS](https://github.com/camel-ai/oasis) | Up to a million AI users on a fake Twitter/Reddit | Later, for misinformation spread. Too costly now |

**Recommendation:** keep our own small script for now. It's free on your Pro plan, simple, and we know exactly what it does. Borrow **TinyTroupe's persona ideas** for richer life stories. If we add a second AI model (e.g. Gemini, free), **EDSL** makes comparing models easy.

## Part B. Research papers that do the same thing as us

### 1. Papers showing AI people CAN copy human experiments
- **Aher, Arriaga & Kalai (2023), "Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies", ICML.**
  - Invented the "Turing Experiment": can AI people copy a *group* of human participants?
  - Copied the Ultimatum Game, garden-path sentences and the Milgram experiment.
  - Found a **"hyper-accuracy distortion"**: on the Wisdom of Crowds test, AI people knew answers too well.
  - They also changed the experiment details, so the AI couldn't simply remember the famous result. **We should do that too.**
- **Hewitt, Ashokkumar, Ghezae & Willer (2024), "Predicting results of social science experiments using large language models"** (Stanford/NYU).
  - GPT-4 predicted results of 70 real US survey experiments (more than 100,000 people). The correlation with real effects was r = 0.85, and r = 0.90 for unpublished studies the AI couldn't have seen.
  - ⚠ But it **overestimated how big the effects are**.
- **Argyle et al. (2023), "Out of One, Many: Using Language Models to Simulate Human Samples", *Political Analysis*.** (From my knowledge, not checked tonight.) AI "silicon samples" given US voter backgrounds matched real survey patterns in politics. **[CHECK]**
- **Park et al. (2024), "Generative Agent Simulations of 1,000 People"** (Stanford). (From my knowledge.) Built AI copies of 1,052 real people from 2-hour interviews; they matched those people's survey answers about as well as the people matched themselves two weeks later. **[CHECK]**

### 2. Papers showing AI people are NOT like humans (this matches our pilot)
- **Liu, Geng, Peterson, Sucholutsky & Griffiths (2024), "Large Language Models Assume People are More Rational than We Really Are"** (arXiv 2406.17055).
  - Tested GPT-4o, Claude 3 Opus, Llama-3 and others on the **choices13k** dataset (the same one in our GitHub list).
  - The AIs predicted that people choose like rational calculators. They tracked the "rational" model far more closely than real human choices.
  - 🔗 **This explains our pilot.** Our AI shoppers were too logical and too suspicious of the countdown.
- **Wang, Morgenstern & Dickerson (2024/2025), "Large language models that replace human participants can harmfully misportray and flatten identity groups"** (arXiv 2402.01908).
  - AI people are **less varied than real people** ("flattening"), and they show what *outsiders* think a group is like.
  - 🔗 **Exactly our pilot result:** 19 of 20 AI people picked the black earbuds.
  - ⚠ They warn against using AI people **instead of** real humans when identity matters, but say AI people can **supplement** real humans. That's how our paper should use them.
- **Many Labs 2 replication with personas (2025):** giving AI people varied backgrounds increased variety, but they still often didn't match human results, especially for studies that also failed with humans. **[CHECK]** the exact paper.

### 3. Papers on AI agents and dark patterns (closest to our shopping test)
- **Guo et al. (2025), "SusBench"** (arXiv 2510.11035): 313 tasks on 55 real shopping websites, testing **both humans and AI agents**.
  - Both were most fooled by **pre-selection**, trick wording and hidden information, but **resisted obvious, loud dark patterns**.
  - 🔗 **This matches our pilot almost exactly:** pre-selection worked, while the loud countdown backfired. Our finding is supported by a much bigger study. ⭐
- **Ersoy et al. (2025), "Investigating the Impact of Dark Patterns on LLM-Based Web Agents"** (arXiv 2510.18113, IEEE S&P 2026): AI web agents fell for a dark pattern **41%** of the time, and the *better* agents were *more* vulnerable.
- **Tang et al. (2025), "Dark Patterns Meet GUI Agents"** (arXiv 2509.10723): humans fall for dark patterns through habit and shortcuts; AI agents fall for them because they focus on finishing the task. **Same result, different reason.**
- **DECEPTICON (Dec 2025, arXiv 2512.22894):** bigger, more "thoughtful" models were **more** susceptible to dark patterns.

## What this means for our project
1. **We're not alone, which is good:** this is an active research area (2023–2025), so the paper has a solid literature to cite.
2. **Our pilot results fit the literature:** pre-selection works, loud tricks backfire, and AI people are too rational and too alike.
3. **Methods we should copy:**
   - **Vary the experiment details** so the AI can't recall famous results (Aher et al.).
   - **Compare with real human data**: classic experiments first, then real classmates if possible.
   - **Use AI people to *supplement*, not replace, humans** (Wang et al.).
   - **Report effect sizes carefully.** AI people may exaggerate them (Hewitt et al.) or shrink them (our scarcity result).
4. **Our original contribution:** most papers test US or Western personas on general tasks. **We test Indian personas on topic cases (universities, healthcare, politics) and compare three kinds of "people"** (rule-based, AI and real experiments). Nobody in these papers did exactly that.

## Sources
- TinyTroupe: https://github.com/microsoft/TinyTroupe · https://arxiv.org/html/2507.09788v1
- EDSL: https://github.com/expectedparrot/edsl
- Concordia: https://github.com/google-deepmind/concordia
- Aher et al.: https://proceedings.mlr.press/v202/aher23a.html
- Hewitt et al.: https://www.gsb.stanford.edu/faculty-research/publications/large-language-models-can-predict-results-social-science-experiments
- Liu et al.: https://arxiv.org/html/2406.17055v4
- Wang et al.: https://arxiv.org/abs/2402.01908v1
- SusBench: https://arxiv.org/abs/2510.11035v1
- Ersoy et al.: https://arxiv.org/html/2510.18113
- Tang et al.: https://www.arxiv.org/abs/2509.10723
- DECEPTICON: https://www.emergentmind.com/papers/2512.22894
- Silicon-sample replication (framing): https://pdf.arxiv.org/pdf/2503.10671
