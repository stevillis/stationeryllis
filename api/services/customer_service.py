"""Customer service module"""

from app.models import Customer


def get_all_customers():
    """Get all Customer from database"""
    return Customer.objects.all()  # pylint: disable=no-member
