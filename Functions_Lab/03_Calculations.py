def my_calculator(operator: str, a: int, b: int,):
    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return int(a / b)
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b

operator = input()
a = int(input())
b = int(input())

print(my_calculator(operator, a, b))

# Втори вариант!
# def multiply (a: int, b: int):
#     return a * b
# def subtract (a: int, b: int):
#     return a - b
# def add (a: int, b: int):
#     return a + b
# def divide (a: int, b: int):
#     return int(a / b)
#
# def my_calculator ():
#     operation = input()
#     a = int(input())
#     b = int(input())
#     result = 0
#
#     if operation == "multiply":
#         result = multiply(a,b)
#     elif operation == "add":
#         result = add(a,b)
#     elif operation == "divide":
#         result = divide(a,b)
#     elif operation == "subtract":
#         result = subtract(a,b)
#
#     print(result)
#
#
# my_calculator()
#
#
#
#
#








