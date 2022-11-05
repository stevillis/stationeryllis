"""Customer service module"""

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
