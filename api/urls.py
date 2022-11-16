"""API urls' module"""

from django.urls import path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

from api.views.customer_views import CustomerDetail, CustomerList
from api.views.order_views import OrderDetail, OrderList
from api.views.product_views import ProductDetail, ProductList
from api.views.seller_views import SellerDetail, SellerList
from api.views.user_views import UserList

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path("customers/", CustomerList.as_view(), name="customers-list"),
    path("customers/<int:pk>", CustomerDetail.as_view(), name="customers-detail"),

    path("sellers/", SellerList.as_view(), name="sellers-list"),
    path("sellers/<int:pk>", SellerDetail.as_view(), name="sellers-detail"),

    path("products/", ProductList.as_view(), name="products-list"),
    path("products/<int:pk>", ProductDetail.as_view(), name="products-detail"),

    path("orders/", OrderList.as_view(), name="orders-list"),
    path("orders/<int:pk>", OrderDetail.as_view(), name="orders-detail"),

    path("users/", UserList.as_view(), name="users-list"),
]
