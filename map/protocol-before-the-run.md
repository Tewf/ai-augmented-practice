# Protocol before the run as preregistration

Before each run the maintainer writes the question, the arms and a prediction, and a program judges the result. This is what the field calls **preregistration**. The practice is already the field's best-known form, short of a third-party record.

Follows the [topic shape](https://github.com/Tewf/reader-ergonomics-topic/blob/86e14fe9a1a9877d6a87a2f8b4e8713f98724b5a/shapes/topic.md).

## The practice

The maintainer's practice, written down for this review.

- A protocol is written before the run: the question, the arms, the cases, the measure.
- A prediction of the result is written with it.
- A program judges the run; a model does not review its own output.
- The protocol and the result are kept together in the run's folder.

## The problem class

- The field's name: **preregistration** (Nosek 2018): define the research questions and the analysis plan before observing the outcomes.
- Its strong form is the **registered report**, where the plan is reviewed before the results are known.
- Grade: measured as to effect on results; supported with caveat as to adherence.

## The best-known algorithm

- A procedure, not an algorithm: write the plan, deposit it with a timestamp that cannot be changed, run, report every deviation.
- Registered reports: 44% positive results against 96% in the standard literature, on 71 reports and 152 studies (Scheel 2021, abstract).
- Preregistration alone is imperfect: all studies in a sample of badged articles deviated from their plan, and all but one left a deviation undisclosed (Claesen 2021, abstract).
- Reference implementation: the Open Science Framework registries (read on 2026-11-03: Apache-2.0, last push 2026-11-03).

## The gap

- The form matches: the plan comes first, and a program judges.
- Two things differ. The protocol sits in the maintainer's own folder, with no third-party timestamp. Deviations are not listed in a fixed place.
- Where people beat algorithms: none applies; the procedure exists to constrain the person, whose hindsight bias it guards against (Nosek 2018).
- Kind: the practice is the field's procedure in its private form. This row is the baseline.

## The change proposed

- Add a Deviations section to each protocol, filled when the run departs from it.
- Commit the protocol before the run, so the history gives the timestamp.
- A pass is a deviations list in every run folder, empty or not.

## Sources

- Nosek 2018: the case for preregistration. Abstract read. Supported with caveat.
- Scheel 2021: registered reports and positive results. Abstract read. Measured, descriptive.
- Claesen 2021: adherence to plans. Abstract read. Measured, one journal.

## See also

[The map](README.md); [the bibliography](../evidence/bibliography.md); [runs per arm](runs-per-arm.md).
