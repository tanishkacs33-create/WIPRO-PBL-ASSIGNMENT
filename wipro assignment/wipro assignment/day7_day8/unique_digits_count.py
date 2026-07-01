n = abs(int(input("Enter a number: ")))

digits = set()

if n == 0:
    digits.add(0)

while n > 0:
    digits.add(n % 10)
    n //= 10

print(len(digits))