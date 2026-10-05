import pytest

import pyisic
from pyisic import NAICS2012, NAICS2012_to_NAICS2017
from pyisic.types import Standards


def test_naics2012_codes_are_six_digits():
    """2012 NAICS has 1,065 six-digit U.S. industries."""
    assert len(NAICS2012) == 1065
    assert all(len(c) == 6 and c.isdigit() for c in NAICS2012)


@pytest.mark.parametrize(
    "code,description",
    [
        ("111110", "Soybean Farming"),
        ("541511", "Custom Computer Programming Services"),
        # codes that exist in 2012 NAICS but not in 2017 NAICS
        ("211111", "Crude Petroleum and Natural Gas Extraction"),
        ("211112", "Natural Gas Liquid Extraction"),
        # the Census concordance file has a typo in this title; the 2012 code list is used
        ("323120", "Support Activities for Printing"),
        # the concordance file appends " - <piece>" to the titles of split industries; the code list does not
        ("452112", "Discount Department Stores"),
    ],
)
def test_naics2012_codes(code: str, description: str):
    """Test NAICS2012 sample codes."""
    assert NAICS2012[code]["description"] == description


@pytest.mark.parametrize("code", ["54", "5415", "541511 ", "455110", "000000", "", "DOESNT EXIST"])
def test_naics2012_rejects_other_codes(code: str):
    """Only the 6-digit 2012 industries are codes (455110 is new in 2022)."""
    assert code not in NAICS2012


def test_naics2012_differs_from_other_revisions():
    only_2012 = set(NAICS2012) - set(pyisic.NAICS2017)
    only_2017 = set(pyisic.NAICS2017) - set(NAICS2012)
    assert (len(only_2012), len(only_2017), len(set(NAICS2012) & set(pyisic.NAICS2017))) == (28, 20, 1037)
    assert "211111" in only_2012 and "211111" not in pyisic.NAICS2022


def test_naics2012_descriptions_are_clean():
    assert all(v["description"] and v["description"] == " ".join(v["description"].split()) for v in NAICS2012.values())


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        # unchanged industries map to themselves
        ("541511", {(Standards.NAICS2017, "541511")}),
        # industries split or combined by 2017
        ("211111", {(Standards.NAICS2017, "211120"), (Standards.NAICS2017, "211130")}),
        ("211112", {(Standards.NAICS2017, "211130")}),
        ("452112", {(Standards.NAICS2017, "452210"), (Standards.NAICS2017, "452311")}),
    ],
)
def test_naics2012_to_naics2017_concordance(code: str, expected: set):
    """Test NAICS2012 to NAICS2017 sample concordances."""
    assert NAICS2012_to_NAICS2017.concordant(code) == expected


def test_naics2012_to_naics2017_coverage():
    """Every 2012 industry maps to at least one 2017 industry and every 2017 industry is mapped to."""
    assert [c for c in NAICS2012 if not NAICS2012_to_NAICS2017.concordant(c)] == []
    targets = {dst for _, (_, dst) in NAICS2012_to_NAICS2017.edges}
    assert sorted(set(pyisic.NAICS2017) - targets) == []


def test_naics2012_to_isic4():
    """NAICS2012 codes convert to ISIC4 through NAICS2017."""
    assert list(pyisic.ToISIC4("541511", Standards.NAICS2012)) == [(Standards.ISIC4, "6201")]
    assert {c for _, c in pyisic.ToISIC4("211112", Standards.NAICS2012)} == {
        c for _, c in pyisic.ToISIC4("211130", Standards.NAICS2017)
    }
