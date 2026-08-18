inventory = {
    "rice": {
        "price": 75.0,
        "quantity": 20
    },
    "milk": {
        "price": 95.0,
        "quantity": 15
    }
}

while True:
    print("\nGrocery Inventory System")
    print("1. Add a new product")
    print("2. Restock an existing product")
    print("3. Sell a product")
    print("4. Display all products and stock values")
    print("5. Display total inventory value")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product = input("Enter product name: ").lower()

        if product in inventory:
            print("Product already exists.")
        else:
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))

            if price < 0 or quantity < 0:
                print("Price and quantity cannot be negative.")
            else:
                inventory[product] = {
                    "price": price,
                    "quantity": quantity
                }
                print("Product added.")

    elif choice == "2":
        product = input("Enter product name: ").lower()

        if product not in inventory:
            print("Product not found.")
        else:
            quantity = int(input("Enter delivery quantity: "))

            if quantity < 0:
                print("Quantity cannot be negative.")
            else:
                inventory[product]["quantity"] += quantity
                print("Stock updated.")

    elif choice == "3":
        product = input("Enter product name: ").lower()

        if product not in inventory:
            print("Product not found.")
        else:
            quantity = int(input("Enter quantity to sell: "))

            if quantity < 0:
                print("Quantity cannot be negative.")
            elif quantity > inventory[product]["quantity"]:
                print("Sale rejected. Not enough stock.")
            else:
                inventory[product]["quantity"] -= quantity
                print("Sale completed.")

    elif choice == "4":
        if len(inventory) == 0:
            print("Inventory is empty.")
        else:
            print("\nProduct Details:")

            for product in sorted(inventory):
                price = inventory[product]["price"]
                quantity = inventory[product]["quantity"]
                stock_value = price * quantity

                print(
                    product,
                    "- Price:", price,
                    "Quantity:", quantity,
                    "Stock Value:", stock_value
                )

    elif choice == "5":
        total_value = 0

        for product in inventory:
            price = inventory[product]["price"]
            quantity = inventory[product]["quantity"]

            total_value += price * quantity

        print("Total inventory value:", total_value)

    elif choice == "6":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")