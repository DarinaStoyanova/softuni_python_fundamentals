def sum_numbers (num1: int, num2:int):
    return num1 + num2
def subtract(result: int, num3: int):
    return result - num3

def add_and_subtract(num1: int, num2: int, num3: int):
    sum = sum_numbers(num1,num2)
    return subtract(sum,num3)

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(add_and_subtract(number_1, number_2, number_3))