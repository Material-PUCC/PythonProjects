import main, math, temp, geometry, time, datetime, combos, order, date, number2words, webbrowser, lineprinting, minmax

def ex26():
    print("\n\nExercise 26: BMI calculating")
    while True:
        try:
            weight = float(input("\n\nEnter your weight in kg: "))
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
            main.ValueErrorEx()
        except ValueError:
            main.ValueErrorEx()


def ex27():
    print("\n\nExercise 27: First-degree equation square root")
    while True:
        try:
            print("The first-degree equation is in the form of ax+b=0.")
            a = float(input("\n\nEnter the value of a: "))
            b = float(input("\n\nEnter the value of b: "))
            x = -b/a
            print("The value of x is: ", x, sep="")
            break
        except ZeroDivisionError:
            main.ZeroInputEx()
        except ValueError:
            main.ValueErrorEx()



def ex39():
    print("\n\nExercise 39: Second-degree equation square root")
    while True:
        try:
            print("The second-degree equation is in the form of ax²+bx+c=0.")
            a = float(input("\n\nEnter the value of a: "))
            b = float(input("\n\nEnter the value of b: "))
            c = float(input("\n\nEnter the value of c: "))
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
            main.ValueErrorEx()

def ex50():
    while True:
        try:
            '''
            if num in [0,1]: # if numero ==0 or numero==1:
                print (num, "nao primo!"
            else:
                possivelDivisor = 2
                metade = num//2

                prime = True
                while possivelDivisor<=metade:
                if num%possivelDivisor==0:
                    prime = False
                    break
                possivelDivisor+=1
            
            if prime:
                print("this is a prime number.")
            else:
                print("this is not a prime number.")
            '''
            num = int(input("Enter a natural number: "))
            half = num // 2
            if num <= 1:
                print("Please enter a natural number.")
                continue
            is_prime = True
            for i in range(2, half + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print("This is a prime number.")
            else:
                print("This is not a prime number.")
            break
        except ValueError:
            main.ValueErrorEx()
            
def ex57():
    print("\n\nExercise 57: Enter a natural number.")
    while True:
        try:
            #how do i check if this is a palindrome?
            num = int(input("Enter a natural number: "))
            reverse = num[::-1]
            length = len(str(num))
            if (length < 3):
                print("Please enter a number with more than 2 digits.")
                continue
            else:
                 if (num == reverse):
                    print("The number is a palindrome.")
                 else:
                    print("The number is a palindrome.")
                    break
        except ValueError:
            main.ValueErrorEx()

def retornar():
    main.cls()
    main.main()

def Cat1():
    while True:
        try:

            print("Select the exercise you want to execute.")
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
            print("[13] Return.")
            desired = int(input("Enter the number of the exercise you want to run from the above:  "))
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
                case 13: retornar()
                case _: print("Invalid entry. Please enter a valid number.")
            break
        except ValueError:
            main.ValueErrorEx()

def Cat2():
    while True:
        try:          
            print("Select the exercise you want to execute.")
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
            print("[35] Check valid triangle sides.")
            print("[36] Check valid triangle sides and type.")
            print("[37] Check valid triangle by angles.")
            print("[38] Check valid triangle by angles and type.")
            print("[39] Return.")
            desired = int(input("Enter the number of the exercise you want to run from the above:  "))
            match desired:
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
                case 35: order.ex35()
                case 36: order.ex36()
                case 37: order.ex37()
                case 38: order.ex38()
                case 39: retornar()
                case _: print("Invalid entry. Please enter a valid number.")
            break
        except ValueError:
            main.ValueErrorEx()
    
def Cat3():
    while True:
        try:
            print("Select the exercise you want to execute.")
            print("[26] BMI calculating.")
            print("[27] First-degree equation square root.")
            print("[39] Second-degree equation square root.")
            print("[50] Prime number checking.")
            print("[57] Palindrome checker.")
            print("[41] Return.")
            desired = int(input("Enter the number of the exercise you want to run from the above:  "))
            match desired:
                case 26: ex26()
                case 27: ex27()
                case 39: ex39()
                case 50: ex50()
                case 57: ex57()
                case 41: retornar()
                case _: print("Invalid entry. Please enter a valid number.")
            break
        except ValueError:
            main.ValueErrorEx()

def Cat4():
    while True:
        try:
            print("Select the exercise you want to execute.")
            print("[28] 1-12 Compilation.")
            print("[29] 13-18 Compilation.")
            print("[30] 19-25 Compilation.")
            print("[31] Return.")
            desired = int(input("Enter the number of the exercise you want to run from the above:  "))
            match desired:
                case 28: combos.ex28()
                case 29: combos.ex29()
                case 30: combos.ex30()
                case 31: retornar()
                case _: print("Invalid entry. Please enter a valid number.")
            break
        except ValueError:
            main.ValueErrorEx()

def Cat5():
    while True:
        try:
            print("Select the exercise you want to execute.")
            print("[31] Ascending order of 2 numbers.")
            print("[32] Ascending order of 3 numbers.")
            print("[33] Ascending order of 4 numbers.")
            print("[34] Return.")
            desired = int(input("Enter the number of the exercise you want to run from the above:  "))
            match desired:
                case 31: order.ex31()
                case 32: order.ex32()
                case 33: order.ex33()
                case 34: retornar()
                case _: print("Invalid entry. Please enter a valid number.")
            break
        except ValueError:
            main.ValueErrorEx()

def Cat6():
    while True:
        try:
            print("Select the exercise you want to execute.")
            print("[34] Valid time check.")
            print("[40] Valid date and year check.")
            print("[41] Return.")
            desired = int(input("Enter the number of the exercise you want to run from the above:  "))
            match desired:
                case 34: date.ex34()
                case 40: date.ex40()
                case 41: retornar()
                case _: print("Invalid entry. Please enter a valid number.")
            break
        except ValueError:
            main.ValueErrorEx()

def Cat7():
    while True:
        try:

            print("Select the exercise you want to execute.")
            print("[41] Number to words.")
            print("[42] Number to words with currency.")
            print("[43] Number to words with ordinal.")
            print("[44] Number to words with ordinal and currency.")
            print("[45] Number to words with ordinal and currency.")
            print("[46] Number to words with ordinal and currency.")
            print("[47] Number to words with ordinal and currency.")
            print("[48] Return.")
            desired = int(input("Enter the number of the exercise you want to run from the above:  "))
            match desired:
                case 41: number2words.ex41()
                case 42: number2words.ex42()
                case 43: number2words.ex43()
                case 44: number2words.ex44()
                case 45: number2words.ex45()
                case 46: number2words.ex46()
                case 47: number2words.ex47()
                case 48: retornar()
                case _: print("Invalid entry. Please enter a valid number.")
        except ValueError:
            main.ValueErrorEx()

def Cat8():
    while True:
        try:
            print("Select the exercise you want to execute.")
            print("[58] Natural number rectangle.")
            print("[59] Natural number hollow rectangle.")
            print("[60] Natural number triangle.")
            print("[61] Natural number hollow triangle.")
            print("[62] Natural number diamond.")
            print("[63] Natural number hollow diamond.") 
            desired = int(input("Enter the number of the exercise you want to run from the above: "))
            match desired:
                case 58: lineprinting.ex58()
                case 59: lineprinting.ex59()
                case 60: lineprinting.ex60()
                case 61: lineprinting.ex61()
                case 62: lineprinting.ex62()
                case 63: lineprinting.ex63()
                case _: print("Invalid entry. Please enter a valid number.")

        except ValueError:
            main.ValueErrorEx()

def Cat9():
    while True:
        try:
            print("Select the exercise you want to execute.")
            print("[3]Highest number in list.")
            print("[4]Lowest number in list.")
            
            desired = int(input("Enter the number of the exercise you want to run from the above: "))
            match desired:
                case 3: minmax.ex3()
                case 4: minmax.ex4()
        except ValueError:
            main.ValueErrorEx()