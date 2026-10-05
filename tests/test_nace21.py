import pytest

import pyisic
from pyisic import NACE21, NACE21_to_NACE2
from pyisic.types import Category, Standards


def test_nace21_level_counts():
    """NACE Rev. 2.1 has 22 sections, 87 divisions, 287 groups and 651 classes."""
    counts = {cat: sum(v["category"] == cat for v in NACE21.values()) for cat in Category}
    assert counts == {
        Category.SECTION: 22,
        Category.DIVISION: 87,
        Category.GROUP: 287,
        Category.CLASS: 651,
        Category.SUBCLASS: 0,
    }


@pytest.mark.parametrize(
    "code,description,category",
    [
        ("A", "AGRICULTURE, FORESTRY AND FISHING", Category.SECTION),
        # the Eurostat vocabulary on Eionet is missing this section
        ("B", "MINING AND QUARRYING", Category.SECTION),
        ("01", "Crop and animal production, hunting and related service activities", Category.DIVISION),
        ("01.1", "Growing of non-perennial crops", Category.GROUP),
        ("01.11", "Growing of cereals, other than rice, leguminous crops and oil seeds", Category.CLASS),
        # classes that exist in NACE Rev. 2.1 but not in NACE Rev. 2
        ("41.00", "Construction of residential and non-residential buildings", Category.CLASS),
        ("46.89", "Other specialised wholesale n.e.c.", Category.CLASS),
        ("99.00", "Activities of extraterritorial organisations and bodies", Category.CLASS),
    ],
)
def test_nace21_codes(code: str, description: str, category: Category):
    """Test NACE21 sample codes."""
    assert NACE21[code]["description"] == description
    assert NACE21[code]["category"] == category


@pytest.mark.parametrize("code", ["A.01", "C.25.30", "4100", "41.000", "41.00 ", "41.10", "", "DOESNT EXIST"])
def test_nace21_rejects_other_formats(code: str):
    """Codes are the plain dotted format; the Eionet section prefix, undotted forms and retired classes are not codes."""
    assert code not in NACE21


def test_nace21_new_classes_are_not_all_in_nace2():
    """NACE Rev. 2.1 added classes (and renamed or merged others), so the revisions are different standards."""
    only_21 = [c for c, v in NACE21.items() if v["category"] == Category.CLASS and c not in pyisic.NACE2]
    assert len(only_21) == 146
    assert "41.00" in only_21 and "70.20" in only_21 and "01.11" not in only_21


def test_nace21_descriptions_are_clean():
    assert all(v["description"] and v["description"] == v["description"].strip() for v in NACE21.values())
    assert all(v["description"] == " ".join(v["description"].split()) for v in NACE21.values())


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        # some activities moved between sections
        ("A", {(Standards.NACE2, "A"), (Standards.NACE2, "C")}),
        ("B", {(Standards.NACE2, "B")}),
        ("01.11", {(Standards.NACE2, "01.11")}),
        # merged / renumbered classes
        ("41.00", {(Standards.NACE2, "41.20")}),
        ("70.20", {(Standards.NACE2, "70.22")}),
        ("62.10", {(Standards.NACE2, "62.01")}),
        # one NACE Rev. 2.1 class covering several NACE Rev. 2 classes
        (
            "47.12",
            {
                (Standards.NACE2, "47.19"),
                (Standards.NACE2, "47.82"),
                (Standards.NACE2, "47.89"),
                (Standards.NACE2, "47.91"),
                (Standards.NACE2, "47.99"),
            },
        ),
        # new class with no NACE Rev. 2 equivalent
        ("46.89", set()),
    ],
)
def test_nace21_to_nace2_concordance(code: str, expected: set):
    """Test NACE21 to NACE2 sample concordances."""
    assert NACE21_to_NACE2.concordant(code) == expected


def test_nace21_to_nace2_coverage():
    """Every NACE Rev. 2.1 code maps to NACE Rev. 2 except the new class 46.89, and every NACE Rev. 2 class is mapped to."""
    unmapped = [c for c in NACE21 if not NACE21_to_NACE2.concordant(c)]
    assert unmapped == ["46.89"]
    targets = {dst for _, (_, dst) in NACE21_to_NACE2.edges}
    assert not [c for c, v in pyisic.NACE2.items() if v["category"] == Category.CLASS and c not in targets]


def test_nace21_to_isic4():
    """NACE21 codes convert to ISIC4 through NACE2."""
    assert list(pyisic.ToISIC4("41.00", Standards.NACE21)) == [(Standards.ISIC4, "4100")]
    assert list(pyisic.ToISIC4("70.20", Standards.NACE21)) == [(Standards.ISIC4, "7020")]
    assert not pyisic.ToISIC4("46.89", Standards.NACE21)
