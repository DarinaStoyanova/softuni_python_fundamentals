strength_values = list(map(int, input().split()))
accuracy_values = list(map(int, input().split()))
scored_goals = 0

while strength_values and accuracy_values:
    last_strength = strength_values[-1]
    first_accuracy = accuracy_values[0]
    sum_data = last_strength + first_accuracy

    if sum_data == 100:
        strength_values.pop()
        accuracy_values.pop(0)
        scored_goals += 1

    elif sum_data < 100:
        if last_strength < first_accuracy:
            strength_values.pop()
        elif last_strength > first_accuracy:
            accuracy_values.pop(0)
        else:
            strength_values[-1] = sum_data
            accuracy_values.pop(0)

    else:
        strength_values[-1] -= 10
        accuracy_values.append(accuracy_values.pop(0))

if scored_goals == 3:
    print("Paul scored a hat-trick!")
elif scored_goals <= 0:
    print("Paul failed to score a single goal.")
elif scored_goals > 3:
    print("Paul performed remarkably well!")
elif 0 < scored_goals < 3:
    print("Paul failed to make a hat-trick.")

if scored_goals:
    print(f"Goals scored: {scored_goals}")

if strength_values:
    print("Strength values left: " + ", ".join(map(str, strength_values)))

if accuracy_values:
    print("Accuracy values left: " + ", ".join(map(str, accuracy_values)))
