"""Control Panels Interfaces."""
from plonegovbr.portal_base import _
from plone.autoform import directives
from plone.schema import JSONField
from zope.interface import Interface

import json


VOCABULARY_SCHEMA = json.dumps(
    {
        "type": "object",
        "properties": {
            "items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "token": {"type": "string"},
                        "titles": {
                            "type": "object",
                            "properties": {
                                "lang": {"type": "string"},
                                "title": {"type": "string"},
                            },
                        },
                    },
                },
            }
        },
    }
)


class IEduSettings(Interface):
    areas = JSONField(
        title=_("label_areas", default="Áreas"),
        description=_("help_areas", default="Vocabulário de áreas"),
        required=True,
        schema=VOCABULARY_SCHEMA,
        default={
            "items": [
                {
                    "token": "sociais",
                    "titles": {
                        "pt-br": "Ciências Sociais",
                    },
                },
                {
                    "token": "engenharia",
                    "titles": {
                        "pt-br": "Engenharias",
                    },
                },
                {
                    "token": "tecnologia",
                    "titles": {
                        "pt-br": "Tecnologia",
                    },
                },
            ]
        },
        missing_value={"items": []},
    )
    directives.widget(
        "areas",
        frontendOptions={"widget": "vocabularyterms"},
    )

    modalidades = JSONField(
        title=_("label_modalidades", default="Modalidades"),
        description=_("help_modalidades", default="Vocabulário de modalidades"),
        required=True,
        schema=VOCABULARY_SCHEMA,
        default={
            "items": [
                {
                    "token": "tecnico",
                    "titles": {
                        "pt-br": "Técnico",
                    },
                },
                {
                    "token": "mestrado",
                    "titles": {
                        "pt-br": "Mestrado",
                    },
                },
                {
                    "token": "doutorado",
                    "titles": {
                        "pt-br": "Doutorado",
                    },
                },
                {
                    "token": "tecnologia",
                    "titles": {
                        "pt-br": "Tecnologia",
                    },
                },
            ]
        },
        missing_value={"items": []},
    )
    directives.widget(
        "modalidades",
        frontendOptions={"widget": "vocabularyterms"},
    )
