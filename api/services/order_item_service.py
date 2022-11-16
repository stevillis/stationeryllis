"""OrderItem service module"""

from typing import Union

from django.db.models import QuerySet
from django.http.response import Http404
from django.shortcuts import get_object_or_404

from api.entities.order_item_entity import OrderItemEntity
from app.models import OrderItem


def get_all_order_items() -> QuerySet:
    """Get all OrderItem from database"""
    return OrderItem.objects.all()  # pylint: disable=no-member


def create_order_item(order_id, product_id, quantity) -> None:
    """Create a OrderItem on the database"""
    OrderItem.objects.create(  # pylint: disable=no-member
        order_id=order_id, product_id=product_id, quantity=quantity
    )


def get_order_item_by_pk(
    pk,
) -> Union[OrderItem, Http404]:  # pylint: disable=invalid-name
    """Get a OrderItem by pk"""
    return get_object_or_404(OrderItem, pk=pk)


def get_order_items_by_order(
    order,
) -> Union[QuerySet, Http404]:  # pylint: disable=invalid-name
    """Get OrderItem objects that match order"""
    return OrderItem.objects.filter(order=order)  # pylint: disable=no-member


def update_order_item(
    old_order_item: OrderItemEntity, new_order_item: OrderItemEntity
) -> None:
    """Update OrderItem data on the database"""
    old_order_item.order = new_order_item.order
    old_order_item.product = new_order_item.product
    old_order_item.quantity = new_order_item.quantity
    old_order_item.save(force_update=True)


def delete_order_item(order_item: OrderItem) -> None:
    """Delete OrderItem from the database"""
    order_item.delete()
