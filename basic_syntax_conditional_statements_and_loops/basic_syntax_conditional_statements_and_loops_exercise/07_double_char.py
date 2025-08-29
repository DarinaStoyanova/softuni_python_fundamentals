command = input()
while command != "End":
    new_string = ""
    for char in command:
        new_string += char * 2
    print(new_string)

    command = input()