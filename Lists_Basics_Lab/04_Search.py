n = int(input())
word = input()
full_list = []
new_list_with_word = []
for string in range(n):
    current_string = input()
    full_list.append(current_string)
    if word in current_string:
        new_list_with_word.append(current_string)
print(full_list)
print(new_list_with_word)


