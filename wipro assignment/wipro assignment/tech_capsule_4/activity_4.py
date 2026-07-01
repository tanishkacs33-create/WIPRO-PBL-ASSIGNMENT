input_string = input("Enter a string: ")

# Track which characters we have already counted to match the exact output format
processed_chars = set()

for char in input_string:
    if char not in processed_chars:
        count = input_string.count(char)
        print(f"{char} – {count}")
        processed_chars.add(char)