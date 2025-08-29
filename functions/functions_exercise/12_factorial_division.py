first_num = int(input())
second_num = int(input())


def factorial_calculation (num: int):
    for char in range(1, num):
        num *= char
    return (num)

first_result = factorial_calculation(first_num)
second_result = factorial_calculation(second_num)
result = first_result / second_result

print(f"{result:.2f}")
