entry_text = input()

for index in range(len(entry_text)):
    if entry_text[index] == ":":
        print(f":{entry_text[index+1]}")