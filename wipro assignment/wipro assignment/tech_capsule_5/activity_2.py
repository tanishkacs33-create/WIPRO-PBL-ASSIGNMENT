def remove_duplicates(arr):
    if not arr:
        return []
    
    # Step 1: Ensure it's an ordered array (Sorting it first)
    arr.sort()
    
    # Step 2: Remove duplicates by shifting elements
    unique_index = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[unique_index]:
            unique_index += 1
            arr[unique_index] = arr[i]
            
    # Contract the array to only keep the unique elements
    return arr[:unique_index + 1]

# Example Input from the sheet
input_array = [2, 4, 2, 5, 3, 4, 6, 5, 1, 7]
print("After ordering & removing duplicates:", remove_duplicates(input_array))