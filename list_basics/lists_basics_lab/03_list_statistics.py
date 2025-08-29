list_positive = []
list_negative = []
count_of_positives = 0
sum_of_negatives = 0
n_times = int(input())
for number in range (n_times):
    current_number = int(input())
    if current_number >= 0:
        list_positive.append(current_number)
        count_of_positives += 1
    else:
        list_negative.append(current_number)
        sum_of_negatives += current_number
print(list_positive)
print(list_negative)
print(f"Count of positives: {count_of_positives}")
print(f"Sum of negatives: {sum_of_negatives}")
# print(len(list_positive))
# print(sum(list_negative))

