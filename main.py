import webbrowser, cats, os, lineprinting
def ValueErrorEx():
    print("Invalid input. Please enter a valid number.")

def ZeroInputEx():
    print("Invalid input. Please enter a number different from zero.")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    while True:
        try:

            print("===================================")
            print("Categories:")
            print("[1]Temperature conversion.")
            print("[2]Perimeter and area of geometric figures.") 
            print("[3]Other exercises.")
            print("[4]Compilations.")
            print("[5]Order.")#THY END IS NOW
            print("[6]Date and time.")
            print("[7]Number to words.")
            print("===================================")
            print("Others")
            print("[8]Exit.")
            print("[9]About.")
            print("[10]Prointer.")
            print("[11]ex58")
            desiredCat = int(input("Enter your option: "))
            #with great help from meid menid amei da but she's not in the same class :(
            match desiredCat:
                case 1: cats.Cat1()
                case 2: cats.Cat2()
                case 3: cats.Cat3()
                case 4: cats.Cat4()
                case 5: cats.Cat5()
                case 6: cats.Cat6()
                case 7: cats.Cat7()
                case 8: die()#CRUSH
                case 9: seeRepo()
                case 10: prointer()
                case 11: lineprinting.ex58()
                case _: print("Invalid entry. Please enter a valid number.")

            break
        except ValueError:
            ValueErrorEx()

def end():
    print("Thank you for using this program. Goodbye!")
    exit()

def seeRepo():
    webbrowser.open("https://www.github.com/Material-PUCC/PythonProjects")
    cls()
    main()

def prointer():
    webbrowser.open_new("https://bigrat.monster/printer")
    cls()
    main()
    
def die():
    print("\n\Are you sure you want to exit?")
    print("[1] Yes")
    print("[2] No")
    ans = int(input("Y/N: "))
    match ans:
        case 1: end()
        case 2: cls(), main()
        case _: print("Invalid entry. Please enter a valid number.")
    
if __name__ == "__main__":
    main()