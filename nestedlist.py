#list inside a bag of list inside a bag of list inside a bag of list
import main

def ex11():
    while True:
        try:
            listSize = int(input("\n\nHow many numbers do you want in your list?"))
            if listSize < 0:
                print("Invalid entry. Please enter a valid number.")
            else:
                current = 1
                numbers = []
                while current <= listSize:
                    numbers.append(int(input("\n\nEnter a number: ")))
                    current += 1
                print("First list: ", numbers)
            listSize2 = int(input("\n\nHow many numbers do you want in your second list?"))
            if listSize2 < 0:
                print("Invalid entry. Please enter a valid number.")
            else:
                current = 1
                numbers2 = []
                while current <= listSize2:
                    numbers2.append(int(input("\n\nEnter a number: ")))
                    current += 1
                print("Second list: ", numbers2)
                #how do I check if a inputted number from the second list is in the first list?
                checkNumber = int(input("\n\nEnter a number from the second list to check if it is in the first list: "))
                if checkNumber in numbers and checkNumber in numbers2:
                    index = numbers.index(checkNumber)
                    if (index == 0):
                        print(checkNumber)
                    else:
                        print("The number 'most to the left' in the first list is: ", numbers[0])

            break
        except ValueError:
            main.ValueErrorEx()
        
    