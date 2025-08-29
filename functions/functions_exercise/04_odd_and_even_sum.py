def sum_odd_even (num: str):
    sum_even = 0
    sum_odd = 0
    for n in num:
        if int(n) % 2 == 0:
            sum_even += int(n)
        else:
            sum_odd += int(n)
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"

received_number = input()
result = sum_odd_even(received_number)
print(result)
