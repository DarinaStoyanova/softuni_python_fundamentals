text = input()
encrypted_version = ""

for letter in text:
    encrypted_version += chr(ord(letter) + 3)

print(encrypted_version)