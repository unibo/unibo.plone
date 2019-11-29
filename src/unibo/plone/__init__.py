# -*- coding: utf-8 -*-
"""Init and utils."""
import logging
from zope.i18nmessageid import MessageFactory


_ = MessageFactory('unibo.plone')
logger = logging.getLogger(__name__)

# TODO: collective.monkeypatcher
from unibo.plone import indexing
indexing.apply_patches()
