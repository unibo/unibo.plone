# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import unibo.plone


class UniboPloneLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=unibo.plone)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "unibo.plone:default")


UNIBO_PLONE_FIXTURE = UniboPloneLayer()


UNIBO_PLONE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(UNIBO_PLONE_FIXTURE,),
    name="UniboPloneLayer:IntegrationTesting",
)


UNIBO_PLONE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(UNIBO_PLONE_FIXTURE,),
    name="UniboPloneLayer:FunctionalTesting",
)


UNIBO_PLONE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        UNIBO_PLONE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="UniboPloneLayer:AcceptanceTesting",
)
