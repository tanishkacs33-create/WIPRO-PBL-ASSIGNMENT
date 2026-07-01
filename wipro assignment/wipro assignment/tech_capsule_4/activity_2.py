input_str = input("Enter a string: ")
vowels = "aeiouAEIOU"
has_vowel = False
result = []

for char in input_str:
    if char in vowels:
        result.append('z')
        has_vowel = True
    else:
        result.append(char)

output_str = "".join(result)

if has_vowel:
    print(output_str)
else:
    print(output_str)
    print("No vowels present")