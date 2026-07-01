s = input("Enter a string: ")

frequency = {}

for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1

odd = 0

for value in frequency.values():
    if value % 2 != 0:
        odd += 1

if odd <= 1:
    print("Yes")
else:
    print("No")