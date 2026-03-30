
def average_ratios(numbers):
    total = 0
    count = 0
    for i in range(len(numbers)):
        if numbers[i] == 0:
            print(f"Warning: Division by zero at index {i}, skipping.")
            continue
        total += 100 / numbers[i]
        count += 1
    if count == 0:
        return 0  # Or raise an exception if all are zero
    return total / count

print(average_ratios([10, 5, 0]))
