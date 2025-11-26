import re
text = input().split(",")
text = [demon.strip() for demon in text]
all_char = r"[^0-9\-+/*.]"
all_num = r"[\-+]?\d+(?:\.\d+)?"
divide_multiply = r"[*/]"
health = 0
damage = 0

text = sorted(text)
for name in text:
    characters = re.findall(all_char, name)
    for char in characters:
        health += ord(char)
    numbers = re.findall(all_num,name)
    for num in numbers:
        damage += float(num)
    result_after_divide_multiply = "".join(re.findall(divide_multiply,name))
    for _ in result_after_divide_multiply:
        if _ == "*":
            damage *= 2
        elif _ == "/":
            damage /= 2
    print(f"{name} - {health} health, {damage:.2f} damage")
    health = 0
    damage = 0