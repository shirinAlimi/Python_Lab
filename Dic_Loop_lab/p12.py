stock = {
    "pen": 25,
    "notebook": 12,
    "marker": 8
}

delivery = {
    "notebook": 10,
    "marker": 5,
    "eraser": 20
}

for product, quantity in delivery.items():
    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity

total_items = 0

print("Updated stock:")

for product in sorted(stock):
    print(product, ":", stock[product])
    total_items += stock[product]

print("Total number of items:", total_items)