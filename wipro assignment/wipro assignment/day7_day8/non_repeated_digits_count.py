n = abs(int(input("Enter a number: ")))

frequency = [0] * 10

if n == 0:
    frequency[0] = 1

while n > 0:
    digit = n % 10
    frequency[digit] += 1
    n //= 10

count = 0

for value in frequency:
    if value == 1:
        count += 1

print(count)