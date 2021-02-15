# -*- coding: utf-8 -*-
import logging
from OFS.interfaces import IItem
from Products.ZCatalog import Catalog

logger = logging.getLogger(__name__)


def safe_callable(ob):
    if IItem.providedBy(ob):
        logger.warning("invalid: try to use %s as index", ob)
        return False
    return Catalog.safe_callable_orig(ob)


def apply_patches():
    logger.info("install Catalog.safe_callable monkey")
    Catalog.safe_callable_orig = Catalog.safe_callable
    Catalog.safe_callable = safe_callable
