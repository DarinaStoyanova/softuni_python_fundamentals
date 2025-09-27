command = input()
stock = {}

while True:
    if command == "statistics":
        break
    command = command.split(": ")
    product = command[0]
    quantity = command[1]
    if product in stock:
        stock[product] += int(quantity)
    else:
        stock[product] = int(quantity)

    command = input()

count_all_products = len(stock)
sum_all_quantities = sum(stock.values())
print("Products in stock:")
for product, quantity in stock.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {count_all_products}")
print(f"Total Quantity: {sum_all_quantities}")