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
        # printed in the publication as a bare code or after its class on the same line
        ("16.24.0", Category.SUBCLASS),
        ("16.29.0", Category.SUBCLASS),
        ("82.19.0", Category.SUBCLASS),
        # omitted from the publication but used in the Slovak register
        ("47.29.0", Category.SUBCLASS),
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
    assert len(subclasses) == 646
    assert all(c[:5] in pyisic.NACE2 for c in subclasses)


def test_sknace2_hierarchy_matches_nace2():
    """Sections to classes are identical to NACE Rev. 2."""
    hierarchy = {c: v for c, v in SKNACE2.items() if v["category"] != Category.SUBCLASS}
    assert len(hierarchy) == len(pyisic.NACE2)
    for code, nace2 in pyisic.NACE2.items():
        assert hierarchy[code]["category"] == nace2["category"]
        assert hierarchy[code]["description"] == nace2["description"].strip()


def test_sknace2_descriptions_are_clean():
    assert all(v["description"] and v["description"] == v["description"].strip() for v in SKNACE2.values())


def test_sknace2_every_nace2_class_has_a_subclass():
    """SK NACE splits or repeats every NACE Rev. 2 class at the 5th level, so none can be left without a subclass."""
    classes = [c for c, v in pyisic.NACE2.items() if v["category"] == Category.CLASS]
    subclassed = {c[:5] for c, v in SKNACE2.items() if v["category"] == Category.SUBCLASS}
    assert sorted(set(classes) - subclassed) == []


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
