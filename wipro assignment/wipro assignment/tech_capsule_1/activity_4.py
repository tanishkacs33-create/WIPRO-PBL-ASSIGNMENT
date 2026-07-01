# Prompting user input
num = int(input("Enter a number: "))

if num == 0:
    print("The number is Zero.")
elif num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")