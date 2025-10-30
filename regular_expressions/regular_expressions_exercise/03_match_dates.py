import re
dates = input()
regex = r"(\d{2})([.\/-])([A-Z][a-z]{2})\2(\d{4})"
final_dates = re.findall(regex,dates)

for data in final_dates:
    day = data[0]
    month = data[2]
    year = data[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")