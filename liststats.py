import main

def ex1():
    while True:
        try:          
            list1 = []
            i = 1
            times = int(input("\n\nEnter how many numbers you want in the list: "))      

            while i <= times:
                while True:
                    try:
                        num = int(input("Insert a number to the list: "))
                        break
                    except ValueError:
                        main.ValueErrorEx() 
                list1.append(num)
                i = i + 1
            total = 0
            for num in list1:
                total = total + num
            print("The sum of the numbers in the list is: ", total)
            break
        except ValueError:
            main.ValueErrorEx()
        
def ex2():
    while True:
        try:
            list1 = []
            i = 1
            times = int(input("\n\nEnter how many numbers you want in the list: "))        
            while i <= times:
                while True:
                    try:
                        num = int(input("Insert a number to the list: "))
                        break
                    except ValueError:
                        main.ValueErrorEx() 
                list1.append(num)
                i = i + 1
            total = 0
            for num in list1:
                total += num
                avg = total / len(list1)
            print("The sum of the numbers in the list is: ", avg)
            break
        except ValueError:
            main.ValueErrorEx()
  