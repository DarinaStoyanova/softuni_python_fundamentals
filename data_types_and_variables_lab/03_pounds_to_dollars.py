# Write a program that converts British pounds (integer) to US dollars formatted to the 3rd decimal point.
pounds = int(input())
pounds_to_usd = pounds * 1.31
print(f"{pounds_to_usd:.3f}")