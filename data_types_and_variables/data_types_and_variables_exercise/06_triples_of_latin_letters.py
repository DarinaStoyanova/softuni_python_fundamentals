# Write a program to read an integer N and print all triples of the first N small Latin letters, ordered alphabetically:
integer_n = int(input())
for letter1 in range (97, 97 + integer_n):
    for letter2 in range (97, 97 + integer_n):
        for letter3 in range (97, 97 + integer_n):
            print(f"{chr(letter1)}{chr(letter2)}{chr(letter3)}")

