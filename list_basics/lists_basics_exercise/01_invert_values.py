# Write a program that receives a single string containing positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.
opposite_list = []
single_string = input()
my_list = list(single_string.split(" "))
for number in (my_list):
    number = int(number)
    opposite_number = -number
    opposite_list.append(opposite_number)
print(opposite_list)