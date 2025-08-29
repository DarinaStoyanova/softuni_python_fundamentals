from os.path import split

words = input(). split(" ")
for word in words:
    if len(word) % 2 == 0:
        print(word)

# second option
# words = input(). split(" ")
# result = [print(word) for word in words if len(word) % 2 == 0]