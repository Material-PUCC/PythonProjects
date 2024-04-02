import main

def ex58():
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
    #how do i print the same rectangle but hollow?
    while True:
        try:
            num = int(input("Enter a natural number: "))
            if num <= 1:
                main.ZeroInputEx()
            else:
                for i in range(num):
                    if i == 0 or i == num - 1:
                        for j in range(num):
                            print("O", end="")
                    else:
                        print("O", end="")
                        for j in range(num - 2):
                            print(" ", end="")
                        print("O", end="")
                    print()
                break
        except ValueError:
            main.ValueErrorEx()

def ex60():
    while True:
        try:
            num = int(input("Enter a natural number: "))
            if num <= 1:
                main.ZeroInputEx()
            else:
                for i in range(num):
                    for j in range(num):
                        if i == 0 or i == num - 1:
                            print("O", end="")
                        else:
                            if j == 0 or j == num - 1:
                                print("O", end="")
                            else:
                                print(" ", end="")
                    print()
                break
        except ValueError:
            main.ValueErrorEx()


def ex61():
    print('a')
def ex62():
    print("a")

def ex63():
    print('a')


