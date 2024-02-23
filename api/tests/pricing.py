from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Pricing, Organization, Item


class PricingAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.org = Organization.objects.create(name="Org1")
        self.item = Item.objects.create(type="perishable", description="Test Item")
        self.pricing_data = {
            "organization": self.org.id,
            "item": self.item.id,
            "zone": "central",
            "base_distance_in_km": 5,
            "km_price": 1.5,
            "fix_price": 10,
        }

    def test_create_pricing(self):
        response = self.client.post(
            "/api/v1/pricing/", self.pricing_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_pricing_list(self):
        response = self.client.get("/api/v1/pricing/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_pricing_detail(self):
        pricing = Pricing.objects.create(
            organization=self.org,
            item=self.item,
            zone="central",
            base_distance_in_km=5,
            km_price=1.5,
            fix_price=10,
        )
        response = self.client.get(f"/api/v1/pricing/{pricing.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_pricing(self):
        pricing = Pricing.objects.create(
            organization=self.org,
            item=self.item,
            zone="central",
            base_distance_in_km=5,
            km_price=1.5,
            fix_price=10,
        )
        updated_data = {
            "organization": self.org.id,
            "item": self.item.id,
            "zone": "central",
            "base_distance_in_km": 10,
            "km_price": 2.5,
            "fix_price": 15,
        }
        response = self.client.put(
            f"/api/v1/pricing/{pricing.id}/", updated_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_pricing(self):
        pricing = Pricing.objects.create(
            organization=self.org,
            item=self.item,
            zone="central",
            base_distance_in_km=5,
            km_price=1.5,
            fix_price=10,
        )
        response = self.client.delete(f"/api/v1/pricing/{pricing.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
