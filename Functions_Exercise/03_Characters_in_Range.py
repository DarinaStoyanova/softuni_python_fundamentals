def char_fun(char1: str, char2: str):
    for char in range(ord(char1) + 1, ord(char2)):
        print(chr(char), end=" ")

character_1 = input()
character_2 = input()

char_fun(character_1,character_2)


