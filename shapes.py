"""
******************************
CS 1026 - Assignment 1 – Shapes and Sizes
Code by: Fardin Abbassi
Student ID: fabbassi
File created: September 19, 2024
******************************
This file is used to calculate the area and perimeter of a given shape. 
Its calculations depend on the shape specified, having different parameters
for each type of shape. If correct parameters are added, the name of the shape
alongside its calculated area and perimeter will be printed. 
"""
import math

# Initializing Variables
area = 0
perimeter = 0
shapeAbandoned = False

# Shape Input
shape = input("What shape do you want to work with? ")

# If rectangle, give parameters
if shape.lower() == "rectangle":
    width = float(input("What is the width of your rectangle? "))
    height = float(input("What is the height of your rectangle? "))
    
    # If values are positive and non-zero, calculate area and perimeter
    if width > 0 and height > 0:
        area = width * height
        perimeter = 2* width + 2 * height
    # Otherwise stop final display
    else:
        print("Invalid input, abandoning rectangle")
        shapeAbandoned = True
        
# If rectangle, give parameters
elif shape.lower() == "triangle":
    base = float(input("What is the length of the base of your triangle? "))
    side1 = float(input("What's the length of one of the other sides of your triangle? "))
    side2 = float(input("What's the length of the the other side of your triangle? "))
    height = float(input("What is the height of your triangle? "))
        
    # If values are positive and non-zero, calculate area and perimeter
    if side1 > 0 and side2 > 0 and base > 0 and height > 0:
        area = base * height / 2
        perimeter = base + side1 + side2

    # Otherwise stop final display
    else:
        print("Invalid input, abandoning triangle")
        shapeAbandoned = True

# If rectangle, give parameters
elif shape.lower() == "circle":
    radius = float(input("What's the radius of your circle? "))
        
    # If value is positive and non-zero, calculate area and perimeter
    if radius > 0:
        area = math.pi * radius**2
        perimeter = 2 * math.pi * radius
    
    # Otherwise stop final display
    else:
        print("Invalid input, abandoning circle")
        shapeAbandoned = True

# If rectangle, give parameters
elif shape.lower() == "trapezoid":
    topSide = float(input("What's the length of the top of your trapezoid? "))
    base = float(input("What is the length of the base of your trapezoid? "))
    leftSide = float(input("What's the length of the left side of your trapezoid? "))
    rightSide = float(input("What's the length of the right side of your trapezoid? "))
    height = float(input("What is the height of your trapezoid? "))
        
    # If values are positive and non-zero, calculate area and perimeter
    if leftSide > 0 and rightSide > 0 and base > 0 and height > 0 and topSide > 0:
        area = (topSide + base) * height / 2
        perimeter = topSide + rightSide + leftSide + base

    # Otherwise stop final display
    else:
        print("Invalid input, abandoning triangle")
        shapeAbandoned = True

# If rectangle, give parameters
elif shape.lower() == "hexagon":
    sideLength = float(input("What's the side length of your hexagon? "))
        
    # If value is positive and non-zero, calculate area and perimeter
    if sideLength > 0:
        area = 3 * math.sqrt(3) / 2 * sideLength**2
        perimeter = 6 * sideLength

    # Otherwise stop final display
    else:
        print("Invalid input, abandoning hexagon")
        shapeAbandoned = True

# If not one of the above shapes, stop final display
else:
    print("Invalid input, abandoning shape")
    shapeAbandoned = True

# If shape is valid, display name, area and perimeter
if not shapeAbandoned:
    perimeter = round(perimeter, 2)
    area = round(area, 2)
    print("Shape made: %s\nPerimeter: %.2f\nArea: %.2f" % (shape, perimeter, area))
