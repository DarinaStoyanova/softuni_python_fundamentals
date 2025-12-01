message = input()
encrypted_message = list(message)

while message != "Decode" :
    message = message.split("|")
    if message[0] == "Move":
        letters_to_move = int(message[1])
        for letter in encrypted_message[:letters_to_move]:
            encrypted_message.remove(letter)
            encrypted_message.append(letter)
    elif message[0] == "Insert":
        index, value = int(message[1]), message[2]
        encrypted_message.insert(index, value)
    elif message[0] == "ChangeAll":
        change_letter, new_letter = message[1], message[2]
        if change_letter in encrypted_message:
            encrypted_message = "".join(encrypted_message)
            encrypted_message = encrypted_message.replace(change_letter, new_letter)
            encrypted_message = list(encrypted_message)

    message = input()


print(f"The decrypted message is: {''.join(encrypted_message)}")