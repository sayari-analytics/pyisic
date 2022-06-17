import pytest

from pyisic import CAEM2005_to_ISIC3
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
