import pytest

import pyisic
from pyisic import NAICS2022, NAICS2022_to_NAICS2017
from pyisic.types import Standards


def test_naics2022_codes_are_six_digits():
    """2022 NAICS has 1,012 six-digit U.S. industries."""
    assert len(NAICS2022) == 1012
    assert all(len(c) == 6 and c.isdigit() for c in NAICS2022)


@pytest.mark.parametrize(
    "code,description",
    [
        ("111110", "Soybean Farming"),
        ("236220", "Commercial and Institutional Building Construction"),
        # codes that exist in 2022 NAICS but not in 2017 NAICS
        ("455110", "Department Stores"),
        ("212114", "Surface Coal Mining"),
        # the Census concordance file has a typo in this title; the structure file is used
        ("323120", "Support Activities for Printing"),
        ("531120", "Lessors of Nonresidential Buildings (except Miniwarehouses)"),
    ],
)
def test_naics2022_codes(code: str, description: str):
    """Test NAICS2022 sample codes."""
    assert NAICS2022[code]["description"] == description


@pytest.mark.parametrize("code", ["54", "5415", "54151", "541511 ", "211111", "000000", "", "DOESNT EXIST"])
def test_naics2022_rejects_other_codes(code: str):
    """Only the 6-digit 2022 industries are codes (211111 was retired in 2022)."""
    assert code not in NAICS2022


def test_naics2022_differs_from_naics2017():
    only_2022 = set(NAICS2022) - set(pyisic.NAICS2017)
    only_2017 = set(pyisic.NAICS2017) - set(NAICS2022)
    assert (len(only_2022), len(only_2017), len(set(NAICS2022) & set(pyisic.NAICS2017))) == (94, 139, 918)


def test_naics2022_descriptions_are_clean():
    assert all(v["description"] and v["description"] == " ".join(v["description"].split()) for v in NAICS2022.values())


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        # unchanged industries map to themselves
        ("236220", {(Standards.NAICS2017, "236220")}),
        ("541511", {(Standards.NAICS2017, "541511")}),
        # industries combined from, or split out of, 2017 industries
        ("455110", {(Standards.NAICS2017, "452210"), (Standards.NAICS2017, "454110")}),
        ("519290", {(Standards.NAICS2017, "519130"), (Standards.NAICS2017, "519190")}),
    ],
)
def test_naics2022_to_naics2017_concordance(code: str, expected: set):
    """Test NAICS2022 to NAICS2017 sample concordances."""
    assert NAICS2022_to_NAICS2017.concordant(code) == expected


def test_naics2022_to_naics2017_coverage():
    """Every 2022 industry maps to at least one 2017 industry and every 2017 industry is mapped to."""
    assert [c for c in NAICS2022 if not NAICS2022_to_NAICS2017.concordant(c)] == []
    targets = {dst for _, (_, dst) in NAICS2022_to_NAICS2017.edges}
    assert sorted(set(pyisic.NAICS2017) - targets) == []


def test_naics2022_to_isic4():
    """NAICS2022 codes convert to ISIC4 through NAICS2017."""
    assert list(pyisic.ToISIC4("541511", Standards.NAICS2022)) == [(Standards.ISIC4, "6201")]
    assert {c for _, c in pyisic.ToISIC4("455110", Standards.NAICS2022)} == {"4719", "4791"}
