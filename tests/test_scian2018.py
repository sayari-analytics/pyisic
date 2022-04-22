import pytest

from pyisic import SCIAN2018_to_ISIC4
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("111219", {(Standards.ISIC4, "0113"), (Standards.ISIC4, "0119")}),
        ("312120", {(Standards.ISIC4, "1103")}),
    ],
)
def test_scian2018_to_isic4_concordance(code: str, expected: set):
    """Test SCIAN2018 to ISIC4 sample concordances."""
    assert SCIAN2018_to_ISIC4.concordant(code) == expected
