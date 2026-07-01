import re
from collections import Counter

def find_secret_message(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
        # 1. Determine Meeting Time based on number of lines
        num_lines = len(lines)
        if num_lines > 12:
            time_str = f"{num_lines - 12} PM"
        elif num_lines == 12:
            time_str = "12 PM"
        else:
            time_str = f"{num_lines} AM"
            
        # 2. Determine Meeting Place based on the most frequent word
        all_words = []
        for line in lines:
            
            words = re.findall(r'\b\w+ \b', line)
            
            words = re.findall(r'[a-zA-Z]+', line)
            all_words.extend(words)
            
        # Count frequencies
        word_counts = Counter(all_words)
        
        # Find the most common word
        if word_counts:
            most_common_word, _ = word_counts.most_common(1)[0]
        else:
            most_common_word = "Unknown"
            
        # Capitalize the street name properly as shown in sample outputs
        meeting_place = f"{most_common_word.capitalize()} Street"
        
        # Print outputs in the required format
        print(f"Meeting time: {time_str}")
        print(f"Meeting place: {meeting_place}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Take file name as input from the user
filename = input("Enter the filename (e.g., Sample.txt): ").strip()
find_secret_message(filename)