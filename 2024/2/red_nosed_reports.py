def is_safe(report):
    direction = 0  # 1 = increasing, -1 = decreasing

    for i in range(1, len(report)):
        difference = report[i] - report[i - 1]

        if difference == 0 or abs(difference) > 3:
            return False

        current_direction = 1 if difference > 0 else -1

        if direction == 0:
            direction = current_direction
        elif current_direction != direction:
            return False

    return True


def is_safe_with_dampener(report):
    # Already safe without removing anything
    if is_safe(report):
        return True

    # Try removing each level once
    for i in range(len(report)):
        shortened_report = report[:i] + report[i + 1:]

        if is_safe(shortened_report):
            return True

    return False


safe_count = 0

with open("input.txt", "r") as file:
    for line in file:
        report = list(map(int, line.split()))

        if is_safe_with_dampener(report):
            safe_count += 1

print(safe_count)