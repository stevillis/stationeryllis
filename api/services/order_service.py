"""Order service module"""

from typing import Union

from django.db.models import QuerySet
from django.http.response import Http404
from django.shortcuts import get_object_or_404

from api.entities.order_entity import OrderEntity
from app.models import Order


def get_all_orders() -> QuerySet:
    """Get all Order from database"""
    return Order.objects.all()  # pylint: disable=no-member


def create_order(order: OrderEntity) -> None:
    """Create a Order on the database"""
    Order.objects.create(  # pylint: disable=no-member
        datetime=order.datetime,
        invoice_number=order.invoice_number,
        customer=order.customer,
        seller=order.seller
    )


def get_order_by_pk(pk) -> Union[Order, Http404]:  # pylint: disable=invalid-name
    """Get a Order by pk"""
    return get_object_or_404(Order, pk=pk)


def update_order(old_order: OrderEntity, new_order: OrderEntity) -> None:
    """Update Order data on the database"""
    old_order.datetime = new_order.datetime
    old_order.invoice_number = new_order.invoice_number
    old_order.customer = new_order.customer
    old_order.seller = new_order.seller
    old_order.save(force_update=True)


def delete_order(order: Order) -> None:
    """Delete Order from the database"""
    order.delete()
