def merge_descending_arrays(arr1, arr2):
    # Rearrange both random arrays in descending order
    arr1.sort(reverse=True)
    arr2.sort(reverse=True)
    
    merged = []
    i, j = 0, 0
    
    # Merge process using two pointers
    while i < len(arr1) and j < len(arr2):
        if arr1[i] >= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
            
    # Copy any remaining elements
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
        
    return merged

# Example Random Arrays
array_a = [12, 45, 2, 89]
array_b = [34, 56, 7, 11, 90]

result = merge_descending_arrays(array_a, array_b)
print("Merged Descending Array:", result)