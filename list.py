import math
def ValueErrorEx():
    print("Invalid input. Please enter a number.")

def ZeroInputEx():
    print("Invalid input. Please enter a number different from zero.")

print("This program was developed by Davi Andrade Macedo.")
print("I could do multiple files for this, but I'd rather do it all here.")

print("\n\nExercise 1: °C to °F converter.")
while True:
    CInput=input("\n\n\n\nEnter the temperature in °C: ")
    try:
        CTemp = float(CInput);
        FTemp = 9*CTemp/5+32
        print("The temperature in °F is: ", FTemp, sep="")
        break
    except:
        ValueErrorEx()
   

print("\n\nExercise 2: °F to °C converter.")
while True: 
    FInput = input("\n\nEnter the temperature in °F: ")
    try:
        FTemp = float(FInput)
        CTemp = (FTemp-32)*5/9
        print("The temperature in °C is: ", CTemp, sep="")
        break   
    except:
        ValueErrorEx()


print("\n\nExercise 3:  °C to °K converter.")
while True:
    CInput = input("\n\nEnter the temperature in °C: ")
    try:
        CTemp = float(CInput)
        KTemp = CTemp + 273.15
        print("The temperature in °K is: ", KTemp, sep="")
        break
    except:
        ValueErrorEx()



print("\n\nExercise 4: °K to °C converter.")
while True:
    KInput = input("\n\nEnter the temperature in °K: ")
    try:
        KTemp = float(KInput)
        CTemp = KTemp - 273.15
        print("The temperature in °C is: ", CTemp, sep="")
        break
    except:
        ValueErrorEx()



print("\n\nExercise 5: °C to °R converter.")
while True:
    CInput = input("\n\nEnter the temperature in °C: ")
    try:
        CTemp = float(CInput)
        RTemp = CTemp*9/5 + 491.67
        print("The temperature in °R is: ", RTemp, sep="")
        break
    except:
        ValueErrorEx()


print("\n\nExercise 6: °R to °C converter.")
while True:
    RInput = input("\n\nEnter the temperature in °R: ")
    try:
        RTemp = float(RInput)
        CTemp = (RTemp - 491.67)/1.8
        print("The temperature in °C is: ", CTemp, sep="")
        break
    except:
        ValueErrorEx()


print("\n\nExercise 7: F to K converter.")
while True:
    FInput = input("\n\nEnter the temperature in °F: ")
    try:
        FTemp = float(FInput)
        CTemp = (FTemp-32)*5/9
        KTemp = CTemp + 273.15
        print("The temperature in °K is: ", KTemp, sep="")
        break
    except:
        ValueErrorEx()


print("\n\nExercise 8: °K to °F converter.")
while True:
    KInput = input("\n\nEnter the temperature in °K: ")
    try:
        KTemp = float(KInput)
        CTemp = KTemp - 273.15
        FTemp = 9*CTemp/5+32
        print("The temperature in °F is: ", FTemp, sep="")  
        break
    except:
        ValueErrorEx()

print("\n\nExercise 9: °F to °R converter.")
while True:
    FInput = input("\n\nEnter the temperature in °F: ")
    try:
        FTemp = float(FInput)
        CTemp = (FTemp-32)*5/9
        RTemp = CTemp*9/5 + 491.67
        print("The temperature in °R is: ", RTemp, sep="")
        break
    except:
        ValueErrorEx()

print("\n\nExercise 10: °R to °F converter.")
while True:
    RInput = input("\n\nEnter the temperature in °R: ")
    try:
        RTemp = float(RInput)
        CTemp = (RTemp - 491.67)/1.8
        FTemp = RTemp - 459.67  
        print("The temperature in °F is: ", FTemp, sep="")
        break
    except:
        ValueErrorEx()


print("\n\nExercise 11: °K to °R converter.")
while True:
    KInput = input("\n\nEnter the temperature in °K: ")
    try:
        KTemp = float(KInput)
        CTemp = KTemp - 273.15
        RTemp = CTemp*9/5 + 491.67
        print("The temperature in °R is: ", RTemp, sep="")
        break
    except:
        ValueErrorEx()

print("\n\nExercise 12: °R to °K converter.")
while True:
    RInput = input("\n\nEnter the temperature in °R: ")
    try:
        RTemp = float(RInput)
        CTemp = (RTemp - 491.67)/1.8
        KTemp = CTemp + 273.15
        print("The temperature in °K is: ", KTemp, sep="")
        break
    except:
        ValueErrorEx()

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
        ValueErrorEx()


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
        ValueErrorEx()
    except ZeroDivisionError:
        ZeroInputEx()


print("\n\nExercise 23: Area of a trapezoid.")
while True:
    try:
        base1I = input("\n\nEnter the length of the first base of the trapezoid: ")
        base1 = float(base1I)
        if (base1 <= 0):
            print("Base can't be lower or equal to zero.")
            continue
        base2I = input("\n\nEnter the length of the second base of the trapezoid: ")
        base2 = float(base2I)
        if (base2 <= 0):
            print("Base can't be lower or equal to zero.")
            continue
        heightI = input("\n\nEnter the height of the trapezoid: ")
        height = float(heightI)
        if (height <= 0):
            print("Height can't be lower or equal to zero.")
            continue     
        area = (base1+base2)*height/2
        print("The area of the trapezoid is: ", area, "cm².", sep="")
        break
    except:
        ValueErrorEx()


print("\n\n Exercise 24: Area of a regular polygon.")
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
        ValueErrorEx()

print("\n\n Exercise 25: Area of a circle.")
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
        ValueErrorEx()


print("\n\n Exercise 26: BMI calculating")
while True:
    try:
        weightI = input("\n\nEnter your weight in kg: ")
        weight = float(weightI)
        if(weight <= 0):
            print("Weight can't be lower or equal to zero.")
            continue
        heightI = input("\n\nEnter your height in meters: ")
        height = float(heightI)
        if(height <= 0):
            print("Height can't be lower or equal to zero.")
            continue
        bmi = weight/(height*height)
        print("Your BMI is: ", bmi, sep="")
        break
    except ZeroDivisionError:
        ValueErrorEx()
    except ValueError:
        ValueErrorEx()



print("\n\n Exercise 27: First-degree equation square root")
while True:
    try:
        print("The first-degree equation is in the form of ax+b=0.")
        aI = input("\n\nEnter the value of a: ")
        bI = input("\n\nEnter the value of b: ")
        a = float(aI)
        b = float(bI)
        x = -b/a
        print("The value of x is: ", x, sep="")
        break
    except ZeroDivisionError:
        ZeroInputEx()
    except ValueError:
        ValueErrorEx()