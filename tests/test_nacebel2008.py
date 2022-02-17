import pytest

from pyisic import NACEBEL2008_to_NACE2
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("01110", {(Standards.NACE2, "01.11")}),
        ("55300", {(Standards.NACE2, "55.30")}),
        ("99000", {(Standards.NACE2, "99.00")}),
    ],
)
def test_nacebel2008_to_nace2_concordance(code: str, expected: set):
    """Test NACEBEL2008 to NACE2 sample concordances."""
    assert NACEBEL2008_to_NACE2.concordant(code) == expected
