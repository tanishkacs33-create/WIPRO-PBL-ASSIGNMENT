import sys

def calculate_happiness():
    # sys.argv[0] is the script name, so we check if all 3 strings are provided
    if len(sys.argv) < 4:
        print("Please provide exactly three space-separated strings as command line arguments.")
        return

    # Extract strings from command line arguments
    string1 = sys.argv[1]
    string2 = sys.argv[2]
    string3 = sys.argv[3]

    # Convert hyphen-separated strings into sets for O(1) fast lookup
    # Using sets ensures optimal performance even with large inputs
    liked_numbers = set(string1.split('-'))
    disliked_numbers = set(string2.split('-'))
    
    # Convert the third string into a list of numbers to iterate through
    my_numbers = string3.split('-')

    happiness = 0

    # Calculate final happiness
    for num in my_numbers:
        if num in liked_numbers:
            happiness += 1
        elif num in disliked_numbers:
            happiness -= 1

    # Output the final happiness
    print(happiness)

if __name__ == "__main__":
    calculate_happiness()