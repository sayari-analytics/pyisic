import pytest

from pyisic import CCNAE2021_to_ISIC4
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("8523", {(Standards.ISIC4, "8521")}),
        ("8562", {(Standards.ISIC4, "8521"), (Standards.ISIC4, "8522")}),
    ],
)
def test_ccnae2021_to_isic4_concordance(code: str, expected: str):
    """Test CCNAE2021 to ISIC4 sample concordances."""
    assert CCNAE2021_to_ISIC4.concordant(code) == expected
