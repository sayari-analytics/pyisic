import pytest

from pyisic import NACEBEL2008_to_NACE2, NACEBEL2008_to_NACEBEL2003
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("01110", {(Standards.NACEBEL2003, "01110"), (Standards.NACEBEL2003, "01121")}),
        ("1031201", {(Standards.NACEBEL2003, "1531202")}),
    ],
)
def test_nacebel2008_to_nacebel2003_concordance(code: str, expected: set):
    """Test NACEBEL2008 to NACEBEL2003 sample concordances."""
    assert NACEBEL2008_to_NACEBEL2003.concordant(code) == expected


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
