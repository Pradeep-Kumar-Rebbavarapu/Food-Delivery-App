from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Organization


class OrganizationAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.organization_data = {"name": "Org1"}

    def test_create_organization(self):
        response = self.client.post(
            "/api/v1/organizations/", self.organization_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_organization_list(self):
        response = self.client.get("/api/v1/organizations/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_organization_detail(self):
        organization = Organization.objects.create(name="Test Org")
        response = self.client.get(f"/api/v1/organizations/{organization.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_organization(self):
        organization = Organization.objects.create(name="Test Org")
        updated_data = {"name": "Updated Org"}
        response = self.client.put(
            f"/api/v1/organizations/{organization.id}/", updated_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_organization(self):
        organization = Organization.objects.create(name="Test Org")
        response = self.client.delete(f"/api/v1/organizations/{organization.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
