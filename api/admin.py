from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Organization, Item, Pricing


class CustomAdminSite(AdminSite):
    site_header = "Custom Admin Header"
    site_title = "Custom Admin Title"
    index_title = "Custom Admin Index"


custom_admin_site = CustomAdminSite(name="custom_admin")


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("type", "description")
    search_fields = ("type", "description")


@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = (
        "organization",
        "item",
        "zone",
        "base_distance_in_km",
        "km_price",
        "fix_price",
    )
    list_filter = ("organization", "item", "zone")
    search_fields = ("organization__name", "item__type", "zone")
    fieldsets = (
        (None, {"fields": ("organization", "item", "zone")}),
        (
            "Pricing Details",
            {"fields": ("base_distance_in_km", "km_price", "fix_price")},
        ),
    )
