# Paywalled sources as the value of information

A source that costs money or an identity is worth reading only if it can change the answer. Decision analysis prices that as the **value of information**. The maintainer's rule is to mark such a source unverifiable. The data-gathering repository holds the value-of-information rule.

Follows the [topic shape](https://github.com/Tewf/reader-ergonomics-topic/blob/86e14fe9a1a9877d6a87a2f8b4e8713f98724b5a/shapes/topic.md).

## The practice

The maintainer's practice, written down for this review.

- A source reachable only with a paid account or an identity is not opened.
- It is marked unverifiable, and the abstract is read instead.
- A number read in a summary is marked secondary.
- No source is priced against what it might change.

## The problem class

- The field's name: **value of information** (Howard 1966), from decision analysis.
- Its quantities: the expected value of perfect information, and of sample information, set against the cost of getting it.
- Jackson 2022 gives a broad overview, from principles to implementation, in health policy models.
- Grade: proved under a stated model; use outside health policy is a convention.

## The best-known algorithm

- Expected value of perfect information: compute the expected gain in the decision if the uncertain quantity were known, by simulation over the model.
- Reference implementation: the R package voi, by the authors of Jackson 2022. Read on 2026-11-03: 11 stars, last push 2024-09-16, no licence declared.
- Grade: supported with caveat. The package computes it for a model with a decision and probabilistic inputs; a review is not yet written as one.

## The gap

- The maintainer's rule is a safe default with a fixed cost: skip. It cannot say when skipping loses.
- Value needs a model of the decision: which answer a paywalled paper could flip, and with what chance. Nothing records that.
- Where people beat algorithms: a reader may know a paper's worth from its citers, which the model must be given as a prior.
- Kind: algorithm, once a decision and a prior exist. Today a rule of prudence.

## The change proposed

- For each unverifiable source, write the claim it was meant to support and how much rested on it.
- Where one claim rests on one paywalled source, record the maintainer's call to pay or not, with the claim.
- Run the value-of-information rule on three recorded cases before building more.

## Sources

- Howard 1966: information value theory. Record only. Proved.
- Jackson 2022: overview and implementation. Abstract read. Supported with caveat.

## See also

[The map](README.md); [the bibliography](../evidence/bibliography.md); [data gathering](data-gathering.md);
[ai-augmented-data-gathering](https://github.com/Tewf/ai-augmented-data-gathering).
