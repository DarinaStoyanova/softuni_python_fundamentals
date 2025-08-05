names_as_strings = input().split(', ')
sorted_list = sorted(names_as_strings, key=lambda x: (-len(x), x))
print(sorted_list)
