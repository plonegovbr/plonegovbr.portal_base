from plonegovbr.portal_base import _
from zope.schema import ValidationError

import validators


class InvalidURL(ValidationError):
    """Exception for invalid url"""

    __doc__ = _("Invalid URL.")


class UrlValidator:
    def __init__(self, value):
        self.value = value
        self._validator()

    def _validator(self):
        if not validators.url(self.value):
            raise InvalidURL()
