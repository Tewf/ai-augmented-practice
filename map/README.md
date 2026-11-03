# The map: twelve practices, each an algorithm for a named problem

One row per practice of the method, with the problem it solves in the field's name, the best-known algorithm and its source, the reference implementation, and the change proposed. A program checks the table; each row opens a page with the reasoning.

Follows the [topic shape](https://github.com/Tewf/reader-ergonomics-topic/blob/86e14fe9a1a9877d6a87a2f8b4e8713f98724b5a/shapes/topic.md).

## The table

The practice is the maintainer's, written down for this review. The Fit column answers one question: is the problem well posed enough to name an algorithm (**algorithm**), posed but without the data to run it (**partly**), or a habit no field has formalised (**habit**).

| Practice | Problem class | Algorithm | Source | Reference implementation | Change | Fit |
|---|---|---|---|---|---|---|
| [scope and review](scope-and-review.md) | sequential decision problem | knowledge gradient | Frazier 2008 | [BoTorch](https://github.com/meta-pytorch/botorch) | replay the policy on about thirty recorded choices | partly |
| [data gathering](data-gathering.md) | information foraging | marginal value rule and Thompson sampling | Russo 2018 | [SMPyBandits](https://github.com/SMPyBandits/SMPyBandits) | log the yield of every search string | algorithm |
| [stopping](stopping.md) | estimating what is still unseen | coverage estimation, Good-Turing and Chao | Chao 2012 | [iNEXT](https://github.com/AnneChao/iNEXT) | record concepts per source and compare the estimate with the stop | algorithm |
| [snowballing](snowballing.md) | traversal of a citation graph | citation chasing with a ranked frontier | Haddaway 2022 | [citationchaser](https://github.com/nealhaddaway/citationchaser) | log each round and rank candidates before reading | algorithm |
| [paywalled sources](paywalled-sources.md) | value of information | expected value of information | Jackson 2022 | [voi](https://github.com/chjackson/voi) | record the claim each unverifiable source was meant to carry | algorithm |
| [deep reading](deep-reading.md) | active learning | uncertainty sampling | van de Schoot 2021 | [ASReview](https://github.com/asreview/asreview) | run it on one finished review's candidates | algorithm |
| [runs per arm](runs-per-arm.md) | sequential testing and factorial design | confidence sequences | Howard 2021 | [confseq](https://github.com/gostevehoward/confseq) | state the smallest effect worth acting on, then set the runs | algorithm |
| [tiers](tiers.md) | multi-fidelity optimisation | Hyperband and the model cascade | Li 2018 | [Optuna](https://github.com/optuna/optuna) | log the tier tried and whether a program accepted it | algorithm |
| [batches](batches.md) | scheduling with precedence | list scheduling and the critical path | Graham 1966 | [OR-Tools](https://github.com/google/or-tools) | write each job's predecessors and compute the critical path | algorithm |
| [the budget cap](the-budget-cap.md) | allocation under a budget | cost-aware Bayesian optimisation | Lee 2020 | [BoTorch](https://github.com/meta-pytorch/botorch) | rank queued jobs by expected gain per cost | partly |
| [protocol before the run](protocol-before-the-run.md) | preregistration | registered report | Nosek 2018 | [OSF](https://github.com/CenterForOpenScience/osf.io) | add a deviations list and commit the protocol first | algorithm |
| [memory](memory.md) | transfer | memory tiers over a retrieve-reuse-revise-retain cycle | Packer 2023 | [Letta](https://github.com/letta-ai/letta) | log which notes were opened and used | habit |

## What a program reads

[map_table.py](../checks/local/map_table.py) fails on an empty cell, a page that does not exist, or a source key missing from the [bibliography](../evidence/bibliography.md) or from its page. It also fails on a reference implementation that is not a GitHub link, a Fit outside the three words, and a practice listed twice. A page missing from the table fails too, and so do fewer than twelve rows.

It cannot decide that an algorithm is the best known, that a repository still runs, or that a change is a good one. Those are the review's and the maintainer's.

## How the rows were found

- Each problem class began as a lead from the maintainer's list and was named again from surveys and seminal papers; [the protocol](../evidence/protocol.md) says how, and what was not searched.
- The reference implementations were looked up under the authors' names. Their licence, size and last push were read on 2026-11-03.
- Rows 2, 3 and 5 are held by [ai-augmented-data-gathering](https://github.com/Tewf/ai-augmented-data-gathering); the algorithm is linked, not copied.

## Contents

| Topic | Summary |
|---|---|
| [scope and review](scope-and-review.md) | the choice of the next step as a sequential decision |
| [data gathering](data-gathering.md) | where to look and when to leave a source |
| [stopping](stopping.md) | how much is still unseen when a review stops |
| [snowballing](snowballing.md) | following citations as a graph traversal |
| [paywalled sources](paywalled-sources.md) | when a costly source is worth opening |
| [deep reading](deep-reading.md) | which sources to read in full |
| [runs per arm](runs-per-arm.md) | how many runs separate two arms |
| [tiers](tiers.md) | cheap evaluators first, dear ones for what they must settle |
| [batches](batches.md) | jobs in waves, as scheduling with precedence |
| [the budget cap](the-budget-cap.md) | a ceiling as allocation under a budget |
| [protocol before the run](protocol-before-the-run.md) | a plan written first, as preregistration |
| [memory](memory.md) | notes kept across sessions, as transfer |

## See also

[The front page](../README.md); [the bibliography](../evidence/bibliography.md); [the protocol](../evidence/protocol.md).
