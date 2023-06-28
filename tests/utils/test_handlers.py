from plonegovbr.portal_base.utils import handlers


class TestHandlers:
    def test_ajusta_idioma(self, portal):
        portal.setLanguage("en")
        handlers.ajusta_idioma(portal)
        assert portal.language == "pt-br"

    def test_converte_logo_data(self):
        logo = "name=teste;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=="
        result = handlers.converte_logo_data(logo)
        expected_result = b"filenameb64:dGVzdGU7ZGF0YTppbWFnZS9wbmc=;datab64:iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=="
        assert result == expected_result
