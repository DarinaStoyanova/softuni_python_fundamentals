text_to_count = input()
counter = {}

for letter in text_to_count:
    if letter == " ":
        continue
    if letter not in counter.keys():
        counter[letter] = 1
    else:
        counter[letter] += 1

for char, occurence in counter.items():
    print(f"{char} -> {counter[char]}")
