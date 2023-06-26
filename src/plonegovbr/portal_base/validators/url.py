# -*- coding: utf-8 -*-
from urllib.parse import urlparse

from plonegovbr.portal_base import _
from zope.schema import ValidationError


class InvalidURL(ValidationError):
    """Exception for invalid url"""
    __doc__ = _('Invalid URL.')


class UrlValidator:

    def __init__(self, value):
        self.value = value
        self._validator()

    def _validator(self):
        parse = urlparse(self.value)
        schema = parse.scheme
        hostname = parse.hostname
        if schema not in ['http', 'https'] or not hostname:
            raise InvalidURL()
