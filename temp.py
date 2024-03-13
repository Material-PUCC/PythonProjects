import math
import list


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
            list.ValueErrorEx()

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
            list.ValueErrorEx()

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
            list.ValueErrorEx()

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
            list.ValueErrorEx()

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
            list.ValueErrorEx()

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
            list.ValueErrorEx()

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
            list.ValueErrorEx()
    
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
            list.ValueErrorEx()

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
            list.ValueErrorEx()

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
            list.ValueErrorEx()

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
            list.ValueErrorEx()

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
            list.ValueErrorEx()