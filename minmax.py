import main

def ex3():
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
            highest = list1[0]
            for num in list1:
                if num > highest:
                    highest = num
            print("The highest number is", highest, "with index", list1.index(highest), ".")
            break
        except ValueError:
            main.ValueErrorEx()
    '''while True:
        try:
            i = 0
            times = int(input("\n\nEnter how many elements the list will have: "))
            while i < times:
                list1 = []
                num = int(input("\n\nEnter a number: "))
                list1.append(num)
                i = i + 1
            print(str(max(list1)))
        
        except ValueError:
            main.ValueErrorEx()
        break'''
        
    
def ex4():
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
            lowest = list1[0]
            for num in list1:
                if num < lowest:
                    lowest = num
            print("The lowest number is", lowest, "with index", list1.index(lowest), ".")
            sortedlis = list1.sort()
            break
        except ValueError:
            main.ValueErrorEx()
    '''
    while True:
        try:
            i = 0
            times = int(input("\n\nEnter how many elements the list will have: "))
            while i < times:
                list1 = []
                num = int(input("\n\nEnter a number: "))
                list1.append(num)
                i = i + 1
            print(str(min(list1)))
        except ValueError:
            main.ValueErrorEx()
            '''
