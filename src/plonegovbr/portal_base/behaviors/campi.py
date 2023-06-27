from plone.app.vocabularies.catalog import StaticCatalogVocabulary
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plonegovbr.portal_base import _
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope.interface import provider


@provider(IFormFieldProvider)
class ICampi(model.Schema):
    """Campi Behavior."""

    # Campi
    campi = RelationList(
        title=_("label_campi", default="Campi"),
        description=_(
            "help_campi", default="Please select Campi related to this content."
        ),
        value_type=RelationChoice(
            vocabulary=StaticCatalogVocabulary({"portal_type": ["Campus"]}),
        ),
        required=False,
        default=[],
    )
    directives.widget(
        "campi",
        RelatedItemsFieldWidget,
        pattern_options={
            "selectableTypes": ["Campus"],
        },
    )
