n = int(input())
registered_cars = {}

command = input()
while n > 0:
    n -= 1
    info = command.split(" ")
    if "register" in info:
        key = info[1]
        if key in registered_cars.keys():
            print(f"ERROR: already registered with plate number {registered_cars[key]}")
            command = input()
            continue
        value = info[2]
        registered_cars[key]=value
        print(f"{key} registered {registered_cars[key]} successfully")
    elif "unregister" in info:
        username = info[1]
        if username not in registered_cars:
            print(f"ERROR: user {username} not found")
        else:
            registered_cars.pop(username)
            print(f"{username} unregistered successfully")
    if n == 0:
        break
    command = input()

for username, licence_plate_number in registered_cars.items():
    print(f"{username} => {registered_cars[username]}")