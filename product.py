
from abc import ABC, abstractmethod


class Product(ABC):
    """Represent one product and manage its stock."""

    def __init__(self, product_id: str, name: str, price: float, stock: int):
        if not isinstance(product_id, str) or not product_id.strip():
            raise ValueError("Product ID cannot be empty.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if not isinstance(stock, int) or isinstance(stock, bool) or stock < 0:
            raise ValueError("Stock must be a non-negative whole number.")

        self.__product_id = product_id.strip()
        self.__name = name.strip()
        self.__price = float(price)
        self.__stock = stock

    @property
    def product_id(self) -> str:
        return self.__product_id

    def update_stock(self, quantity: int) -> None:
        """Set the stock quantity to a new non-negative total."""
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity < 0:
            raise ValueError("Stock must be a non-negative whole number.")
        self.__stock = quantity

    def display_information(self) -> None:
        print(f"{self.__product_id:<10} {self.__name:<20} ${self.__price:>10.2f} {self.__stock:>8}")

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """Return how this product is fulfilled."""
        raise NotImplementedError

    def to_dict(self) -> dict:
        """Return serializable values without exposing private attributes."""
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
        }
