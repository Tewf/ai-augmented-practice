# The budget cap as allocation under a budget

The maintainer sets a ceiling on use for a period and stops launching work when it is reached. The field calls this allocation under a budget. **Bandits with knapsacks** give a policy for it; cost-aware optimisation has a library implementation.

Follows the [topic shape](https://github.com/Tewf/reader-ergonomics-topic/blob/86e14fe9a1a9877d6a87a2f8b4e8713f98724b5a/shapes/topic.md).

## The practice

The maintainer's practice, written down for this review.

- A ceiling on use is set for a period and raised by hand.
- New jobs wait when the ceiling is near.
- The cheapest worker that can do a job gets it.
- Expected yield per unit of cost is not computed.

## The problem class

- The field's name: **bandits with knapsacks** (Badanidiyuru 2018): a bandit that ends when any resource budget is used up.
- In optimisation: **cost-aware Bayesian optimisation** (Lee 2020), which measures progress per unit of cost, not per iteration.
- Grade: proved regret bounds for the first; measured on twenty benchmark problems for the second.

## The best-known algorithm

- Bandits with knapsacks: primal-dual and confidence-bound algorithms with regret near the best fixed policy (Badanidiyuru 2018; record only).
- Cost-aware: CArBO (Lee 2020) combines a cheap initial design with a learned cost model whose weight fades over time. It found better configurations at equal cost on 20 problems (abstract).
- Reference implementation: BoTorch, with `InverseCostWeightedUtility` in its cost-aware module (read on 2026-11-03).
- No implementation of Bandits with Knapsacks by its authors was found. A search of public repositories returned two unrelated student projects.

## The gap

- A cap bounds the spend; it does not allocate it. Two jobs with different yield get the same priority.
- The cheapest-worker rule is a greedy rule by cost alone. The field divides expected gain by cost.
- Where people beat algorithms: the person knows the stakes of a job, which no yield estimate holds.
- Kind: partly an algorithm. The knapsack form fits; yields are not measured.

## The change proposed

- Record per job the cost spent and a verdict of whether it moved the work.
- Rank queued jobs by the maintainer's expected gain divided by cost, and run in that order.
- A pass is a month in which the cap is not reached before the jobs the maintainer ranked highest are done.

## Sources

- Badanidiyuru 2018: bandits with knapsacks. Record only. Proved.
- Lee 2020: cost-aware optimisation. Abstract read. Measured on benchmarks.
- BoTorch 2026: the cost-aware module. Documentation read in part.

## See also

[The map](README.md); [the bibliography](../evidence/bibliography.md); [tiers](tiers.md); [batches](batches.md).
