import math
group_size = int(input())
days = int(input())
days_count = 0
gained_money = 0

while days_count < days:
    days_count += 1
    gained_money += 50
    if days_count % 10 == 0:
        group_size = group_size - 2
    if days_count % 15 == 0:
        group_size = group_size + 5
    gained_money = gained_money - (2*group_size)
    if days_count % 3 == 0:
        gained_money = gained_money - (3 * group_size)
    if days_count % 5 == 0:
        gained_money = gained_money + (20 * group_size)
        if days_count % 3 == 0:
            gained_money = gained_money - (2 * group_size)
coins_per_person = gained_money / group_size
print(f"{group_size} companions received {math.floor(coins_per_person)} coins each.")


