countries = input().split(", ")
capitals = input().split(", ")
# ordered_data = {}
# ordered_data = dict(zip(countries, capitals))
ordered_data = {countries[index]:capitals[index] for index in range(len(capitals))}

for country,capital in ordered_data.items():
    print(f"{country} -> {capital}")