import pytest
from sqlalchemy import insert, select
from tests.conftest import client, async_session_maker


def test_register():
    response = client.post("/auth/register", json={
            "email": "string",
            "password": "string",
            "is_active": True,
            "is_superuser": False,
            "is_verified": False,
            "username": "string"
    })

    assert response.status_code == 201
