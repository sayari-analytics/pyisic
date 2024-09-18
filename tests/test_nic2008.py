# -*- coding: utf-8 -*-
import pytest

from pyisic import NIC2008_to_ISIC4
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("01", {(Standards.ISIC4, "01")}),
        ("3240", {(Standards.ISIC4, "3240")}),
    ],
)
def test_nic2008_to_isic4_concordance(code: str, expected: set):
    """Test NIC2008 to ISIC4 sample concordances."""
    assert NIC2008_to_ISIC4.concordant(code) == expected
