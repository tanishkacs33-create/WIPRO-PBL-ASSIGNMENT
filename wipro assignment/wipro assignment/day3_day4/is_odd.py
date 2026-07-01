def is_odd(n):
    if n % 2 != 0:
        return 2
    return 1


n = int(input("Enter a number: "))
print(is_odd(n))