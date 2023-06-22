"""Module where all interfaces, events and exceptions live."""
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IPersonLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
