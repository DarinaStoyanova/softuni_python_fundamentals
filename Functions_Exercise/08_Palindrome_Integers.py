
numbers_as_list_as_int = list(map(int, input().split(", ")))
def palindrome(num:str):
    return num == num[::-1]

for number in numbers_as_list_as_int:
    number = str(number)
    print(palindrome(number))