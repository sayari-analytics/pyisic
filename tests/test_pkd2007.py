# -*- coding: utf-8 -*-
import pytest

from pyisic import PKD2007_to_NACE2
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("46.77.Z", {(Standards.NACE2, "46.77")}),
        ("21", {(Standards.NACE2, "21")}),
    ],
)
def test_pkd2007_to_nace2_concordance(code: str, expected: set):
    """Test PKD2007 to NACE2 sample concordances."""
    assert PKD2007_to_NACE2.concordant(code) == expected
