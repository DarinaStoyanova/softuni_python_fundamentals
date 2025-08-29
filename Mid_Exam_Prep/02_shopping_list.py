initial_list_groceries = input().split("!")
command = input()
while command != "Go Shopping!":
    item_and_new_command = command.split(" ")
    new_command = item_and_new_command[0]
    item = item_and_new_command[1]
    if new_command == "Urgent":
        if item in initial_list_groceries:
            command = input()
            continue
        else:
            initial_list_groceries.insert(0, item)
    elif new_command == "Unnecessary":
        if item in initial_list_groceries:
            initial_list_groceries.remove(item)
        else:
            command = input()
            continue
    elif new_command == "Correct":
        if item_and_new_command[1] in initial_list_groceries:
            new_item = item_and_new_command[2]
            old_item = item_and_new_command[1]
            if old_item in initial_list_groceries:
                index = initial_list_groceries.index(old_item)
                initial_list_groceries[index] = new_item
        else:
            command = input()
            continue
    elif new_command == "Rearrange":
        if item in initial_list_groceries:
            initial_list_groceries.remove(item)
            initial_list_groceries.append(item)
        else:
            command = input()
            continue
    command = input()

initial_list_groceries = ', '.join(initial_list_groceries)
print(initial_list_groceries)