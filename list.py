def error():
    print("Invalid input. Please enter a number.")
    exit()

print("This program was developed by Davi Andrade Macedo.")
print("I could do multiple files for this, but I'd rather do it all here.")


print("\n\nExercise 1: °C to °F converter.")

CInput=input("Enter the temperature in °C: ")
try:
    CTemp = float(CInput);
    FTemp = 9*CTemp/5+32
    print("The temperature in °F is: ", FTemp, sep="")

except:
    error()
   

print("\n\nExercise 2: °F to °C converter.")
FInput = input("Enter the temperature in °F: ")
try:
    FTemp = float(FInput)
    CTemp = (FTemp-32)*5/9
    print("The temperature in °C is: ", CTemp, sep="")
except:
    error()


print("\n\nExercise 3:  °C to °K converter.")
CInput = input("Enter the temperature in °C: ")
try:
    CTemp = float(CInput)
    KTemp = CTemp + 273.15
    print("The temperature in °K is: ", KTemp, sep="")
except:
    error()


print("\n\nExercise 4: °K to °C converter.")
KInput = input("Enter the temperature in °K: ")
try:
    KTemp = float(KInput)
    CTemp = KTemp - 273.15
    print("The temperature in °C is: ", CTemp, sep="")
except:
    error()


print("\n\nExercise 5: °C to °R converter.")
CInput = input("Enter the temperature in °C: ")
try:
    CTemp = float(CInput)
    RTemp = CTemp*9/5 + 491.67
    print("The temperature in °R is: ", RTemp, sep="")
except:
    error()


print("\n\nExercise 6: °R to °C converter.")
RInput = input("Enter the temperature in °R: ")
try:
    RTemp = float(RInput)
    CTemp = (RTemp - 491.67)/1.8
    print("The temperature in °C is: ", CTemp, sep="")
except ValueError:
    error()

print("\n\nExercise 7: F to K converter.")
FInput = input("Enter the temperature in °F: ")
try:
    FTemp = float(FInput)
    CTemp = (FTemp-32)*5/9
    KTemp = CTemp + 273.15
    print("The temperature in °K is: ", KTemp, sep="")
except:
    error()


print("\n\nExercise 8: °K to °F converter.")
KInput = input("Enter the temperature in °K: ")
try:
    KTemp = float(KInput)
    CTemp = KTemp - 273.15
    FTemp = 9*CTemp/5+32
    print("The temperature in °F is: ", FTemp, sep="")  
except:
    error()

print("\n\nExercise 9: °F to °R converter.")
FInput = input("Enter the temperature in °F: ")
try:
    FTemp = float(FInput)
    CTemp = (FTemp-32)*5/9
    RTemp = CTemp*9/5 + 491.67
    print("The temperature in °R is: ", RTemp, sep="")
except:
    error()

print("\n\nExercise 10: °R to °F converter.")
RInput = input("Enter the temperature in °R: ")
try:
    RTemp = float(RInput)
    CTemp = (RTemp - 491.67)/1.8
    FTemp = RTemp - 459.67
    print("The temperature in °F is: ", FTemp, sep="")
except:
    error()


print("\n\nExercise 11: °K to °R converter.")
KInput = input("Enter the temperature in °K: ")
try:
    KTemp = float(KInput)
    CTemp = KTemp - 273.15
    RTemp = CTemp*9/5 + 491.67
    print("The temperature in °R is: ", RTemp, sep="")
except:
    error()

print("\n\nExercise 12: °R to °K converter.")
RInput = input("Enter the temperature in °R: ")
try:
    RTemp = float(RInput)
    CTemp = (RTemp - 491.67)/1.8
    KTemp = CTemp + 273.15
    print("The temperature in °K is: ", KTemp, sep="")
except:
    error()

print("\n\nExercise 13: Perimeter of a triangle")
side1 = input("Enter the length of the first side: ")
side2 = input("Enter the length of the second side: ")
side3 = input("Enter the length of the third side: ")
try:
    side1 = float(side1)
    side2 = float(side2)
    side3 = float(side3)
    perimeter = side1 + side2 + side3
    print("The perimeter of the triangle is: ", perimeter, sep="")
except:
    error()

print("\n\nExercise 14: Perimeter of a square")
side = input("Enter the length of the side: ")
try:
    side = float(side)
    perimeter = 4*side
    print("The perimeter of the square is: ", perimeter, sep="")
except:
    error()


print("\n\nExercise 15: Perimeter of a rectangle")
length = input("Enter the length of the rectangle: ")
width = input("Enter the width of the rectangle: ")
try:
    length = float(length)
    width = float(width)
    perimeter = 2*length + 2*width
    print("The perimeter of the rectangle is: ", perimeter, sep="")
except:
    error()

print("\n\nExercise 16: Area of a triangle")
base = input("Enter the length of the base: ")
height = input("Enter the height of the triangle: ")
try:
    base = float(base)
    height = float(height)
    area = base*height/2
    print("The area of the triangle is: ", area, sep="")
except:
    error()

print("\n\nExercise 17: Area of a square")



