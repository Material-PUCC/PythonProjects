import main, cats

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


            