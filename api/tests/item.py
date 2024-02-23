from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Item, Pricing


class ItemAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item_data = {"type": "perishable", "description": "Test Item"}

    def test_create_item(self):
        response = self.client.post("/api/v1/items/", self.item_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_item_list(self):
        response = self.client.get("/api/v1/items/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_item_detail(self):
        item = Item.objects.create(type="perishable", description="Test Item")
        response = self.client.get(f"/api/v1/items/{item.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item(self):
        item = Item.objects.create(type="perishable", description="Test Item")
        updated_data = {"type": "non-perishable", "description": "Updated Item"}
        response = self.client.put(
            f"/api/v1/items/{item.id}/", updated_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_item(self):
        item = Item.objects.create(type="perishable", description="Test Item")
        response = self.client.delete(f"/api/v1/items/{item.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
