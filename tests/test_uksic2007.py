import pytest

import pyisic
from pyisic import UKSIC2007, UKSIC2007_to_NACE2
from pyisic.types import Category, Standards


@pytest.mark.parametrize(
    "code,description,category",
    [
        ("A", "AGRICULTURE, FORESTRY AND FISHING", Category.SECTION),
        ("95", "Repair of computers and personal and household goods", Category.DIVISION),
        ("9511", "Repair of computers and peripheral equipment", Category.CLASS),
        ("95110", "Repair of computers and peripheral equipment", Category.SUBCLASS),
        (
            "01629",
            "Support activities for animal production (other than farm animal boarding and care) n.e.c.",
            Category.SUBCLASS,
        ),
        # Companies House specific codes
        ("74990", "Non-trading company", Category.SUBCLASS),
        ("99999", "Dormant Company", Category.SUBCLASS),
    ],
)
def test_uksic2007_codes(code: str, description: str, category: Category):
    """Test UKSIC2007 sample codes."""
    assert UKSIC2007[code]["description"] == description
    assert UKSIC2007[code]["category"] == category


@pytest.mark.parametrize("code", ["9511.0", "95.11", "95.110", "1623 1629", "899900", "", "DOESNT EXIST"])
def test_uksic2007_rejects_other_formats(code: str):
    """Dotted, padded and multi-code strings are not UKSIC2007 codes."""
    assert code not in UKSIC2007


def test_uksic2007_hierarchy_matches_nace2():
    """Sections to classes are NACE Rev. 2 with the dots removed."""
    hierarchy = {c: v for c, v in UKSIC2007.items() if v["category"] != Category.SUBCLASS}
    assert len(hierarchy) == len(pyisic.NACE2)
    for code, nace2 in pyisic.NACE2.items():
        assert hierarchy[code.replace(".", "")]["category"] == nace2["category"]
        assert hierarchy[code.replace(".", "")]["description"] == nace2["description"].strip()


def test_uksic2007_every_nace2_class_has_a_subclass():
    """Every NACE Rev. 2 class has at least one 5-digit UK subclass."""
    subclass_classes = {c[:4] for c, v in UKSIC2007.items() if v["category"] == Category.SUBCLASS}
    classes = {c.replace(".", "") for c, v in pyisic.NACE2.items() if v["category"] == Category.CLASS}
    assert sorted(classes - subclass_classes) == []


def test_uksic2007_subclasses_without_nace2_class():
    """Only the Companies House specific codes are not under a NACE Rev. 2 class."""
    subclasses = [c for c, v in UKSIC2007.items() if v["category"] == Category.SUBCLASS]
    assert sorted(c for c in subclasses if f"{c[:2]}.{c[2:4]}" not in pyisic.NACE2) == ["74990", "98000", "99999"]


def test_uksic2007_descriptions_are_clean():
    assert all(v["description"] and v["description"] == v["description"].strip() for v in UKSIC2007.values())


def test_uksic2007_subclasses():
    """The 5-digit subclasses are the 731 codes on the Companies House condensed list."""
    subclasses = [c for c, v in UKSIC2007.items() if v["category"] == Category.SUBCLASS]
    assert len(subclasses) == 731
    assert all(len(c) == 5 and c.isdigit() for c in subclasses)


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("A", {(Standards.NACE2, "A")}),
        ("9511", {(Standards.NACE2, "95.11")}),
        ("95110", {(Standards.NACE2, "95.11")}),
        ("43999", {(Standards.NACE2, "43.99")}),
        # no NACE2 equivalent
        ("74990", set()),
        ("98000", set()),
        ("99999", set()),
    ],
)
def test_uksic2007_to_nace2_concordance(code: str, expected: set):
    """Test UKSIC2007 to NACE2 sample concordances."""
    assert UKSIC2007_to_NACE2.concordant(code) == expected


def test_uksic2007_to_isic4():
    """UKSIC2007 codes convert to ISIC4 through NACE2."""
    assert list(pyisic.ToISIC4("95110", Standards.UKSIC2007)) == [(Standards.ISIC4, "9511")]
