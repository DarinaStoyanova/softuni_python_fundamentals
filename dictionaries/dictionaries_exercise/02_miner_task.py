command = input()
line_counter = 0
resources_collector = {}

while command != "stop":
    line_counter += 1
    if line_counter % 2 != 0:
        resource = command
    elif line_counter % 2 == 0:
        quantity = int(command)
        if resource in resources_collector.keys():
            resources_collector[resource] += quantity
        else:
            resources_collector[resource] = quantity
    command = input()

for resource,quantity in resources_collector.items():
    print(f"{resource} -> {quantity}")

