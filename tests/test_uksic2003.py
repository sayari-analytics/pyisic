import pytest

import pyisic
from pyisic import UKSIC2003, UKSIC2003_to_NACE1
from pyisic.types import Category, Standards


@pytest.mark.parametrize(
    "code,description",
    [
        ("7487", "Other business activities"),
        ("7222", "Other software consultancy and supply"),
        ("4521", "General construction & civil engineer"),
        ("7499", "Non-trading company"),
        ("9999", "Dormant company"),
    ],
)
def test_uksic2003_codes(code: str, description: str):
    """Test UKSIC2003 sample codes."""
    assert UKSIC2003[code]["description"] == description
    assert UKSIC2003[code]["category"] == Category.CLASS


@pytest.mark.parametrize("code", ["74.87", "74879", "89990", "99999", "", "DOESNT EXIST"])
def test_uksic2003_rejects_other_formats(code: str):
    """Only the 4-digit codes are UKSIC2003 codes."""
    assert code not in UKSIC2003


def test_uksic2003_codes_are_four_digits():
    assert len(UKSIC2003) == 534
    assert all(len(c) == 4 and c.isdigit() for c in UKSIC2003)


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        # NACE1 class
        ("7487", {(Standards.NACE1, "74.87")}),
        ("0111", {(Standards.NACE1, "01.11")}),
        # NACE1 group or division when the class is not listed
        ("1010", {(Standards.NACE1, "10.1")}),
        ("1600", {(Standards.NACE1, "16")}),
        # no NACE1 equivalent
        ("7499", set()),
        ("9999", set()),
    ],
)
def test_uksic2003_to_nace1_concordance(code: str, expected: set):
    """Test UKSIC2003 to NACE1 sample concordances."""
    assert UKSIC2003_to_NACE1.concordant(code) == expected


def test_uksic2003_to_nace1_coverage():
    """The partial coverage stated in the module docstrings: 517 of 534 codes map, 17 do not."""
    mapped = {src: dst for (_, src), (_, dst) in UKSIC2003_to_NACE1.edges if src in UKSIC2003}
    levels = {"class": 0, "group": 0, "division": 0}
    for dst in mapped.values():
        levels[{5: "class", 4: "group", 2: "division"}[len(dst)]] += 1
    assert levels == {"class": 399, "group": 110, "division": 8}
    unmapped = ["2735", "4010", "4020", "5161", "5162", "5163", "5164", "5165", "5166"]
    unmapped += ["5170", "7220", "7483", "7484", "7499", "9000", "9800", "9999"]
    assert sorted(set(UKSIC2003) - set(mapped)) == unmapped


def test_uksic2003_to_isic4():
    """UKSIC2003 codes convert to ISIC4 through NACE1 and NACE2."""
    converted = set(pyisic.ToISIC4("7222", Standards.UKSIC2003))
    assert converted == {(Standards.ISIC4, "6201"), (Standards.ISIC4, "6202"), (Standards.ISIC4, "6209")}
