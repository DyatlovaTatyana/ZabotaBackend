import pytest
import requests
from dotenv import load_dotenv
import os
from faker import Faker
from dbclient.dbclient import PgClient
from dbsteps.dbsteps import DbSteps
from api_clients.zabota_api_client import ZabotaApiClient
from config import Dbconfig
from config import Adminconfig

load_dotenv()

@pytest.fixture(scope='session')
def fake():
    return Faker("ru_RU")

@pytest.fixture(scope='session')
def api():
    host = Adminconfig.host_admin
    return ZabotaApiClient(host=host)


@pytest.fixture(scope="session")
def db():
    host = Dbconfig.host
    user = Dbconfig.user
    password = Dbconfig.password
    port = Dbconfig.port
    db_name = Dbconfig.db_name
    with PgClient(host=host, user=user,
                  password=password,
                  port=port, db_name=db_name) as client:
        yield DbSteps(client)