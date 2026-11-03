"""Tests of the map-table check in checks/local/: it fails where a row of the map is incomplete or unresolved and
stays silent where the table is whole.

Run: python3 -m unittest discover -s checks
The standard's checks/ folder must be importable: set READER_ERGONOMICS_CHECKS to it, or check
reader-ergonomics out beside this repository (as CI does, under the name standard).
"""
import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve()
REPOSITORY = HERE.parents[1]
CANDIDATES = [os.environ.get("READER_ERGONOMICS_CHECKS", ""),
              REPOSITORY.parent / "standard" / "checks", REPOSITORY / "checks" / "out" / "standard" / "checks",
              REPOSITORY.parent / "reader-ergonomics" / "checks"]
sys.path.insert(0, str(next(Path(c) for c in CANDIDATES if c and (Path(c) / "framework").is_dir())))

spec = importlib.util.spec_from_file_location("map_table", REPOSITORY / "checks" / "local" / "map_table.py")
map_table = importlib.util.module_from_spec(spec)
spec.loader.exec_module(map_table)

HEADER = ("| Practice | Problem class | Algorithm | Source | Reference implementation | Change | Fit |\n"
          "|---|---|---|---|---|---|---|\n")
BIBLIOGRAPHY = ("| Key | Citation | Link |\n|---|---|---|\n"
                "| Frazier 2008 | Frazier (2008). x | https://doi.org/x |\n"
                "| van de Schoot 2021 | van de Schoot (2021). y | https://doi.org/y |\n")
GOOD_ROWS = [
    "| [scope](scope.md) | sequential decision | knowledge gradient | Frazier 2008 | [BoTorch](https://github.com/meta-pytorch/botorch) | replay | partly |",
    "| [reading](reading.md) | active learning | uncertainty sampling | van de Schoot 2021 | [ASReview](https://github.com/asreview/asreview) | run it | algorithm |",
]
PAGES = {"scope.md": "# Scope\n\nFrazier 2008 gives it.\n", "reading.md": "# Reading\n\nvan de Schoot 2021 gives it.\n"}


def run(rows, pages=None, bibliography=BIBLIOGRAPHY, config=None, header=HEADER):
    """Build a repository in a temporary folder and return the messages of the check."""
    with tempfile.TemporaryDirectory() as folder:
        root = Path(folder)
        (root / "map").mkdir()
        (root / "evidence").mkdir()
        (root / "map" / "README.md").write_text("# Map\n\n" + header + "\n".join(rows) + "\n", encoding="utf-8")
        (root / "evidence" / "bibliography.md").write_text(bibliography, encoding="utf-8")
        for name, text in (PAGES if pages is None else pages).items():
            (root / "map" / name).write_text(text, encoding="utf-8")
        return [f.message for f in map_table.check(root, {"map_table": {"min_rows": 2, **(config or {})}})]


class MapTableTests(unittest.TestCase):
    def test_a_whole_table_passes(self):
        self.assertEqual(run(GOOD_ROWS), [])

    def test_an_empty_cell_fails(self):
        rows = [GOOD_ROWS[0].replace("replay", "  "), GOOD_ROWS[1]]
        self.assertTrue(any("'Change' is empty" in m for m in run(rows)))

    def test_a_placeholder_counts_as_empty(self):
        rows = [GOOD_ROWS[0].replace("knowledge gradient", "TBD"), GOOD_ROWS[1]]
        self.assertTrue(any("'Algorithm' is empty" in m for m in run(rows)))

    def test_a_missing_page_fails(self):
        self.assertTrue(any("does not exist" in m for m in run(GOOD_ROWS, pages={"scope.md": PAGES["scope.md"]})))

    def test_a_key_outside_the_bibliography_fails(self):
        rows = [GOOD_ROWS[0].replace("Frazier 2008", "Nobody 1999"), GOOD_ROWS[1]]
        self.assertTrue(any("'Nobody 1999' is not in the bibliography" in m for m in run(rows)))

    def test_a_key_not_cited_in_its_page_fails(self):
        pages = {**PAGES, "scope.md": "# Scope\n\nNothing cited.\n"}
        self.assertTrue(any("not cited in the row's page" in m for m in run(GOOD_ROWS, pages=pages)))

    def test_a_source_cell_without_a_key_fails(self):
        rows = [GOOD_ROWS[0].replace("Frazier 2008", "the literature"), GOOD_ROWS[1]]
        self.assertTrue(any("holds no key" in m for m in run(rows)))

    def test_a_repository_that_is_not_github_fails(self):
        rows = [GOOD_ROWS[0].replace("https://github.com/meta-pytorch/botorch", "https://example.org/botorch"), GOOD_ROWS[1]]
        self.assertTrue(any("GitHub repository" in m for m in run(rows)))

    def test_a_repository_given_as_text_fails(self):
        rows = [GOOD_ROWS[0].replace("[BoTorch](https://github.com/meta-pytorch/botorch)", "BoTorch"), GOOD_ROWS[1]]
        self.assertTrue(any("GitHub repository" in m for m in run(rows)))

    def test_a_fit_outside_the_vocabulary_fails(self):
        rows = [GOOD_ROWS[0].replace("partly", "mostly"), GOOD_ROWS[1]]
        self.assertTrue(any("'mostly' is not one of" in m for m in run(rows)))

    def test_a_practice_listed_twice_fails(self):
        self.assertTrue(any("already listed" in m for m in run([GOOD_ROWS[0], GOOD_ROWS[0], GOOD_ROWS[1]])))

    def test_a_page_missing_from_the_table_fails(self):
        pages = {**PAGES, "stray.md": "# Stray\n"}
        self.assertTrue(any("not in the map table" in m for m in run(GOOD_ROWS, pages=pages)))

    def test_too_few_rows_fail(self):
        self.assertTrue(any("1 rows, at least 2" in m for m in run(GOOD_ROWS[:1], pages={"scope.md": PAGES["scope.md"]})))

    def test_the_wrong_columns_fail(self):
        header = HEADER.replace("Change", "Idea")
        self.assertTrue(any("columns are" in m for m in run(GOOD_ROWS, header=header)))

    def test_a_row_with_a_missing_cell_fails(self):
        rows = [GOOD_ROWS[0].rsplit("|", 2)[0] + "|", GOOD_ROWS[1]]
        self.assertTrue(any("cells, expected 7" in m for m in run(rows)))

    def test_a_missing_table_fails(self):
        with tempfile.TemporaryDirectory() as folder:
            findings = map_table.check(Path(folder), {})
        self.assertEqual([f.message for f in findings], ["the map table file does not exist"])


if __name__ == "__main__":
    unittest.main()
