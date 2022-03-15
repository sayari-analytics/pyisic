import pytest

from pyisic import NACE1_to_NACE2
from pyisic.types import Standards


@pytest.mark.parametrize(
    "code,expected",
    [
        ("DOESNT EXIST", set()),
        (
            "01.11",
            {
                (Standards.NACE2, "01.11"),
                (Standards.NACE2, "01.12"),
                (Standards.NACE2, "01.13"),
                (Standards.NACE2, "01.14"),
                (Standards.NACE2, "01.15"),
                (Standards.NACE2, "01.16"),
                (Standards.NACE2, "01.19"),
                (Standards.NACE2, "01.26"),
                (Standards.NACE2, "01.28"),
                (Standards.NACE2, "01.29"),
                (Standards.NACE2, "01.63"),
                (Standards.NACE2, "01.64"),
            },
        ),
        ("95", {(Standards.NACE2, "97")}),
        ("67.12", {(Standards.NACE2, "66.12"), (Standards.NACE2, "66.3")}),
        ("97", {(Standards.NACE2, "98.2")}),
    ],
)
def test_nace1_to_nace2_concordance(code: str, expected: set):
    """Test NACE1 to NACE2 sample concordances."""
    assert NACE1_to_NACE2.concordant(code) == expected
