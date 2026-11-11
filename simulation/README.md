# Simulations

Two kinds of simulation, used together.

| Folder | What it is | Strength | Weakness |
|---|---|---|---|
| [`rule_based/`](rule_based/) | 1,000 simulated people follow fixed rules. Each trick's strength is tuned to a published experiment. | Fast and transparent. Tests **stacking** of tricks and how robust the results are to every assumption. | People can only react the way the rules allow. |
| [`ai_people/`](ai_people/) | Each "person" is a fresh AI-model call with an Indian or American life story. It reads a realistic choice and answers with a choice and a reason. | Gives reasons in their own words. Tests realistic, high-stakes situations built from research. | AI people match humans in direction more often than in size. |

`requirements.txt` is only needed for the SALib and NDlib robustness checks in `rule_based/`. Everything else uses the Python standard library.
