# -*- coding: utf-8 -*-
import pytest

from pyisic import SKIS2010


@pytest.mark.parametrize(
    "code,expected",
    [
        ("S.1", "Total economy"),
        ("S.14", "Households"),
        ("S.212", "Institutions and bodies of the European Union"),
    ],
)
def test_skis_classifications(code: str, expected: set):
    """Test SKIS2010 sample classifications."""
    assert code in SKIS2010
    assert SKIS2010[code]["description"] == expected
