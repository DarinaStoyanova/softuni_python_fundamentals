list_of_character = input().split(", ")
char_dict = {char:ord(char) for char in list_of_character}
print(char_dict)
