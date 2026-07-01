def second_last_digit(n):
    n = abs(n)

    if n < 10:
        return -1

    return (n // 10) % 10


n = int(input("Enter a number: "))
print(second_last_digit(n))