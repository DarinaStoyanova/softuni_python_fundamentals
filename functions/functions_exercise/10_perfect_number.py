received_number = int(input())

def perfect_number_founder(rec_num:int):
    list_divisors = []
    counter_div = 1

    while counter_div < rec_num:
        if rec_num % counter_div == 0:
            list_divisors.append(counter_div)
        counter_div += 1
    sum_divisors = sum(list_divisors)
    if sum_divisors == rec_num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

print(perfect_number_founder(received_number))