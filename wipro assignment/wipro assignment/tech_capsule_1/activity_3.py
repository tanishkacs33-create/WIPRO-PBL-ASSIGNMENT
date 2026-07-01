# Sample list of 5 numbers
numbers = [-5, 12, 0, -3, 8]

negative_count = 0
non_negative_count = 0

for num in numbers:
    if num < 0:
        negative_count += 1
    else:
        non_negative_count += 1

print(f"Negative numbers: {negative_count}")
print(f"Non-negative numbers: {non_negative_count}")