# You have a water tank with a capacity of 255 liters.
# On the first line, you will receive n – the number of lines, which will follow.
# On the following n lines, you will receive liters of water (integers), which you should pour into your tank.
# If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line. On the last line, print the liters in the tank.

number_of_doses = int(input())
litters_accumulated = 0

for dose in range (1, number_of_doses+1):
    litters_added = int(input())
    litters_accumulated += litters_added
    if litters_accumulated > 255:
        print("Insufficient capacity!")
        litters_accumulated -= litters_added
print(litters_accumulated)