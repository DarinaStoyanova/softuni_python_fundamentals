received_numbers = input().split(" ")
numbers_as_num = list(map(int,received_numbers))
my_list = numbers_as_num.copy()
count_numbers_to_remove = int(input())
numbers_as_num.sort()
min_numbers = numbers_as_num[:count_numbers_to_remove]
final_list = []

for number in my_list:
    if number not in min_numbers:
        final_list.append(number)
print(", ".join(map(str, final_list)))

