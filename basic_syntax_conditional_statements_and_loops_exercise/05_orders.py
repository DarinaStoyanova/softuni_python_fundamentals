number_of_orders = int(input())

total = 0
for order in range(0,number_of_orders):
    price_per_caps = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    total_per_order = (price_per_caps * capsules_needed_per_day) * days
    if 1<= days <= 31 and 1 <= capsules_needed_per_day <= 2000 and 0.01 <= price_per_caps <= 100.00:
        print(f"The price for the coffee is: ${total_per_order:.2f}")
        total += total_per_order
print(f"Total: ${total:.2f}")


