from product import Product


class Inventory:
    """Manage a collection of Product objects."""

    def __init__(self):
        self.__products = []

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added.")
        if self.search_product(product.product_id) is not None:
            raise ValueError("A product with this ID already exists.")
        self.__products.append(product)

    def search_product(self, product_id: str):
        for product in self.__products:
            if product.product_id.lower() == product_id.strip().lower():
                return product
        return None

    def display_all(self) -> None:
        if not self.__products:
            print("No products in inventory.")
            return

        print(f"{'ID':<10} {'Name':<20} {'Price':>11} {'Stock':>8}")
        print("-" * 53)

        for product in self.__products:
            product.display_information()

    def get_products(self) -> list:
        """Provide a copy of the product list for serialization."""
        return self.__products.copy()
