from datetime import datetime, timedelta

def main():
    """
    This function prompts the user for their birthday and calculates their age
    in years, months, weeks, days, hours, and minutes using the datetime module.
    """

    try:
        # Ask the user for their birth year
        birth_year = int(input("What year were you born? "))

        # Ask the user for their birth month (as a number)
        birth_month = int(input("What month were you born (as a number. May would be 5)? "))

        # Ask the user for the day of the month they were born
        birth_day = int(input("What day of the month were you born? "))

        # Create a datetime object for the user's birthday
        birthday = datetime(birth_year, birth_month, birth_day)

        # Print the birthday in YYYY-MM-DD format
        print("\nYour birthday is:")
        print(birthday.strftime("%Y-%m-%d"))

        # Get the current date and time
        now = datetime.now()

        # Calculate the difference between now and the birthday
        difference = now - birthday

        # Total number of days
        total_days = difference.days
        print(f"The difference is {total_days} days")

        # Calculate age in years (approximate, accounting for leap years)
        years = total_days / 365.25
        print(f"You are {years:.1f} years old")

        # Calculate age in months (approximate)
        months = years * 12
        print(f"You are approximately {months:.1f} months old")

        # Calculate age in weeks
        weeks = total_days / 7
        print(f"You are approximately {weeks:.1f} weeks old")

        # Calculate age in hours
        hours = difference.total_seconds() / 3600
        print(f"You are approximately {hours:,.0f} hours old")

        # Calculate age in minutes
        minutes = difference.total_seconds() / 60
        print(f"You are approximately {minutes:,.0f} minutes old")

    except ValueError as e:
        # Handle invalid input
        print(f"Invalid input: {e}. Please enter numeric values for year, month, and day.")

# Run the main function
if __name__ == "__main__":
    main()
# This script calculates the user's age based on their birthday input.
# It uses the datetime module to handle date calculations and formatting.
# The script prompts the user for their birth date, calculates the difference