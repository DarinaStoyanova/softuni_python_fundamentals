import re
total_cost = 0
pattern = r">>([a-zA-Z]+)<<(\d+\.\d+|\d+)!(\d+)"

command = input()
print("Bought furniture:")
while command != "Purchase":
    matches = re.search(pattern,command)
    if matches:
        furniture,price,quantity = matches.group(1), matches.group(2), matches.group(3)
        print(furniture)
        cost = int(quantity) * float(price)
        total_cost += cost
    command = input()
print(f"Total money spend: {total_cost:.2f}")