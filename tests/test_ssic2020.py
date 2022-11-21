# -*- coding: utf-8 -*-
import pytest

from pyisic import SSIC2020_to_ISIC4
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("01111", {(Standards.ISIC4, "0113")}),
        ("63205", {(Standards.ISIC4, "5819"), (Standards.ISIC4, "6820")}),
        ("81211", {(Standards.ISIC4, "8121"), (Standards.ISIC4, "8129")}),
    ],
)
def test_ssic2020_to_isic4_concordance(code: str, expected: set):
    """Test SSIC2020 to ISIC4 sample concordances."""
    assert SSIC2020_to_ISIC4.concordant(code) == expected
