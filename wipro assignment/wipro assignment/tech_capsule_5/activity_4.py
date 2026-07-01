def find_element_x(arr, x):
    # Search linearly through the array
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Return index position if found
    return -1  # Return -1 if X does not exist

# Simulating 15 elements entered by a user
user_array = [10, 22, 35, 47, 50, 63, 75, 88, 91, 14, 25, 36, 49, 80, 99]
X = int(input("Enter the number X to search: "))

position = find_element_x(user_array, X)

if position != -1:
    print(f"Number {X} found at index position: {position}")
else:
    print(f"Number {X} is not present in the array.")