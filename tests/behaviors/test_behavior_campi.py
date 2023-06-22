from plone import api
from plone.dexterity.schema import SchemaInvalidatedEvent
from plonegovbr.portal_base.behaviors.campi import ICampi
from z3c.relationfield.relation import RelationValue
from zope.event import notify

import pytest


BEHAVIOR = "plonegovbr.portal_base.campi"
TYPE = "Document"


@pytest.fixture
def portal(integration, get_fti):
    fti = get_fti(TYPE)
    current = list(fti.behaviors)
    behaviors = current[:]
    # Add local behaviors
    behaviors.append(BEHAVIOR)
    fti.behaviors = tuple(behaviors)
    notify(SchemaInvalidatedEvent(TYPE))
    yield integration["portal"]
    fti.behaviors = tuple(current)
    notify(SchemaInvalidatedEvent(TYPE))


@pytest.fixture
def document(portal):
    with api.env.adopt_roles(["Manager"]):
        document = api.content.create(
            container=portal,
            type=TYPE,
            id="document",
            title="Página",
        )
    return document


@pytest.fixture
def document_with_relation(document, campus):
    api.relation.create(source=document, target=campus, relationship="campi")
    document.reindexObject(idxs=["campi"])
    return document


class TestPloneUserBehavior:
    @pytest.fixture(autouse=True)
    def _init(self, portal, document, campus):
        self.portal = portal
        self.document = document
        self.campus = campus

    def test_behavior_enabled(self, get_behaviors):
        """Test if behavior is installed for Document."""
        assert BEHAVIOR in get_behaviors(TYPE)

    def test_behavior_is_provided(self):
        """Test if behavior is provided by a Document instance."""
        document = self.document
        assert ICampi.providedBy(document)

    def test_behavior_default_value(self):
        """Test if behavior returns a list as default value."""
        document = self.document
        assert document.campi == []

    def test_behavior_set_relation(self):
        document = self.document
        campus = self.campus
        api.relation.create(source=document, target=campus, relationship="campi")
        assert isinstance(document.campi, list)
        assert len(document.campi) == 1
        assert isinstance(document.campi[0], RelationValue)

    def test_indexer_campi(self):
        """Test campi indexer."""
        document = self.document
        campus = self.campus
        campus_uuid = api.content.get_uuid(campus)
        brains = api.content.find(campi=campus_uuid)
        assert len(brains) == 0
        # Add relation and reindex campi
        api.relation.create(source=document, target=campus, relationship="campi")
        document.reindexObject(idxs=["campi"])
        brains = api.content.find(campi=campus_uuid)
        assert len(brains) == 1

    def test_qs(self, document_with_relation):
        """Test qs."""
        querybuilder = api.content.get_view("querybuilderresults", context=self.portal)
        campus_uuid = api.content.get_uuid(self.campus)
        query = [
            {
                "i": "campi",
                "o": "plone.app.querystring.operation.selection.any",
                "v": [campus_uuid],
            }
        ]
        results = querybuilder(query=query)
        assert len(results) == 1
