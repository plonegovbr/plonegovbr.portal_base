from plonegovbr.portal_base import PACKAGE_NAME
from zope.schema.vocabulary import SimpleVocabulary

import pytest


class TestVocabCampi:
    name = f"{PACKAGE_NAME}.vocab.campi"

    @pytest.fixture(autouse=True)
    def _vocab(self, get_vocabulary, portal, campi):
        self.campi = campi
        self.vocab = get_vocabulary(self.name, portal)

    def test_vocabulary(self):
        assert self.vocab is not None
        assert isinstance(self.vocab, SimpleVocabulary)

    def test_vocabulary_items(self):
        campi_uids = [uid for uid in self.campi]
        tokens = [token for token in self.vocab.by_token]
        assert len(campi_uids) == len(tokens)
        assert campi_uids[0] in tokens
