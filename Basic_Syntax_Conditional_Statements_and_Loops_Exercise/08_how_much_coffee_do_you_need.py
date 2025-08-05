command = input()
number_of_coffees = 0
while command != "END":
    if command == "coding":
        number_of_coffees += 1
    elif command == "CODING":
        number_of_coffees += 2
    elif command == "dog":
        number_of_coffees += 1
    elif command == "DOG":
        number_of_coffees += 2
    elif command == "cat":
        number_of_coffees += 1
    elif command == "CAT":
        number_of_coffees += 2
    elif command == "movie":
        number_of_coffees += 1
    elif command == "MOVIE":
        number_of_coffees += 2

    command = input()

if number_of_coffees > 5:
    print("You need extra sleep")
else:
    print (number_of_coffees)
