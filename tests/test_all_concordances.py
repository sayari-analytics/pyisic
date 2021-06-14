# -*- coding: utf-8 -*-
import pytest

import pyisic


@pytest.mark.parametrize(
    "standard,concordance,minimum",
    [
        (pyisic.ISIC3, pyisic.ISIC3_to_ISIC31, 0.5),
        (pyisic.ISIC31, pyisic.ISIC31_to_ISIC4, 0.5),
        (pyisic.NACE2, pyisic.NACE2_to_ISIC4, 1.0),
        (pyisic.NAICS2017, pyisic.NAICS2017_to_ISIC4, 0.9),
        (pyisic.TSIC2552, pyisic.TSIC2552_to_ISIC3, 0.5),
    ],
)
def test_minimum_concordance(standard, concordance, minimum: float):
    """Ensure each concordances has some minimum level of concordance."""
    concordant = [c for c in standard if any(concordance.concordant(c))]
    assert (len(concordant) / len(standard)) >= minimum


@pytest.mark.parametrize(
    "standard",
    [
        pyisic.ISIC3_to_ISIC31,
        pyisic.ISIC31_to_ISIC4,
        pyisic.NACE2_to_ISIC4,
        pyisic.NAICS2017_to_ISIC4,
        pyisic.TSIC2552_to_ISIC3,
    ],
)
def test_to_isic4(standard):
    """Ensure all nodes and relationships are included in the ToISIC4 graph."""
    assert all([n in pyisic.ToISIC4 for n in standard.nodes])
    assert all([e in pyisic.ToISIC4.edges for e in standard.edges])
