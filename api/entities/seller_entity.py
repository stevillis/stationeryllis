"""Seller entity module."""


class SellerEntity:
    """Seller Entity"""

    def __init__(self, name, email, phone) -> None:
        self.__name = name
        self.__email = email
        self.__phone = phone

    @property
    def name(self):
        """Name property"""
        return self.__name

    @name.setter
    def name(self, name):
        """Name setter"""
        self.__name = name

    @property
    def email(self):
        """Email property"""
        return self.__email

    @email.setter
    def email(self, email):
        """Email setter"""
        self.__email = email

    @property
    def phone(self):
        """Phone property"""
        return self.__phone

    @phone.setter
    def phone(self, phone):
        """Phone setter"""
        self.__phone = phone
