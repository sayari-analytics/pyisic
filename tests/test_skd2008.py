# -*- coding: utf-8 -*-
import pytest

from pyisic import SKD2008_to_SKD2002
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        (
            "01.110",
            {
                (Standards.SKD2002, "01.110"),
                (Standards.SKD2002, "01.120"),
            },
        ),
        (
            "71.129",
            {
                (Standards.SKD2002, "74.204"),
                (Standards.SKD2002, "74.203"),
            },
        ),
    ],
)
def test_skd2008_to_skd2002_concordance(code: str, expected: set):
    """Test SKD2008 to SKD2002 sample concordances."""
    assert SKD2008_to_SKD2002.concordant(code) == expected
