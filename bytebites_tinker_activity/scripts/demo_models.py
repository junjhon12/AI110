from datetime import datetime
from models import Drinks, Desserts, Sides, Main, ItemCollection, Transaction, Customer


def main():
    cola = Drinks(name="Cola", price=1.99, category="Drinks", size="LARGE", is_carbonated=True)
    burger = Main(name="Spicy Burger", price=8.5, category="Main", spice_level="Hot", is_vegetarian=False)
    fries = Sides(name="Fries", price=2.5, category="Sides", portion_size="Medium")
    cake = Desserts(name="Chocolate Cake", price=4.0, category="Desserts", calories=450)

    menu = ItemCollection()
    for item in (cola, burger, fries, cake):
        menu.add(item)

    print("Menu items:")
    for it in menu.items:
        print(f"- {it.name} ({it.category}): ${it.get_price():.2f}")

    tx = Transaction()
    tx.add_item(cola)
    tx.add_item(burger)
    print(f"Transaction total: ${tx.total:.2f}")

    customer = Customer(name="Alex")
    customer.add_transaction(tx)

    print(f"Customer {customer.name} has {len(customer.purchase_history)} transactions.")


if __name__ == "__main__":
    main()
