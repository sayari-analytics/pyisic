import pytest

from pyisic import GCED2011, NACE2, GCED2011_to_NACE2
from pyisic.types import Category, Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("A", {(Standards.NACE2, "A")}),
        ("01", {(Standards.NACE2, "01")}),
        ("15.1", {(Standards.NACE2, "15.1")}),
        ("20.53", {(Standards.NACE2, "20.53")}),
        ("21.10.0", set()),
        ("CF", set()),
    ],
)
def test_gced2011_to_nace2_concordance(code: str, expected: set):
    """Test GCED2011 to NACE2 sample concordances."""
    assert GCED2011_to_NACE2.concordant(code) == expected


def test_gced2011_counts():
    gced2011_main_counts = sum((1 for v in GCED2011.values() if v["category"] != Category.SUBCLASS))

    assert gced2011_main_counts - 21 == GCED2011_to_NACE2.size()
    assert len(NACE2.keys()) - 2 == GCED2011_to_NACE2.size()
