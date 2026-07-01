def process_purchase():
    # Prompting the user for the file name during run time
    filename = input("Enter the file name: ").strip()
    
    # Appending .txt extension if the user didn't type it
    if not filename.lower().endswith('.txt'):
        filename += '.txt'

    # Initialize counters and accumulators
    total_items = 0
    free_items = 0
    total_amount = 0
    discount = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skip any blank lines
                
                # Split item name and price (assuming they are separated by space)
                # rsplit(' ', 1) helps handle item names with spaces (e.g., "Ice Cream 50")
                parts = line.rsplit(maxsplit=1)
                
                if len(parts) != 2:
                    continue  # Safeguard against malformed lines
                
                key, value = parts[0], parts[1]

                # Check if the line indicates the discount amount
                if key.lower() == 'discount':
                    try:
                        discount = float(value)
                    except ValueError:
                        print(f"Warning: Invalid discount value '{value}' encountered.")
                # Check if the item is free
                elif value.lower() == 'free':
                    free_items += 1
                # Otherwise, treat it as a regular purchased item
                else:
                    try:
                        price = float(value)
                        total_amount += price
                        total_items += 1
                    except ValueError:
                        print(f"Warning: Skipping invalid price format for line: '{line}'")

        # Calculating the final amount
        final_amount = total_amount - discount

        # Displaying the final formatted output
        print(f"No of items purchased: {total_items}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {int(total_amount) if total_amount.is_integer() else total_amount}")
        print(f"Discount given: {int(discount) if discount.is_integer() else discount}")
        print(f"Final amount paid: {int(final_amount) if final_amount.is_integer() else final_amount}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' could not be found. Please check the path and try again.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    process_purchase()