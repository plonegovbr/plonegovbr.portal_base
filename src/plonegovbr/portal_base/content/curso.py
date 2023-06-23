"""Um Curso oferecido pela instituição."""
from plonegovbr.portal_base import _
from plone.dexterity.content import Container
from plone.supermodel.model import Schema
from zope import schema
from zope.interface import implementer


class ICurso(Schema):
    """Definição do Curso."""

    areas = schema.List(
        title=_("label_curso_area", default="Área"),
        value_type=schema.Choice(
            vocabulary="plonegovbr.portal_base.vocab.available_areas",
        ),
        required=True,
    )

    modalidades = schema.List(
        title=_("label_curso_modalidade", default="Modalidade"),
        value_type=schema.Choice(
            vocabulary="plonegovbr.portal_base.vocab.available_modalidades",
        ),
        required=True,
    )


@implementer(ICurso)
class Curso(Container):
    """Um Curso oferecido pela instituição."""
