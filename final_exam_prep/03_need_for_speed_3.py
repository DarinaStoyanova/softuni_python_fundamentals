n = int(input())
owned_cars = {}

while n > 0:
    n -= 1
    car_info = input().split("|")
    key = car_info[0]
    owned_cars[key] = [int(car_info[1]), int(car_info[2])]

command = input()
while command != "Stop":
    command = command.split(" : ")

    if command[0] == "Drive":
        car_model = command[1]
        km_to_drive = command[2]
        fuel_needed = command[3]
        if int(fuel_needed) <= owned_cars[car_model][1]:
            owned_cars[car_model][0] += int(km_to_drive)
            if owned_cars[car_model][0] > 100000:
                owned_cars.pop(car_model)
                print(f"Time to sell the {car_model}!")
        else:
            print("Not enough fuel to make that ride")
    elif command[0] == "Refuel":
        car_model = command[1]
        fuel_to_add = command[2]
        current_fuel = owned_cars[car_model][1]
        current_fuel += int(fuel_to_add)
        if current_fuel > 75:
            added_fuel = owned_cars[car_model][1] - 75
            owned_cars[car_model][1] = 75
            print(f"{car_model} refueled with {added_fuel} liters")
        else:
            print(f"{car_model} refueled with {fuel} liters")
    elif command[0] == "Revert":
        car_model = command[1]
        km_to_revert = command[2]
        owned_cars[car_model][0] -= int(km_to_revert)
        if owned_cars[car_model][0] < 10000:
            owned_cars[car_model][0] = 10000
        else:
            print(f"{car_model} mileage decreased by {km_to_revert} kilometers")

    command = input()

for car in owned_cars:
    print(f"{car} -> Mileage: {car[0]} kms, Fuel in the tank: {car[1]} lt.")