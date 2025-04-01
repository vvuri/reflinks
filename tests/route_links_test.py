from fastapi.testclient import TestClient
from pydantic import HttpUrl

from app.main import app
from app.models.links import ClientUrlLink

client = TestClient(app)


def test_read_main():
    response = client.get("/api/version")
    assert response.status_code == 200
    assert response.json() == {"ver": "0.0.1"}


def test_get_link_by_id():
    response = client.get("/api/link/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


# def test_link_add():
#     fakedata = ClientUrlLink(url=HttpUrl("http://vvuri.ru"))
#     response = client.post("/api/link/add", content=fakedata)
#     assert response.status_code == 200
