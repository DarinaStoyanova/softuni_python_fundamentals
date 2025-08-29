money_as_integers = input() # 1, 2, 3, 4, 5
count_beggars = int(input()) # 3
money_as_integers = list(map(int,money_as_integers.split(", ")))
start_index = 0
final_list = []
money_accumulated = 0

for beggar in range (1, count_beggars+1):
    for money_take in range(start_index, len(money_as_integers), count_beggars):
        money_accumulated += money_as_integers[money_take]
    final_list.append(money_accumulated)
    money_accumulated = 0
    start_index += 1
print(final_list)
