def rounded_numbers():
    numbers = input().split(" ")
    final_numbers = []
    for number in numbers:
        number = round(float(number))
        final_numbers.append(number)
    return final_numbers

print(rounded_numbers())
