# employee_happiness_list = input().split(' ')
# employee_happiness_as_int = list(map(int,employee_happiness_list))
# factor = int(input())
# multiplied_happiness = []
# happy_count = 0
# total_employees = len(employee_happiness_as_int)
#
# for value in employee_happiness_as_int:
#     new_value = value * factor
#     multiplied_happiness.append(new_value)
#
# average_happiness = sum(multiplied_happiness) / len(multiplied_happiness)
#
# for value in multiplied_happiness:
#     if value >= average_happiness:
#         happy_count += 1
#
# if happy_count >= total_employees / 2:
#     print(f"Score: {happy_count}/{total_employees}. Employees are happy!")
# else:
#     print(f"Score: {happy_count}/{total_employees}. Employees are not happy!")

employee_happiness_list = input().split(' ')
employee_happiness_as_int = list(map(int,employee_happiness_list))
factor = int(input())
happy_count = 0
total_employees = len(employee_happiness_as_int)

multiplied_happiness = list(map(lambda x: x * factor, employee_happiness_as_int))

average_happiness = sum(multiplied_happiness) / len(multiplied_happiness)

for value in multiplied_happiness:
    if value >= average_happiness:
        happy_count += 1

if happy_count >= total_employees / 2:
    print(f"Score: {happy_count}/{total_employees}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_employees}. Employees are not happy!")


