# Employee superclass
class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    # Accessors (getters)
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    # Mutators (setters)
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number


# ProductionWorker subclass
class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        super().__init__(name, number)
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

    # Accessors
    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate

    # Mutators
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    # Method to return shift as string
    def get_shift_name(self):
        return "Day" if self.__shift_number == 1 else "Night"
def main():
    print("Enter the following details of the Employee")
    print("-" * 60)

    # User input
    name = input("Enter Employee Name: ")
    number = input("Enter Employee Number: ")
    pay_rate = float(input("Enter Pay Rate: "))
    shift_number = int(input("Enter Shift Number (1 for Day, 2 for Night): "))

    # Create ProductionWorker instance
    worker = ProductionWorker(name, number, shift_number, pay_rate)

    # Display employee details
    print("-" * 60)
    print("Details of Employee:")
    print("-" * 60)
    print(f"Name: {worker.get_name()}")
    print(f"Employee Number: {worker.get_number()}")
    print(f"Shift: {worker.get_shift_name()}")
    print(f"Pay Rate: {worker.get_hourly_pay_rate():.2f}")


# Run the program
if __name__ == "__main__":
    main()
# End of the code