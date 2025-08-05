numbers = input().split(" ")
list_numbers = []
for number in numbers:
    number = abs(float(number))
    list_numbers.append(number)
print(list_numbers)

