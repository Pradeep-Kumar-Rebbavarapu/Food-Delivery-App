from django.test import TestCase, Client
from rest_framework import status
import json
from ..models import Pricing, Item, Organization


class CalculatePriceTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Create a pricing object for testing
        self.item = Item.objects.create(type="perishable", description="Test Item")
        self.organization = Organization.objects.create(name="Org1")
        self.pricing = Pricing.objects.create(
            organization=self.organization,
            zone="A",
            base_distance_in_km=5,
            km_price=1.5,
            fix_price=10,
            item=self.item,
        )

    def test_calculate_price_success(self):
        data = {
            "zone": "A",
            "organization_id": self.organization.id,
            "total_distance": 12,
            "item_type": "perishable",
        }
        response = self.client.post(
            "/api/v1/calculate-price/",
            data=json.dumps(data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total_price"], 20.5)

    def test_calculate_price_error_with_zone(self):
        data = {
            "zone": "B",
            "organization_id": self.organization.id,
            "total_distance": 12,
            "item_type": "perishable",
        }
        response = self.client.post(
            "/api/v1/calculate-price/",
            data=json.dumps(data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["error"], "Pricing not found")

    def test_calculate_price_error_with_item_type(self):
        data = {
            "zone": "A",
            "organization_id": self.organization.id,
            "total_distance": 12,
            "item_type": "non-perishable",
        }
        response = self.client.post(
            "/api/v1/calculate-price/",
            data=json.dumps(data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["error"], "Pricing not found")
