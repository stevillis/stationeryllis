"""API urls' module"""

from django.urls import path

from api.views.customer_views import CustomerDetail, CustomerList
from api.views.order_views import OrderDetail, OrderList
from api.views.product_views import ProductDetail, ProductList
from api.views.seller_views import SellerDetail, SellerList

urlpatterns = [
    path("customers/", CustomerList.as_view(), name="customers-list"),
    path("customers/<int:pk>", CustomerDetail.as_view(), name="customers-detail"),

    path("sellers/", SellerList.as_view(), name="sellers-list"),
    path("sellers/<int:pk>", SellerDetail.as_view(), name="sellers-detail"),

    path("products/", ProductList.as_view(), name="products-list"),
    path("products/<int:pk>", ProductDetail.as_view(), name="products-detail"),

    path("orders/", OrderList.as_view(), name="orders-list"),
    path("orders/<int:pk>", OrderDetail.as_view(), name="orders-detail"),
]
