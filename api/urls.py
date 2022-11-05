"""API urls' module"""

from django.urls import path

from api.views.customer_views import CustomerDetail, CustomerList

urlpatterns = [
    path("customers/", CustomerList.as_view(), name="customers-list"),
    path("customers/<int:pk>", CustomerDetail.as_view(), name="customers-detail"),
]
