n = abs(int(input("Enter a number: ")))

even_sum = 0
odd_sum = 0

while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit

    n //= 10

print("Even Digit Sum:", even_sum)
print("Odd Digit Sum:", odd_sum)