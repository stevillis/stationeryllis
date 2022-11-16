"""Product service module"""

from typing import Union

from django.db.models import QuerySet
from django.http.response import Http404
from django.shortcuts import get_object_or_404

from api.entities.product_entity import ProductEntity
from app.models import Product


def get_all_products() -> QuerySet:
    """Get all Product from database"""
    return Product.objects.all()  # pylint: disable=no-member


def create_product(product: ProductEntity) -> None:
    """Create a Product on the database"""
    Product.objects.create(  # pylint: disable=no-member
        description=product.description,
        unit_price=product.unit_price,
        commission_percentage=product.commission_percentage,
    )


def get_product_by_pk(pk) -> Union[Product, Http404]:  # pylint: disable=invalid-name
    """Get a Product by pk"""
    return get_object_or_404(Product, pk=pk)


def update_product(old_product: ProductEntity, new_product: ProductEntity) -> None:
    """Update Product data on the database"""
    old_product.description = new_product.description
    old_product.unit_price = new_product.unit_price
    old_product.commission_percentage = new_product.commission_percentage
    old_product.save(force_update=True)


def delete_product(product: Product) -> None:
    """Delete Product from the database"""
    product.delete()
