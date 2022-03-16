# -*- coding: utf-8 -*-
import pytest

import pyisic


@pytest.mark.parametrize(
    "concordance,minimum",
    [
        (pyisic.ISIC3_to_ISIC31, 0.5),
        (pyisic.ISIC31_to_ISIC4, 0.5),
        (pyisic.NACE2_to_ISIC4, 1.0),
        (pyisic.NAICS2017_to_ISIC4, 0.9),
        (pyisic.TSIC2552_to_ISIC3, 0.5),
        (pyisic.KSIC10_to_ISIC4, 0.4),
        (pyisic.SKD2002_to_NACE2, 1.0),
        (pyisic.SKD2002_to_SKD2008, 0.9),
        (pyisic.SKD2008_to_SKD2002, 0.3),
        (pyisic.CNAE2_to_ISIC4, 1.0),
        (pyisic.NACEBEL2003_to_NACEBEL2008, 1.0),
        (pyisic.NACEBEL2008_to_NACE2, 0.2),
        (pyisic.NAF1_to_NAF2, 0.6),
        (pyisic.NAF2_to_NACE2, 1.0),
        (pyisic.GCED2011_to_NACE2, 0.5),
        (pyisic.NACE1_to_NACE2, 1.0),
    ],
)
def test_minimum_concordance(concordance, minimum: float):
    """Ensure each concordances has some minimum level of concordance."""
    standard = concordance.src
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
        pyisic.JSIC13_to_ISIC4,
        pyisic.KSIC10_to_ISIC4,
        pyisic.SKD2008_to_SKD2002,
        pyisic.SKD2002_to_NACE2,
        pyisic.CNAE2_to_ISIC4,
        pyisic.NACEBEL2003_to_NACEBEL2008,
        pyisic.NACEBEL2008_to_NACE2,
        pyisic.NAF1_to_NAF2,
        pyisic.NAF2_to_NACE2,
        pyisic.GCED2011_to_NACE2,
        pyisic.NACE1_to_NACE2,
    ],
)
def test_to_isic4(standard):
    """Ensure all nodes and relationships are included in the ToISIC4 graph."""
    assert all([n in pyisic.ToISIC4 for n in standard.nodes])
    assert all([e in pyisic.ToISIC4.edges for e in standard.edges])
