choice = int(input("Which shape do you want to calculate?: \n1 = Triangle \n2 = Rectangle \n3 = Circle\n"))

if choice == 1:
    choice2 = int(input("Which formula u want to use to calculate?: \n1 = Area \n2 = Circumference \n"))

    if choice2 == 1:
        base = int(input("Input the base: "))
        height = int(input("Input the height: "))
        area1 = (1 / 2) * base * height
        print("This is the Area of Triangle:", area1)
    elif choice2 == 2:
        side1 = int(input("Input the first side of the triangle: "))
        side2 = int(input("Input the second side of the triangle: "))
        side3 = int(input("Input the third side of the triangle: "))
        circumference1 = side1 + side2 + side3
        print("This is the Circumference of the Triangle:", circumference1)

elif choice == 2:
    choice2 = int(input("Which formula u want to use to calculate?: \n1 = Area \n2 = Circumference \n"))

    if choice2 == 1:
        length1 = int(input("Input the length of the Rectangle: "))
        width1 = int(input("Input the width of the Rectangle: "))
        area2 = length1 * width1
        print("This is the Area of Rectangle:", area2)
    elif choice2 == 2:
        length2 = int(input("Input the length of the Rectangle: "))
        width2 = int(input("Input the width of the Rectangle: "))
        circumference2 = (2 * length2) + (2 * width2)
        print("This is the Circumference of the Rectangle:", circumference2)

elif choice == 3:
    choice2 = int(input("Which formula u want to use to calculate?: \n1 = Area \n2 = Circumference \n"))

    if choice2 == 1:
        radius1 = float(input("Input the radius: "))
        area = 3.14 * radius1 ** 2
        print("This is the Area of the Circle:", area)
    elif choice2 == 2:
        radius2 = float(input("Input the radius: "))
        circumference3 = 2 * 3.14 * radius2
        print("This is the Circumference of the Circle:", circumference3)

else:
    print("Enter a valid number!")