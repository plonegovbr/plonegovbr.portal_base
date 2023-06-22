from plone import api
from plone.dexterity.fti import DexterityFTI
from plonegovbr.portal_base.content.campus import Campus
from zope.component import createObject

import pytest


CONTENT_TYPE = "Campus"
PERMISSION = "plonegovbr.portal_base: Add Campus"


class TestCampus:
    @pytest.fixture(autouse=True)
    def _fti(self, get_fti, integration):
        self.fti = get_fti(CONTENT_TYPE)

    def test_fti(self):
        assert isinstance(self.fti, DexterityFTI)

    def test_factory(self):
        factory = self.fti.factory
        obj = createObject(factory)
        assert obj is not None
        assert isinstance(obj, Campus)

    @pytest.mark.parametrize(
        "behavior",
        [
            "plone.basic",
            "plone.categorization",
            "collective.contact_behaviors.contact_info",
            "collective.contact_behaviors.address_info",
            "volto.blocks",
            "plone.namefromtitle",
            "plone.shortname",
            "plone.excludefromnavigation",
            "volto.navtitle",
            "volto.preview_image",
            "plone.relateditems",
            "plone.versioning",
        ],
    )
    def test_has_behavior(self, get_behaviors, behavior):
        assert behavior in get_behaviors(CONTENT_TYPE)

    def test_create(self, portal, campi_payload):
        payload = campi_payload[0]
        with api.env.adopt_roles(["Manager"]):
            content = api.content.create(container=portal, **payload)
        assert content.portal_type == CONTENT_TYPE
        assert isinstance(content, Campus)

    @pytest.mark.parametrize(
        "role,expected",
        [
            ("Manager", True),
            ("Site Administrator", True),
            ("Editor", True),
            ("Owner", True),
            ("Member", False),
            ("Contributor", True),
        ],
    )
    def test_add_permission_site(self, portal, check_permission, role, expected):
        assert check_permission(portal, PERMISSION, role) is expected

    def test_indexer_contact_email(self, portal, campi_payload):
        payload = campi_payload[0]
        brains = api.content.find(contact_email=payload["contact_email"])
        assert len(brains) == 0

        with api.env.adopt_roles(["Manager"]):
            content = api.content.create(container=portal, **payload)

        brains = api.content.find(contact_email=payload["contact_email"])
        assert len(brains) == 1
        assert brains[0].Title == content.title

    def test_indexer_country(self, portal, campi_payload):
        payload = campi_payload[0]
        brains = api.content.find(country=payload["country"])
        assert len(brains) == 0

        with api.env.adopt_roles(["Manager"]):
            content = api.content.create(container=portal, **payload)

        brains = api.content.find(country=payload["country"])
        assert len(brains) == 1
        assert brains[0].Title == content.title
