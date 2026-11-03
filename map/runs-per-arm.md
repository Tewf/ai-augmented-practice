# Runs per arm as sequential testing and factorial design

The maintainer runs ten calls per arm, then sixty. The field fixes the number from the effect to detect, or tests as the runs arrive and stops with a guarantee. Ten per arm detects a large effect and misses a medium one.

Follows the [topic shape](https://github.com/Tewf/reader-ergonomics-topic/blob/86e14fe9a1a9877d6a87a2f8b4e8713f98724b5a/shapes/topic.md).

## The practice

The maintainer's practice, written down for this review.

- Arms differ by one thing, such as the brief given to a model.
- Each arm gets ten runs in a first round, then sixty (three tasks, two tiers, ten each) in a second.
- A program judges each run on cases the arm did not see.
- The number of runs is set by cost and habit, not by a power calculation.

## The problem class

- The field's names: **power analysis** for a fixed sample, **sequential testing** (Wald 1945) for runs that arrive one by one, and **confidence sequences** (Howard 2021) valid at any stopping time.
- With several arms and several factors, **factorial design** varies factors together.
- Grade: proved for the tests; for language-model runs, supported with caveat, since runs are not independent draws of a fixed process.

## The best-known algorithm

- Sequential probability ratio test (Wald 1945): stop as soon as the evidence passes a bound set by the two error rates.
- Anytime-valid inference: confidence sequences (Howard 2021) allow a look after every run without inflating the error.
- Reference implementation: confseq, by the authors of Howard 2021. Read on 2026-11-03: 88 stars, MIT licence, last push 2026-01-07.

## The gap

- Computed here, with Fisher's exact test, two-sided, 3000 simulated draws per case:
  - 0 of 10 against 5 of 10 gives p = 0.033 (the family's first round).
  - At ten per arm, power is 0.63 for a rise from 0 to 0.5, and 0.95 for a rise from 0 to 0.7.
  - At ten per arm, power is 0.23 for 0.3 to 0.7, and 0.14 for 0.5 to 0.8.
  - At sixty per arm, power is 0.91 for 0.5 to 0.8, and 0.31 for 0.5 to 0.65.
- The second round's two briefed arms, 30 of 60 against 29 of 60, give p = 1.0: no difference seen, which sixty runs can rule out only for large effects.
- Kind: algorithm. The practice detects large effects and cannot rule out medium ones.

## The change proposed

- State the smallest effect worth acting on before the run, and set the runs from the power table above.
- Where runs are costly, use a confidence sequence and stop when it excludes zero or the budget ends.
- A pass is a stated minimal effect in every protocol.

## Sources

- Wald 1945: the sequential test. Record only. Proved.
- Howard 2021: confidence sequences. Record only. Proved.
- The power figures: computed for this page, not from a source.

## See also

[The map](README.md); [the bibliography](../evidence/bibliography.md); [protocol before the run](protocol-before-the-run.md).
