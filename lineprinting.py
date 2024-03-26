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
                #how can i do it without multiplying a string by the number?
                for i in range(num):
                    for j in range(num):
                        print("O", end="")
                    print()
                break
        except ValueError:
            main.ValueErrorEx()