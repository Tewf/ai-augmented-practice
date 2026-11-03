# Batches as scheduling with precedence

The maintainer launches jobs in waves, several at once, each in its own folder. The field calls this scheduling with precedence constraints. The classical rules are old and have solvers with a maintained implementation.

Follows the [topic shape](https://github.com/Tewf/reader-ergonomics-topic/blob/86e14fe9a1a9877d6a87a2f8b4e8713f98724b5a/shapes/topic.md).

## The practice

The maintainer's practice, written down for this review.

- Jobs that do not depend on each other are launched together, in a wave.
- A job that needs another's output waits for the next wave.
- A lead reads each result before the next wave starts.
- A limit on how many run at once is set by the machine and the budget.

## The problem class

- The field's name: **scheduling with precedence constraints** on parallel machines (Graham 1966); with limited resources, the **resource-constrained project scheduling problem** (Hartmann 2010).
- The longest chain of dependent jobs is the **critical path** (Kelley 1959).
- Grade: proved. The problem is hard in general; simple rules have proved bounds.

## The best-known algorithm

- **List scheduling** (Graham 1966): whenever a machine is free, start any job whose predecessors are done. Its length is within a factor of 2 - 1/m of the best, for m machines (a known result; secondary, from the paper's title and its use).
- **Critical path method** (Kelley 1959): the longest chain bounds any schedule from below.
- Reference implementation: OR-Tools, whose CP-SAT solver handles job-shop and project scheduling. Read on 2026-11-03: Apache-2.0, 14322 stars, active.

## The gap

- Waves are list scheduling with a barrier: the next wave waits for every job of the last, though one job could start earlier.
- The barrier is a choice, since the lead reads each result. It trades idle time for review.
- The family's lower bound, the critical path, is not computed. The gap cannot be stated in hours.
- Kind: algorithm. The practice is a restricted form with a reason.

## The change proposed

- Write each job's predecessors in its brief.
- Compute the critical path and the number of waves it forces; compare with the waves used.
- A pass is a wave count equal to the critical path length, or a stated reason for each extra wave.

## Sources

- Graham 1966: bound for list scheduling. Record only. Proved.
- Kelley 1959: critical path. Record only. Convention in practice, exact as a method.
- Hartmann 2010: survey of resource limits. Record only.

## See also

[The map](README.md); [the bibliography](../evidence/bibliography.md); [tiers](tiers.md).
