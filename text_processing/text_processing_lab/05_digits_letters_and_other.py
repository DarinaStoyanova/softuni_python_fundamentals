string_to_be_sorted = input()
digits = ""
letters = ""
other_char = ""

for char in string_to_be_sorted:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        other_char += char

print(digits)
print(letters)
print(other_char)