def smallest_number_cal():
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())
    cur_smallest_num = 9999999999
    smallest_nums = [num_1, num_2, num_3]
    for number in smallest_nums:
        if number < cur_smallest_num:
            cur_smallest_num = number
    return cur_smallest_num

print(smallest_number_cal())

