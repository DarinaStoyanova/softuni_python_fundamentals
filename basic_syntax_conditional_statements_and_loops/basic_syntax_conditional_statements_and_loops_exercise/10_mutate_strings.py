# first_string = input()
# # second_string = input()
# #
# # last_printed_string = first_string
# #
# # for char_index in range (len(first_string)):
# #     left_part = second_string[:char_index + 1]
# #     right_part = first_string[char_index + 1:]
# #     new_string = left_part + right_part
# #     if new_string != last_printed_string:
# #         print(new_string)
# #         last_printed_string = new_string
from unittest.mock import right

# Дадени са два низа с еднаква дължина – start и target.
# Трябва да преобразуваш start в target, като на всяка стъпка променяш един символ от start на съответния символ от target.
# След всяка промяна отпечатваш новия низ, само ако той е различен от предишния отпечатан.

start = input()
end = input()

last_printed = start
for char_index in range (len(start)): # 0
    left_part = end[:char_index+1] # 0
    right_part = start[char_index+1:]
    new_str = left_part + right_part
    if new_str != last_printed:
        print(new_str)
        last_printed = new_str













