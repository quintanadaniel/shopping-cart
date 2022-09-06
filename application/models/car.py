from dataclasses import dataclass
from typing import Dict
from typing import Optional

from application.models.discount import Discount
from application.models.product import Product


@dataclass
class Car:
    id: int
    product: Dict[int, Product]
    discount: Optional[Dict[int, Discount]]
    quantity: float
    status: str
