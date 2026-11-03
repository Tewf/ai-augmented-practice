# Memory as transfer

The maintainer keeps notes that every later session reads, one fact per note, with an index. The field names the problem transfer, and the older form **case-based reasoning**. For language-model agents there are memory systems with code, and no measure of this practice.

Follows the [topic shape](https://github.com/Tewf/reader-ergonomics-topic/blob/86e14fe9a1a9877d6a87a2f8b4e8713f98724b5a/shapes/topic.md).

## The practice

The maintainer's practice, written down for this review.

- Notes live in one place read by every model the maintainer uses.
- A note holds one fact, in a fixed format, with an index line.
- The index is read at the start of a session; a note is opened when the task needs it.
- Notes are written after a decision or a failure.

## The problem class

- The field's name: **transfer**, using what was learned on one task for another. Its older, symbolic form is **case-based reasoning**: retrieve, reuse, revise, retain (Aamodt 1994).
- For language-model agents: memory management across a limited context (Packer 2023) and retrieval by recency, importance and relevance (Park 2023).
- Grade: convention. The sources describe designs; none measures a person's notes.

## The best-known algorithm

- Case-based reasoning cycle (Aamodt 1994): find the nearest past case, adapt its solution, store the result.
- Agent memory: MemGPT moves data between a fast and a slow memory tier (Packer 2023, abstract); Park 2023 adds a reflection step over retrieved memories (abstract read in part).
- Reference implementation: Letta, the successor of MemGPT. Read on 2026-11-03: 25337 stars, Apache-2.0, last push 2026-10-18.
- No implementation of case-based reasoning by its authors was found.

## The gap

- The practice has the retain step and an index. It has no measure of whether a note changed a later decision.
- Staleness is the known risk: an old note read as true. The family's project repository asks for a program to find stale text.
- Where people beat algorithms: the person decides what is worth writing down, which no retrieval rule decides.
- Kind: habit. A well-posed form exists in the field, and nobody has measured it for this use.

## The change proposed

- Log, per session, which notes were opened and whether the work used them.
- After a month, list notes never opened and notes opened and contradicted.
- A pass is a count of notes that changed a decision, from the log.

## Sources

- Aamodt 1994: case-based reasoning. Record only. Convention.
- Packer 2023: memory tiers. Abstract read. Measured by its authors on their tasks.
- Park 2023: retrieval and reflection. Abstract read in part.

## See also

[The map](README.md); [the bibliography](../evidence/bibliography.md); [scope and review](scope-and-review.md);
[the family's project repository](https://github.com/Tewf/ai-augmented-project).
