# -*- coding: utf-8 -*-
import pytest

from pyisic import JSIC13_to_ISIC4
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("A", set()),
        ("0100", {(Standards.ISIC4, "7010")}),
    ],
)
def test_jsic13_to_isic4_concordance(code: str, expected: set):
    """Test NAICS2017 to ISIC4 sample concordances."""
    assert JSIC13_to_ISIC4.concordant(code) == expected
