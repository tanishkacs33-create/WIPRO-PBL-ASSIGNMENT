def add_last_digits(a, b):
    return abs(a) % 10 + abs(b) % 10


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(add_last_digits(a, b))