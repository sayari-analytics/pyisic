import pytest

from pyisic import CNAE2_to_ISIC4
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("A", {(Standards.ISIC4, "A")}),
        ("56.11-2", {(Standards.ISIC4, "5610"), (Standards.ISIC4, "5630")}),
    ],
)
def test_cnae2_to_isic4_concordance(code: str, expected: str):
    """Test CNAE2 to ISIC4 sample concordances."""
    assert CNAE2_to_ISIC4.concordant(code) == expected
