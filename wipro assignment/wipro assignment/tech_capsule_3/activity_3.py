print("Enter 10 integers:")
numbers = [int(input(f"Element {i+1}: ")) for i in range(10)]

# Reverse the array manually using swapping
start = 0
end = len(numbers) - 1

while start < end:
    # Swap elements
    numbers[start], numbers[end] = numbers[end], numbers[start]
    start += 1
    end -= 1

print(f"\nReversed array: {numbers}")