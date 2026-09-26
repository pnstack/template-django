import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_ping(client):
    response = client.get(reverse("ping"))
    assert response.status_code == 200
    assert response.json() == "pong"


def test_health(client):
    response = client.get(reverse("health"))
    assert response.json() == {"status": "ok"}


@pytest.mark.django_db
def test_schema(client):
    assert client.get(reverse("schema")).status_code == 200
