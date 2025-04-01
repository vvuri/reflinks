from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/api/version")
    assert response.status_code == 200
    assert response.json() == {'ver': '0.0.1'}