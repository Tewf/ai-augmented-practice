# Deep reading as active learning

The maintainer reads some sources in full and others by abstract. The field calls the choice of what to label next **active learning**, and it has a tool for exactly this step in systematic reviews.

Follows the [topic shape](https://github.com/Tewf/reader-ergonomics-topic/blob/86e14fe9a1a9877d6a87a2f8b4e8713f98724b5a/shapes/topic.md).

## The practice

The maintainer's practice, written down for this review.

- A first pass reads abstracts and records, not full text.
- Each source is marked with how it was read: in full, in part, abstract, record only.
- Full reading goes to sources that the claims rest on.
- The choice is made by hand, source by source.

## The problem class

- The field's name: **active learning** (Settles 2009), the learner chooses which items a person labels.
- In reviews it is **technology-assisted review** or prioritised screening (Cormack 2014; van de Schoot 2021).
- Grade: measured. Cormack 2014 found, on eight review tasks, that active learning needed significantly less review effort than passive learning for any recall level (P<0.01, abstract).

## The best-known algorithm

- **Uncertainty sampling** (Lewis 1994): label next the item the classifier is least sure of; in screening, the item most likely relevant is read first.
- Reference implementation: ASReview (van de Schoot 2021). Read on 2026-11-03: 1063 stars, Apache-2.0, last push 2026-11-02.
- The authors report simulations showing far more efficient reviewing than manual (abstract; the figure is not in the abstract).

## The gap

- The maintainer's order is by hand. The rule has no ranking and no record of how many read sources were useful.
- The tool ranks title and abstract records; the family's depth choice is about full text, a different step. The match is partial.
- Where people beat algorithms: a reader judges which claim carries the weight, which a ranker trained on relevance does not see.
- Kind: algorithm for screening; partly a habit for choosing depth.

## The change proposed

- Run ASReview on one finished review's candidate list, with the maintainer's inclusions as labels.
- Measure the share of included records found after reading half of the list, against reading in the order found.
- Keep depth marking by hand; add a column for whether a full read changed a claim.

## Sources

- Settles 2009: survey. Record only. Convention.
- Lewis 1994: uncertainty sampling. Record only.
- Cormack 2014: protocols compared. Abstract read. Measured.
- van de Schoot 2021: the tool. Abstract read. Measured by simulation.

## See also

[The map](README.md); [the bibliography](../evidence/bibliography.md); [snowballing](snowballing.md).
