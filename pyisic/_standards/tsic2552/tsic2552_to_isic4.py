# -*- coding: utf-8 -*-
from ...types import Concordance
from ..isic3 import ISIC3_to_ISIC4
from ..isic4 import ISIC4
from .tsic2552 import TSIC2552
from .tsic2552_to_isic3 import TSIC2552_to_ISIC3

TSIC2552_to_ISIC4 = Concordance(
    src=TSIC2552, dst=ISIC4, concordances=TSIC2552_to_ISIC3._concordances + ISIC3_to_ISIC4._concordances
)
