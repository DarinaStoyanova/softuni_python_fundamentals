received_strings = input().split()
total_sum = 0

for string in received_strings:
    number = int(string[1:-1])
    if string[0].isupper():
        letter_position = ord(string[0]) - 64
        result = number / letter_position
    elif string[0].islower():
        letter_position = ord(string[0]) - 96
        result = number * letter_position

    if string[-1].isupper():
        letter_position = ord(string[-1]) - 64
        result -= letter_position
    elif string[-1].islower():
        letter_position = ord(string[-1]) - 96
        result += letter_position

    total_sum += result

print(f"{total_sum:.2f}")