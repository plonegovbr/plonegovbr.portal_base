from plone import api
from plone.dexterity.schema import SchemaInvalidatedEvent
from plonegovbr.portal_base.behaviors.eagendas import IEAgendas
from plonegovbr.portal_base.behaviors.eagendas import is_url
from plonegovbr.portal_base.validators.url import InvalidURL
from zope.event import notify

import pytest


BEHAVIOR = "plonegovbr.portal_base.eagendas"
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


class TestEAgendasBehavior:
    @pytest.fixture(autouse=True)
    def _init(self, portal, document, campus):
        self.portal = portal
        self.document = document

    def test_behavior_enabled(self, get_behaviors):
        """Test if behavior is installed for Document."""
        assert BEHAVIOR in get_behaviors(TYPE)

    def test_behavior_is_provided(self):
        """Test if behavior is provided by a Document instance."""
        document = self.document
        assert IEAgendas.providedBy(document)

    def test_behavior_default_value(self):
        """Test if the behavior returns an empty string as the default value."""
        document = self.document
        assert document.url_agenda == ""

    def test_behavior_constraint_is_url(self):
        """Test if the URL not is valid."""
        with pytest.raises(InvalidURL):
            is_url("http://xpto")
