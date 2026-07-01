print("Enter 20 integers:")
numbers = [int(input(f"Element {i+1}: ")) for i in range(20)]

# Initialize tracking lists with infinity values to easily overwrite them
max_three = [-float('inf'), -float('inf'), -float('inf')]
min_three = [float('inf'), float('inf'), float('inf')]

for num in numbers:
    # Update maximum 3 elements
    if num > max_three[0]:
        max_three[2] = max_three[1]
        max_three[1] = max_three[0]
        max_three[0] = num
    elif num > max_three[1]:
        max_three[2] = max_three[1]
        max_three[1] = num
    elif num > max_three[2]:
        max_three[2] = num

    # Update minimum 3 elements
    if num < min_three[0]:
        min_three[2] = min_three[1]
        min_three[1] = min_three[0]
        min_three[0] = num
    elif num < min_three[1]:
        min_three[2] = min_three[1]
        min_three[1] = num
    elif num < min_three[2]:
        min_three[2] = num

print(f"\nMaximum 3 elements: {max_three}")
print(f"Minimum 3 elements: {min_three}")