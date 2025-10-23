ban_list = input().split(", ")
text = input()

for ban_word in ban_list:
    if ban_word in text:
        text = text.replace(ban_word, "*" * len(ban_word))

print(text)