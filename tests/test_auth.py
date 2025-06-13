from fastapi.testclient import TestClient
from main import app  # your FastAPI app

client = TestClient(app)

def test_register_and_login():
    # register
    res = client.post("/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123"
    })
    assert res.status_code == 200

    # login
    res = client.post("/login", data={
        "username": "testuser",
        "password": "password123"
    })
    assert res.status_code == 200
    assert "access_token" in res.json()
