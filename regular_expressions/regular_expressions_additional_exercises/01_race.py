import re
pattern_name = r"([A-Za-z]+)"
pattern_km = r"(\d+)"
list_of_participants = input().split(", ")
distances = {name: 0 for name in list_of_participants}

info = input()
while info != "end of race":
    name_as_list = re.findall(pattern_name,info)
    km_as_list = re.findall(pattern_km,info)
    name = "".join(name_as_list)
    km = "".join(km_as_list)
    sum_km = sum(int(k) for k in km)
    if name in distances:
        distances[name] += sum_km
    info = input()

sorted_participants = sorted(distances.items(), key=lambda item: item[1])

print(f"1st place: {sorted_participants[-1][0]}")
print(f"2nd place: {sorted_participants[-2][0]}")
print(f"3rd place: {sorted_participants[-3][0]}")

