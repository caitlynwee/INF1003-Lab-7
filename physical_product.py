import math

from interfaces import CanBeShipped
from product import Product


class PhysicalProduct(Product, CanBeShipped):
    """A product that is stored and shipped physically."""

    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float):
        super().__init__(product_id, name, price, stock)
        if (
            not isinstance(weight, (int, float))
            or isinstance(weight, bool)
            or not math.isfinite(weight)
            or weight < 0
        ):
            raise ValueError("Weight must be a non-negative number.")
        self.__weight = float(weight)

    @property
    def weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        super().display_information()
        print(f"           Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return round(self.__weight * 5.0, 2)

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({"type": "physical", "weight": self.__weight})
        return data
