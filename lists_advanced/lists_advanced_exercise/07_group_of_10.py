sequence_of_number = [int(number) for number in input().split(", ")]
group = 10
while sequence_of_number:
    list_of_numbers = [number for number in sequence_of_number if number <= group]
    print(f"Group of {group}'s: {list_of_numbers}")
    sequence_of_number = [number for number in sequence_of_number if number not in list_of_numbers]
    group += 10