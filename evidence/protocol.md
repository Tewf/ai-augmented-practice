# Protocol: how the twelve rows were found

A first pass. It says how sources were chosen and read, and what was not searched. Reading is by abstract or record; no full text was read.

## Steps

1. **Frame:** the maintainer's twelve practices, each with a lead for its problem class, were renamed from surveys and seminal papers ([frame](frame.md)).
2. **Review:** for each row, the survey or seminal paper of the problem class, then the paper behind the best-known algorithm, then its implementation.
3. **Implementations:** each looked up under the authors' names, and verified on 2026-11-03 from the public repository (licence, size, date of last push). A repository counts only if it implements that algorithm.
4. **People against algorithms:** one meta-analysis and one account of expert intuition, to set the rows against.

## Pool

- 40 sources; 2 to 4 for each row, and five that cut across rows.
- Stopping rule: the rule was set by size, a pool of at most 40 and 2 to 4 sources a row, not by saturation.
- Metadata and abstracts were read from the publishers' records, OpenAlex, Crossref and arXiv, with no account and no email sent.
- Search strings and hit counts were not logged in this pass.

## Grades and reading

- A work read by abstract or record is marked so in the bibliography. A number is quoted only from an abstract, and the page says so.
- Grey sources are kept apart as Garousi 2019 advises, but none is scored in this pass. The only one is BoTorch 2026, the owner's account of its own library. It confirms that an implementation exists and supports no claim of effect.
- Computed figures (the power table of runs per arm) are marked as computed on their page.

## What was not searched

- Full texts, forward citations of the seminal papers, and grey literature beyond library documentation.
- Non-English sources, and preprint servers other than arXiv.
- Whether a person with judgment beats the algorithm on each row. Only the general literature was read.
- Other algorithms for rows with several (a ranking by citations for snowballing, other stopping rules): named in the page, not compared.

## Limits

- One reviewer and no second rater.
- A row's best-known algorithm is the one the review found most cited or most implemented, not a ranking by benchmark.
- Claims about the maintainer's practice are the maintainer's own, written down for this review.

## See also

[The evidence](README.md); [the frame](frame.md); [the bibliography](bibliography.md).
