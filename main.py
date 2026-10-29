
from digital_product import DigitalProduct
from file_handling import load_inventory, save_inventory
from physical_product import PhysicalProduct


def read_non_negative_float(message):
    while True:
        try:
            value = float(input(message))
            if value >= 0 and value != float('inf') and value == value:
                return value
        except ValueError:
            pass
        print("Please enter a valid non-negative price.")


def read_non_negative_int(message):
    while True:
        try:
            value = int(input(message))
            if value >= 0:
                return value
        except ValueError:
            pass
        print("Please enter a non-negative whole number.")


def read_product_type():
    while True:
        product_type = input("Enter product type (physical/digital): ").strip().lower()
        if product_type in ("physical", "digital"):
            return product_type
        print("Please enter physical or digital.")


def main():
    try:
        inventory = load_inventory()
        print("Inventory loaded successfully.")
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Unable to load inventory: {error}")
        print("Starting with an empty inventory. Existing file will not be changed unless you save.")
        from inventory import Inventory
        inventory = Inventory()

    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Display all products")
        print("2. Add a product")
        print("3. Update stock")
        print("4. Search for a product")
        print("5. Save inventory")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            product_id = input("Enter product ID: ").strip()
            name = input("Enter product name: ").strip()
            price = read_non_negative_float("Enter price: $")
            stock = read_non_negative_int("Enter stock quantity: ")
            product_type = read_product_type()

            try:
                if product_type == "physical":
                    extra_value = read_non_negative_float("Enter weight (kg): ")
                    product = PhysicalProduct(product_id, name, price, stock, extra_value)
                else:
                    extra_value = read_non_negative_float("Enter download size (MB): ")
                    product = DigitalProduct(product_id, name, price, stock, extra_value)
                inventory.add_product(product)
                print("Product added successfully!")
            except (ValueError, TypeError) as error:
                print(f"Could not add product: {error}")

        elif choice == "3":
            product_id = input("Enter product ID to update: ").strip()
            product = inventory.search_product(product_id)

            if product is None:
                print("Product not found.")
            else:
                quantity = read_non_negative_int("Enter new total stock quantity: ")
                product.update_stock(quantity)
                print("Stock updated successfully!")

        elif choice == "4":
            product_id = input("Enter product ID to search: ").strip()
            product = inventory.search_product(product_id)

            if product is None:
                print("Product not found.")
            else:
                print(f"{'ID':<10} {'Name':<20} {'Price':>11} {'Stock':>8}")
                print("-" * 53)
                product.display_information()

        elif choice == "5":
            try:
                save_inventory(inventory)
                print("Inventory saved successfully!")
            except OSError as error:
                print(f"Could not save inventory: {error}")

        elif choice == "6":
            print("Goodbye! Save first using option 5 if you want to keep changes.")
            break

        else:
            print("Invalid option. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
