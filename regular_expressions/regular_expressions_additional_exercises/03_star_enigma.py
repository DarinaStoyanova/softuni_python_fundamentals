import re
filtered_list = []
attacked_planets_counter = 0
destroyed_planets_counter = 0
attacked_planets = []
destroyed_planets = []
pattern = r"[starSTAR]+"
new_pattern = r"@([A-Za-z]+)[^@!,:'\->]*:([0-9]+)[^@!,:'\->]*!([AD])![^@!,:'\->]*->([0-9]+)"
new_message = ""
n = int(input())

while n > 0:
    n -= 1
    message = input()
    filtered_message = re.findall(pattern, message)
    removal_counter = int(len("".join(filtered_message)))

    for char in message:
        new_char = chr(ord(char) - removal_counter)
        new_message += new_char
    decrypted_message = re.findall(new_pattern,new_message)

    if decrypted_message:
        planet,population,attack_type,soldier_count = decrypted_message[0][0],decrypted_message[0][1],decrypted_message[0][2],decrypted_message[0][3]
        if attack_type == "A":
            attacked_planets_counter += 1
            attacked_planets.append(planet)
        elif attack_type == "D":
            destroyed_planets_counter += 1
            destroyed_planets.append(planet)

    new_message = ""

print(f"Attacked planets: {attacked_planets_counter}")
attacked_planets = sorted(attacked_planets)
for planet in attacked_planets:
    print(f"-> {planet}")

print(f"Destroyed planets: {destroyed_planets_counter}")
destroyed_planets = sorted(destroyed_planets)
for planet in destroyed_planets:
    print(f"-> {planet}")