str_with_numbers = input().split(", ")
list_with_num = (list(map(int,str_with_numbers)))
list_with_even_ind = []

for (ind, value) in enumerate(list_with_num):
    if value % 2 == 0:
        list_with_even_ind.append(ind)
print(list_with_even_ind)

