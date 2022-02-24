# -*- coding: utf-8 -*-
import pytest

from pyisic import NAF2_to_NACE2
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("A", {(Standards.NACE2, "A")}),
        ("01", {(Standards.NACE2, "01")}),
        ("11.07", {(Standards.NACE2, "11.07")}),
        ("11.07A", {(Standards.NACE2, "11.07")}),
    ],
)
def test_naf2_to_nace2_concordance(code: str, expected: set):
    """Test NAF2 to NACE2 sample concordances."""
    assert NAF2_to_NACE2.concordant(code) == expected
