level_of_fire = input().split("#")
water_i_have = int(input())
effort = 0
list_cells = []

for fire in level_of_fire:
    data = fire.split(" = ")
    fire_degree = data[0]
    needed_water = int(data[1])
    if fire_degree == "High" and 81 <= needed_water <= 125:
        water_i_have -= needed_water
        effort += 0.25 * needed_water
        if water_i_have < 0:
            water_i_have += needed_water
            effort -= 0.25 * needed_water
    elif fire_degree == "Medium" and 51 <= needed_water <= 80:
        water_i_have -= needed_water
        effort += 0.25 * needed_water
        if water_i_have < 0:
            water_i_have += needed_water
            effort -= 0.25 * needed_water
    elif fire_degree == "Low" and 1 <= needed_water <= 50:
        water_i_have -= needed_water
        effort += 0.25 * needed_water
        if water_i_have < 0:
            water_i_have += needed_water
            effort -= 0.25 * needed_water

print(effort)
