import requests


class BaseClient:
    def check_status(self, response, status):
        assert response.status_code == status