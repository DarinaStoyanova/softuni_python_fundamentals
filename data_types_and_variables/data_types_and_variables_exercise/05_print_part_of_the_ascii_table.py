#
# Write a program that prints part of the ASCII table characters on the console, separated by a single space.
# On the first line of input, you will receive the char index you should start with.
# On the second line - the index of the last character you should print.

char_index_start = int(input())
char_index_stop = int(input())

for char in range (char_index_start, char_index_stop+1):
    char = chr(char)
    print(char, end=" ")