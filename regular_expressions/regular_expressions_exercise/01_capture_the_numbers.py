import re
string = input()
while string:
    regex = r"\d+"
    result = re.findall(regex,string)
    if result:
        print(" ".join(result), end=" ")
    string = input()