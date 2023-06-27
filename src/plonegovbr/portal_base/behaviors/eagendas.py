from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from plonegovbr.portal_base import _
from plonegovbr.portal_base.validators.url import UrlValidator
from zope.interface import provider


def is_url(value):
    if value:
        UrlValidator(value)
    return True


@provider(IFormFieldProvider)
class IEAgendas(model.Schema):
    """E-Agendas Behavior."""

    fieldset(
        "eagendas",
        label=_("label_schema_eagendas", default="E-Agendas"),
        fields=["url_agenda"],
    )

    # url agenda
    url_agenda = schema.TextLine(
        title=_("label_url_agenda", default="URL"),
        description=_(
            "help_url_agenda", default="Please enter the URL of the e-Agendas"
        ),
        required=False,
        missing_value="",
        default="",
        constraint=is_url,
    )
