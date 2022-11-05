"""Customer service module"""

from django.shortcuts import get_object_or_404

from app.models import Customer


def get_all_customers():
    """Get all Customer from database"""
    return Customer.objects.all()  # pylint: disable=no-member


def create_customer(customer):
    """Create a Customer in the database"""
    return Customer.objects.create(  # pylint: disable=no-member
        name=customer.name,
        email=customer.email,
        phone=customer.phone
    )


def get_customer_by_pk(pk):  # pylint: disable=invalid-name
    """Get a Customer by pk"""
    return get_object_or_404(Customer, pk=pk)
