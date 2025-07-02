from math_operations import calculator

from math_operations import geometry

result = calculator.add(7, 2)
print("Addition result:", result)

result = calculator.subtract(10, 4)
print("Subtraction result:", result)

circle_area = geometry.area_of_circle(5)
print("Area of circle:", circle_area)

rectangle_area = geometry.area_of_rectangle(4, 6)
print("Area of rectangle:", rectangle_area)
# This is a simple main module that imports functions from the math_operations package
# and uses them to perform some calculations.