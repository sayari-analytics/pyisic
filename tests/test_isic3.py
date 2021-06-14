# -*- coding: utf-8 -*-
import pytest

from pyisic import ISIC3_to_ISIC31, ToISIC4
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("0200", {(Standards.ISIC31, "0113"), (Standards.ISIC31, "0200")}),
        ("9500", {(Standards.ISIC31, "9500")}),
        ("6599", {(Standards.ISIC31, "6599")}),
    ],
)
def test_isic3_to_isic31_concordance(code: str, expected: set):
    """Test ISIC3 to ISIC31 sample concordances."""
    assert ISIC3_to_ISIC31.concordant(code) == expected


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("9500", {(Standards.ISIC4, "9700")}),
        ("9900", {(Standards.ISIC4, "9900")}),
        (
            "6599",
            {
                (Standards.ISIC4, "6420"),
                (Standards.ISIC4, "6430"),
                (Standards.ISIC4, "6499"),
                (Standards.ISIC4, "6619"),
                (Standards.ISIC4, "7740"),
                (Standards.ISIC4, "9499"),
            },
        ),
    ],
)
def test_isic3_to_isic4_concordance(code: str, expected: set):
    """Test ISIC3 to ISIC4 sample concordances."""
    assert ToISIC4(code, Standards.ISIC3) == expected
