events = input().split("|")
initial_energy = 100
initial_coins = 100
bakery_open = True
total_energy = initial_energy
total_coins = initial_coins

for event in events:
    event_items = event.split("-")
    type_of_event = event_items[0]
    value_of_event = event_items[1]
    if type_of_event == "rest":
        gained_energy = int(value_of_event)
        total_energy = total_energy + gained_energy
        if total_energy > 100:
            total_energy = 100
            gained_energy = 100 - initial_energy
            print(f"You gained {gained_energy} energy.")
            current_energy = 100
        print(f"Current energy: {total_energy}.")
    elif type_of_event == "order":
        earned_coins = int(value_of_event)
        total_coins = total_coins + earned_coins
        if total_energy >= 0:
            total_energy -= 30
            print(f"You earned {earned_coins} coins.")
        else:
            total_energy += 50
            print(f"You had to rest!")
    else:
        ingredient = type_of_event
        if total_coins >= 0:
            total_coins = total_coins - int(value_of_event)
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            bakery_open = False
            break
if bakery_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")



