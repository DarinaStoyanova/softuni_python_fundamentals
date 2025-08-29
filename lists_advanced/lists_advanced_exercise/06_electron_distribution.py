number_of_electrons = int(input())
shell_number = 0
list_with_electrons_per_shell = []
while number_of_electrons > 0:
    shell_number += 1
    max_capacity = 2 * shell_number **2
    if number_of_electrons > max_capacity:
        number_of_electrons -= max_capacity
        list_with_electrons_per_shell.append(max_capacity)
    elif number_of_electrons <= max_capacity:
        list_with_electrons_per_shell.append(number_of_electrons)
        number_of_electrons -= number_of_electrons
print(list_with_electrons_per_shell)

