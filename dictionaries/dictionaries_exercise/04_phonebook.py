dict_with_data = {}
command = input()

while True:
    if command.isdigit():
        digit = int(command)
        break
    name_and_number = command.split("-")
    name = name_and_number[0]
    number = name_and_number[1]
    # name, number = command.split("-")
    dict_with_data[name] = number
    command = input()

while digit > 0:
    digit -= 1
    name_to_search = input()
    if name_to_search in dict_with_data.keys():
        print(f"{name_to_search} -> {dict_with_data[name_to_search]}")
    else:
        print(f"Contact {name_to_search} does not exist.")