from main import ValueErrorEx, ZeroInputEx, cls

def ex48():
    print("\n\nExercise 48: Number switching interval")
    
def ex51():
    print("\n\nExercise 51: Prime numbers interval")    

def ex55():
    print("\n\nExercise 55: Friendly numbers pairs interval")
    while True:
        try:
            print("Enter two numbers to check if they are friendly numbers.")
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            if num1 <= 0 or num2 <= 0:
                ZeroInputEx()
            else:
                if num1 == num2:
                    print("The numbers are not friendly.")
                else:
                    sum1 = sum2 = 0
                    for i in range(1, num1):
                        if num1 % i == 0:
                            sum1 += i
                    for i in range(1, num2):
                        if num2 % i == 0:
                            sum2 += i
                    if sum1 / num1 == sum2 / num2:
                        print("The numbers are friendly.")
                    else:
                        print("The numbers are not friendly.")
                break
        except ValueError:
            ValueErrorEx()