import re
string = input()
word_to_find = input()
regex = rf"(?i)\b({word_to_find})\b"
results = re.findall(regex,string)
counter = len(results)
print(counter)

