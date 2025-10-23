entry_string = input()
final_string = ""
total = 0

for index in range (len(entry_string)):
    for entry_string[index] in entry_string:
        if entry_string[index] == ">":
            total += int(entry_string[index + 1])

for char in entry_string:
    if char == ">":
        entry_string = entry_string.pop()