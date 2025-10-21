force_users_and_sides = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        side, user = command.split(" | ")
        if side not in force_users_and_sides.keys():
            if user not in force_users_and_sides.values():
                force_users_and_sides[side] = []
                force_users_and_sides[side].append(user)

        elif user in force_users_and_sides.values():
            command = input()
            continue

    elif " -> " in command:
        side, user = command.split(" -> ")
        if user in force_users_and_sides.values():

            current_side = force_users_and_sides

    command = input()