company_ids = {}

command = input()
while command != "End":
    name, id = command.split(" -> ")
    if name not in company_ids:
        company_ids[name] = []
        company_ids[name].append(id)
    else:
        if id not in company_ids[name]:
            company_ids[name].append(id)
    command = input()

for name,id in company_ids.items():
    print(name)
    for i in id: # for the specific id in the list of ID-s
        print(f"-- {i}")