"""OrderItem entity module."""


class OrderItemEntity:
    """OrderItem Entity"""

    def __init__(self, order_id, product_id, quantity) -> None:
        self.__order_id = order_id
        self.__product_id = product_id
        self.__quantity = quantity

    @property
    def order_id(self):
        """order_id property"""
        return self.__order_id

    @order_id.setter
    def order_id(self, order_id):
        """order_id setter"""
        self.__order_id = order_id

    @property
    def product_id(self):
        """product_id property"""
        return self.__product_id

    @product_id.setter
    def product_id(self, product_id):
        """product_id setter"""
        self.__product_id = product_id

    @property
    def quantity(self):
        """quantity property"""
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        """quantity setter"""
        self.__quantity = quantity
