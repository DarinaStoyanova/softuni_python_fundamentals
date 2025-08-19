received_numbers = input().split(", ")
positive_numbers = []
negative_numbers = []
odd_numbers = []
even_numbers = []

received_numbers_as_int = [int(number) for number in received_numbers]
for number in received_numbers_as_int:
    if number >= 0:
        positive_numbers.append(number)
    elif number < 0:
        negative_numbers.append(number)
    if number % 2 == 0:
        even_numbers.append(number)
    elif number % 2 != 0:
        odd_numbers.append(number)

positive = ", ".join(str(num) for num in positive_numbers)
negative = ", ".join(str(num) for num in negative_numbers)
odd = ", ".join(str(num) for num in odd_numbers)
even = ", ".join(str(num) for num in even_numbers)

print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {even}")
print(f"Odd: {odd}")
