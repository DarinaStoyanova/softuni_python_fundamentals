# import random
# received_str = input().split(" ")
# count_of_faro_shuffle = int(input())
# # print(received_str)
# half = len(received_str) // 2
# x = received_str[:half]
# y = received_str[half:]
# # print(f"{x} and {y}")
#
# rest_x = x[1:]
# random.shuffle(rest_x)
# shuffled_lst_x = [x[0]] + rest_x
# # print(shuffled_lst_x)
#
# rest_y = y[:-1]
# for _ in range(count_of_faro_shuffle):
#     random.shuffle(rest_y)
#     shuffled_lst_y = rest_y + [y[-1]]
# print(shuffled_lst_y)

cards = input().split()
shuffles = int(input())

for _ in range(shuffles):
    half = len(cards) // 2
    first_half = cards[:half]
    second_half = cards[half:]

    # Faro Shuffle: Преплитане на двете половини
    shuffled = []
    for i in range(half):
        shuffled.append(first_half[i])
        shuffled.append(second_half[i])

    cards = shuffled  # Запазваш новото разбъркване за следващия цикъл

print(cards)