# -*- coding: utf-8 -*-
import pytest

from pyisic import ToISIC4, TSIC2552_to_ISIC3
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("01111", {(Standards.ISIC3, "0111")}),
        ("01139", {(Standards.ISIC3, "0111"), (Standards.ISIC3, "0112")}),
        ("27902", {(Standards.ISIC3, "3190"), (Standards.ISIC3, "3150")}),
    ],
)
def test_tsic2552_to_isic3_concordance(code: str, expected: set):
    """Test TSIC2552 to ISIC3 sample concordances."""
    assert TSIC2552_to_ISIC3.concordant(code) == expected


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("96103", {(Standards.ISIC4, "9602")}),
        ("99001", {(Standards.ISIC4, "9900")}),
    ],
)
def test_tsic2552_to_isic4_concordance(code: str, expected: set):
    """Test TSIC2552 to ISIC4 sample concordances."""
    assert ToISIC4(code, Standards.TSIC2552) == expected
