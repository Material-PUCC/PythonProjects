import math
def ValueErrorEx():
    print("Invalid input. Please enter a  valid number.")

def ZeroInputEx():
    print("Invalid input. Please enter a number different from zero.")

def main():
    print("This list was developed by Davi Andrade Macedo.")
    print("Category 1: Temperature conversion.")
    print("===================================")
    print("[1] °C to °F converter.")
    print("[2] °F to °C converter.")
    print("[3] °C to °K converter.")
    print("[4] °K to °C converter.")
    print("[5] °C to °R converter.")
    print("[6] °R to °C converter.")
    print("[7] °F to °K converter.")
    print("[8] °K to °F converter.")
    print("[9] °F to °R converter.")
    print("[10] °R to °F converter.")
    print("[11] °K to °R converter.")
    print("[12] °R to °K converter.")
    print("Category 2: Perimeter and area of geometric figures.")
    print("===================================")
    print("[13] Perimeter of a triangle.")
    print("[14] Perimeter of a square.")
    print("[15] Perimeter of a rectangle.")
    print("[16] Perimeter of a trapezoid.")
    print("[17] Area of a regular polygon.")
    print("[18] Perimeter of a circle.")
    print("[19] Area of a triangle.")
    print("[20] Area of a square.")
    print("[21] Area of a rectangle.")
    print("[22] Area of a diamond.")
    print("[23] Area of a trapezoid.")
    print("[24] Area of a regular polygon.")
    print("[25] Area of a circle.")
    print("Category 3: Other calculations.")
    print("===================================")
    print("[26] BMI calculating.")
    print("[27] First-degree equation square root.")
    print("[28] 1-12 Compilation.")
    print("[29] 13-18 Compilation.")
    print("[30] 19-25 Compilation.")
    print("[31] 2 numbers organized in ascending order.")
    print("[32] 3 numbers organized in ascending order.")
    print("[33] 4 numbers organized in ascending order.")
    print("[34] Valid time check.")
    print("[35] Check valid triangle sides.")
    print("[36] Check valid triangle sides and type.")
    print("[37] Check valid triangle by angles.")
    print("[38] Check valid triangle by angles and type.")
    print("[39] Second-degree equation square root.")
    print("[40] Valid date and year check.")
    print("[41] Natural number up to 9 written in words.")
    print("[42] Natural number between -9 and 9 written in words.")
    print("[43] Natural number between -99 and 99 written in words.")
    print("[44] Natural number between -999 and 999 written in words.")
    print("[45] Monetary value between -9,99 R$ and 9,99 R$ written in words.")
    print("[46] Monetary value between -99,99 R$ and 99,99 R$ written in words.")
    print("[47] Monetary value between -999,99 R$ and 999,99 R$ written in words.")
    print("[48] Exit.")
    
    
    desired = int(input("Enter the number of the exercise you want to execute (1-48):  "))
    #with great help from meid menid amei da but she's not in the same class :(
    match desired:
        case 1: ex1()
        case 2: ex2()
        case 3: ex3()
        case 4: ex4()
        case 5: ex5()
        case 6: ex6()
        case 7: ex7()
        case 8: ex8()
        case 9: ex9()
        case 10: ex10()
        case 11: ex11()
        case 12: ex12()
        case 13: ex13()
        case 14: ex14()
        case 15: ex15()
        case 16: ex16()
        case 17: ex17()
        case 18: ex18()
        case 19: ex19()
        case 20: ex20()
        case 21: ex21()
        case 22: ex22()
        case 23: ex23()
        case 24: ex24()
        case 25: ex25()
        case 26: ex26()
        case 27: ex27()
        case 28: ex28()
        case 29: ex29()
        case 30: ex30()
        case 31: ex31()
        case 32: ex32()
        case 33: ex33()
        case 34: ex34()
        case 35: ex35()
        case 36: ex36()
        case 37: ex37()
        case 38: ex38()
        case 39: ex39()
        case 40: ex40()
        case 41: ex41()
        case 42: ex42()
        case 43: ex43()
        case 44: ex44()
        case 45: ex45()
        case 46: ex46()
        case 47: ex47()
        case 48: end()
        case _: print("Invalid number. Please enter a number between 1 and 27.")

def end():
    print("Thank you for using this program. Goodbye!")
    exit()
def ex1():
    print("\n\nExercise 1: °C to °F converter.")
    while True:
        CInput=input("\n\nEnter the temperature in °C: ")
        try:
            CTemp = float(CInput);
            if (CTemp < -273.15):
                print("\n\nTemperatures below absolute zero are not valid. Please input a correct value.")
                continue
            FTemp = 9*CTemp/5+32
            print("The temperature in °F is: ", FTemp, sep="")
            break
        except:
            ValueErrorEx()

def ex2():
    print("\n\nExercise 2: °F to °C converter.")
    while True: 
        FInput = input("\n\nEnter the temperature in °F: ")
        try:
            FTemp = float(FInput)
            if (FTemp < -459.67):
                print("\n\nTemperatures below absolute zero are not valid. Please input a correct value.")
                continue
            CTemp = (FTemp-32)*5/9
            print("The temperature in °C is: ", CTemp, sep="")
            break   
        except:
            ValueErrorEx()

