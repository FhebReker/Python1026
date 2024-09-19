""""
File Created: September 19, 2024
""""





import math

area = 0
perimeter = 0
shapeAbandoned = False
shape = input("What shape do you want to work with? ").lower()
if shape == "rectangle":
    width = int(input("What is the width of your rectangle? "))
    height = int(input("What is the height of your rectangle? "))
    if width > 0 and height > 0:
        area = width * height
        perimeter = 2* width + 2 * height
    else:
        print("Invalid input, abandoning rectangle")
elif shape == "triangle":
    base = int(input("What is the length of the base of your triangle? "))
    height = int(input("What is the height of your triangle? "))
    side1 = int(input("What's the length of one of the other sides of your triangle? "))
    side2 = int(input("What's the length of one of the other sides of your triangle? "))
    if side1 > 0 and side2 > 0 and base > 0 and height > 0:
        area = base * height / 2
        perimeter = base + side1 + side2
    else:
        print("Invalid input, abandoning triangle")
elif shape == "circle":
    radius = int(input("What's the radius of your circle? "))
    if radius > 0:
        area = math.pi * radius**2
        perimeter = 2 * math.pi * radius
    else:
        print("Invalid input, abandoning circle")
elif shape == "trapezoid":
    base = int(input("What is the length of the base of your trapezoid? "))
    height = int(input("What is the height of your trapezoid? "))
    leftSide = int(input("What's the length of the left side of your trapezoid? "))
    rightSide = int(input("What's the length of the right side of your trapezoid? "))
    topSide = int(input("What's the length of the top of your trapezoid? "))
    if leftSide > 0 and rightSide > 0 and base > 0 and height > 0 and topSide > 0:
        area = (topSide + base) * height / 2
        perimeter = topSide + rightSide + leftSide + base
    else:
        print("Invalid input, abandoning triangle")
elif shape == "hexagon":
    sideLength = int(input("What's the side length of your hexagon? "))
    if sideLength > 0:
        area = 3 * math.sqrt(3) / 2 * sideLength**2
        perimeter = 6 * sideLength
    else:
        print("Invalid input, abandoning hexagon")
else:
    print("Invalid input, abandoning shape")
    shapeAbandoned = True

if not shapeAbandoned:
    print("Shape made: %s\nPerimeter: %.2f\nArea: %.2f" % (shape, perimeter, area))
