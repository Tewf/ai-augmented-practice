# Data gathering as information foraging

The maintainer searches each term three ways and moves to the next source when a string stops adding concepts. The field calls this **information foraging**, with a leaving rule from ecology. The choice of the next source is a bandit. The data-gathering repository holds the algorithm for where to look.

Follows the [topic shape](https://github.com/Tewf/reader-ergonomics-topic/blob/86e14fe9a1a9877d6a87a2f8b4e8713f98724b5a/shapes/topic.md).

## The practice

The maintainer's practice, written down for this review.

- Each term is searched by its academic name, its acronym and its author.
- Surveys are read first, then the seminal paper, then its citations.
- A search string is dropped after five results in a row that add no concept.
- The order of sources follows habit and the last result.

## The problem class

- The field's name: **information foraging** (Pirolli 1999), borrowed from optimal foraging in ecology.
- The leaving rule is the **marginal value theorem** (Charnov 1976): leave a patch when the rate of gain falls to the average rate of the environment.
- Choosing which source to try next is a **multi-armed bandit** (Russo 2018).
- Grade: the theorem is proved under its assumptions; its use on literature search is a convention.

## The best-known algorithm

- Patch leaving: the marginal value theorem, a rule of one line.
- Next source: **Thompson sampling** (Russo 2018), a tutorial with a worked algorithm for Bernoulli arms.
- Reference implementation: SMPyBandits, a library of bandit policies. Read on 2026-11-03: MIT licence, last push 2026-06-19.
- Pirolli's own model of a person at a search interface was not searched for in this pass. The row leaves it open.

## The gap

- The five-in-a-row rule is a leaving rule with a fixed count. The theorem asks for a rate and an average.
- The rate is not recorded in a form a program can read. The data-gathering repository asks this as an open question.
- Where people beat algorithms: a reader who knows the field spots a better term than any rate would.
- Kind: algorithm. The problem is well posed once yield per string is logged.

## The change proposed

- Log, for each search string, the results screened and the concepts they added.
- Compute the marginal value rule on those logs and compare its stopping point with five in a row.
- Hold the work in [ai-augmented-data-gathering](https://github.com/Tewf/ai-augmented-data-gathering), which owns this row's algorithm.

## Sources

- Pirolli 1999: information foraging. Foundational; convention for search.
- Charnov 1976: the theorem. Record only. Proved.
- Russo 2018: Thompson sampling. Abstract read. Measured on benchmarks.
- Marshall 2019 reviews machine learning for systematic reviews, which covers this row. Abstract read.

## See also

[The map](README.md); [the bibliography](../evidence/bibliography.md); [stopping](stopping.md);
[ai-augmented-data-gathering](https://github.com/Tewf/ai-augmented-data-gathering).
