# -*- coding: utf-8 -*-
from ._standards.cnae2 import CNAE2, CNAE2_to_ISIC4
from ._standards.gced2011 import GCED2011, GCED2011_to_NACE2
from ._standards.isic3 import ISIC3, ISIC3_to_ISIC31
from ._standards.isic4 import ISIC4
from ._standards.isic31 import ISIC31, ISIC31_to_ISIC4
from ._standards.jsic13 import JSIC13, JSIC13_to_ISIC4
from ._standards.ksic10 import KSIC10, KSIC10_to_ISIC4
from ._standards.nace1 import NACE1, NACE1_to_NACE2
from ._standards.nace2 import NACE2, NACE2_to_ISIC4
from ._standards.nacebel2003 import NACEBEL2003, NACEBEL2003_to_NACEBEL2008
from ._standards.nacebel2008 import NACEBEL2008, NACEBEL2008_to_NACE2
from ._standards.naf1 import NAF1, NAF1_to_NAF2
from ._standards.naf2 import NAF2, NAF2_to_NACE2
from ._standards.naics2017 import NAICS2017, NAICS2017_to_ISIC4
from ._standards.skd2002 import SKD2002, SKD2002_to_NACE2, SKD2002_to_SKD2008
from ._standards.skd2008 import SKD2008, SKD2008_to_SKD2002
from ._standards.skis2010 import SKIS2010
from ._standards.tsic2552 import TSIC2552, TSIC2552_to_ISIC3
from .types import ComposedGraph, Standards

ToISIC4 = ComposedGraph(
    Standards.ISIC4,
    [
        ISIC3_to_ISIC31,
        ISIC31_to_ISIC4,
        NACE2_to_ISIC4,
        NAICS2017_to_ISIC4,
        TSIC2552_to_ISIC3,
        JSIC13_to_ISIC4,
        KSIC10_to_ISIC4,
        SKD2008_to_SKD2002,
        SKD2002_to_NACE2,
        CNAE2_to_ISIC4,
        NACEBEL2003_to_NACEBEL2008,
        NACEBEL2008_to_NACE2,
        NAF1_to_NAF2,
        NAF2_to_NACE2,
        GCED2011_to_NACE2,
        NACE1_to_NACE2,
    ],
)
