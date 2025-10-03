products_with_prices = {}

command = input()
while command != "buy":
    products = command.split(" ")
    key = products[0]
    price = float(products[1])
    quantity = int(products[2])

    if key in products_with_prices:
        products_with_prices[key]["quantity"] += quantity
        if products_with_prices[key]["price"] != price:
            products_with_prices[key]["price"] = price

    else:
        products_with_prices[key] = {"price": price, "quantity": quantity}

    command = input()

for key in products_with_prices:
    value_no_format = products_with_prices[key]["price"] * products_with_prices[key]["quantity"]
    value = f"{value_no_format:.2f}"
    print(f"{key} -> {value}")