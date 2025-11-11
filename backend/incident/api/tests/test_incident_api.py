import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from incident.domain.models import Incident


@pytest.mark.django_db
class TestIncidentAPI:
    def setup_method(self):
        self.client = APIClient()

    def test_create_incident(self):
        url = reverse("incident-list")
        data = {
            "description": "string",
            "status": "new",
            "source": "operator"
        }
        response = self.client.post(url, data, format="json")
        assert response.status_code == 201
        assert response.data["status"] == "new"

    def test_list_incidents(self):
        Incident.objects.create(status="new")
        url = reverse("incident-list")
        response = self.client.get(url)
        assert response.status_code == 200
        assert len(response.data) >= 1

    def test_change_status(self):
        incident = Incident.objects.create(status="new")
        url = reverse("incident-detail", args=[incident.id])
        data = {"status": "accepted"}
        response = self.client.patch(url, data, format="json")
        assert response.status_code == 200
        assert response.data["status"] == "accepted"