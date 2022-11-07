"""Product entity module."""


class ProductEntity:
    """Product Entity"""

    def __init__(self, description, unit_price, commission_percentage) -> None:
        self.__description = description
        self.__unit_price = unit_price
        self.__commission_percentage = commission_percentage

    @property
    def description(self):
        """Name property"""
        return self.__description

    @description.setter
    def description(self, description):
        """Name setter"""
        self.__description = description

    @property
    def unit_price(self):
        """Email property"""
        return self.__unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Email setter"""
        self.__unit_price = unit_price

    @property
    def commission_percentage(self):
        """Phone property"""
        return self.__commission_percentage

    @commission_percentage.setter
    def commission_percentage(self, commission_percentage):
        """Phone setter"""
        self.__commission_percentage = commission_percentage
