string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

# Reverse string2 and concatenate
string3 = string1 + " " + string2[::-1]

print("Result:", string3)