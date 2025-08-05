
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also breaks.
# Every second time his shield breaks, his armor also needs to be repaired.
# You will receive the price of each item in his equipment.
# Calculate his expenses for the year for renewing his equipment.


# · As output, you must print Peter`s total expenses for new equipment: "Gladiator expenses: {expenses} aureus"

lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
shield_count_break = 0

for current_lost_game in range (1,lost_fights_count+1):
    if current_lost_game % 2 == 0:
        expenses += helmet_price
    if current_lost_game % 3 == 0:
        expenses += sword_price
        if current_lost_game % 2 == 0:
            expenses += shield_price
            shield_count_break += 1
            if shield_count_break % 2 == 0:
                expenses += armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")