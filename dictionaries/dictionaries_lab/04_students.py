command = input()
people_and_courses = []

while True:
    if ":" not in command:
        course_to_search_for = command
        break
    name, id_, course = command.split(":")
    people_and_courses.append({"name":name, "id":id_, "course":course})
    command = input()

for student in people_and_courses:
    if course_to_search_for.startswith(student['course'][0:4]):
        print(f"{student['name']} - {student['id']}")
