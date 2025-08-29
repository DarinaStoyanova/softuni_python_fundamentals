total_days = int(input())
plunder_per_day = int(input())
expected_plunder = int(input())
total_plunder = 0
count_days = 0

while total_days > 0:
    total_days -= 1
    count_days += 1
    if count_days % 3 == 0:
        total_plunder += 0.5 * plunder_per_day
    if count_days % 5 == 0:
        total_plunder += plunder_per_day
        total_plunder -= 0.3 * total_plunder
    else:
        total_plunder += plunder_per_day

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    left_as_percent = (total_plunder / expected_plunder) * 100
    print(f"Collected only {left_as_percent:.2f}% of the plunder.")