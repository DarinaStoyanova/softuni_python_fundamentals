food = input().split(" ")
storage = {}

for index in range(0,len(food), 2):
    key = food[index]
    value = food[index+1]
    storage[key] = int(value)

print(storage)