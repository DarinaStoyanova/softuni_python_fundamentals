word = input()

inverse_word = ""

for i in range (len(word) - 1,-1, -1):
    inverse_word += word[i]

print(inverse_word)