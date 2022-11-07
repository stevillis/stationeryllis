"""Seller service module"""

from typing import Union

from django.db.models import QuerySet
from django.http.response import Http404
from django.shortcuts import get_object_or_404

from api.entities.seller_entity import SellerEntity
from app.models import Seller


def get_all_sellers() -> QuerySet:
    """Get all Seller from database"""
    return Seller.objects.all()  # pylint: disable=no-member


def create_seller(seller: SellerEntity) -> None:
    """Create a Seller on the database"""
    Seller.objects.create(  # pylint: disable=no-member
        name=seller.name,
        email=seller.email,
        phone=seller.phone
    )


def get_seller_by_pk(pk) -> Union[Seller, Http404]:  # pylint: disable=invalid-name
    """Get a Seller by pk"""
    return get_object_or_404(Seller, pk=pk)


def update_seller(old_seller: SellerEntity, new_seller: SellerEntity) -> None:
    """Update Seller data on the database"""
    old_seller.name = new_seller.name
    old_seller.email = new_seller.email
    old_seller.phone = new_seller.phone
    old_seller.save(force_update=True)


def delete_seller(seller: Seller) -> None:
    """Delete Seller from the database"""
    seller.delete()
