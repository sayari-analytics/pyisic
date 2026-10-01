import pytest

import pyisic
from pyisic import SKNACE2, SKNACE2_to_NACE2
from pyisic.types import Category, Standards


@pytest.mark.parametrize(
    "code,category",
    [
        ("52", Category.DIVISION),
        ("52.1", Category.GROUP),
        ("52.10", Category.CLASS),
        ("52.10.0", Category.SUBCLASS),
        ("01.49.1", Category.SUBCLASS),
        ("99.00.0", Category.SUBCLASS),
    ],
)
def test_sknace2_codes(code: str, category: Category):
    """Test SKNACE2 sample codes."""
    assert code in SKNACE2
    assert SKNACE2[code]["category"] == category


@pytest.mark.parametrize("code", ["52100", "5210", "52.100", "52.10.00", "", "DOESNT EXIST"])
def test_sknace2_rejects_other_formats(code: str):
    """Subclasses are only valid in the official dotted NN.NN.N format."""
    assert code not in SKNACE2


def test_sknace2_subclasses():
    """Every national subclass belongs to a NACE Rev. 2 class."""
    subclasses = [c for c, v in SKNACE2.items() if v["category"] == Category.SUBCLASS]
    assert len(subclasses) == 637
    assert all(c[:5] in pyisic.NACE2 for c in subclasses)


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        ("52", {(Standards.NACE2, "52")}),
        ("52.10", {(Standards.NACE2, "52.10")}),
        ("52.10.0", {(Standards.NACE2, "52.10")}),
        ("47.19.0", {(Standards.NACE2, "47.19")}),
    ],
)
def test_sknace2_to_nace2_concordance(code: str, expected: set):
    """Test SKNACE2 to NACE2 sample concordances."""
    assert SKNACE2_to_NACE2.concordant(code) == expected


def test_sknace2_to_isic4():
    """SKNACE2 codes convert to ISIC4 through NACE2."""
    assert list(pyisic.ToISIC4("52.10.0", Standards.SKNACE2)) == [(Standards.ISIC4, "5210")]
