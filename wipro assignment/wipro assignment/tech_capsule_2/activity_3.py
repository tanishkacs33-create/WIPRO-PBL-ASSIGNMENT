def decimal_to_binary(n):
    if n == 0:
        return "0"
        
    binary_str = ""
    while n > 0:
        remainder = n % 2
        binary_str = str(remainder) + binary_str  # Append to the front
        n = n // 2
        
    return binary_str

# Example usage:
print(decimal_to_binary(10))  # Output: "1010"
print(decimal_to_binary(25))  # Output: "11001"