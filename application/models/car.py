from dataclasses import dataclass
from dataclasses import field
from itertools import count

from typing import Dict
from typing import Optional

from application.models.discount import Discount
from application.models.product import Product


@dataclass
class Car:
    id: int = field(init=False, default=count(1).__next__())
    product: Dict[int, Product]
    discount: Optional[Dict[int, Discount]]
    quantity: float
    status: str
