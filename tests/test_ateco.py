import pytest

from pyisic import ATECO_to_NACE2
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("01.11", {(Standards.NACE2, "01.11")}),
        ("55.30", {(Standards.NACE2, "55.30")}),
        ("99.00", {(Standards.NACE2, "99.00")}),
    ],
)
def test_ateco_to_nace2_concordance(code: str, expected: set):
    """Test ATECO to NACE2 sample concordances."""
    assert ATECO_to_NACE2.concordant(code) == expected
