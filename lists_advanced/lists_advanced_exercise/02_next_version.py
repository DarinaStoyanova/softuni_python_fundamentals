# current_version = input().split(".")
# current_version_as_int = int("".join(current_version))
# new_version_as_int = current_version_as_int + 1
# new_version = [digit for digit in str(new_version_as_int)]
# new_version = ".".join(new_version)
# print(new_version)

# second option
version = [int(digit) for digit in input().split(".")]
version[-1] += 1
for index in range(len(version) - 1, 0, -1):
    if version[index] > 9:
        version[index] = 0
        version[index - 1] += 1
print(".".join([str(digit) for digit in version]))