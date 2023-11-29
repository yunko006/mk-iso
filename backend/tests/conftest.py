import os
from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import create_application
from app.config import get_settings, Settings
from sqlalchemy.orm import sessionmaker

from app.database import engine


@pytest.fixture(scope="module")
def client() -> Generator:
    app = create_application()
    with TestClient(app) as c:
        yield c


def get_settings_override():
    return Settings(testing=1)


# @pytest.fixture(scope="module")
# def test_app():
#     # set up
#     app = create_application()
#     app.dependency_overrides[get_settings] = get_settings_override
#     with TestClient(app) as test_client:
#         # testing
#         yield test_client

#     # tear down


# # new
# @pytest.fixture(scope="module")
# def test_app_with_db():
#     # set up
#     app = create_application()
#     app.dependency_overrides[get_settings] = get_settings_override

#     with TestClient(app) as test_client:
#         # testing
#         yield test_client

#     # tear down
