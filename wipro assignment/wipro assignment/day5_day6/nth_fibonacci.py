n = int(input("Enter the value of N: "))

if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    a = 0
    b = 1

    for _ in range(3, n + 1):
        c = a + b
        a = b
        b = c

    print(b)