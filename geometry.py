import math

def ex13():
    print("\n\nExercise 13: Perimeter of a triangle.")
    while True:  
        try:
            side1 = input("\n\nEnter the length of the first side: ")
            side1 = float(side1)
            if side1 < 0:
                print("\n\nNegative numbers are not valid. Please input a correct value.")
                continue
            side2 = input("\n\nEnter the length of the second side: ")
            side2 = float(side2)
            if side2 < 0:
                print("\n\nNegative numbers are not valid. Please input a correct value.")
                continue
            side3 = input("\n\nEnter the length of the third side: ")
            side3 = float(side3)
            if side3 < 0:
                print("\n\nNegative numbers are not valid. Please input a correct value.")
                continue
            longest = max(side1, side2, side3)
            if (side1 + side2 + side3 - longest <= longest):
                print("\n\nThe sum of the two smaller sides must be greater than the longest side.")
                continue
            perimeter = side1 + side2 + side3
            print("\n\nThe perimeter of the triangle is: ", perimeter, sep="")
            break
        except ValueError:
            list.ValueErrorEx()

def ex14():
    print("\n\nExercise 14: Perimeter of a square.")
    while True:
        try:
            side = input("\n\nEnter the length of the side: ")
            side = float(side)
            if(side <= 0):
                print("Side can't be lower or equal to zero.")
                continue
            perimeter = 4*side
            print("The perimeter of the square is: ", perimeter, sep="")
            break
        except ValueError:
            list.ValueErrorEx()
        except ZeroDivisionError:
            list.ZeroInputEx()

def ex15():
    print("\n\nExercise 15: Perimeter of a rectangle.")
    while True:
        try:
            side1 = input("\n\nEnter the length of the first side: ")
            side1 = float(side1)
            if(side1 <= 0):
                print("Side can't be lower or equal to zero.")
                continue
            side2 = input("\n\nEnter the length of the second side: ")
            side2 = float(side2)
            if(side2 <= 0):
                print("Side can't be lower or equal to zero.")
                continue
            perimeter = 2*(side1+side2)
            print("The perimeter of the rectangle is: ", perimeter, sep="")
            break
        except ValueError:
            list.ValueErrorEx()
        except ZeroDivisionError:
            list.ZeroInputEx()

def ex16():
    print("\n\nExercise 16: Perimeter of a trapezoid.")
    while True:
        try:
            base1 = input("\n\nEnter the length of the first base of the trapezoid: ")
            base1 = float(base1)
            if(base1 <= 0):
                print("Base can't be lower or equal to zero.")
                continue
            base2 = input("\n\nEnter the length of the second base of the trapezoid: ")
            base2 = float(base2)
            if(base2 <= 0):
                print("Base can't be lower or equal to zero.")
                continue
            side1 = input("\n\nEnter the length of the first side of the trapezoid: ")
            side1 = float(side1)
            if(side1 <= 0):
                print("Side can't be lower or equal to zero.")
                continue
            side2 = input("\n\nEnter the length of the second side of the trapezoid: ")
            side2 = float(side2)
            if(side2 <= 0):
                print("Side can't be lower or equal to zero.")
                continue
            perimeter = base1+base2+side1+side2
            print("The perimeter of the trapezoid is: ", perimeter, sep="")
            break
        except ValueError:
            list.ValueErrorEx()
         

def ex17():
    print("\n\nExercise 17: Area of a regular polygon.")
    while True:
        try:
            sides = input("\n\nEnter the number of sides of the polygon: ")
            sides = float(sides)
            if(sides < 3):
                print("The number of sides must be greater than 2.")
                continue
            base = input("\n\nEnter the length of the base of the polygon: ")
            base = float(base)
            if (base <= 0):
                print("Base can't be lower or equal to zero.")
                continue
            apothem = input("\n\nEnter the length of the apothem of the polygon: ")
            apothem = float(apothem)
            if (apothem <= 0):
                print("Apothem can't be lower or equal to zero.")
                continue
            area = (sides*base*apothem)/2
            print("The area of the polygon is: ", area, "cm².", sep="")
            break
        except ValueError:
            list.ValueErrorEx()


def ex18():
    print("\n\nExercise 18: Perimeter of a circle.")
    while True:
        try:
            radius = input("\n\nEnter the radius of the circle: ")
            radius = float(radius)
            if (radius <= 0):
                print("Radius can't be lower or equal to zero.")
                continue
            perimeter = 2*math.pi*radius
            print("The perimeter of the circle is: ", perimeter, "cm.", sep="")
            break
        except ValueError:
            list.ValueErrorEx()
   

