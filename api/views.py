from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Organization, Item, Pricing
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import OrganizationSerializer, ItemSerializer, PricingSerializer


class OrganizationListCreateAPIView(ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class ItemListCreateAPIView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class PricingListCreateAPIView(ListCreateAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer


class PricingDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer


class CalculatePrice(APIView):
    def post(self, request):
        data = request.data
        zone = data.get("zone")
        organization_id = data.get("organization_id")
        total_distance = data.get("total_distance")
        item_type = data.get("item_type")

        try:
            pricing = Pricing.objects.get(
                organization_id=organization_id, zone=zone, item__type=item_type
            )
            base_distance = pricing.base_distance_in_km
            km_price = pricing.km_price
            fix_price = pricing.fix_price

            if total_distance <= base_distance:
                total_price = fix_price
            else:
                total_price = fix_price + ((total_distance - base_distance) * km_price)

            return Response({"total_price": total_price}, status=status.HTTP_200_OK)
        except Pricing.DoesNotExist:
            return Response(
                {"error": "Pricing not found"}, status=status.HTTP_404_NOT_FOUND
            )
