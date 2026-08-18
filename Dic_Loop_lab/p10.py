prices = {
    "rice": 75.0,
    "oil": 185.0,
    "milk": 95.0,
    "eggs": 12.0
}

quantities = {
    "rice": 20,
    "oil": 10,
    "milk": 15,
    "eggs": 60
}

total_inventory_value = 0
highest_product = ""
highest_value = 0

for product in prices:
    stock_value = prices[product] * quantities[product]

    print(product, ":", stock_value)

    total_inventory_value += stock_value

    if stock_value > highest_value:
        highest_value = stock_value
        highest_product = product

print("Total inventory value:", total_inventory_value)
print("Product with greatest stock value:", highest_product)
print("Greatest stock value:", highest_value)