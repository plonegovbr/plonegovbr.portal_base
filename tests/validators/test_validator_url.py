from plonegovbr.portal_base.validators.url import InvalidURL
from plonegovbr.portal_base.validators.url import UrlValidator

import pytest


class TestValidatorURL:
    def test_valid_url(self):
        """Test if the URL is valid."""
        assert UrlValidator("https://plone.org.br")

    def test_invalid_url(self):
        """Test if the URL not is valid."""
        with pytest.raises(InvalidURL):
            UrlValidator("https://xpto")
