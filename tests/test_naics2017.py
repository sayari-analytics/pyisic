# -*- coding: utf-8 -*-
import pytest

from pyisic import NAICS2017_to_ISIC4
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("927110", {(Standards.ISIC4, "5120"), (Standards.ISIC4, "8413")}),
        ("423320", {(Standards.ISIC4, "4663")}),
    ],
)
def test_naics_to_isic4_concordance(code: str, expected: set):
    """Test NAICS2017 to ISIC4 sample concordances."""
    assert NAICS2017_to_ISIC4.concordant(code) == expected
