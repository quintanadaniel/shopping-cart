from dataclasses import dataclass
from typing import Dict
from typing import Optional

from application.exceptions.ProductInvalidKeyErrorException import ProductIsInvalidKeyException
from application.models.car import Car
from application.models.product import Product


@dataclass()
class DataBase:
    """Clas to defined an object Data Base"""
    product: Optional[Dict[str, Product]]
    car: Optional[Dict[int, Car]]

    def save_product(self, product: Product):
        """Save Products"""
        self.product[product.code] = Product(
            code=product.code, name=product.name, price=product.price
        )

    def get_product_by_code(self, code_id: str) -> Optional[Product]:
        """Get product by code_id"""
        try:
            product = self.product[code_id]
            return product
        except BaseException:
            raise ProductIsInvalidKeyException(code_id)
