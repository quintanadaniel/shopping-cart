from flask import request

from application.models.data_base import DataBase
from application.models.product import Product


class ProductService:
    def __init__(self, db: DataBase):
        self.db = db

    def create(self, request: request) -> None:

        self.__validate_code(request["code"])
        self.__validate_name(request["name"])
        self.__validate_price(request["price"])

        product = Product(
            code=request["code"], name=request["name"], price=float(request["price"])
        )

        self.db.save_product(product=product)

    def __validate_code(self, code: str) -> None:
        if code is None:
            raise  # TODO create exception

    def __validate_name(self, name: str) -> None:
        if name is None:
            raise  # TODO create exception

    def __validate_price(self, price: float) -> None:
        if price is None:
            raise  # TODO create exception

    def get_by_id(self, request: request) -> Product:
        product_code = request.values["code"]

        if product_code is None:
            # TODO create an exception
            raise

        product: Product = self.db.get_product_by_code(product_code)

        return product
