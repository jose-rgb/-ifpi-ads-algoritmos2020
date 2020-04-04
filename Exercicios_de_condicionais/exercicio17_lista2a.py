def main():
    var1 = int(input('Digite o primeiro valor: '))
    var2 = int(input('Digite o segundo valor: '))
    calculo(var1, var2)


def calculo(var1, var2):
    if var1 % var2 == 1:
        print(var1 + var2 + 1)
    elif var1 % var2 == 2:
        par_impar(var1)
        par_impar2(var2)
    elif var1 % var2 ==3:
        print(var1 * var2 + var1)
    elif var1 % var2 == 4:
        print((var1 + var2)/var2)
    else:
        print(var1**1/2, var2**1/2)


def par_impar(var1):
    if var1 % 2 == 0:
        print('O primeiro valor é par')
    else:
        print('O primeiro valor é ímpar')


def par_impar2(var2):
    if var2 % 2 == 0:
        print('O segundo valor é par')
    else:
        print('O segundo valor é ímpar')


main()