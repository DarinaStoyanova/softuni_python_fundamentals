part_1 = input()
part_2 = input()
part_3 = input()
my_list = [part_1, part_2, part_3]
my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)

