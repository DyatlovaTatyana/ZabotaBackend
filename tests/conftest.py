import pytest
import requests
from dotenv import load_dotenv
import os
from faker import Faker

from db_client.dbclient import PgClient
# from db_client.dbclient import PgClient
from dbsteps.dbsteps import DbSteps
from api_clients.zabota_api_client import ZabotaApiClient
from config import project_config


load_dotenv()

@pytest.fixture(scope='session')
def fake():
    return Faker("ru_RU")

@pytest.fixture(scope='session')
def api():
    host = project_config.api_host_admin
    return ZabotaApiClient(host=host)


@pytest.fixture(scope="session")
def db():
    host = project_config.db_host
    user = project_config.db_user
    password = project_config.db_password
    port = project_config.db_port
    db_name = project_config.db_name
    with PgClient(host=host, user=user,
                  password=password,
                  port=port, db_name=db_name) as client:
        yield DbSteps(client)