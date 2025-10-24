string = input()
filtered_string = ""
explosion_strength = 0

for index in range(0, len(string)):
    if string[index] == ">":
        filtered_string += string[index]
        explosion_strength += int(string[index+1])
    elif string[index] != ">" and explosion_strength <= 0:
        filtered_string += string[index]
    elif string[index] != ">" and explosion_strength > 0:
        explosion_strength -= 1

print(filtered_string)