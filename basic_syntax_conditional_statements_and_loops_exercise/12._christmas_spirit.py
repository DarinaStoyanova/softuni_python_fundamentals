quantity_of_decorations = int(input())
days_left_till_christmas = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights = 15

day_count = 0
current_total = 0
christmas_spirit = 0
last_day = days_left_till_christmas

while days_left_till_christmas > 0:
    day_count += 1
    days_left_till_christmas -= 1
    if day_count % 11 == 0:
        quantity_of_decorations += 2
    if day_count % 2 == 0:
        current_total += quantity_of_decorations * ornament_set_price
        christmas_spirit += 5
    if day_count % 3 == 0:
        current_total += (quantity_of_decorations * tree_skirt_price) + (quantity_of_decorations * tree_garland_price)
        christmas_spirit += 13
    if day_count % 5 == 0:
        current_total += tree_lights * quantity_of_decorations
        christmas_spirit += 17
    if day_count % 5 == 0 and day_count % 3 == 0:
        christmas_spirit += 30
    if day_count % 10 == 0:
        christmas_spirit -= 20
        current_total += tree_skirt_price + tree_garland_price + tree_lights

if last_day % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {current_total}")
print(f"Total spirit: {christmas_spirit}")
