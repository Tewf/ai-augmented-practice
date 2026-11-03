# Scope and review as a sequential decision problem

The maintainer fixes a scope, reviews, reads the result and chooses the next step by hand. The field calls this a sequential decision problem. A policy that values each step by what it will change exists, with an implementation. The family's own steps are too few to run it.

Follows the [topic shape](https://github.com/Tewf/reader-ergonomics-topic/blob/86e14fe9a1a9877d6a87a2f8b4e8713f98724b5a/shapes/topic.md).

## The practice

The maintainer's practice, written down for this review.

- A scope is written first: what is in, what is out, the questions to answer.
- A review follows in five steps, and ends when a baseline can be named.
- The next step is chosen by the maintainer after reading the last result.
- Each job is a few dozen sources, then a stop.

## The problem class

- The field's name: **sequential decision problem**. Powell 2019 unifies the methods of the field under one framework with four classes of policy.
- The choice of a next evaluation of an expensive unknown function is **Bayesian optimisation**. The family's foundations repository already reads its loop that way.
- Grade of the class: supported with caveat. The family's steps change the objective, which the standard model does not allow.

## The best-known algorithm

- **Knowledge gradient** (Frazier 2008): choose the step whose result is expected to change the decision most. It is a one-step lookahead policy.
- The common alternative is a Gaussian-process surrogate with noisy expected improvement.
- Reference implementation: BoTorch, `qKnowledgeGradient` in its acquisition module (Balandat 2020; BoTorch 2026). Read on 2026-11-03: active, MIT licence.
- Grade: supported with caveat, measured on tuning benchmarks, not on research projects.

## The gap

- The maintainer's rule is a judgment after each result. No policy has been run on the same sequence.
- The foundations repository replayed a recorded sequence under several policies. None beat random at naming the kind of next job, on seven waves (that repository's record, not re-run here).
- Where a person with judgment beats an algorithm: when the environment is regular and the person has had feedback (Kahneman 2009). A project with one run of each step is neither.
- Kind: partly an algorithm. The problem is named; the data to run it is thin.

## The change proposed

- Keep the manual choice. Write each choice and its result as one row, so a policy can be replayed on it later.
- Replay the knowledge gradient and random choice on the rows when about thirty exist.
- A pass is a policy that names the maintainer's choice more often than random does.

## Sources

- Powell 2019: the unified framework. Record only. Convention.
- Frazier 2008: knowledge gradient. Abstract read. Proved for normal beliefs.
- Balandat 2020 and BoTorch 2026: the implementation. Abstract read; documentation read in part.
- Kahneman 2009: when judgment holds. Record only.

## See also

[The map](README.md); [the bibliography](../evidence/bibliography.md); [the front page](../README.md);
[the foundations review of Bayesian optimisation](https://github.com/Tewf/ai-augmented-foundations/tree/master/evidence/bayesian-optimisation).
