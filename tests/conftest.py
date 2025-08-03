import pytest
import requests
from dotenv import load_dotenv
import os

from dbclient.dbclient import PgClient
from dbsteps.dbsteps import DbSteps
from api_clients.zabota_api_client import ZabotaApiClient

@pytest.fixture(scope='session')
def api():
    return ZabotaApiClient(host="https://api.dev.admin-stand-zabotaservice.ru")


@pytest.fixture(scope="session")
def db():
    load_dotenv()
    host = os.getenv('HOST')
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    port = os.getenv('PORT')
    db_name = os.getenv('DB_NAME')
    with PgClient(host=host, user=user,
                  password=password,
                  port=port, db_name=db_name) as client:
        yield DbSteps(client)