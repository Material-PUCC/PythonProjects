import main

def ex58():
    #enter a natural number and write an amount of lines equal to the number in the shape of a rectangle
    print("\n\nExercise 58: Enter a natural number.")
    while True:
        try:
            num = int(input("Enter a natural number: "))
            if num <= 1:
                main.ZeroInputEx()
            else:
                '''for i in range(num):
                    print("O" * num)'''
                '''
                qtdLins=qtdCols=int(input("Deseja um quadrado de quantas linhas"?))
                if (qtdLins <= 1):
                    print("A quantidade de linhas deve ser maior que 1!")
                else:
                    lin = 1
                    while lin <= qtdLins:
                        col = 1
                        while col <= qtdCols:
                            print("O", end="")
                            col += 1
                        print()
                        lin += 1
                '''
                for i in range(num):
                    for j in range(num):
                        print("O", end="")
                    print()
                break
        except ValueError:
            main.ValueErrorEx()

def ex59():
    print("\n\nExercise 59: Enter a natural number.")
    #how do i print the same rectangle but hollow?
    while True:
        try:
            num = int(input("Enter a natural number: "))
            if num <= 1:
                main.ZeroInputEx()
            else:
                for i in range(num):
                    if i == 0 or i == num - 1:
                        print("O" * num)
                    else:
                        print("O" + " " * (num - 2) + "O")
                break
        except ValueError:
            main.ValueErrorEx()
