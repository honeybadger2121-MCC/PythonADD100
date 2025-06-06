# Ask the user to enter the first number and convert it to an integer
num1 = int(input("Enter a number: "))

# Ask the user to enter the second number and convert it to an integer
num2 = int(input("Enter another number: "))

# Check if both numbers are the same
if num1 == num2:
    # If they are equal, print a message and stop the program
    print("The numbers should be different.")
else:
    # If the numbers are different, continue with logical comparisons
    print("\nLet's look at some logic with your numbers:\n")

    # --- AND Operators ---
    # This checks if num1 is greater than num2 AND if num1 is also positive
    print("Both num1 is bigger than num2 AND num1 is positive:", num1 > num2 and num1 > 0)

    # This checks if num2 is greater than num1 AND if num2 is less than 100
    print("Both num2 is bigger than num1 AND num2 is less than 100:", num2 > num1 and num2 < 100)

    # --- OR Operators ---
    # This checks if either num1 is negative OR num2 is positive
    print("Either num1 is negative OR num2 is positive:", num1 < 0 or num2 > 0)

    # This checks if either num1 is zero OR num2 is zero
    print("Either num1 is zero OR num2 is zero:", num1 == 0 or num2 == 0)

    # --- NOT Operators ---
    # This checks if it is NOT true that num1 is greater than num2
    print("It is NOT true that num1 is bigger than num2:", not num1 > num2)

    # This checks if it is NOT true that num2 is less than 50
    print("It is NOT true that num2 is less than 50:", not (num2 < 50))
