def main():
    print(10 * '#' + ' Arredondamento de números ' + 10 * '#')
    num = float(input('Digite um número: '))
    calculo(num)


def calculo(num):
    num2 = int(num)
    flutuante = num - num2
    if flutuante >= 0.5:
        print(f'Como a parte decimal {flutuante:.1f} é superior ou igual á 0,5 arredonda-se o número para {num2 + 1}')
    else:
        print(f'Como a parte decimal {flutuante:.1f} é inferior á 0,5 arredonda-se o número para {num2} ')


main()



