import pytest

import pyisic
from pyisic import ISIC4, ISIC5, ISIC4_to_ISIC5, ISIC5_to_ISIC4
from pyisic.types import Category, Standards


def classes(standard):
    return {c for c, v in standard.items() if v["category"] == Category.CLASS}


def test_isic5_level_counts():
    """ISIC Rev. 5 has 22 sections, 87 divisions, 258 groups and 463 classes."""
    counts = {cat: sum(v["category"] == cat for v in ISIC5.values()) for cat in Category}
    assert counts == {
        Category.SECTION: 22,
        Category.DIVISION: 87,
        Category.GROUP: 258,
        Category.CLASS: 463,
        Category.SUBCLASS: 0,
    }


@pytest.mark.parametrize(
    "code,description,category",
    [
        ("A", "Agriculture, forestry and fishing", Category.SECTION),
        ("01", "Crop and animal production, hunting and related service activities", Category.DIVISION),
        ("011", "Growing of non-perennial crops", Category.GROUP),
        ("0111", "Growing of cereals (except rice), leguminous crops and oil seeds", Category.CLASS),
        # ISIC Rev. 5 added a section: Other service activities moved from S to T, households to U, extraterritorial to V
        ("T", "Other service activities", Category.SECTION),
        ("V", "Activities of extraterritorial organizations and bodies", Category.SECTION),
        # classes that exist in ISIC Rev. 5 but not in ISIC Rev. 4
        ("4790", "Intermediation service activities for retail sale", Category.CLASS),
        (
            "8240",
            "Intermediation service activities for business support activities n.e.c., except financial intermediation",
            Category.CLASS,
        ),
        ("9900", "Activities of extraterritorial organizations and bodies", Category.CLASS),
    ],
)
def test_isic5_codes(code: str, description: str, category: Category):
    """Test ISIC5 sample codes."""
    assert ISIC5[code]["description"] == description
    assert ISIC5[code]["category"] == category


@pytest.mark.parametrize("code", ["A0111", "A01", "01.11", "01 11", "011 ", "9999", "99000", "", "DOESNT EXIST"])
def test_isic5_rejects_other_formats(code: str):
    """Codes are the plain UNSD format; the section-prefixed form of the workbook is not a code."""
    assert code not in ISIC5


def test_isic5_is_not_isic4():
    """ISIC Rev. 5 renumbers, splits and merges ISIC Rev. 4 classes, so the revisions are different standards."""
    shared, only_4, only_5 = (
        classes(ISIC4) & classes(ISIC5),
        classes(ISIC4) - classes(ISIC5),
        classes(ISIC5) - classes(ISIC4),
    )
    assert (len(shared), len(only_4), len(only_5)) == (366, 53, 97)
    assert {"4791", "4799", "2610"} <= only_4 and {"4790", "6039", "2611"} <= only_5 and "0111" in shared


def test_isic5_descriptions_are_clean():
    assert all(v["description"] and v["description"] == v["description"].strip() for v in ISIC5.values())
    assert all(v["description"] == " ".join(v["description"].split()) for v in ISIC5.values())


