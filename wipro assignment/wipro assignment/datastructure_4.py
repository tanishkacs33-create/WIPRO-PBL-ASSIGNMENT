import re

def count_alex_occurrences(input_string):
    # Use re.findall to find all occurrences of the substring 'Alex'
    matches = re.findall(r'Alex', input_string)
    return len(matches)

# --- Test with the sample input ---
if __name__ == "__main__":
    sample_input = "Hi Alex WelcomeAlex Bye Alex."
    
    # Calculate and print the output
    output = count_alex_occurrences(sample_input)
    print(output)