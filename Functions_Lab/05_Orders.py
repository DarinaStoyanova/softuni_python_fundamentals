def order_bill ():
    product = input()
    quantity = int(input())
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00
    total = quantity * price
    return f"{total:.2f}"

print(order_bill())