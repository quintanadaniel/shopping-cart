import unittest

from application.models.data_base import DataBase
from application.models.product import Product
from application.product.product_service import ProductService


class TestProductService(unittest.TestCase):
    def setUp(self) -> None:
        self.db = DataBase(product={}, car=None)
        self.product_service = ProductService(self.db)

    def test_create(self):
        request = {"code": "T-SHIRT-A1", "name": "t-shirt", "price": 12.12}
        self.product_service.create(request)

        self.assertTrue(self.db.product)
        self.assertCountEqual(
            {"T-SHIRT-A1": Product(code="T-SHIRT-A1", name="t-shirt", price=12.12)},
            self.db.product,
        )

    def test_create_when_code_is_none_with_raises_exception(self):
        pass

    def test_create_when_name_is_none_with_raises_exception(self):
        pass

    def test_create_when_price_is_none_with_raises_exception(self):
        pass
