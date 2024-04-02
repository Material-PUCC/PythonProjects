import main
import num2words

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
            main.ValueErrorEx()

def ex42():
    print("\n\nExercise 42: Natural number from -9 to 9 written in words")
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
            main.ValueErrorEx()

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
            main.ValueErrorEx()

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
            main.ValueErrorEx()

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
            main.ValueErrorEx()

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
            main.ValueErrorEx()

def ex47():
    '''print("\n\nExercise 47: Monetary value between R$-999.99 and R$999.99 written in words")
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
            ValueErrorEx()'''
    print("\n\nExercise 47: Monetary value between R$-999.99 and R$999.99 written in words")
    while True:
        try:
            num = input("\n\nEnter a value between R$-999.99 and R$999.99: ")
            if (num < -999.99 or num > 999.99):
                print("Invalid input. Please enter a number between R$-999.99 and R$999.99.")
                continue
            if (num[0] == '-'):
                numNeg = True
                char1 = num[1]
                char2 = num[2]
                char3 = num[3]
                char4 = num[5]
                char5 = num[6]
                
                num1 = int(char1)
                match num1:
                    case 0: num1 = "zero"
                    case 1: num1 = "one"
                    case 2: num1 = "two"
                    case 3: num1 = "three"
                    case 4: num1 = "four"
                    case 5: num1 = "five"
                    case 6: num1 = "six"
                    case 7: num1 = "seven"
                    case 8: num1 = "eight"
                    case 9: num1 = "nine"
                
        except ValueError:
            main.ValueErrorEx()