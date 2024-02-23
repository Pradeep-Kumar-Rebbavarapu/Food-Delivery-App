from django.urls import path
from .views import (
    CalculatePrice,
    OrganizationListCreateAPIView,
    OrganizationDetailAPIView,
    ItemListCreateAPIView,
    ItemDetailAPIView,
    PricingListCreateAPIView,
    PricingDetailAPIView,
)

urlpatterns = [
    # Organization URLs
    path(
        "organizations/",
        OrganizationListCreateAPIView.as_view(),
        name="organization-list",
    ),
    path(
        "organizations/<int:pk>/",
        OrganizationDetailAPIView.as_view(),
        name="organization-detail",
    ),
    # Item URLs
    path("items/", ItemListCreateAPIView.as_view(), name="item-list"),
    path("items/<int:pk>/", ItemDetailAPIView.as_view(), name="item-detail"),
    # Pricing URLs
    path("pricing/", PricingListCreateAPIView.as_view(), name="pricing-list"),
    path("pricing/<int:pk>/", PricingDetailAPIView.as_view(), name="pricing-detail"),
    # calculate price URLs
    path("calculate-price/", CalculatePrice.as_view(), name="calculate_price"),
]
