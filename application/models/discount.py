from dataclasses import dataclass
from dataclasses import field


@dataclass
class Discount:
    code: str
    name: str
    prince: float
    available: bool = field(default=True)
