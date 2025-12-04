import re
import math
calories_counter = 0
pattern = r"([#|])([A-Za-z\s]+)\1([\d]{2}\/[\d]{2}\/[\d]{2})\1(\d+)\1"

info = input()
decrypted_info = re.findall(pattern, info)

for data in decrypted_info:
    calories_counter += int(data[3])

days = calories_counter / 2000
print(f"You have food to last you for: {math.floor(days)} days!")

for data in decrypted_info:
    print(f"Item: {data[1]}, Best before: {data[2]}, Nutrition: {data[3]}")