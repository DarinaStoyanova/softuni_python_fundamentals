import re
phones = input()
regex = r"(\+359([ -])2\2\d{3}\2\d{4}\b)"
matches = re.findall(regex,phones)
filtered_phones = [match[0] for match in matches]
print(", ".join(filtered_phones))