def ex19():
    print("\n\nExercise 19: Area of a triangle.")
    while True:
        try:
            base = input("\n\nEnter the length of the base of the triangle: ")
            base = float(base)
            if(base <= 0):
                print("Base can't be lower or equal to zero.")
                continue
            height = input("\n\nEnter the height of the triangle: ")
            height = float(height)
            if(height <= 0):
                print("Height can't be lower or equal to zero.")
                continue
            area = (base*height)/2
            print("The area of the triangle is: ", area, "cm².", sep="")
            break
        except ValueError:
            list.ValueErrorEx()
            

def ex20():
    print("\n\nExercise 20: Area of a square.")
    while True:
        try:
            side = input("\n\nEnter the length of the side of the square: ")
            side = float(side)
            if(side <= 0):
                print("Side can't be lower or equal to zero.")
                continue
            area = side*side
            print("The area of the square is: ", area, "cm².", sep="")
            break
        except ValueError:
            list.ValueErrorEx()

def ex21():
    print("\n\nExercise 21: Area of a rectangle.")
    while True:
        try:
            side1 = input("\n\nEnter the length of the first side of the rectangle: ")
            side1 = float(side1)
            if(side1 <= 0):
                print("Side can't be lower or equal to zero.")
                continue
            side2 = input("\n\nEnter the length of the second side of the rectangle: ")
            side2 = float(side2)
            if(side2 <= 0):
                print("Side can't be lower or equal to zero.")
                continue
            area = side1*side2
            print("The area of the rectangle is: ", area, "cm².", sep="")
            break
        except ValueError:
            list.ValueErrorEx()

def ex22():
    print("\n\nExercise 22: Area of a diamond.")
    while True:
        try:
            diagonal1 = input("\n\nEnter the length of the first diagonal of the diamond: ")
            diagonal1 = float(diagonal1)
            if(diagonal1 <= 0):
                print("Diagonal can't be lower or equal to zero.")
                continue
            diagonal2 = input("\n\nEnter the length of the second diagonal of the diamond: ")
            diagonal2 = float(diagonal2)
            if(diagonal2 <= 0):
                print("Diagonal can't be lower or equal to zero.")
                continue
            area = (diagonal1*diagonal2)/2
            print("The area of the diamond is: ", area, "cm².", sep="")
            break
        except ValueError:
            list.ValueErrorEx()

def ex23():
    print("\n\nExercise 23: Area of a trapezoid.")
    while True:
        try:
            base1 = input("\n\nEnter the length of the first base of the trapezoid: ")
            base1 = float(base1)
            if(base1 <= 0):
                print("Base can't be lower or equal to zero.")
                continue
            base2 = input("\n\nEnter the length of the second base of the trapezoid: ")
            base2 = float(base2)
            if(base2 <= 0):
                print("Base can't be lower or equal to zero.")
                continue
            height = input("\n\nEnter the height of the trapezoid: ")
            height = float(height)
            if(height <= 0):
                print("Height can't be lower or equal to zero.")
                continue
            area = (base1+base2)*height/2
            print("The area of the trapezoid is: ", area, "cm².", sep="")
            break
        except ValueError:
            list.ValueErrorEx()


def ex24():
    print("\n\nExercise 24: Area of a regular polygon.")
    while True:
        try:
            sidesI = input("\n\nEnter the number of sides of the polygon: ")
            sides = float(sidesI)
            if(sides < 3):
                print("The number of sides must be greater than 2.")
                continue
            baseI = input("\n\nEnter the length of the base of the polygon: ")
            base = float(baseI)
            if (base <= 0):
                print("Base can't be lower or equal to zero.")
                continue
            apothemI = input("\n\nEnter the length of the apothem of the polygon: ")
            apothem = float(apothemI)
            if (apothem <= 0):
                print("Apothem can't be lower or equal to zero.")
                continue
            area = (sides*base*apothem)/2
            print("The area of the polygon is: ", area, "cm².", sep="")
            break
        except:
            list.ValueErrorEx()

def ex25():
    print("\n\nExercise 25: Area of a circle.")
    while True:
        try:
            radiusI = input("\n\nEnter the radius of the circle: ")
            radius = float(radiusI)
            if (radius <= 0):
                print("Radius can't be lower or equal to zero.")
                continue
            area = math.pi*math.pow(radius,2)
            print("The area of the circle is: ", area, "cm².", sep="")
            break
        except:
            list.ValueErrorEx()