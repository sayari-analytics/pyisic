# -*- coding: utf-8 -*-
from ._standards.isic3 import ISIC3, ISIC3_to_ISIC31
from ._standards.isic4 import ISIC4
from ._standards.isic31 import ISIC31, ISIC31_to_ISIC4
from ._standards.jsic13 import JSIC13, JSIC13_to_ISIC4
from ._standards.nace2 import NACE2, NACE2_to_ISIC4
from ._standards.naics2017 import NAICS2017, NAICS2017_to_ISIC4
from ._standards.tsic2552 import TSIC2552, TSIC2552_to_ISIC3
from .types import ComposedGraph, Standards

ToISIC4 = ComposedGraph(
    Standards.ISIC4,
    [ISIC3_to_ISIC31, ISIC31_to_ISIC4, NACE2_to_ISIC4, NAICS2017_to_ISIC4, TSIC2552_to_ISIC3, JSIC13_to_ISIC4],
)
