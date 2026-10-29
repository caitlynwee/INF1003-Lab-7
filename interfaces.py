from abc import ABC, abstractmethod


class CanBeShipped(ABC):
    """Interface-style contract for products that require shipping."""

    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        """Calculate the cost to ship this item."""
        raise NotImplementedError
