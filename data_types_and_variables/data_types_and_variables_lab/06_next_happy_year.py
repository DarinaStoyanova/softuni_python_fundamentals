# You are saying goodbye to your best friend: "See you next happy year".
# Happy Year is the year with only distinct digits, for example, 2018.
# Write a program that receives an integer number and finds the next happy year.
current_year = int(input()) # 2019
while True:
    current_year += 1
    if len(set(str(current_year))) == len(str(current_year)):
        break
print(current_year)