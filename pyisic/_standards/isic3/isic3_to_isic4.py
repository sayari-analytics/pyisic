# -*- coding: utf-8 -*-
from ...types import Concordance
from ..isic4 import ISIC4
from ..isic31 import ISIC31_to_ISIC4
from .isic3 import ISIC3
from .isic3_to_isic31 import ISIC3_to_ISIC31

ISIC3_to_ISIC4 = Concordance(
    src=ISIC3, dst=ISIC4, concordances=ISIC3_to_ISIC31._concordances + ISIC31_to_ISIC4._concordances
)
