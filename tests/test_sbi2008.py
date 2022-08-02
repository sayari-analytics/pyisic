# -*- coding: utf-8 -*-
import pytest

from pyisic import SBI2008_to_NACE2
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("43221", {(Standards.NACE2, "43.22")}),
        ("4617", {(Standards.NACE2, "46.17")}),
    ],
)
def test_sbi2008_to_nace2_concordance(code: str, expected: set):
    """Test SBI2008 to NACE2 sample concordances."""
    assert SBI2008_to_NACE2.concordant(code) == expected
