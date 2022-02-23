# -*- coding: utf-8 -*-
import pytest

from pyisic import NAF1_to_NAF2
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        (
            "01.1A",
            {
                (Standards.NAF2, "01.11Z"),
                (Standards.NAF2, "01.12Z"),
                (Standards.NAF2, "01.13Z"),
                (Standards.NAF2, "01.14Z"),
                (Standards.NAF2, "01.15Z"),
                (Standards.NAF2, "01.16Z"),
                (Standards.NAF2, "01.19Z"),
                (Standards.NAF2, "01.26Z"),
                (Standards.NAF2, "01.28Z"),
                (Standards.NAF2, "01.29Z"),
                (Standards.NAF2, "01.63Z"),
                (Standards.NAF2, "01.64Z"),
            },
        ),
        ("45.4A", {(Standards.NAF2, "43.31Z")}),
    ],
)
def test_naf1_to_naf2_concordance(code: str, expected: set):
    """Test NAF1 to NAF2 sample concordances."""
    assert NAF1_to_NAF2.concordant(code) == expected
