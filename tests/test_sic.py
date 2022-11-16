# -*- coding: utf-8 -*-
import pytest

from pyisic import SIC_to_NAICS2017
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("1044", {(Standards.NAICS2017, "212222")}),
        ("2048", {(Standards.NAICS2017, "311119"), (Standards.NAICS2017, "311611")}),
    ],
)
def test_nace2_to_isic4_concordance(code: str, expected: set):
    """Test NACE2 to ISIC4 sample concordances."""
    assert SIC_to_NAICS2017.concordant(code) == expected
