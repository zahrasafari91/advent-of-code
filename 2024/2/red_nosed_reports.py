def is_safe(report):
    direction = 0  # 1 = increasing, -1 = decreasing

    for i in range(1, len(report)):
        difference = report[i] - report[i - 1]

        # Difference must be between 1 and 3
        if difference == 0 or abs(difference) > 3:
            return False

        current_direction = 1 if difference > 0 else -1

        # Set direction using the first pair
        if direction == 0:
            direction = current_direction

        # Direction changed
        elif current_direction != direction:
            return False

    return True


safe_count = 0

with open("input.txt", "r") as file:
    for line in file:
        report = list(map(int, line.split()))

        if is_safe(report):
            safe_count += 1

print(safe_count)