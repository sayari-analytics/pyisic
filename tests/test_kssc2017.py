import pytest

from pyisic import KSSC2017


@pytest.mark.parametrize(
    "code,description",
    [
        ("A", "Agriculture, forestry and fishing"),
        ("17", "Manufacture of pulp, paper and paper products"),
        ("312", "Manufacture of railway locomotives and rolling stock"),
        ("4669", "Wholesale of other construction materials"),
        ("86202", "Dental clinics"),
    ],
)
def test_kssc2017(code: str, description: str):
    """Test KSSC2017 lookups."""
    assert KSSC2017[code]["description"] == description
