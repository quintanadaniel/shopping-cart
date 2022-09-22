import unittest

from application.exceptions.product_is_invalid_exception import (
    ProductIsInvalidException,
)
from application.exceptions.product_is_none_exception import ProductIsNoneException
from application.models.data_base import DataBase
from application.models.product import Product
from application.product.product_service import ProductService


class TestProductService(unittest.TestCase):
    def setUp(self) -> None:
        self.db = DataBase(product={}, car=None)
        self.product_service = ProductService(self.db)

        self.db.product["T-SHIRT-B1"] = Product(
            code="T-SHIRT-B1", name="t-shirt", price=12.12
        )

    def test_create_when_code_is_none_with_raises_exception(self):
        request = {"code": None, "name": "t-shirt", "price": 12.12}
        with self.assertRaises(ProductIsNoneException):
            self.product_service.create(request)

    def test_create_when_code_is_invalid_with_raises_exception(self):
        request = {"code": 111, "name": "t-shirt", "price": 12.12}
        with self.assertRaises(ProductIsInvalidException):
            self.product_service.create(request)

    def test_create_when_name_is_none_with_raises_exception(self):
        request = {"code": "T-SHIRT-A1", "name": "", "price": 12.12}
        with self.assertRaises(ProductIsNoneException):
            self.product_service.create(request)

    def test_create_when_name_is_invalid_with_raises_exception(self):
        request = {"code": "T-SHIRT-A1", "name": 111, "price": 12.12}
        with self.assertRaises(ProductIsInvalidException):
            self.product_service.create(request)

    def test_create_when_price_is_none_with_raises_exception(self):
        request = {"code": "T-SHIRT-A1", "name": "t-shirt", "price": None}
        with self.assertRaises(ProductIsNoneException):
            self.product_service.create(request)

    def test_create_when_price_is_invalid_with_raises_exception(self):
        request = {"code": "T-SHIRT-A1", "name": "t-shirt", "price": 12}
        with self.assertRaises(ProductIsInvalidException):
            self.product_service.create(request)

    def test_create(self):
        request = {"code": "T-SHIRT-A1", "name": "t-shirt", "price": 12.12}
        self.product_service.create(request)

        self.assertTrue(self.db.product)
        self.assertCountEqual(
            {
                "T-SHIRT-B1": Product(code="T-SHIRT-B1", name="t-shirt", price=12.12),
                "T-SHIRT-A1": Product(code="T-SHIRT-A1", name="t-shirt", price=12.12),
            },
            self.db.product,
        )

    def test_get_by_id_when_is_none_exception(self):
        with self.assertRaises(ProductIsInvalidException):
            self.product_service.get_by_id("test")

    def test_get_by_id(self):
        self.product_service.get_by_id("T-SHIRT-B1")

        self.assertCountEqual(
            {"T-SHIRT-B1": Product(code="T-SHIRT-B1", name="t-shirt", price=12.12)},
            self.db.product,
        )
