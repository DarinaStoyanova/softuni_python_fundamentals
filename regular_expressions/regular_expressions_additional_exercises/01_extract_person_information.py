import re
n = int(input())

for _ in range(n):
    text = input()
    names = re.findall(r'@([A-Za-z]+)\|', text)
    ages = re.findall(r'#(\d+)\*', text)
    for i in range(len(names)):
        print(f"{names[i]} is {ages[i]} years old.")