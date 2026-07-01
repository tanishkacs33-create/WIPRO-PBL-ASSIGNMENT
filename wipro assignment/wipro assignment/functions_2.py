def ispalindrome(name):
    """
    Checks if the given name is a palindrome.
    Ignores spaces to accurately check full names.
    """
    # Remove spaces to check the actual letter sequence
    clean_name = name.replace(" ", "")
    if clean_name == clean_name[::-1]:
        return "Yes it is a palindrome."
    else:
        return "No it is not a palindrome."


def count_the_vowels(name):
    """
    Counts the number of vowels (a, e, i, o, u) in the name.
    """
    vowels = "aeiouAEIOU"
    count = sum(1 for char in name if char in vowels)
    return f"No of vowels: {count}"


def frequency_of_letters(name):
    """
    Calculates the frequency of each letter in the name,
    maintaining the order of appearance and ignoring spaces.
    """
    freq = {}
    for char in name:
        if char != " ":
            freq[char] = freq.get(char, 0) + 1
            
    # Format the dictionary into the required string output
    freq_items = [f"{char} - {count}" for char, count in freq.items()]
    return "Frequency of letters: " + ", ".join(freq_items)