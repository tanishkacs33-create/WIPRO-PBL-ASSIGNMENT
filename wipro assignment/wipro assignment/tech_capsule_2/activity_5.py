def smallest_divisor(n):
    if n <= 1:
        return "No divisor greater than 1 exists."
        
    divisor = 2
    # Loop until we find a number that perfectly divides n
    while n % divisor != 0:
        divisor += 1
        
    return divisor

# Example usage:
print(smallest_divisor(9))   # Output: 3
print(smallest_divisor(35))  # Output: 5
print(smallest_divisor(17))  # Output: 17 (since it's a prime number)