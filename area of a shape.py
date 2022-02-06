#write an aria() function to print the selective type of area(circle,triangle,square,rectangle,trapezium)

def calculate_area():
    print("circle // triangle // rectangle // square // trapezium\n")
    print("Enter the shape you want to know the area: ")
    shape = input()

    if shape == "circle":
        print("please enter the Radius:")
        r = float(input())
        area = 3.1416*r*r
        print("The area is: ", area)

    elif shape == "triangle":
        print("please enter the base:")
        base = float(input())
        print("please enter the height: ")
        height = float(input())
        area = 0.5*base*height
        print("The area is: ", area)

    elif shape == "rectangle":
        print("please enter the length: ")
        length = float(input())
        print("please enter the breadth: ")
        breadth = float(input())
        area = length*breadth
        print("The area is: ", area)

    elif shape == "square":
        print("please enter the length: ")
        length = float(input())
        area = length**2
        print("The area is: ", area)

    elif shape == "trapezium":
        print("please enter the side 1: ")
        side1 = float(input())
        print("please enter the side 2: ")
        side2 = float(input())
        print("please enter the height: ")
        height = float(input())
        area = 0.5*(side1+side2)*height
        print("The area is: ", area)
calculate_area()

