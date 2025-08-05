command = input()
priority_list = []
while command != "End":
    command = command.split("-")
    priority = int(command[0]), command[1]
    priority_list.append(priority)
    command = input()
priority_list.sort()
result = [task for index,task in priority_list]
print(result)