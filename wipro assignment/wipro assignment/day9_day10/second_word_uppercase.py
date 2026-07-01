sentence = input("Enter a sentence: ")

words = sentence.split()

if len(words) >= 2:
    print(words[1].upper())
else:
    print("Second word not found")