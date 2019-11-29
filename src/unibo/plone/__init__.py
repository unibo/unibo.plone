# -*- coding: utf-8 -*-
"""Init and utils."""
import logging
from unibo.plone import indexing
from unibo.plone import noacquisition
from zope.i18nmessageid import MessageFactory


_ = MessageFactory('unibo.plone')
logger = logging.getLogger(__name__)

# TODO: collective.monkeypatcher
indexing.apply_patches()
noacquisition.apply_patches()

