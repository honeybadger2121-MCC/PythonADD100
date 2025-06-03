# Function to calculate factorial
def factorial(n):
    """
    Function to calculate the factorial of a number using recursion.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    """
    Main function to drive the program.
    """
    # Asking for user input
    num = int(input("Enter a non-negative integer: "))
   
    # Calling the factorial function
    print(f"Factorial of {num} is {factorial(num)}")

# Launching the program
main()