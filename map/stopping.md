# Stopping as estimating what is still unseen

The maintainer stops a review when a baseline can be named. The field has estimators of how much is still unseen, and stopping criteria with a confidence level. The data-gathering repository holds the estimator.

Follows the [topic shape](https://github.com/Tewf/reader-ergonomics-topic/blob/86e14fe9a1a9877d6a87a2f8b4e8713f98724b5a/shapes/topic.md).

## The practice

The maintainer's practice, written down for this review.

- A review stops when it can name the baseline it compares against.
- A search string stops after five results in a row add no concept.
- The pool is capped at a size set in advance, about forty sources.
- No estimate is made of how many relevant sources were missed.

## The problem class

- The field's names: the **unseen species problem**, with the **Good-Turing estimator** (Good 1953), and **species richness estimation** with coverage (Chao 2012).
- In screening for reviews it is a **stopping criterion for technology-assisted review** (Cormack 2016; Callaghan 2020).
- Grade: the estimators are mathematics; the guarantees on reviews are measured on test collections.

## The best-known algorithm

- Coverage estimation by Good-Turing, extended by Chao, tells how much of the probability mass is unseen.
- For screening, Cormack 2016 shows how to augment a review method to guarantee a target recall for a stated extra effort, tested on 555 topics (abstract).
- Callaghan 2020 rejects the hypothesis of having missed a recall target at a chosen confidence. On test sets it gave work savings of 17% on average and reliable recall; earlier rules were inconsistent (abstract).
- Reference implementation: iNEXT for the ecology estimators (Chao 2012 is its method; read on 2026-11-03: last push 2025-07-31, no licence declared).

## The gap

- The maintainer's stops are rules of thumb: a count and a named baseline. They give no confidence level.
- The family's sets are small, a few dozen sources. Estimators need many samples; this is a caveat to test, not a measured limit.
- Kind: algorithm, with a small-sample caveat.

## The change proposed

- For each review, record the concepts found per source in order.
- Compute the coverage estimate and the point where it passes a set value; compare with the stop actually made.
- A pass is a stop within the estimator's interval on at least most of the family's reviews.

## Sources

- Good 1953: the estimator. Record only. Proved.
- Chao 2012: coverage-based extrapolation. Record only. Supported with caveat for small samples.
- Cormack 2016: guaranteed reliability. Abstract read. Measured on 555 topics.
- Callaghan 2020: statistical stopping. Abstract read. Measured on test datasets.

## See also

[The map](README.md); [the bibliography](../evidence/bibliography.md); [data gathering](data-gathering.md);
[ai-augmented-data-gathering](https://github.com/Tewf/ai-augmented-data-gathering).
