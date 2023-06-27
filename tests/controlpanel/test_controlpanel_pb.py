import pytest


class TestControlPanelPB:
    CONFIGLET_ID: str = "pb"

    @pytest.fixture(autouse=True)
    def _init(self, portal):
        self.portal = portal
        self.control_panels = portal["portal_controlpanel"]
        filtered = [
            configlet
            for configlet in self.control_panels.listActions()
            if configlet.id == self.CONFIGLET_ID
        ]
        self.control_panel = filtered[0] if filtered else None

    def test_pb_exists(self):
        assert self.control_panel

    def test_pb_is_visible(self):
        assert self.control_panel.visible

    @pytest.mark.parametrize(
        "attr,expected",
        [
            ["appId", "pb-controlpanel"],
            ["id", "pb"],
            ["title", "PortalBrasil: Configurações"],
        ],
    )
    def test_controlpanel_attributes(self, attr, expected):
        assert getattr(self.control_panel, attr, None) == expected
