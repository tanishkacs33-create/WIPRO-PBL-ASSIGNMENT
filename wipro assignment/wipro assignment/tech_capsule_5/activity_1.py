def sort_descending(arr):
    n = len(arr)
    # Outer loop to traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is less than the next element
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example Input (10 integer elements)
input_array = [23, 1, 45, 9, 56, 12, 89, 4, 7, 55]
print("Original Array:", input_array)

sorted_array = sort_descending(input_array)
print("Descending Order:", sorted_array)