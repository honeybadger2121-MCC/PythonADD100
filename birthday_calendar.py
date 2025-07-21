import calendar
import datetime

def main():
    """
    This function asks the user for their birth month and displays
    the calendar for that month in the current year.
    """

    # Get the current year using datetime
    current_year = datetime.datetime.now().year

    try:
        # Ask the user for their birth month
        birth_month = int(input("Enter your birth month (1-12): "))

        # Validate the input
        if 1 <= birth_month <= 12:
            # Generate and display the calendar for the given month and current year
            print(f"\nHere is your birth month calendar for {calendar.month_name[birth_month]} {current_year}:\n")
            print(calendar.month(current_year, birth_month))
        else:
            print("Invalid month. Please enter a number between 1 and 12.")

    except ValueError:
        # Handle non-integer input
        print("Invalid input. Please enter a numeric value between 1 and 12.")

# Run the main function
if __name__ == "__main__":
    main()
# This script displays the calendar for the user's birth month in the current year.
# It uses the calendar module to generate the calendar and datetime to get the current year.