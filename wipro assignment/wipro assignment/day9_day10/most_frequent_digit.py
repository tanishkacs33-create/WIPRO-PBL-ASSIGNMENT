n = abs(int(input("Enter a number: ")))

frequency = [0] * 10

if n == 0:
    frequency[0] = 1

while n > 0:
    digit = n % 10
    frequency[digit] += 1
    n //= 10

maximum = max(frequency)

for i in range(10):
    if frequency[i] == maximum:
        print(i)
        break