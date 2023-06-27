from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.restapi.controlpanels import RegistryConfigletPanel
from plonegovbr.portal_base import _
from plonegovbr.portal_base.controlpanel.interfaces import IPBSettings
from plonegovbr.portal_base.interfaces import IBrasilLayer
from zope.component import adapter
from zope.interface import Interface


SCHEMA_PREFIX = "pb"
LABEL = "PortalBrasil: Configurações"


class SettingsEditForm(RegistryEditForm):
    schema = IPBSettings
    schema_prefix = SCHEMA_PREFIX
    label = LABEL


class SettingsControlPanelFormWrapper(ControlPanelFormWrapper):
    form = SettingsEditForm


@adapter(Interface, IBrasilLayer)
class SettingsConfigletPanel(RegistryConfigletPanel):
    """Control Panel endpoint"""

    schema = IPBSettings
    configlet_id = "pb"
    configlet_category_id = "Products"
    title = _(LABEL)
    group = "Products"
    schema_prefix = SCHEMA_PREFIX
