print("This program was developed by Davi Andrade Macedo.")
print("I could do multiple files for this, but I'd rather do it all here.")
print("Exercise 1: C to F converter.")

CInput=input("Enter the temperature in C°: ")

CTemp = float(CInput);

FTemp = 9*CTemp/5+32

print("The temperature in F° is: ", FTemp, sep="")

print("Exercise 2: F to C converter.")
FInput = input("Enter the temperature in F°: ")

FTemp = float(FInput)

CTemp = (FTemp-32)*5/9

print("The temperature in C° is: ", CTemp, sep="")

print("Exercise 3:  C to K converter.")
CInput = input("Enter the temperature in C°: ")
CTemp = float(CInput)
KTemp = CTemp + 273.15
print("The temperature in K is: ", KTemp, sep="")

print("Exercise 4: K to C converter.")
KInput = input("Enter the temperature in K: ")
KTemp = float(KInput)
CTemp = KTemp - 273.15
print("The temperature in C° is: ", CTemp, sep="")