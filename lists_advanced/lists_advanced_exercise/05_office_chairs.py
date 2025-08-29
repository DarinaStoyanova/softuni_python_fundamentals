number_of_rooms = int(input())
free_chairs_left = []
needed_chairs = []
room_where_chairs_was_needed = []
room = 0
while room < number_of_rooms:
    room += 1
    chairs_and_visitors = input()
    chairs_and_visitors_separated = chairs_and_visitors.split(" ")
    visitors_as_int = int(chairs_and_visitors_separated[1])
    total_free_chairs = len(chairs_and_visitors_separated[0]) - visitors_as_int
    if len(chairs_and_visitors_separated[0]) >= visitors_as_int:
        free_chairs_left.append(total_free_chairs)
    else:
        needed_chairs_in_room = abs(total_free_chairs)
        room_where_chairs_was_needed.append(room)
        needed_chairs.append(needed_chairs_in_room)
total_free_seats = sum(free_chairs_left)

if needed_chairs:
    for index in range(len(needed_chairs)):
        print(f"{needed_chairs[index]} more chairs needed in room {room_where_chairs_was_needed[index]}")
else:
    print(f"Game On, {sum(free_chairs_left)} free chairs left")