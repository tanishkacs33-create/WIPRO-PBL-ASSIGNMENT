even = 0
odd = 0

for _ in range(5):
    n = int(input())
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)