def ex3():
    print("\n\nExercise 3:  °C to °K converter.")
    while True:
        CInput = input("\n\nEnter the temperature in °C: ")
        try:
            CTemp = float(CInput)
            if (CTemp < -273.15):
                print("\n\nTemperatures below absolute zero are not valid. Please input a correct value.")
                continue
            KTemp = CTemp + 273.15
            print("The temperature in °K is: ", KTemp, sep="")
            break
        except:
            ValueErrorEx()

def ex4():
    print("\n\nExercise 4: °K to °C converter.")
    while True:
        KInput = input("\n\nEnter the temperature in °K: ")
        try:
            KTemp = float(KInput)
            if (KTemp < 0):
                print("\n\nTemperatures below absolute zero are not valid. Please input a correct value.")
                continue
            CTemp = KTemp - 273.15
            print("The temperature in °C is: ", CTemp, sep="")
            break
        except:
            ValueErrorEx()

def ex5(): 
    print("\n\nExercise 5: °C to °R converter.")
    while True:
        CInput = input("\n\nEnter the temperature in °C: ")
        try:
            CTemp = float(CInput)
            if (CTemp < -273.15):
                print("\n\nTemperatures below absolute zero are not valid. Please input a correct value.")
                continue
            RTemp = CTemp*9/5 + 491.67
            print("The temperature in °R is: ", RTemp, sep="")
            break
        except:
            ValueErrorEx()

def ex6():
    print("\n\nExercise 6: °R to °C converter.")
    while True:
        RInput = input("\n\nEnter the temperature in °R: ")
        try:
            RTemp = float(RInput)
            if (RTemp < 0):
                print("\n\nTemperatures below absolute zero are not valid. Please input a correct value.")
                continue
            CTemp = (RTemp - 491.67)/1.8
            print("The temperature in °C is: ", CTemp, sep="")
            break
        except:
            ValueErrorEx()

def ex7():
    print("\n\nExercise 7: F to K converter.")
    while True:
        FInput = input("\n\nEnter the temperature in °F: ")
        try:
            FTemp = float(FInput)
            if (FTemp < -459.67):
                print("\n\nTemperatures below absolute zero are not valid. Please input a correct value.")
                continue
            CTemp = (FTemp-32)*5/9
            KTemp = CTemp + 273.15
            print("The temperature in °K is: ", KTemp, sep="")
            break
        except:
            ValueErrorEx()
    
def ex8():
    print("\n\nExercise 8: °K to °F converter.")
    while True:
        KInput = input("\n\nEnter the temperature in °K: ")
        try:
            KTemp = float(KInput)
            if (KTemp < 0):
                print("\n\nTemperatures below absolute zero are not valid. Please input a correct value.")
                continue
            CTemp = KTemp - 273.15
            FTemp = 9*CTemp/5+32
            print("The temperature in °F is: ", FTemp, sep="")  
            break
        except:
            ValueErrorEx()

def ex9():
    print("\n\nExercise 9: °F to °R converter.")
    while True:
        FInput = input("\n\nEnter the temperature in °F: ")
        try:
            FTemp = float(FInput)
            if (FTemp < -459.67):
                print("\n\nTemperatures below absolute zero are not valid. Please input a correct value.")
                continue
            CTemp = (FTemp-32)*5/9
            RTemp = CTemp*9/5 + 491.67
            print("The temperature in °R is: ", RTemp, sep="")
            break
        except:
            ValueErrorEx()

def ex10():
    print("\n\nExercise 10: °R to °F converter.")
    while True:
        RInput = input("\n\nEnter the temperature in °R: ")
        try:
            RTemp = float(RInput)
            if (RTemp < 0):
                print("\n\nTemperatures below absolute zero are not valid. Please input a correct value.")
                continue
            CTemp = (RTemp - 491.67)/1.8
            FTemp = RTemp - 459.67  
            print("The temperature in °F is: ", FTemp, sep="")
            break
        except:
            ValueErrorEx()

def ex11():
    print("\n\nExercise 11: °K to °R converter.")
    while True:
        KInput = input("\n\nEnter the temperature in °K: ")
        try:
            KTemp = float(KInput)
            if (KTemp < 0):
                print("\n\nTemperatures below absolute zero are not valid. Please input a correct value.")
                continue
            CTemp = KTemp - 273.15
            RTemp = CTemp*9/5 + 491.67
            print("The temperature in °R is: ", RTemp, sep="")
            break
        except:
            ValueErrorEx()

