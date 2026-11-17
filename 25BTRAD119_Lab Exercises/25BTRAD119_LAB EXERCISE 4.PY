# Simple calculator and area calculation program

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nCalculator")
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")

radius = float(input("\nEnter radius of circle: "))
circle_area = 3.14 * radius * radius
print(f"Area of circle: {circle_area:.2f}")

length = float(input("\nEnter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
rectangle_area = length * breadth
print(f"Area of rectangle: {rectangle_area:.2f}")

base = float(input("\nEnter base of triangle: "))
height = float(input("Enter height of triangle: "))
triangle_area = 0.5 * base * height
print(f"Area of triangle: {triangle_area:.2f}")