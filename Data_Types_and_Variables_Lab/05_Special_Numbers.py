# Write a program that reads an integer n. Then, for all numbers in the range [1, n],
# print the number and if it is special or not (True / False).
# A number is special when the sum of its digits is 5, 7, or 11.
digit_sum = 0
integer_n = int(input())
for number in range (1,integer_n+1): #200,201,203,205..209
    number = str(number)
    for digit in number:
        digit = int(digit)
        digit_sum += digit
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")
    digit_sum = 0