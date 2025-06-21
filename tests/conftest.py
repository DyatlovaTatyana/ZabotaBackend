import pytest
import requests

from endpoints.zabota_api_client import ZabotaApiClient

@pytest.fixture(scope='session')
def api():
    return ZabotaApiClient(host="https://api.dev.admin-stand-zabotaservice.ru")