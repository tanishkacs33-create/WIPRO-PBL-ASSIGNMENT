n = abs(int(input("Enter a number: ")))

if n == 0:
    print(1)
else:
    count = 0

    while n > 0:
        count += 1
        n //= 10

    print(count)