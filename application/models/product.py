from dataclasses import dataclass
from dataclasses import field
from itertools import count


@dataclass()
class Product:
    id: int = field(init=False, default=count(1).__next__())
    code: str
    name: str
    price: float
