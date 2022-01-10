# -*- coding: utf-8 -*-
import pytest

from pyisic import SKD_to_NACE2
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
def test_skd_to_naics2017_concordance(code: str, expected: set):
    """Test SKD to NAICS2017 sample concordances."""
    assert SKD_to_NACE2.concordant(code) == expected
