# -*- coding: utf-8 -*-
import pytest

from pyisic import SKD2002_to_NACE2, SKD2002_to_SKD2008
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        (
            "01.110",
            {
                (Standards.NACE2, "01.11"),
                (Standards.NACE2, "01.12"),
                (Standards.NACE2, "01.13"),
                (Standards.NACE2, "01.14"),
                (Standards.NACE2, "01.15"),
                (Standards.NACE2, "01.16"),
                (Standards.NACE2, "01.19"),
                (Standards.NACE2, "01.28"),
                (Standards.NACE2, "01.63"),
                (Standards.NACE2, "01.64"),
            },
        ),
        (
            "11.100",
            {
                (Standards.NACE2, "06.10"),
                (Standards.NACE2, "06.20"),
                (Standards.NACE2, "09.10"),
            },
        ),
        ("28.520", {(Standards.NACE2, "25.62"), (Standards.NACE2, "33.12")}),
    ],
)
def test_skd2002_to_naics2017_concordance(code: str, expected: set):
    """Test SKD2002 to NAICS2017 sample concordances."""
    assert SKD2002_to_NACE2.concordant(code) == expected


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        (
            "01.131",
            {
                (Standards.SKD2008, "11.020"),
                (Standards.SKD2008, "01.210"),
            },
        ),
        (
            "93.050",
            {
                (Standards.SKD2008, "96.090"),
                (Standards.SKD2008, "85.510"),
                (Standards.SKD2008, "88.910"),
            },
        ),
    ],
)
def test_skd2002_to_skd2008_concordance(code: str, expected: set):
    """Test SKD2002 to SKD2008 sample concordances."""
    assert SKD2002_to_SKD2008.concordant(code) == expected
