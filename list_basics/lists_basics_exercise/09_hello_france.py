items_with_prices = input().split("|")
starting_budget = int(input())
budget_left = starting_budget
budget_after_selling = 0
list_prices_after_sell = []

for item_or_price in items_with_prices:
    real_item_or_price = (item_or_price.split("->"))
    item = real_item_or_price[0]
    price = float(real_item_or_price[1])
    if budget_left > 0:
        if item == "Clothes" and price <= 50.00:
            budget_left -= price
            if budget_left < 0:
                budget_left += price
            else:
                price_after_sell = (price * 0.4) + price
                budget_after_selling += price_after_sell - price
                list_prices_after_sell.append(f"{price_after_sell:.2f}")
        elif item == "Shoes" and price <= 35.00:
            budget_left -= price
            if budget_left < 0:
                budget_left += price
            else:
                price_after_sell = (price * 0.4) + price
                budget_after_selling += price_after_sell - price
                list_prices_after_sell.append(f"{price_after_sell:.2f}")
        elif item == "Accessories" and price <= 20.50:
            budget_left -= price
            if budget_left < 0:
                budget_left += price
            else:
                price_after_sell = (price * 0.4) + price
                budget_after_selling += price_after_sell - price
                list_prices_after_sell.append(f"{price_after_sell:.2f}")
    elif budget_left == 0:
        break

for price in list_prices_after_sell:
    print(price, end=" ")
print()
print(f"Profit: {budget_after_selling:.2f}")
if starting_budget + budget_after_selling >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
