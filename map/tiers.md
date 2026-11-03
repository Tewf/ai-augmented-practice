# Tiers as multi-fidelity optimisation

The maintainer sends a task first to a free local model, then to a cheaper hosted one, then to a strong one. The field calls this multi-fidelity optimisation, with a bandit algorithm for it and a **cascade** for language models.

Follows the [topic shape](https://github.com/Tewf/reader-ergonomics-topic/blob/86e14fe9a1a9877d6a87a2f8b4e8713f98724b5a/shapes/topic.md).

## The practice

The maintainer's practice, written down for this review.

- A bulk or mechanical task goes first to a free local model.
- The next step is a cheaper hosted model, then a small cloud model with tools.
- The strongest model keeps judgment and any answer whose error would not be noticed.
- The tier is chosen by the maintainer from the kind of task.

## The problem class

- The field's name: **multi-fidelity methods** (Peherstorfer 2018): cheap, biased evaluators used with a costly exact one.
- For hyperparameters it is a **bandit with a resource** allocated to configurations (Li 2018).
- For language models it is a **cascade** (Chen 2023b): ask the cheap model, escalate when a scorer doubts the answer.
- Grade: measured in the settings tested; not tested for one person delegating.

## The best-known algorithm

- **Hyperband** (Li 2018): successive halving over many configurations with different budgets. The authors report over an order of magnitude speedup against Bayesian optimisation on their problems (abstract).
- **FrugalGPT** (Chen 2023b): a learned cascade. It matched the best single model with up to 98% lower cost, or beat it by 4% at equal cost (abstract).
- Reference implementations: Optuna's `HyperbandPruner` (read on 2026-11-03: 15007 stars, MIT, active); the FrugalGPT code (291 stars, Apache-2.0, last push 2025-02-10).

## The gap

- The practice is the cascade of Chen 2023b done by hand: cheap first, strong for judgment.
- What it lacks is the scorer. The maintainer decides when to escalate; the algorithm learns a threshold from labelled answers.
- Where people beat algorithms: a task whose error would not be noticed is exactly where a scorer is weakest, so judgment stays with the person.
- Kind: algorithm, matched in form, unmeasured in the family.

## The change proposed

- Log each task: tier first tried, whether a program accepted the answer, whether it was escalated.
- Estimate from the log the share of tasks the cheap tier passes; set an escalation rule on the program's verdict.
- A pass is a rule with fewer escalations than now at the same accepted share.

## Sources

- Peherstorfer 2018: survey. Abstract read. Supported with caveat.
- Li 2018: Hyperband. Abstract read. Measured.
- Chen 2023b: FrugalGPT. Abstract read. Measured on its datasets.

## See also

[The map](README.md); [the bibliography](../evidence/bibliography.md); [the budget cap](the-budget-cap.md).
