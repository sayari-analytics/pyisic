import pytest

from pyisic import CAEM2005_to_CAEM2009, CAEM2005_to_ISIC3
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("22.14.0", {(Standards.ISIC3, "2213")}),
    ],
)
def test_caem2005_to_isic3_concordance(code: str, expected: str):
    """Test CAEM2005 to ISIC3 sample concordances."""
    assert CAEM2005_to_ISIC3.concordant(code) == expected


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("85.2", {(Standards.CAEM2009, "75.0")}),
        ("60.24.0", {(Standards.CAEM2009, "49.41"), (Standards.CAEM2009, "49.42")}),
    ],
)
def test_caem2005_to_caem2009_concordance(code: str, expected: str):
    """Test CAEM2005 to CAEM2009 sample concordances."""
    assert CAEM2005_to_CAEM2009.concordant(code) == expected
