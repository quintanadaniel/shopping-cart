from typing import Optional

from flask import request

from application.exceptions.product_is_invalid_exception import (
    ProductIsInvalidException,
)
from application.exceptions.product_is_none_exception import ProductIsNoneException
from application.models.data_base import DataBase
from application.models.product import Product


class ProductService:
    """Class object to include all the services about Products"""

    def __init__(self, database: DataBase):
        self.database = database

    def create(self, req: request) -> None:
        """Method to create new Products"""
        self.__validate_code(req["code"])
        self.__validate_name(req["name"])
        self.__validate_price(req["price"])

        product = Product(code=req["code"], name=req["name"], price=float(req["price"]))

        self.database.save_product(product=product)

    @staticmethod
    def __validate_code(code: str) -> None:
        if code is None or code == "":
            raise ProductIsNoneException("code")
        if not isinstance(code, str):
            raise ProductIsInvalidException("code")

    @staticmethod
    def __validate_name(name: str) -> None:
        if name is None or name == "":
            raise ProductIsNoneException("name")
        if not isinstance(name, str):
            raise ProductIsInvalidException("name")

    @staticmethod
    def __validate_price(price: float) -> None:
        if price is None:
            raise ProductIsNoneException("price")
        if not isinstance(price, float):
            raise ProductIsInvalidException("price")

    def get_by_id(self, code: str) -> Product:
        """Find in the database product by id and return a Product object"""
        product: Optional[Product] = self.database.get_product_by_code(code)

        if code is None:
            raise ProductIsNoneException("code")

        return product
