def binary_to_decimal(binary_input):
    # Convert to string to easily process digit by digit
    binary_str = str(binary_input)
    decimal_value = 0
    base = 1  # Represents 2^0 initially
    
    # Process from the last character to the first
    for digit in reversed(binary_str):
        if digit == '1':
            decimal_value += base
        base = base * 2  # Increase power of 2 for the next position
        
    return decimal_value

# Example usage:
print(binary_to_decimal("1010"))   # Output: 10
print(binary_to_decimal(11001))   # Output: 25