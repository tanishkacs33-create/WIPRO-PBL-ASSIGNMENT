def sum_of_digits(n):
    n = abs(n)
    total_sum = 0
    
    while n > 0:
        digit = n % 10  # Extract the last digit
        total_sum += digit
        n = n // 10     # Remove the last digit
        
    return total_sum

# Example usage:
print(sum_of_digits(12345))  # Output: 15 (1 + 2 + 3 + 4 + 5)