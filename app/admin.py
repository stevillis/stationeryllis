"""Admin related definitions."""

from django.contrib import admin

from app.models import CommissionParam, Customer, Seller


@admin.register(CommissionParam)
class CommissionParamAdmin(admin.ModelAdmin):
    """CommissionParam Model definitions for Django Admin."""
    fields = ["day_of_the_week", "min_percentage", "max_percentage"]
    list_display = ["day_of_the_week", "min_percentage", "max_percentage"]
    list_filter = ["min_percentage", "max_percentage"]
    search_fields = ["day_of_the_week"]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Customer Model definitions for Django Admin."""
    fields = ["name", "email", "phone"]
    list_display = ["name", "email", "phone"]
    search_fields = ["name", "email", "phone"]


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    """Seller Model definitions for Django Admin."""
    fields = ["name", "email", "phone"]
    list_display = ["name", "email", "phone"]
    search_fields = ["name", "email", "phone"]
