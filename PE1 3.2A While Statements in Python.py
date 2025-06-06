# Initialize the bottle count to 99
count = 99

# Loop while there are still bottles remaining
while count > 0:
    # Check if only one bottle is left to use singular 'bottle'
    if count == 1:
        print(f"{count} bottle of beer on the wall, {count} bottle of beer.")
        print("Take it down, pass it around, no more bottles of beer on the wall.\n")
    else:
        # For more than one bottle, use plural 'bottles'
        print(f"{count} bottles of beer on the wall, {count} bottles of beer.")
        # After taking one down, update the count and grammar accordingly
        print(f"Take one down, pass it around, {count - 1} {'bottle' if count - 1 == 1 else 'bottles'} of beer on the wall.\n")
    # Decrease the bottle count by 1 after each verse
    count -= 1