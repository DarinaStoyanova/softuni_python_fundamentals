# You will be given an integer that represents a distance in meters.
# Write a program that converts meters to kilometers, formatted to the second decimal point.

distance_in_meters = int(input())
meters_to_km = distance_in_meters / 1000
print(f"{meters_to_km:.2f}")