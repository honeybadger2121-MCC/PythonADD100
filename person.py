# Class definition for a Person
class Person:
    # Initializer with private variables
    def __init__(self, name, address, age, phone):
        self.__name = name        # Private variable for name
        self.__address = address  # Private variable for address
        self.__age = age          # Private variable for age
        self.__phone = phone      # Private variable for phone number

    # Method to get person's info as a formatted string
    def get_info(self):
        return f"Name: {self.__name}, Address: {self.__address}, Age: {self.__age}, Phone: {self.__phone}"

    # Getter for name
    def get_name(self):
        return self.__name

    # Getter for address
    def get_address(self):
        return self.__address

    # Getter for age
    def get_age(self):
        return self.__age

    # Getter for phone
    def get_phone(self):
        return self.__phone

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Setter for address
    def set_address(self, address):
        self.__address = address

    # Setter for age
    def set_age(self, age):
        self.__age = age

    # Setter for phone
    def set_phone(self, phone):
        self.__phone = phone


# Creating three Person objects
person1 = Person("Alex Johnson", "123 Maple St", 30, "555-1234")
person2 = Person("Jamie Rivera", "456 Oak Ave", 28, "555-5678")
person3 = Person("Taylor Kim", "789 Pine Rd", 35, "555-9012")

# Printing their information
print(person1.get_info())
print(person2.get_info())
print(person3.get_info())
