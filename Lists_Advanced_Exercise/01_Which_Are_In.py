first_sequence = input().split(", ")
second_sequence = input().split(", ")

matches = [word for word in first_sequence if word in second_sequence]