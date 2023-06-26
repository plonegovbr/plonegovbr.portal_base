from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.restapi.controlpanels import RegistryConfigletPanel
from plonegovbr.portal_base import _
from plonegovbr.portal_base.controlpanel.interfaces import IEduSettings
from plonegovbr.portal_base.interfaces import IBrasilLayer
from zope.component import adapter
from zope.interface import Interface


SCHEMA_PREFIX = "pb_edu"
LABEL = "PortalBrasil.edu: Configurações"


class SettingsEditForm(RegistryEditForm):
    schema = IEduSettings
    schema_prefix = SCHEMA_PREFIX
    label = LABEL


class SettingsControlPanelFormWrapper(ControlPanelFormWrapper):
    form = SettingsEditForm


@adapter(Interface, IBrasilLayer)
class SettingsConfigletPanel(RegistryConfigletPanel):
    """Control Panel endpoint"""

    schema = IEduSettings
    configlet_id = "pb_edu"
    configlet_category_id = "Products"
    title = _(LABEL)
    group = "Products"
    schema_prefix = SCHEMA_PREFIX
