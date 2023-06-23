from plonegovbr.portal_base.vocabularies import active_vocab_from_registry
from plonegovbr.portal_base.vocabularies import vocab_from_registry
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


@provider(IVocabularyFactory)
def available_areas_vocabulary(context) -> SimpleVocabulary:
    """Vocabulary of all areas that could be used."""
    return vocab_from_registry("pb_edu.areas")


@provider(IVocabularyFactory)
def areas_vocabulary(context) -> SimpleVocabulary:
    """Vocabulary of areas that already have a value."""
    return active_vocab_from_registry("pb_edu.areas", "areas")


@provider(IVocabularyFactory)
def available_modalidades_vocabulary(context) -> SimpleVocabulary:
    """Vocabulary of all modalidades that could be used."""
    return vocab_from_registry("pb_edu.modalidades")


@provider(IVocabularyFactory)
def modalidades_vocabulary(context) -> SimpleVocabulary:
    """Vocabulary of modalidades that already have a value."""
    return active_vocab_from_registry("pb_edu.modalidades", "modalidades")
