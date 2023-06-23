from plone import api
from plone.dexterity.fti import DexterityFTI
from plonegovbr.portal_base.content.curso import Curso
from zope.component import createObject

import pytest


CONTENT_TYPE = "Curso"
PERMISSION = "plonegovbr.portal_base: Add Curso"


class TestCurso:
    @pytest.fixture(autouse=True)
    def _fti(self, get_fti, integration):
        self.fti = get_fti(CONTENT_TYPE)

    def test_fti(self):
        assert isinstance(self.fti, DexterityFTI)

    def test_factory(self):
        factory = self.fti.factory
        obj = createObject(factory)
        assert obj is not None
        assert isinstance(obj, Curso)

    @pytest.mark.parametrize(
        "behavior",
        [
            "plone.basic",
            "plone.categorization",
            "plonegovbr.portal_base.campi",
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

    def test_create(self, portal, cursos_payload):
        payload = cursos_payload[0]
        with api.env.adopt_roles(["Manager"]):
            content = api.content.create(container=portal, **payload)
        assert content.portal_type == CONTENT_TYPE
        assert isinstance(content, Curso)

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

    def test_indexer_campi(self, portal, cursos_payload, campus):
        payload = cursos_payload[0]
        campus_uuid = api.content.get_uuid(campus)
        brains = api.content.find(campi=campus_uuid)
        assert len(brains) == 0

        with api.env.adopt_roles(["Manager"]):
            content = api.content.create(container=portal, **payload)
            api.relation.create(source=content, target=campus, relationship="campi")
            content.reindexObject(idxs=["campi"])

        brains = api.content.find(campi=campus_uuid)
        assert len(brains) == 1
        assert brains[0].Title == content.title

    def test_indexer_areas(self, portal, cursos_payload):
        payload = cursos_payload[0]
        area = payload["areas"][0]
        brains = api.content.find(areas=area)
        assert len(brains) == 0

        with api.env.adopt_roles(["Manager"]):
            content = api.content.create(container=portal, **payload)

        brains = api.content.find(areas=area)
        assert len(brains) == 1
        assert brains[0].Title == content.title

    def test_indexer_modalidades(self, portal, cursos_payload):
        payload = cursos_payload[0]
        modalidade = payload["modalidades"][0]
        brains = api.content.find(modalidades=modalidade)
        assert len(brains) == 0

        with api.env.adopt_roles(["Manager"]):
            content = api.content.create(container=portal, **payload)

        brains = api.content.find(modalidades=modalidade)
        assert len(brains) == 1
        assert brains[0].Title == content.title
