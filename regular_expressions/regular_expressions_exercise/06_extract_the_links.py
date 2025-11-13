import re
text = input()
regex = r"((www\.[a-zA-Z0-9\-]+)(\.[a-z]+)+)"

while text:
    match = re.search(regex,text)
    if match:
        link = match.group(1)
        print(link)
    text = input()