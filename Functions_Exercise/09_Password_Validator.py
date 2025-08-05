password = input()

def password_checker(passw:str):
    counter_pass = 0
    counter = 0
    if 6 <= len(passw) <= 10:
        counter_pass += 1
    else:
        print("Password must be between 6 and 10 characters")
    if passw.isalnum():
        counter_pass += 1
    else:
        print("Password must consist only of letters and digits")
    for char in passw:
        if char.isdigit():
            counter += 1
        else:
            continue
    if counter >= 2:
        counter_pass += 1
    else:
        print("Password must have at least 2 digits")

    if counter_pass == 3:
        print("Password is valid")

password_checker(password)






