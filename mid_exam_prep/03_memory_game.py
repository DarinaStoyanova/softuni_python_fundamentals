sequence_of_elements = list(map(int,(input().split())))
number_of_moves = 0
command = list(map(int,(input().split())))
while command != "End":
    index_1 = command[0]
    index_2 = command[1]
    if index_1 < 0 or index_1 >= len(sequence_of_elements) or index_2 < 0 or index_2 >= len(sequence_of_elements):
        number_of_moves += 1
        midpoint = len(sequence_of_elements) // 2
        strings_of_sequence = [str(num) for num in sequence_of_elements]
        sequence_of_elements = sequence_of_elements[0:midpoint] + [f"-{number_of_moves}a," f"-{number_of_moves}a"] + sequence_of_elements[midpoint:]
        print("Invalid input! Adding additional elements to the board")
    elif sequence_of_elements[index_1] == sequence_of_elements[index_2]:
        number_of_moves += 1
        print(f"Congrats! You have found matching elements - {sequence_of_elements[index_1]}!")
        sequence_of_elements.pop(index_1)
        sequence_of_elements.pop(index_2)
    elif sequence_of_elements[index_1] != sequence_of_elements[index_2]:
        number_of_moves += 1
        print("Try again!")
    elif sequence_of_elements is False:
        print(f"You have won in {number_of_moves} turns!")

    command = list(map(int,(input().split())))

if command == "End" and sequence_of_elements is False:
    print("Sorry you lose :(")
    print(sequence_of_elements)