def ex12():
    print("\n\nExercise 12: °R to °K converter.")
    while True:
        RInput = input("\n\nEnter the temperature in °R: ")
        try:
            RTemp = float(RInput)
            if (RTemp < 0):
                print("\n\nTemperatures below absolute zero are not valid. Please input a correct value.")
                continue
            CTemp = (RTemp - 491.67)/1.8
            KTemp = CTemp + 273.15
            print("The temperature in °K is: ", KTemp, sep="")
            break
        except:
            ValueErrorEx()

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
            ValueErrorEx()

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
            ValueErrorEx()
        except ZeroDivisionError:
            ZeroInputEx()

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
            ValueErrorEx()
        except ZeroDivisionError:
            ZeroInputEx()

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
            ValueErrorEx()
         

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
            ValueErrorEx()


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
            ValueErrorEx()
   

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
            ValueErrorEx()
            

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
            ValueErrorEx()

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
            ValueErrorEx()

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
            ValueErrorEx()

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
            ValueErrorEx()


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
            ValueErrorEx()

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
            ValueErrorEx()

def ex26():
    print("\n\nExercise 26: BMI calculating")
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


def ex27():
    print("\n\nExercise 27: First-degree equation square root")
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
            
def ex28():
    print("\n\nExercise 28: 1-12 Compilation")
    print("This exercise is a compilation of exercises 1 to 12.")
    ex1()
    ex2()
    ex3()
    ex4()
    ex5()
    ex6()
    ex7()
    ex8()
    ex9()
    ex10()
    ex11()
    ex12()       
    
def ex29():
    print("\n\nExercise 29: 13-18 Compilation")
    print("This exercise is a compilation of exercises 13 to 18.")
    ex13()
    ex14()
    ex15()
    ex16()
    ex17()
    ex18()
    
def ex30():
    print("\n\nExercise 30: 19-25 Compilation")        
    print("This exercise is a compilation of exercises 19 to 25.")
    ex19()
    ex20()
    ex21()
    ex22()
    ex23()
    ex24()
    ex25()
    
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

def ex34(): 
    print("\n\nExercise 34: Valid time check")
    while True:
        try:
            hour = input("\n\nEnter the hour: ")
            hour = int(hour)
            if(hour < 0 or hour > 23):
                print("Invalid hour. Please enter a valid hour.")
                continue
            minute = input("\n\nEnter the minute: ")
            minute = int(minute)
            if(minute < 0 or minute > 59):
                print("Invalid minute. Please enter a valid minute.")
                continue
            second = input("\n\nEnter the second: ")
            second = int(second)
            if(second < 0 or second > 59):
                print("Invalid second. Please enter a valid second.")
                continue
            print("The time is: ", hour, ":", minute, ":", second, ".", sep="")
            break
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
            
def ex39():
    print("\n\nExercise 39: Second-degree equation square root")
    while True:
        try:
            print("The second-degree equation is in the form of ax²+bx+c=0.")
            aI = input("\n\nEnter the value of a: ")
            a = float(aI)
            bI = input("\n\nEnter the value of b: ")
            b = float(bI)
            cI = input("\n\nEnter the value of c: ")
            c = float(cI)
            delta = b**2 - 4*a*c
            if(delta < 0):
                print("The equation has no roots.")
            elif(delta == 0):
                x = -b/(2*a)
                print("The equation has one root: ", x, sep="")
            else:
                x1 = (-b + math.sqrt(delta))/(2*a)
                x2 = (-b - math.sqrt(delta))/(2*a)
                print("The equation has two roots: ", x1, " and ", x2, ".", sep="")
            break
        except: 
            ValueErrorEx()

def ex40():
    print("\n\nExercise 40: Valid date and year check")
    while True:
        #try:
            year = int(input("\n\nEnter a year: "))
            if (year == 0 or year < -45):
                print("\n\nInvalid input. Enter a valid year.")
                continue
            else:
                if (year < 1583):
                    if (year%4 == 0):
                        leapY = True
                    else:
                        leapY = False
                else:
                    if(year%400 == 0):
                        leapY = True
                    else: 
                        leapY = False              
            month = int(input("\n\nEnter a month: "))
            if (month < 1 or month > 12):
                print("\n\nInvalid input. Enter a valid month.")
                continue
            match month:
                    case "1", "3", "5", "7", "8", "10", "12":
                        print("oi")
                        day = int(input("\n\nEnter a day: "))
                        
                        if (day < 1 or day > 31):
                            print("Invalid input. Enter a valid day.")
                            continue
                        elif(day >= 5 and day <= 14 and month == 10 and year == 1582):
                            print("This day does not exist.")
                            continue
                        else:
                            print("The date is: ", day, "/", month, "/", year, ".", sep="")
                            continue
                    case "4", "6", "9", "11":
                        print("oi")
                        day = int(input("\n\nEnter a day: "))
                        if (day < 1 or day > 30):
                            print("\n\nInvalid input. Enter a valid day.")
                            continue
                    case "2":
                        if (leapY):
                            if(day <1 or day > 29):
                                print("\n\nInvalid input. Enter a valid day.")
                        else: 
                            if (day == 29):
                                print("\n\nInvalid input. Enter a valid day.")

                
                
               
                

                        
                 
                     
                
if __name__ == "__main__":
    main()