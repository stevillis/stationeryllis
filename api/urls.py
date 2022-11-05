"""API urls' module"""

from django.urls import path

from api.views.customer_views import CustomerList

urlpatterns = [
    path("customers/", CustomerList.as_view(), name="customers"),
]
