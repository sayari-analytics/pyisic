import pytest

from pyisic import CAEM2009_to_ISIC4
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("02.30", {(Standards.ISIC4, "0230")}),
    ],
)
def test_caem2009_to_isic4_concordance(code: str, expected: str):
    """Test CAEM2009 to ISIC4 sample concordances."""
    assert CAEM2009_to_ISIC4.concordant(code) == expected
