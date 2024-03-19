import main

def ex34(): 
    print("\n\nExercise 34: Valid time check")
    while True:
        try:
            hour = input("\n\nEnter the hour: ")
            hour = int(hour)
            if(hour < 0 or hour > 23):
                print("Invalid hour. Please enter a valid hour.")
                continue
            minute = input("\n\nEnter the minute: ")
            minute = int(minute)
            if(minute < 0 or minute > 59):
                print("Invalid minute. Please enter a valid minute.")
                continue
            second = input("\n\nEnter the second: ")
            second = int(second)
            if(second < 0 or second > 59):
                print("Invalid second. Please enter a valid second.")
                continue
            print("The time is: ", hour, ":", minute, ":", second, ".", sep="")
            break
        except ValueError:
            ValueErrorEx()

def ex40():
    print("\n\nExercise 40: Valid date and year check")
    while True:
        try:
            day = input("\n\nEnter the day: ")
            day = int(day)
            if (day < 1 or day > 31):
                print("Invalid input. Please enter a valid day.")
                continue
            month = input("\n\nEnter the month: ")
            month = int(month)
            if (month < 1 or month > 12):
                print("Invalid input. Please enter a valid month.")
                continue
            year = input("\n\nEnter the year: ")
            year = int(year)
            if (year == 0 or year > 9999 or year < -45):
                print("Invalid input. Please enter a valid year.")
                continue
            match month:
                case 2:
                    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                        if (day > 29):
                            print("Invalid input. Please enter a valid day.")
                            continue
                    else:
                        if (day > 28):
                            print("Invalid input. Please enter a valid day.")
                            continue
                case 4, 6, 9, 11:
                    if (day > 30):
                        print("Invalid input. Please enter a valid day.")
                        continue
                case 10:
                    if (day >= 5 and day <= 14 and year == 1582):
                        print("Invalid input. This day does not exist.")
                        continue
            print("The date is: ", day, "/", month, "/", year, ".", sep="")
            break
        except ValueError:
            ValueErrorEx()