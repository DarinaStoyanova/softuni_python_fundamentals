received_numbers = list(map(int,(input().split(" "))))
result_min = min(received_numbers)
result_max = max(received_numbers)
result_sum = sum(received_numbers)

print(f"The minimum number is {result_min}")
print(f"The maximum number is {result_max}")
print(f"The sum number is: {result_sum}")
