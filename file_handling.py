
"""Read and write JSON inventory records separately from product management."""

import json
from pathlib import Path
from inventory import Inventory
from digital_product import DigitalProduct
from physical_product import PhysicalProduct
from product import Product

DATA_FILE = Path(__file__).with_name("inventory.json")


def save_inventory(inventory: Inventory, filename=DATA_FILE) -> None:
    products = [product.to_dict() for product in inventory.get_products()]

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(products, file, indent=4)


def load_inventory(filename=DATA_FILE) -> Inventory:
    inventory = Inventory()

    if not Path(filename).exists():
        return inventory

    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("Inventory JSON must contain a list of products.")

    for item in data:
        product_type = item.get("type")
        product_class = {
            "physical": PhysicalProduct,
            "digital": DigitalProduct,
        }.get(product_type)
        if product_class is None:
            raise ValueError(f"Unknown product type: {product_type!r}.")

        extra_field = "weight" if product_type == "physical" else "download_size"
        inventory.add_product(product_class(
            item["product_id"],
            item["name"],
            item["price"],
            item["stock"],
            item[extra_field],
        ))

    return inventory
