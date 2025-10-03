n = int(input())
data = {}

for times in range(n):
    name = input()
    grade = float(input())
    if name not in data:
        data[name] = []
        data[name].append(grade)
    else:
        data[name].append(grade)
for name, grades in data.items():
    if len(data[name]) == 1:
        average_grade = grades[0]
    else:
        average_grade = sum(data[name]) / 2
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")

