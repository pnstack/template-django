import pytest


@pytest.fixture(autouse=True)
def _no_ssl_redirect(settings):
    settings.SECURE_SSL_REDIRECT = False
