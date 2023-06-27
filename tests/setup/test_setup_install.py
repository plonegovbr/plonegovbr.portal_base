from plone import api
from plonegovbr.portal_base import PACKAGE_NAME

import pytest


class TestSetupInstall:
    def test_addon_installed(self, installer):
        assert installer.is_product_installed(PACKAGE_NAME) is True

    def test_latest_version(self, profile_last_version):
        """Test latest version of default profile."""
        assert profile_last_version(f"{PACKAGE_NAME}:default") == "1000"

    @pytest.mark.parametrize("package_name", ["collective.person"])
    def test_dependency_installed(self, installer, package_name):
        """Test dependencies are installed."""
        assert installer.is_product_installed(package_name) is True

    @pytest.mark.parametrize(
        "key,expected",
        [
            ["contact.default_country", "BR"],
        ],
    )
    def test_registry_keys(self, installer, key, expected):
        """Test if registry keys are set."""
        value = api.portal.get_registry_record(key, default=None)
        assert value == expected
