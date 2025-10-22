def username_valid_length(user:str):
    if 3<= len(user) <= 16:
        return True
    return False

def username_valid_char (user:str):
    for char in user:
        if not (char.isalnum() or char == "-" or char == "_"):
            return False
    return True

def username_no_redundant_symbol(user:str):
    for char in user:
        if char == " ":
            return False
    return True

def username_is_valid(user:str):
    if username_valid_length(user) and username_valid_char(user) and username_no_redundant_symbol(user):
        return True
    return False

usernames_to_check = input().split(", ")

for username in usernames_to_check:
    if username_is_valid(username):
        print(username)