def test_isic5_hierarchy():
    """Every group and class sits under the code prefix; the 87 divisions are the same as in the NACE Rev. 2.1 divisions."""
    assert all(c[:-1] in ISIC5 for c, v in ISIC5.items() if v["category"] in (Category.GROUP, Category.CLASS))
    divisions = {c for c, v in ISIC5.items() if v["category"] == Category.DIVISION}
    assert divisions == {c for c, v in pyisic.NACE21.items() if v["category"] == Category.DIVISION}
    assert {c for c, v in ISIC5.items() if v["category"] == Category.SECTION} == {
        c for c, v in pyisic.NACE21.items() if v["category"] == Category.SECTION
    }


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        # a class that did not change
        ("0111", {(Standards.ISIC5, "0111")}),
        ("9900", {(Standards.ISIC5, "9900")}),
        # renumbered or split classes
        ("6201", {(Standards.ISIC5, "6211"), (Standards.ISIC5, "6219")}),
        ("6202", {(Standards.ISIC5, "6220")}),
        ("6820", {(Standards.ISIC5, "6821"), (Standards.ISIC5, "6829")}),
        # added in the 17 January 2025 version of the UNSD table
        ("4100", {(Standards.ISIC5, "4100"), (Standards.ISIC5, "6810")}),
        ("4773", {(Standards.ISIC5, "4769"), (Standards.ISIC5, "4773"), (Standards.ISIC5, "4790")}),
        # retail via the internet is broken down by product in ISIC Rev. 5
        (
            "4791",
            {
                (Standards.ISIC5, c)
                for c in "4711 4719 4721 4722 4723 4740 4751 4752 4753 4759 4761 4762 4763 4769 4771 4772 4774 4790 6039".split()
            },
        ),
    ],
)
def test_isic4_to_isic5(code, expected):
    """Test ISIC4 to ISIC5 sample concordances."""
    assert ISIC4_to_ISIC5.concordant(code) == expected


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("0111", {(Standards.ISIC4, "0111")}),
        ("6211", {(Standards.ISIC4, "6201")}),
        ("6810", {(Standards.ISIC4, "4100"), (Standards.ISIC4, "6810")}),
        ("8240", {(Standards.ISIC4, "7990"), (Standards.ISIC4, "8230"), (Standards.ISIC4, "8299")}),
        ("6039", {(Standards.ISIC4, "4791"), (Standards.ISIC4, "6312")}),
    ],
)
def test_isic5_to_isic4(code, expected):
    """Test ISIC5 to ISIC4 sample concordances."""
    assert ISIC5_to_ISIC4.concordant(code) == expected


def test_isic_concordances_cover_every_class():
    """The UNSD table maps every ISIC Rev. 4 class to ISIC Rev. 5 classes, and the reverse."""
    assert len(ISIC4_to_ISIC5.edges) == len(ISIC5_to_ISIC4.edges) == 605
    assert [c for c in classes(ISIC4) if not ISIC4_to_ISIC5.concordant(c)] == []
    assert [c for c in classes(ISIC5) if not ISIC5_to_ISIC4.concordant(c)] == []
    targets = {dst for _, (_, dst) in ISIC4_to_ISIC5.edges}
    assert sorted(classes(ISIC5) - targets) == []
    targets = {dst for _, (_, dst) in ISIC5_to_ISIC4.edges}
    assert sorted(classes(ISIC4) - targets) == []


def test_isic_concordances_are_the_same_pairs():
    forward = {(a, b) for (_, a), (_, b) in ISIC4_to_ISIC5.edges}
    backward = {(b, a) for (_, a), (_, b) in ISIC5_to_ISIC4.edges}
    assert forward == backward


def test_isic_concordances_are_class_level():
    """The UNSD table only has four-digit classes, so higher levels have no concordance."""
    assert all(ISIC4[c]["category"] == Category.CLASS for (_, c), _ in ISIC4_to_ISIC5.edges)
    assert all(ISIC5[c]["category"] == Category.CLASS for (_, c), _ in ISIC5_to_ISIC4.edges)
    assert not ISIC4_to_ISIC5.concordant("01") and not ISIC5_to_ISIC4.concordant("A")


def test_isic5_to_isic4_in_toisic4():
    """ISIC5 codes convert to ISIC4, and the reverse concordance is kept out of ToISIC4 so ISIC4 codes do not loop back."""
    assert {c for _, c in pyisic.ToISIC4("6211", Standards.ISIC5)} == {"6201"}
    assert pyisic.ToISIC4("6201", Standards.ISIC4) == set()
    assert not any(e in pyisic.ToISIC4.edges for e in ISIC4_to_ISIC5.edges)


def test_isic4_to_isic5_in_toisic5():
    """Everything that converts to ISIC4 converts on to ISIC5, and ISIC5 codes are not echoed back."""
    assert all(e in pyisic.ToISIC5.edges for e in ISIC4_to_ISIC5.edges)
    assert not any(e in pyisic.ToISIC5.edges for e in ISIC5_to_ISIC4.edges)
    assert {c for _, c in pyisic.ToISIC5("6201", Standards.ISIC4)} == {"6211", "6219"}
    assert {c for _, c in pyisic.ToISIC5("62.01", Standards.NACE2)} == {"6211", "6219"}
    assert {c for _, c in pyisic.ToISIC5("62.10", Standards.NACE21)} == {"6211", "6219"}
    assert {c for _, c in pyisic.ToISIC5("541511", Standards.NAICS2017)} == {
        c for _, c in pyisic.ToISIC5("6201", Standards.ISIC4)
    }
    assert pyisic.ToISIC5("6211", Standards.ISIC5) == set()
