str1, str2 = input().split(" ")
total_sum = 0

if len(str1) == len(str2):
    for index in range(len(str1)):
        total_sum += ord(str1[index]) * ord(str2[index])
elif len(str1) > len(str2):
    for index in range(len(str2)):
        total_sum += ord(str1[index]) * ord(str2[index])
    for index in range(len(str2),len(str1)):
        total_sum += ord(str1[index])
elif len(str1) < len(str2):
    for index in range(len(str1)):
        total_sum += ord(str1[index]) * ord(str2[index])
    for index in range(len(str1), len(str2)):
        total_sum += ord(str2[index])

print(total_sum)
