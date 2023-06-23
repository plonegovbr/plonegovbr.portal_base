from plone import api
from typing import List
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


def _vocab_for_key(registry_key: str) -> dict:
    """Return all entries for a vocabulary in the registry."""
    registry_value = api.portal.get_registry_record(registry_key)
    items = registry_value.get("items", [])
    lang = api.portal.get_current_language()
    entries = {}
    for item in items:
        key = item["token"]
        titles = item["titles"]
        if lang not in titles:
            default_lang = list(titles.keys())[0]
            title = titles[default_lang]
        else:
            title = titles[lang]
        entries[key] = title
    return entries


def _unique_values(index: str) -> List[str]:
    """Return a list of unique values for a given index."""
    ct = api.portal.get_tool("portal_catalog")
    return ct.uniqueValuesFor(index)


def _vocabulary_from_dict(vocab: dict, sort: bool = True) -> SimpleVocabulary:
    """Create a SimpleVocabulary from a dictionary."""
    terms = []
    for token, title in vocab.items():
        terms.append(SimpleTerm(token, token, title))
    if sort:
        # Sort by title
        terms = sorted(terms, key=lambda x: x.title)
    return SimpleVocabulary(terms)


def vocab_from_registry(key: str) -> SimpleVocabulary:
    """Return a SimpleVocabulary with items from registry."""
    vocab = _vocab_for_key(key)
    return _vocabulary_from_dict(vocab)


def active_vocab_from_registry(key: str, index: str) -> SimpleVocabulary:
    """Return a SimpleVocabulary with items from registry that are used."""
    vocab = _vocab_for_key(key)
    existing = _unique_values(index)
    filtered = {token: title for token, title in vocab.items() if token in existing}
    return _vocabulary_from_dict(filtered)
