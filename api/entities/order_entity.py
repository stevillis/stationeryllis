"""Order entity module."""


class OrderEntity:
    """Order Entity"""

    def __init__(self, datetime, invoice_number, customer, seller) -> None:
        self.__datetime = datetime
        self.__invoice_number = invoice_number
        self.__customer = customer
        self.__seller = seller

    @property
    def datetime(self):
        """datetime property"""
        return self.__datetime

    @datetime.setter
    def datetime(self, datetime):
        """datetime setter"""
        self.__datetime = datetime

    @property
    def invoice_number(self):
        """invoice_number property"""
        return self.__invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """invoice_number setter"""
        self.__invoice_number = invoice_number

    @property
    def customer(self):
        """customer property"""
        return self.__customer

    @customer.setter
    def customer(self, customer):
        """customer setter"""
        self.__customer = customer

    @property
    def seller(self):
        """seller property"""
        return self.__seller

    @seller.setter
    def seller(self, seller):
        """seller setter"""
        self.__seller = seller
