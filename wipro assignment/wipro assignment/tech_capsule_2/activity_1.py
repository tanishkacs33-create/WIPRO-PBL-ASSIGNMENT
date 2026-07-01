def count_digits(n):
    # Handle the edge case where the number is 0
    if n == 0:
        return 1
    
    # Take the absolute value to handle negative numbers
    n = abs(n)
    count = 0
    
    while n > 0:
        count += 1
        n = n // 10  # Integer division to remove the last digit
        
    return count

# Example usage:
print(count_digits(12345))  # Output: 5
print(count_digits(123))    # Output: 3