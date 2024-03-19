import main

def ex31():
    print("\n\nExercise 31: 2 numbers organized in ascending order")
    while True:                 
        try:
            num1 = input("\n\nEnter the first number: ")
            num1 = float(num1)
            num2 = input("\n\nEnter the second number: ")
            num2 = float(num2)
            if(num1 > num2):
                print("The numbers in ascending order are: ", num2,num1, ".", sep="")
            else: 
                print("The numbers in ascending order are: ", num1,num2, ".", sep="")
        except ValueError:
            ValueErrorEx()

def ex32():
    print("\n\nExercise 32: 3 numbers organized in ascending order")
    while True:
        try:
            num1 = input("\n\nEnter the first number: ")
            num1 = int(num1)
            num2 = input("\n\nEnter the second number: ")
            num2 = int(num2)
            num3 = input("\n\nEnter the third number: ")
            num3 = int(num3)
            if(num1 > num2):
                if(num2 > num3):
                    print("The numbers in ascending order are: ", num3,num2,num1, ".", sep=" ")
                elif(num1 > num3):
                    print("The numbers in ascending order are: ", num2,num3,num1, ".", sep=" ")
                else:
                    print("The numbers in ascending order are: ", num2, num1, num3, ".", sep=" ")
            else:
                if(num1 > num3):
                    print("The numbers in ascending order are: ", num3,num1,num2, ".", sep=" ")
                elif(num2 > num3):
                    print("The numbers in ascending order are: ", num1,num3,num2, ".", sep=" ")
                else:
                    print("The numbers in ascending order are: ", num1,num2,num3, ".", sep=" ")
            break
        except ValueError:
            ValueErrorEx()

def ex33():
    print("\n\nExercise 33: 4 numbers organized in ascending order")
    while True:
        try:
            num1 = input("\n\nEnter the first number: ")
            num1 = int(num1)
            num2 = input("\n\nEnter the second number: ")
            num2 = int(num2)
            num3 = input("\n\nEnter the third number: ")
            num3 = int(num3)
            num4 = input("\n\nEnter the fourth number: ")
            num4 = int(num4)
            if(num1 > num2):
                if(num2 > num3):
                    if(num3 > num4):
                        print("The numbers in ascending order are: ", num4,num3,num2,num1, ".", sep=" ")
                    elif(num2 > num4):
                        print("The numbers in ascending order are: ", num3,num4,num2,num1, ".", sep=" ")
                    else:
                        print("The numbers in ascending order are: ", num3,num2,num4,num1, ".", sep=" ")
                elif(num1 > num3):
                    print("The numbers in ascending order are: ", num2,num3,num1,num4, ".", sep=" ")
                else:
                    print("The numbers in ascending order are: ", num2,num1,num3,num4, ".", sep=" ")
        except ValueError:
            ValueErrorEx()

def ex35():
    print("\n\nExercise 35: Check valid triangle sides")
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
            side3 = input("\n\nEnter the length of the third side: ")
            side3 = float(side3)
            if(side3 <= 0):
                print("Side can't be lower or equal to zero.")
                continue
            longest = max(side1, side2, side3)
            if (side1 + side2 + side3 - longest <= longest):
                print("The sum of the two smaller sides must be greater than the longest side.")
            else:
                print("The sides form a valid triangle.")
            break
        except ValueError:
            ValueErrorEx()

def ex36():
    print("\n\nExercise 36: Check valid triangle sides and type")
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
            side3 = input("\n\nEnter the length of the third side: ")
            side3 = float(side3)
            if(side3 <= 0):
                print("Side can't be lower or equal to zero.")
                continue
            longest = max(side1, side2, side3)
            if (side1 + side2 + side3 - longest < longest):
                print("The sum of the two smaller sides must be greater or equal than the longest side.")
                continue
            elif(side1 == side2 and side2 == side3 and side1 == side3):
                print("The sides form an equilateral triangle.")
            elif(side1 == side2 or side2 == side3 or side1 == side3):
                print("The sides form an isosceles triangle.")
            else:
                print("The sides form a scalene triangle.")
                break
        except ValueError:
            ValueErrorEx()

def ex37():
    print("\n\nExercise 37: Check valid triangle by angles")
    while True:
        try:
            angle1 = input("\n\nEnter the value of the first angle: ")
            angle1 = float(angle1)
            if(angle1 <= 0 or angle1 >= 180):
                print("Invalid angle. Please enter a valid angle.")
                continue
            angle2 = input("\n\nEnter the value of the second angle: ")
            angle2 = float(angle2)
            if(angle2 <= 0 or angle2 >= 180):
                print("Invalid angle. Please enter a valid angle.")
                continue
            angle3 = input("\n\nEnter the value of the third angle: ")
            angle3 = float(angle3)
            if(angle3 <= 0 or angle3 >= 180):
                print("Invalid angle. Please enter a valid angle.")
                continue
            if(angle1 + angle2 + angle3 != 180):
                print("The sum of the angles must be equal to 180.")
                continue
            print("The angles form a valid triangle.")
            break
        except ValueError:
            ValueErrorEx()

def ex38():
    print("\n\nExercise 38: Check valid triangle by angles and type")
    while True:
        try:
            angle1 = input("\n\nEnter the value of the first angle: ")
            angle1 = float(angle1)
            if(angle1 <= 0 or angle1 >= 180):
                print("Invalid angle. Please enter a valid angle.")
                continue
            angle2 = input("\n\nEnter the value of the second angle: ")
            angle2 = float(angle2)
            if(angle2 <= 0 or angle2 >= 180):
                print("Invalid angle. Please enter a valid angle.")
                continue
            angle3 = input("\n\nEnter the value of the third angle: ")
            angle3 = float(angle3)
            if(angle3 <= 0 or angle3 >= 180):
                print("Invalid angle. Please enter a valid angle.")
                continue
            if(angle1 + angle2 + angle3 != 180):
                print("The sum of the angles must be equal to 180.")
                continue
            if(angle1 == 90 or angle2 == 90 or angle3 == 90):
                print("The angles form a right-angled triangle.")
            elif(angle1 > 90 or angle2 > 90 or angle3 > 90):
                print("The angles form an obtuse triangle.")
            elif(angle1 < 90 and angle2 < 90 and angle3 < 90):
                print("The angles form an acute triangle.")
            break
        except ValueError:
            ValueErrorEx()
            