import fractions

def main():
    # Introduction to the calculator
    print("Welcome to the Simple Calculator!")
    print("You can perform division operations here.")
    
    while True:
        try:
            # Get user input and convert to float
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Perform division and calculate the result
            result = num1 / num2
            
            # Convert the decimal result to a fraction
            fraction_result = fractions.Fraction(result).limit_denominator()
            
        except ZeroDivisionError:
            # Handle division by zero error
            print("Oops! Can't divide by zero. Try a different number.")
        except ValueError:
            # Handle invalid input error (non-numeric values)
            print("That's not a valid number! Please enter a valid number.")
        except Exception as e:
            # Handle any other unexpected errors
            print(f"An unexpected error occurred: {e}")
        else:
            # Display the result as both a decimal and a fraction
            print(f"The result of {num1} / {num2} is: {result} (or {fraction_result} as a fraction)")
            break  # Exit the loop after successful calculation

if __name__ == "__main__":
    # Entry point of the program
    main()
# and can win or lose based on their guesses.
# The game continues until the player either guesses the word or exceeds the maximum number of wrong guesses