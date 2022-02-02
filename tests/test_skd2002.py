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
            "01.110",
            {
                (Standards.SKD2008, "01.110"),
                (Standards.SKD2008, "01.120"),
                (Standards.SKD2008, "01.130"),
                (Standards.SKD2008, "01.140"),
                (Standards.SKD2008, "01.150"),
                (Standards.SKD2008, "01.160"),
                (Standards.SKD2008, "01.190"),
                (Standards.SKD2008, "01.260"),
                (Standards.SKD2008, "01.280"),
                (Standards.SKD2008, "01.290"),
                (Standards.SKD2008, "01.630"),
                (Standards.SKD2008, "01.640"),
            },
        ),
        (
            "92.720",
            {
                (Standards.SKD2008, "01.620"),
                (Standards.SKD2008, "78.100"),
                (Standards.SKD2008, "79.900"),
                (Standards.SKD2008, "93.299"),
            },
        ),
    ],
)
def test_skd2002_to_skd2008_concordance(code: str, expected: set):
    """Test SKD2002 to SKD2008 sample concordances."""
    assert SKD2002_to_SKD2008.concordant(code) == expected
