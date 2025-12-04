cities_info = input()
cities_info_list = {}

while cities_info != "Sail":
    cities_info = cities_info.split("||")
    city = cities_info[0]
    population = cities_info[1]
    gold = cities_info[2]

    if city in cities_info_list:
        cities_info_list[city] = [(int(cities_info_list[city][0])+int(population)), int(cities_info_list[city][1])+int(gold)]
    else:
        cities_info_list[city] = [int(population), int(gold)]

    cities_info = input()

event =  input()
while event != "End":
    event = event.split("=>")

    if event[0] == "Plunder":
        town = event[1]
        people_killed = event[2]
        gold_stolen = event[3]
        cities_info_list[town] = [(int(cities_info_list[town][0]) - int(people_killed)), (int(cities_info_list[town][1]) - int(gold_stolen))]
        print(f"{town} plundered! {gold_stolen} gold stolen, {people_killed} citizens killed.")

        if int(cities_info_list[town][0]) == 0 or int(cities_info_list[town][1]) == 0:
            cities_info_list.pop(town)
            print(f"{town} has been wiped off the map!")

    elif event[0] == "Prosper":
        town = event[1]
        added_gold = event[2]
        if int(added_gold) < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities_info_list[town] = [int(cities_info_list[town][0]), int(cities_info_list[town][1]) + int(added_gold)]
            total_gold = cities_info_list[town][1]
            print(f"{added_gold} gold added to the city treasury. {town} now has {total_gold} gold.")

    event = input()

count = len(cities_info_list)

if cities_info_list:
    print(f"Ahoy, Captain! There are {count} wealthy settlements to go to:")
    for town in cities_info_list:
        people = cities_info_list[town][0]
        gold = cities_info_list[town][1]
        print(f"{town} -> Population: {people} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")