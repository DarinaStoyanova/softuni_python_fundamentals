import re

income = 0
info = input()
pattern = r"^%([A-Z][a-z]+)%[^|$%.]*<(\w+)>[^|$%.]*\|(\d+)\|[^|$%.]*?(\d+(?:\.\d+)?)\$"

while info != "end of shift":
    result = re.findall(pattern,info)
    if result:
        customer_name = result[0][0]
        product = result[0][1]
        total_price = int(result[0][2]) * float(result[0][3])
        print(f"{customer_name}: {product} - {total_price:.2f}")
        income += total_price
    info = input()

print(f"Total income: {income:.2f}")