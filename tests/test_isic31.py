# -*- coding: utf-8 -*-
import pytest

from pyisic import ISIC31_to_ISIC4
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("9309", {(Standards.ISIC4, "8541"), (Standards.ISIC4, "9609")}),
        ("9700", {(Standards.ISIC4, "9820")}),
        ("9900", {(Standards.ISIC4, "9900")}),
    ],
)
def test_isic31_to_isic4_concordance(code: str, expected: set):
    """Test ISIC31 to ISIC4 sample concordances."""
    assert ISIC31_to_ISIC4.concordant(code) == expected
