from dataclasses import dataclass
from typing import Dict
from typing import Optional

from application.models.car import Car
from application.models.product import Product


@dataclass()
class DataBase:
    product: Optional[Dict[int, Product]]
    car: Optional[Dict[int, Car]]
