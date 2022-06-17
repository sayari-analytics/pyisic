# -*- coding: utf-8 -*-
from collections import defaultdict

import pytest

import pyisic

CONCORDANCE_TO_MINIMUM = {
    pyisic.ISIC3_to_ISIC31: 0.5,
    pyisic.ISIC31_to_ISIC4: 0.5,
    pyisic.NACE2_to_ISIC4: 1.0,
    pyisic.NAICS2017_to_ISIC4: 0.9,
    pyisic.TSIC2552_to_ISIC3: 0.5,
    pyisic.KSIC10_to_ISIC4: 0.4,
    pyisic.SKD2002_to_NACE2: 1.0,
    pyisic.SKD2002_to_SKD2008: 0.9,
    pyisic.SKD2008_to_SKD2002: 0.3,
    pyisic.CNAE2_to_ISIC4: 0.9,
    pyisic.NACEBEL2003_to_NACEBEL2008: 1.0,
    pyisic.NACEBEL2008_to_NACE2: 0.2,
    pyisic.NAF1_to_NAF2: 0.6,
    pyisic.NAF2_to_NACE2: 1.0,
    pyisic.GCED2011_to_NACE2: 0.5,
    pyisic.NACE1_to_NACE2: 1.0,
    pyisic.SCIAN2018_to_ISIC4: 0.5,
    pyisic.CCNAE2021_to_ISIC4: 0.5,
    pyisic.CAEM2005_to_ISIC3: 0.99,
    pyisic.CAEM2009_to_ISIC4: 0.6,
}

# creates a mapping of the standard name to standard object
name_to_standard = {}
for name in pyisic.__dir__():
    attr = getattr(pyisic, name)
    if isinstance(attr, pyisic.types.Standard):
        name_to_standard[name] = attr


def calc_id(param):
    """Calculates the pytest test case id."""
    if isinstance(param, pyisic.types.Concordance):
        return repr(param)[12:-1]


@pytest.mark.parametrize("concordance,minimum", list(CONCORDANCE_TO_MINIMUM.items()), ids=calc_id)
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
        pyisic.SCIAN2018_to_ISIC4,
        pyisic.CCNAE2021_to_ISIC4,
        pyisic.CAEM2005_to_ISIC3,
        pyisic.CAEM2009_to_ISIC4,
    ],
)
def test_to_isic4(standard):
    """Ensure all nodes and relationships are included in the ToISIC4 graph."""
    assert all([n in pyisic.ToISIC4 for n in standard.nodes])
    assert all([e in pyisic.ToISIC4.edges for e in standard.edges])


@pytest.mark.parametrize("concordance", CONCORDANCE_TO_MINIMUM.keys(), ids=calc_id)
def test_valid_concordance(concordance):
    """Checks that all codes in the concordance are valid."""

    def preprocess_standard_name(s):
        return str(s).split(".", 1)[1]

    standard_to_codes = defaultdict(set)

    for (src_standard, src_code), (dst_standard, dst_code) in concordance.edges:
        if src_code not in name_to_standard[preprocess_standard_name(src_standard)]:
            standard_to_codes[preprocess_standard_name(src_standard)].add(src_code)

        if dst_code not in name_to_standard[preprocess_standard_name(dst_standard)]:
            standard_to_codes[preprocess_standard_name(dst_standard)].add(dst_code)

    count = sum(len(codes) for codes in standard_to_codes.values())

    assert not standard_to_codes, "There are {} invalid codes".format(count)
