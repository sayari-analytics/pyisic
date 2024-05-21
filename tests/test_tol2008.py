# -*- coding: utf-8 -*-
import pytest

from pyisic import TOL2008_to_NACE2
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("01110", {(Standards.NACE2, "01.11")}),
    ],
)
def test_tol2008_to_nace2_concordance(code: str, expected: set):
    """Test TOL2008 to NACE2 sample concordances."""
    assert TOL2008_to_NACE2.concordant(code) == expected
