import pytest

from pyisic import NACEBEL2003_to_NACEBEL2008
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        (
            "01110",
            {
                (Standards.NACEBEL2008, "01110"),
                (Standards.NACEBEL2008, "01120"),
                (Standards.NACEBEL2008, "01130"),
                (Standards.NACEBEL2008, "01140"),
                (Standards.NACEBEL2008, "01150"),
                (Standards.NACEBEL2008, "01160"),
                (Standards.NACEBEL2008, "01199"),
                (Standards.NACEBEL2008, "01260"),
                (Standards.NACEBEL2008, "01280"),
                (Standards.NACEBEL2008, "01290"),
                (Standards.NACEBEL2008, "01630"),
                (Standards.NACEBEL2008, "01640"),
            },
        ),
        ("1531202", {(Standards.NACEBEL2008, "1031201")}),
    ],
)
def test_nacebel2003_to_nacebel2008_concordance(code: str, expected: set):
    """Test NACEBEL2003 to NACEBEL2008 sample concordances."""
    assert NACEBEL2003_to_NACEBEL2008.concordant(code) == expected
