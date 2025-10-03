courses = {}
command = input()
while command != "end":
    command = command.split(" : ")
    key, value = command
    if key not in courses:
        courses[key] = []
        courses[key].append(value)
    else:
        courses[key].append(value)

    command = input()

for course,names in courses.items():
    print(f"{course}: {len(courses[course])}")
    for name in names:
        print(f"-- {name}")
