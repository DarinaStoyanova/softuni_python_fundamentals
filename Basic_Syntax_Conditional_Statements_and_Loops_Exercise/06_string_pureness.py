number_n = int(input())

for _ in range (1, number_n + 1):
    string = input()
    if "." in string or "," in string or "_" in string :
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")