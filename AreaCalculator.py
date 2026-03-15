print("***AREA CALCULATOR***")
while True:
    print("""Press 1 to get the area of square
    Press 2 to get the area of rectangle
    Press 3 to get the area of circle
    Press 4 to get the area of triangle""")

    Choice = int(input("Enter a number between 1 - 4:"))

    if Choice == 1:
        while True:
            side = float(input("enter the length of one side:"))
            area = side ** 2
            print("The area of the square is", area)
        repeat = input("do you want to try again with square?")
        if repeat == "no":
            break
    elif Choice == 2:
        while True:
            length = float(input("Enter the length of the rectangle:"))
            width = float(input("Enter the width of the rectangle:"))
            area = length * width
            print("The area of the rectangle is", area)
            repeat = input("do you want to try again with rectangle?")
            if repeat == "no":
                break
    elif Choice == 3:
        while True:
             radius = float(input("Enter the radius of the circle:"))
             area = ((22/7)*(radius**2))
             print("The area of the circle is", area)
             repeat = input("do you want to try again with circle?")
             if repeat == "no":
                 break
    elif Choice == 4:
        while True:
            base = float(input("Enter the base of the triangle:"))
            height = float(input("Enter the height of the triangle:"))
            area = 0.5 * base * height
            print("The area of the triangle is", area)
            repeat = input("do you want to try again with triangle?")
            if repeat == "no":
                break

