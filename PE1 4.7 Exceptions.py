# Simple Python program to calculate the square of a number with error handling

def square_number():
    try:
        number = int(input("Enter a number to square: "))
        squared_number = number ** 2
        print(f"The square of {number} is {squared_number}.")
    except ValueError:
        print("Error: Please enter a valid number.")

square_number()