import pytest

from pyisic import KSIC10_to_ISIC4
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("A", set()),
        ("14112", {(Standards.ISIC4, "1410")}),
    ],
)
def test_ksic10_to_isic4_concordance(code: str, expected: str):
    """Test KSIC10 to ISIC4 sample concordances."""
    assert KSIC10_to_ISIC4.concordant(code) == expected
