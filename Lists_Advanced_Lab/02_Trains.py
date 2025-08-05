number_of_wagons = int(input())
train = [0 * wag for wag in range(number_of_wagons)]

command = input()
while command != "End":
    data = command.split(" ")
    final_command = data[0]
    index = int(data[1])
    if final_command == "add":
        train[-1] = train[-1] + index
    elif final_command == "insert":
        number = int(data[2])
        train[index] = train[index] + number
    elif final_command == "leave":
        number = int(data[2])
        train[index] = train[index] - number

    command = input()
print(train)