# Python String Methods Practice

# Use the capitalize() method to capitalize the first letter of the string
string1 = "python"
print(f"{string1} -> {string1.capitalize()}")
string1 = string1.capitalize()

# Use the center() method to center the string in a string of specified width
string2 = "python"
print(f"{string2} -> {string2.center(10)}")
string2 = string2.center(10)

# Use the endswith() method to check if the string ends with a specified substring
string3 = "python"
print(f"{string3} ends with 'on' -> {string3.endswith('on')}")
ends_with_on = string3.endswith("on")

# Use the find() method to find the first occurrence of a substring in the string
string4 = "python"
print(f"{string4} find 'th' -> {string4.find('th')}")
position_th = string4.find("th")

# Use the isalnum() method to check if all characters in the string are alphanumeric
string5 = "python3"
print(f"{string5} is alphanumeric -> {string5.isalnum()}")
is_alnum = string5.isalnum()

# Use the isalpha() method to check if all characters in the string are alphabetic
string6 = "python"
print(f"{string6} is alphabetic -> {string6.isalpha()}")
is_alpha = string6.isalpha()

# Use the islower() method to check if all characters in the string are lowercase
string7 = "python"
print(f"{string7} is lowercase -> {string7.islower()}")
is_lower = string7.islower()

# Use the isspace() method to check if all characters in the string are whitespaces
string8 = "   "
print(f"'{string8}' is whitespace -> {string8.isspace()}")
is_space = string8.isspace()

# Use the isupper() method to check if all characters in the string are uppercase
string9 = "PYTHON"
print(f"{string9} is uppercase -> {string9.isupper()}")
is_upper = string9.isupper()

# Use the join() method to join elements of an iterable with the string as the separator
iterable1 = ["Python", "is", "fun"]
separator = "-"
print(f"{iterable1} joined with '{separator}' -> {separator.join(iterable1)}")
joined_string = separator.join(iterable1)

# Use the lower() method to convert all characters in the string to lowercase
string10 = "PYTHON"
print(f"{string10} -> {string10.lower()}")
string10 = string10.lower()

# Use the lstrip() method to remove leading characters (spaces by default)
string11 = "  python"
print(f"'{string11}' -> '{string11.lstrip()}'")
string11 = string11.lstrip()

# Use the rstrip() method to remove trailing characters (spaces by default)
string12 = "python  "
print(f"'{string12}' -> '{string12.rstrip()}'")
string12 = string12.rstrip()

# Use the replace() method to replace all occurrences of a substring with another substring
string13 = "I love python"
print(f"{string13} -> {string13.replace('python', 'snake')}")
string13 = string13.replace("python", "snake")

# Use the rfind() method to find the highest index of a substring
string14 = "python"
print(f"{string14} rfind 'n' -> {string14.rfind('n')}")
highest_index_n = string14.rfind("n")

# Use the split() method to split the string at a specified separator
string15 = "python-is-fun"
print(f"{string15} split at '-' -> {string15.split('-')}")
split_string = string15.split("-")

# Use the startswith() method to check if the string starts with a specified substring
string16 = "python"
print(f"{string16} starts with 'py' -> {string16.startswith('py')}")
starts_with_py = string16.startswith("py")

# Use the strip() method to remove both leading and trailing characters (spaces by default)
string17 = "  python  "
print(f"'{string17}' -> '{string17.strip()}'")
string17 = string17.strip()

# Use the swapcase() method to swap the case of all characters in the string
string18 = "Python"
print(f"{string18} -> {string18.swapcase()}")
string18 = string18.swapcase()

# Use the title() method to convert the first character of each word to uppercase
string19 = "python is fun"
print(f"{string19} -> {string19.title()}")
string19 = string19.title()

# Use the upper() method to convert all characters in the string to uppercase
string20 = "python"
print(f"{string20} -> {string20.upper()}")
string20 = string20.upper()
# Use the zfill() method to pad the string with zeros on the left