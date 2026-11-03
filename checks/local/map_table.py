"""Map table: every row of the map names a practice page, a problem, an algorithm with a source key, a repository and a change.

`[map_table]` in checks/config.toml gives the table's file (default map/README.md), the bibliography (default
evidence/bibliography.md), the columns in order, the vocabulary of the Fit column and the fewest rows. A run with no
error guarantees, for every row: no empty cell; the Practice cell links a page of the map that exists; every source key
in the Source cell is a key of the bibliography and appears in that page; the Reference implementation cell holds a
GitHub link; the Fit cell is one word of the vocabulary; no practice is listed twice; every page of the map
is in the table; there are at least `min_rows` rows.
It does not decide that the algorithm is the best known for the problem, that the repository still runs, or that the
change is a good one: those are the review and the maintainer's.
Time O(size of the table and its pages).
"""
from __future__ import annotations

import re
from pathlib import Path

from framework.check_api import Finding

NAME = "map-table"
EXACT = True
DEFAULTS = {
    "table": "map/README.md",
    "bibliography": "evidence/bibliography.md",
    "columns": ["Practice", "Problem class", "Algorithm", "Source", "Reference implementation", "Change", "Fit"],
    "fit": ["algorithm", "partly", "habit"],
    "min_rows": 12,
}
KEY = re.compile(r"(?:(?:van|de|von|der|den) )*[A-Z][A-Za-z'\u00c0-\u024f-]*(?: [a-z]+)* \d{4}[a-z]?")
LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
GITHUB = re.compile(r"^https://github\.com/[\w.-]+/[\w.-]+/?$")
PLACEHOLDER = {"", "-", "?", "tbd", "todo", "none", "n/a"}


def cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def table_rows(text: str) -> tuple[list[str] | None, list[tuple[int, list[str]]]]:
    """The header cells and the (line number, cells) of each body row of the first table."""
    header, rows = None, []
    for number, line in enumerate(text.splitlines(), start=1):
        if not line.startswith("|"):
            if header is not None:
                break
            continue
        if header is None:
            header = cells(line)
        elif not re.fullmatch(r"\|[\s:|-]+\|", line.strip()):
            rows.append((number, cells(line)))
    return header, rows


def bibliography_keys(text: str) -> set[str]:
    return {m.group(1).strip() for line in text.splitlines() if (m := re.match(r"\|\s*([^|]+?)\s*\|", line))}


def check(root: Path, config: dict) -> list[Finding]:
    settings = {**DEFAULTS, **config.get("map_table", {})}
    table = settings["table"]
    path = root / table
    if not path.is_file():
        return [Finding(NAME, table, 0, "the map table file does not exist")]
    folder = path.parent
    findings: list[Finding] = []
    header, rows = table_rows(path.read_text(encoding="utf-8"))
    columns = settings["columns"]
    if header != columns:
        return [Finding(NAME, table, 1, f"the columns are {header}, expected {columns}")]
    bib_path = root / settings["bibliography"]
    keys = bibliography_keys(bib_path.read_text(encoding="utf-8")) if bib_path.is_file() else set()
    if not keys:
        findings.append(Finding(NAME, settings["bibliography"], 0, "no bibliography keys found"))
    if len(rows) < settings["min_rows"]:
        findings.append(Finding(NAME, table, 0, f"{len(rows)} rows, at least {settings['min_rows']} expected"))
    seen: dict[str, int] = {}
    linked: set[str] = set()
    for number, row in rows:
        if len(row) != len(columns):
            findings.append(Finding(NAME, table, number, f"{len(row)} cells, expected {len(columns)}"))
            continue
        cell = dict(zip(columns, row))
        for name, value in cell.items():
            if value.strip().lower() in PLACEHOLDER:
                findings.append(Finding(NAME, table, number, f"the cell '{name}' is empty"))
        practice = LINK.search(cell["Practice"])
        page_text = ""
        if not practice:
            findings.append(Finding(NAME, table, number, "the Practice cell links no page"))
        else:
            target = (folder / practice.group(2)).resolve()
            linked.add(target.name)
            if not target.is_file():
                findings.append(Finding(NAME, table, number, f"the page '{practice.group(2)}' does not exist"))
            else:
                page_text = target.read_text(encoding="utf-8")
            name = practice.group(1).lower()
            if name in seen:
                findings.append(Finding(NAME, table, number, f"'{practice.group(1)}' is already listed on line {seen[name]}"))
            seen.setdefault(name, number)
        found = KEY.findall(cell["Source"])
        if not found:
            findings.append(Finding(NAME, table, number, "the Source cell holds no key of the form 'Author 2020'"))
        for key in found:
            if key not in keys:
                findings.append(Finding(NAME, table, number, f"the key '{key}' is not in the bibliography"))
            elif page_text and key not in page_text:
                findings.append(Finding(NAME, table, number, f"the key '{key}' is not cited in the row's page"))
        urls = [url for _, url in LINK.findall(cell["Reference implementation"])]
        if not any(GITHUB.match(url) for url in urls):
            findings.append(Finding(NAME, table, number, "the Reference implementation cell holds no link to a GitHub repository"))
        if cell["Fit"] not in settings["fit"]:
            findings.append(Finding(NAME, table, number, f"the Fit '{cell['Fit']}' is not one of {settings['fit']}"))
    for page in sorted(folder.glob("*.md")):
        if page.name != Path(table).name and page.name not in linked:
            findings.append(Finding(NAME, str(page.relative_to(root)), 0, "the page is not in the map table"))
    return findings
