# Initialize an empty list
numbers = []

print("Enter 10 integers:")
for i in range(10):
    val = int(input(f"Element {i+1}: "))
    numbers.append(val)

# Calculate sum
total_sum = sum(numbers)

print(f"\nThe sum of all elements is: {total_sum}")