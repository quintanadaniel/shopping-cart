from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import Optional

from application.models.car import Car
from application.models.product import Product


@dataclass()
class DataBase:
    product: Optional[Dict[str, Product]]
    car: Optional[Dict[int, Car]]

    def save_product(self, product: Product):
        self.product[product.code] = Product(
            code=product.code, name=product.name, price=product.price
        )

    def get_product_by_code(self, code_id: str) -> Product:
        product = self.product[code_id]
        return product
