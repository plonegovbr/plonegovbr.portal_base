"""Control Panels Interfaces."""
from plone import schema
from plone.supermodel.directives import fieldset
from plonegovbr.portal_base import _
from zope.interface import Interface


class IPBSettings(Interface):
    siorg = schema.TextLine(
        title=_("label_siorg", default="SIORG"),
        description=_("help_siorg", default="Please enter the code of the SIORG"),
        required=False,
        missing_value="",
        default="",
    )

    fieldset(
        "eagendas",
        label=_("label_fieldset_eagendas", default="E-Agendas"),
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
    )
