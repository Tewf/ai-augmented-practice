# Snowballing as a traversal of the citation graph

The maintainer follows the citations of the seminal paper forward and backward by hand. The field gives written guidelines for it, a tool that does it from a set of articles, and a ranking-driven crawler as the general form.

Follows the [topic shape](https://github.com/Tewf/reader-ergonomics-topic/blob/86e14fe9a1a9877d6a87a2f8b4e8713f98724b5a/shapes/topic.md).

## The practice

The maintainer's practice, written down for this review.

- A survey and a seminal paper are read first.
- Citations are followed backward from them and forward from their citers.
- A paper joins the pool when its abstract fits the question.
- No count of papers per round is kept.

## The problem class

- The field's name in review methods: **snowballing** or **citation chasing** (Wohlin 2014; Haddaway 2022).
- In computer science the general form is **focused crawling**: visit a graph guided by a relevance score (Chakrabarti 1999).
- Grade: the guidelines are a convention, tested by a replication in one field; the crawler is measured on web pages.

## The best-known algorithm

- Guidelines: Wohlin 2014 sets the procedure: iterate backward and forward until no new paper is included (secondary: read from the title and the field's use, not the full text).
- Tool: citationchaser (Haddaway 2022), an R package and web app for forward and backward chasing from a set of articles. Read on 2026-11-03: 163 stars, last push 2025-03-21, no licence declared.
- General algorithm: a best-first traversal with a classifier on the text, as Chakrabarti 1999 does for web pages.

## The gap

- The stopping point matches Wohlin's: stop when a round adds nothing. The practice is the guideline.
- What is missing: a record per round, and a ranking of candidates so the strongest are read first.
- Where people beat algorithms: the maintainer reads the abstract and judges fit better than a score does.
- Kind: algorithm, with human judgment on inclusion.

## The change proposed

- Log each round: papers found, papers included.
- Rank the candidates by overlap with the included set before reading; compare the order with what was included.
- A pass is a ranking that puts included papers in the first half of the candidates.

## Sources

- Wohlin 2014: guidelines and a replication. Abstract read in part. Convention.
- Haddaway 2022: the tool. Abstract read. Software description.
- Chakrabarti 1999: focused crawling. Record only. Measured on web data.

## See also

[The map](README.md); [the bibliography](../evidence/bibliography.md); [deep reading](deep-reading.md).
