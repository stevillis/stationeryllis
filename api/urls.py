"""API urls' module"""

from django.urls import path

from api.views.customer_views import CustomerDetail, CustomerList
from api.views.seller_views import SellerDetail, SellerList

urlpatterns = [
    path("customers/", CustomerList.as_view(), name="customers-list"),
    path("customers/<int:pk>", CustomerDetail.as_view(), name="customers-detail"),

    path("sellers/", SellerList.as_view(), name="sellers-list"),
    path("sellers/<int:pk>", SellerDetail.as_view(), name="sellers-detail"),
]
