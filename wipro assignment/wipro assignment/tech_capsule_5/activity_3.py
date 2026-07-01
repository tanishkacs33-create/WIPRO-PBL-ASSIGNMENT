def find_max_positions(arr):
    if not arr:
        return None
    
    max_val = arr[0]
    first_pos = 0
    last_pos = 0
    
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            first_pos = i  # Update first occurrence
            last_pos = i   # Reset last occurrence to the same spot
        elif arr[i] == max_val:
            last_pos = i   # Update only the last occurrence
            
    return max_val, first_pos, last_pos

# Example Input (25 integer elements)
elements = [12, 35, 7, 45, 23, 45, 12, 5, 45, 3, 9, 14, 21, 45, 2, 8, 45, 19, 31, 40, 22, 11, 6, 17, 13]

max_value, first_idx, last_idx = find_max_positions(elements)
print(f"Maximum Value: {max_value}")
print(f"First Occurrence Position (Index): {first_idx}")
print(f"Last Occurrence Position (Index): {last_idx}")