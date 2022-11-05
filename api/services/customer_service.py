"""Customer service module"""

from typing import Union

from django.db.models import QuerySet
from django.http.response import Http404
from django.shortcuts import get_object_or_404

from api.entities.customer_entity import CustomerEntity
from app.models import Customer


def get_all_customers() -> QuerySet:
    """Get all Customer from database"""
    return Customer.objects.all()  # pylint: disable=no-member


def create_customer(customer: CustomerEntity) -> None:
    """Create a Customer on the database"""
    Customer.objects.create(  # pylint: disable=no-member
        name=customer.name,
        email=customer.email,
        phone=customer.phone
    )


def get_customer_by_pk(pk) -> Union[Customer, Http404]:  # pylint: disable=invalid-name
    """Get a Customer by pk"""
    return get_object_or_404(Customer, pk=pk)


def update_customer(old_customer: CustomerEntity, new_customer: CustomerEntity) -> None:
    """Update Customer data on the database"""
    old_customer.name = new_customer.name
    old_customer.email = new_customer.email
    old_customer.phone = new_customer.phone
    old_customer.save(force_update=True)


def delete_customer(customer: Customer) -> None:
    """Delete Customer from the database"""
    customer.delete()
