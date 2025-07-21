def main():
    """
    Reads a list of number strings, converts them to floats,
    prints each formatted number, and calculates total, count, and average.
    Includes error handling for invalid input.
    """

    # List of number strings
    number_strings = [
        "13420.22",
        "45229.32",
        "35223.22",
        "29302.20",
        "95893.21",
        "94721.94",
        "84720.32",
        "84793.02",
        "10394.21",
        "30233.33",
        "23432.32"
    ]

    total = 0.0
    count = 0

    try:
        for line in number_strings:
            # Strip newline characters and convert to float
            number = float(line.strip())
            # Print formatted number with commas and 2 decimal places
            print(f"{number:,.2f}")
            # Update total and count
            total += number
            count += 1

        # Calculate average
        average = total / count if count > 0 else 0

        # Print summary
        print(f"Total: {total:,.2f}")
        print(f"Number of entries: {count}")
        print(f"Average: {average:,.2f}")

    except ValueError as e:
        print(f"Error converting line to float: {e}")

# Run the main function
if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# This script reads a list of number strings, converts them to floats,