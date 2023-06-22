from plone import api
from plone.indexer import indexer
from plonegovbr.portal_base.behaviors.campi import ICampi


@indexer(ICampi)
def indexer(obj):
    """Index objects with ICampi behavior."""
    relations = obj.campi or []
    campi = [rel.to_object for rel in relations]
    return [api.content.get_uuid(campus) for campus in campi]
