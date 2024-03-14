import math, temp, geometry, time, datetime
from num2words import num2words
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
        case 1: temp.ex1()
        case 2: temp.ex2()
        case 3: temp.ex3()
        case 4: temp.ex4()
        case 5: temp.ex5()
        case 6: temp.ex6()
        case 7: temp.ex7()
        case 8: temp.ex8()
        case 9: temp.ex9()
        case 10: temp.ex10()
        case 11: temp.ex11()
        case 12: temp.ex12()
        case 13: geometry.ex13()
        case 14: geometry.ex14()
        case 15: geometry.ex15()
        case 16: geometry.ex16()
        case 17: geometry.ex17()
        case 18: geometry.ex18()
        case 19: geometry.ex19()
        case 20: geometry.ex20()
        case 21: geometry.ex21()
        case 22: geometry.ex22()
        case 23: geometry.ex23()
        case 24: geometry.ex24()
        case 25: geometry.ex25()
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
    temp.ex1()
    temp.ex2()
    temp.ex3()
    temp.ex4()
    temp.ex5()
    temp.ex6()
    temp.ex7()
    temp.ex8()
    temp.ex9()
    temp.ex10()
    temp.ex11()
    temp.ex12()       
    
def ex29():
    print("\n\nExercise 29: 13-18 Compilation")
    print("This exercise is a compilation of exercises 13 to 18.")
    geometry.ex13()
    geometry.ex14()
    geometry.ex15()
    geometry.ex16()
    geometry.ex17()
    geometry.ex18()
    
def ex30():
    print("\n\nExercise 30: 19-25 Compilation")        
    print("This exercise is a compilation of exercises 19 to 25.")
    geometry.ex19()
    geometry.ex20()
    geometry.ex21()
    geometry.ex22()
    geometry.ex23()
    geometry.ex24()
    geometry.ex25()
    
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
        try:
            day = input("\n\nEnter the day: ")
            day = int(day)
            if (day < 1 or day > 31):
                print("Invalid input. Please enter a valid day.")
                continue
            month = input("\n\nEnter the month: ")
            month = int(month)
            if (month < 1 or month > 12):
                print("Invalid input. Please enter a valid month.")
                continue
            year = input("\n\nEnter the year: ")
            year = int(year)
            if (year == 0 or year > 9999 or year < -45):
                print("Invalid input. Please enter a valid year.")
                continue
            match month:
                case 2:
                    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                        if (day > 29):
                            print("Invalid input. Please enter a valid day.")
                            continue
                    else:
                        if (day > 28):
                            print("Invalid input. Please enter a valid day.")
                            continue
                case 4, 6, 9, 11:
                    if (day > 30):
                        print("Invalid input. Please enter a valid day.")
                        continue
                case 10:
                    if (day >= 5 and day <= 14 and year == 1582):
                        print("Invalid input. This day does not exist.")
                        continue
            print("The date is: ", day, "/", month, "/", year, ".", sep="")
            break
        except ValueError:
            ValueErrorEx()

def ex41():
    print("\n\nExercise 41: Natural number up to 9 written in words")
    while True:
        try:
            num = input("\n\nEnter a number between 0 and 9: ")
            num = int(num)
            if(num <= 0 or num > 9):
                print("Invalid input. Please enter a number between 0 and 9.")
                continue
            print("Your number is ", num2words(num), "!")
            break
        except ValueError:
            ValueErrorEx()

def ex42():
    print("\n\nExercise 41: Natural number from -9 to 9 written in words")
    while True:
        try:
            num = input("\n\nEnter a number between 0 and 9: ")
            num = int(num)
            if(num < -9 or num > 9):
                print("Invalid input. Please enter a number between 0 and 9.")
                continue
            print("Your number is ", num2words(num), "!")
            break
        except ValueError:
            ValueErrorEx()

def ex43():
    print("\n\nExercise 43: Natural number from -999 to 999 written in words")
    while True:
        try:
            num = input("\n\nEnter a number between -999 and 999: ")
            num = int(num)
            if(num < -99 or num > 99):
                print("Invalid input. Please enter a number between -999 and 999.")
                continue
            print("Your number is ", num2words(num), "!")
            break
        except ValueError:
            ValueErrorEx()

def ex44():
    print("\n\nExercise 44: Natural number from -999 to 999 written in words")
    while True:
        try:
            num = input("\n\nEnter a number between -999 and 999: ")
            num = int(num)
            if(num < -999 or num > 999):
                print("Invalid input. Please enter a number between -999 and 999.")
                continue
            print("Your number is ", num2words(num), "!")
            break
        except ValueError:
            ValueErrorEx()

def ex45():
    print("\n\nExercise 45: Monetary value between R$-9.99 and R$9.99 written in words")
    while True:
        try:
            num = input("\n\nEnter a value between R$-9.99 and R$9.99: ")
            num = float(num)
            if(num < -9.99 or num > 9.99):
                print("Invalid input. Please enter a number between R$-9.99 and R$9.99.")
                continue
            print("Your number is ", num2words(num, to = 'currency', lang='pt_BR'))
            break
        except ValueError:
            ValueErrorEx()

def ex46():
    print("\n\nExercise 46: Monetary value between R$-99.99 and R$99.99 written in words")
    while True:
        try:
            num = input("\n\nEnter a value between R$-99.99 and R$99.99: ")
            num = float(num)
            if(num < -99.99 or num > 99.99):
                print("Invalid input. Please enter a number between R$-99.99 and R$99.99.")
                continue
            print("Your number is ", num2words(num, to = 'currency', lang='pt_BR'))
            break
        except ValueError:
            ValueErrorEx()

def ex47():
    print("\n\nExercise 47: Monetary value between R$-999.99 and R$999.99 written in words")
    while True:
        try:
            num = input("\n\nEnter a value between R$-999.99 and R$999.99: ")
            num = float(num)
            if(num < -999.99 or num > 999.99):
                print("Invalid input. Please enter a number between R$-999.99 and R$999.99.")
                continue
            print("Your number is", num2words(num, to = 'currency', lang = 'pt_BR'))
            break
        except ValueError:
            ValueErrorEx()

def ex48():
    print("\n\nExercise 48: Exit")
    end()
    
if __name__ == "__main__":
    main()