divisor = int(input())
boundary = int(input())

largest_int_N = 0
for number in range (1, boundary+1):
    if number % divisor == 0:
        if number > largest_int_N:
            largest_int_N = number
print(largest_int_N)