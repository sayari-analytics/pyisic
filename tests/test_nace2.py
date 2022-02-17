# -*- coding: utf-8 -*-
import pytest

from pyisic import NACE2_to_ISIC4, NACE2_to_NACEBEL2008
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("A", {(Standards.ISIC4, "A")}),
        ("01", {(Standards.ISIC4, "01")}),
        ("01.1", {(Standards.ISIC4, "011")}),
        ("01.11", {(Standards.ISIC4, "0111")}),
    ],
)
def test_nace2_to_isic4_concordance(code: str, expected: set):
    """Test NACE2 to ISIC4 sample concordances."""
    assert NACE2_to_ISIC4.concordant(code) == expected


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("01.11", {(Standards.NACEBEL2008, "01110")}),
        ("55.30", {(Standards.NACEBEL2008, "55300")}),
        ("99.00", {(Standards.NACEBEL2008, "99000")}),
    ],
)
def test_nace2_to_nacebel2008_concordance(code: str, expected: set):
    """Test NACE2 to NACEBEL2008 sample concordances."""
    assert NACE2_to_NACEBEL2008.concordant(code) == expected
