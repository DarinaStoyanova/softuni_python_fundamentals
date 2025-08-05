# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a sorted list of numbers in ascending order. Use sorted().
# Първи вариант:
# first_received_numbers = map(int, input().split(" "))
# sorted_list = sorted(first_received_numbers)
# print(sorted_list)

# Втори вариант:
first_received_numbers = input().split(" ")
numbers_as_list_and_num = []

for digit in first_received_numbers:
    numbers_as_list_and_num.append(int(digit))

sorted_list = sorted(numbers_as_list_and_num)
print(sorted_list)