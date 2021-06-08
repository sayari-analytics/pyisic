# -*- coding: utf-8 -*-
import pytest

from pyisic import ISIC4, NAICS2017
from pyisic.types import Category, Classification, Concordance, Standard, Standards


def test_classification_dataclass():
    """Dummy test dataclass to_dict() conversion."""
    kwargs = {"code": "12345", "description": "dummy", "category": Category.CLASS}

    x = Classification(**kwargs)
    assert x.to_dict() == kwargs


def test_standardimpl_Nones():
    """Dummy init failure."""
    with pytest.raises(TypeError):
        Standard(Standards.ISIC4, None)

    with pytest.raises(AttributeError):
        repr(Standard(None, [Classification("fail", "fail")]))


def test_concordance_Nones():
    """Dummy init failure."""
    with pytest.raises(AttributeError):
        Concordance(None, None, None)

    with pytest.raises(TypeError):
        Concordance(NAICS2017, ISIC4, None)
