# Loop through numbers from 1 to 300 (inclusive)
for num in range(1, 301):
    # Check if the current number is divisible by 7 (no remainder)
    if num % 7 == 0:
        # If divisible, print the number
        print(num)