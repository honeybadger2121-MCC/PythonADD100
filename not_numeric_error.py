# Define a custom exception class
class NotNumericError(Exception):
    """Exception raised when input is not numeric.

    Attributes:
        input_value -- the invalid input provided by the user
        message -- explanation of the error
    """
    def __init__(self, input_value, message="Input must be a numeric value."):
        self.input_value = input_value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"'{self.input_value}' -> {self.message}"


# Function to prompt user for numeric input
def get_numeric_input():
    while True:
        try:
            user_input = input("Please enter a number: ")
            if not user_input.isnumeric():
                raise NotNumericError(user_input)
        except NotNumericError as e:
            print(f"Error: {e}")
        else:
            print(f"Thank you! You entered the number: {user_input}")
            break
        finally:
            print("End of this input attempt.\n")


# Run the program
if __name__ == "__main__":
    get_numeric_input()
# This code defines a custom exception for non-numeric input and prompts the user for numeric input.
# If the input is not numeric, it raises the custom exception and handles it gracefully.