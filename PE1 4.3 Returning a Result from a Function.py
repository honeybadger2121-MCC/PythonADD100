def calculate_interest(principal, rate, time):
    """
    Calculate the simple interest based on principal, rate, and time.
    Formula: (Principal × Rate × Time) / 100
    """
    # Calculate interest using the formula
    interest = (principal * rate * time) / 100
    return interest

def main():
    # Prompt user to enter the principal amount and convert it to a float
    principal = float(input("Enter the principal amount: "))
    
    # Prompt user to enter the annual interest rate and convert it to a float
    rate = float(input("Enter the annual interest rate (%): "))
    
    # Prompt user to enter the time in years and convert it to a float
    time = float(input("Enter the time in years: "))

    # Calculate interest using the calculate_interest function
    interest = calculate_interest(principal, rate, time)

    # Print the result with formatted strings to show the interest calculation
    print(f"The simple interest for ${principal:,.2f} at {rate}% over {time} years is ${interest:,.2f}.")

# Check if the script is being run directly (not imported) and call the main function
if __name__ == "__main__":
    main()
# This code defines a function to calculate simple interest and uses it in a main function to interact with the user.