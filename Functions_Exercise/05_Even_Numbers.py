# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a list of only the even numbers. Use filter().
sequence_of_num = input().split(" ")
sequence_of_num = list(map(int,sequence_of_num))
even = lambda x: x % 2 == 0
result = list(filter(even, sequence_of_num))
print(result)













# # list_even = []
# # for num in sequence_of_num:
# #     if int(num) % 2 == 0:
# #         list_even.append(int(num))
# # print(list_even)
# filter(sequence_of_num,2)
