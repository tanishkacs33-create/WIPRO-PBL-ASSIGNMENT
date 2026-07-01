n = int(input("Enter a number: "))

original = abs(n)
temp = original
reverse = 0

while temp > 0:
    reverse = reverse * 10 + temp % 10
    temp //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")