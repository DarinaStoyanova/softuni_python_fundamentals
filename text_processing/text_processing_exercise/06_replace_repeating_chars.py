entry_text = input()
last_char = ""
text_for_print = ""

for index in range(len(entry_text)):
    if entry_text[index] != last_char:
        text_for_print += entry_text[index]
        last_char = entry_text[index]

print(text_for_print)