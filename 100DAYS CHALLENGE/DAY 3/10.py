side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))


if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    if side1 == side2 == side3:
        print("These side lengths form an equilateral triangle.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("These side lengths form an isosceles triangle.")
    else:
        print("These side lengths form a scalene triangle.")
else:
    print("These side lengths cannot form a triangle.")
