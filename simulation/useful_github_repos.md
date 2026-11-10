# Useful GitHub repos for the simulation and the paper
*Searched 9 Nov 2026. I checked that each repo exists, and its stars and last update, on GitHub. I have **not** downloaded or run any of them yet.*

## ⭐ Most useful for us (free, and they fit the paper)

### 1. Dark patterns at scale: real data on how common the tricks are
- **Repo:** [aruneshmathur/dark-patterns](https://github.com/aruneshmathur/dark-patterns) (Princeton, 141 ★, GPL-3.0, last updated 2019)
- **What it is:** a crawl of about 11,000 shopping websites. It found 1,818 dark patterns on about 11% of them (fake countdowns, "only 2 left", pre-ticked boxes, fake "X people bought this").
- **Why it matters:** our paper's big weakness is that we can't say **how common** the tricks are (Limits, point 6). This dataset can. We could count how often several tricks appear *together on one site*, which is real-world evidence for our "stacking" finding.
- **Related:** [yamanalab/ec-darkpattern](https://github.com/yamanalab/ec-darkpattern) (43 ★): the same data turned into a text dataset for spotting dark patterns automatically.

### 2. choices13k: 13,006 real human choices between two options
- **Repo:** [jcpeterson/choices13k](https://github.com/jcpeterson/choices13k) (79 ★, updated 2026)
- **What it is:** real people choosing between two gambles, from Peterson et al., *Science* 2021.
- **Why it matters:** our model's choice rule (the S-curve) is a guess. We could **test it against real human choices**: does a simple S-curve predict people's choices well, and where does it fail? That would make the simulation much more believable.
- ⚠ These are money gambles, not tricks, so it tests the choice rule, not the manipulation.

### 3. SALib: a better robustness test
- **Repo:** [SALib/SALib](https://github.com/SALib/SALib) (1,025 ★, MIT, updated Nov 2026)
- **What it is:** a standard Python tool for "sensitivity analysis", which asks which assumption changes the results most.
- **Why it matters:** our robustness test changes one guess at a time (18 tests). SALib changes **all guesses at once** in thousands of combinations, then tells you which guess matters most. That's the method a real reviewer would expect. It would turn "18/18 held" into a stronger claim, or show us a weakness.

### 4. NDlib: standard opinion-spreading models
- **Repo:** [GiulioRossetti/ndlib](https://github.com/GiulioRossetti/ndlib) (302 ★, BSD-2, updated 2026)
- **What it is:** a Python library with the standard models of how opinions spread through networks, including the **Deffuant** bounded-confidence model our confirmation bias is based on.
- **Why it matters:** we can **check our network result against the textbook version**. If NDlib's Deffuant model shows the same thing (extreme influencers get ignored, mild ones get through), our finding is much more trustworthy.

## 🔍 Interesting, but probably not for now

### 5. AI agents that act like people (needs a paid AI API)
- [joonspk-research/generative_agents](https://github.com/joonspk-research/generative_agents) (22,359 ★, Stanford's "Generative Agents", 2023): 25 AI characters living in a small town.
- [camel-ai/oasis](https://github.com/camel-ai/oasis) (5,404 ★, very active): simulates up to a million AI "users" on a fake Twitter or Reddit, including misinformation spread.
- **Why it's interesting:** instead of rules we invent, each person is an AI that reads posts and decides. This would directly test the WTF "AI finds the right words" idea.
- **Why not now:** each simulated person calls an AI model, so even a small run costs real money (likely more than your $60 limit for anything big). And "AI pretending to be humans" is a debated research method: AI agents don't always behave like real people.

### 6. Centaur: an AI trained to predict human choices
- Binz et al., *Nature* 2025: a language model fine-tuned on **Psych-101** (160 psychology experiments, 60,000 people, 10 million choices). Older code is at [marcelbinz/CENTaUR](https://github.com/marcelbinz/CENTaUR).
- **Why interesting:** it's the closest thing to "predicting human behaviour" in research today. You could **cite it** in Section 5 as the big-budget version of what we're doing.
- **Why not run it:** the model is huge (70 billion parameters) and won't run on a laptop. **[CHECK]** whether Psych-101 itself is freely downloadable (it may be on Hugging Face). If it is, it could be useful data.

### 7. Mesa and NetLogo
- **Mesa** (github.com/mesa/mesa) is the standard Python library for this kind of simulation, and **NetLogo** is a visual tool with a large models library.
- We don't need them, because our plain Python model is simpler to explain. NetLogo's **models library** is still worth browsing for ideas.

## My suggested order
1. **SALib**: a stronger robustness test. Small job, big gain in credibility.
2. **NDlib**: check the confirmation-bias result (from the paper review, fix 2).
3. **Dark patterns dataset**: count how often tricks are stacked on real websites.
4. **choices13k**: test the choice rule (a bigger job).

Steps 1 and 2 need `pip install SALib ndlib`, which are free, well-known packages.
