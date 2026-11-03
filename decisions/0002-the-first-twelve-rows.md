# 0002: The map starts with the maintainer's twelve practices

**Decision:** The map's first twelve rows are the maintainer's twelve practices, one page each, with preregistration as the baseline and the repository's name kept.

**Status:** accepted, 2026-11-03. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/shapes/decision-record.md).

## Context

- The front page lists twelve practices with a lead for each problem class. The review had to name each class again from the field's own words.
- Rows 2, 3 and 5 are held by the data-gathering repository. A row without a page would leave the table with a hole.
- A review is finished when it can name its baseline ([protocol](../evidence/protocol.md)).
- The frame found no field that names the whole ([frame](../evidence/frame.md)).

## Decision

- Twelve rows, one page each, in the topic shape; the table is checked by [map_table.py](../checks/local/map_table.py) with unit tests.
- Rows held by data gathering get a page here that links that repository's algorithm and does not copy it.
- Each row carries a Fit: algorithm, partly, or habit. The words are fixed so a program can read them.
- The baseline is the row for protocol before the run: the practice is already the field's procedure, and the gap is the third-party timestamp and the list of deviations.
- The name stays. The nearest field name for the whole is sequential decision analytics.

## Consequences

- A reader sees at once which practices have an algorithm and which are habits: eleven are algorithm or partly, one is a habit.
- A later row is added to the table and gets a page; the check fails until both exist.
- **Bad:** the pool is a first pass from abstracts, so a Fit can change when a full text is read.
- **Bad:** the maintainer's practice is described by the maintainer, with no control and no measure; the change column is a claim until a case runs it.

## See also

[Decisions](README.md); [the map](../map/README.md); [record 0001](0001-a-repository-of-its-own.md).
